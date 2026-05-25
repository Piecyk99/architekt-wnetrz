"use client";
import { Suspense, useEffect, useRef, useState } from "react";
import { api } from "@/lib/api";
import { extractRenderBlocks, sendMessageStream } from "@/lib/stream";
import type { Project, Render, Room } from "@/lib/types";
import { Button, Spinner, Textarea } from "@/components/ui";
import { TopBar } from "@/components/TopBar";
import { ChatMessage, type ChatMessageData } from "@/components/ChatMessage";
import { useProjectId } from "@/lib/projectId";

export default function ChatPageWrapper() {
  return (
    <Suspense fallback={<div className="flex h-screen items-center justify-center"><Spinner /></div>}>
      <ChatPage />
    </Suspense>
  );
}

function ChatPage() {
  const id = useProjectId();
  const [project, setProject] = useState<Project | null>(null);
  const [rooms, setRooms] = useState<Room[]>([]);
  const [activeRoomId, setActiveRoomId] = useState<string | null>(null);
  const [messages, setMessages] = useState<ChatMessageData[]>([]);
  const [rendersByMsg, setRendersByMsg] = useState<Record<string, Render[]>>({});
  const [input, setInput] = useState("");
  const [pendingPhotos, setPendingPhotos] = useState<Array<{ url: string; previewUrl: string }>>([]);
  const [streaming, setStreaming] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const scrollRef = useRef<HTMLDivElement | null>(null);
  const fileInputRef = useRef<HTMLInputElement | null>(null);

  // initial load
  useEffect(() => {
    if (!id) return;
    (async () => {
      try {
        const [p, m, r] = await Promise.all([
          api.getProject(id),
          api.listMessages(id),
          api.listRenders(id),
        ]);
        setProject(p.project);
        setRooms(p.rooms);
        setActiveRoomId(p.rooms[0]?.id ?? null);
        setMessages(
          m.messages.map((msg) => ({
            id: msg.id,
            role: msg.role,
            content: msg.content,
            images: msg.images ? (JSON.parse(msg.images) as string[]) : undefined,
          })),
        );
        const grouped: Record<string, Render[]> = {};
        for (const rnd of r.renders) {
          if (rnd.message_id) {
            (grouped[rnd.message_id] ||= []).push(rnd);
          }
        }
        setRendersByMsg(grouped);
      } catch (e: any) {
        setErr(String(e.message ?? e));
      }
    })();
  }, [id]);

  // autoscroll
  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
  }, [messages]);

  const handleFile = async (file: File) => {
    if (!id) return;
    setErr(null);
    try {
      const uploaded = await api.uploadPhoto(id, file);
      setPendingPhotos((p) => [...p, { url: uploaded.url, previewUrl: URL.createObjectURL(file) }]);
    } catch (e: any) {
      setErr(`Upload failed: ${e.message ?? e}`);
    }
  };

  const send = async () => {
    if (!id || (!input.trim() && pendingPhotos.length === 0) || streaming) return;
    const text = input.trim() || "[zdjęcie]";
    const imageUrls = pendingPhotos.map((p) => p.url);
    const previewImages = pendingPhotos.map((p) => p.url);

    setInput("");
    setPendingPhotos([]);
    setStreaming(true);
    setErr(null);

    const tempUserId = `tmp_user_${Date.now()}`;
    const tempAssistantId = `tmp_asst_${Date.now()}`;
    setMessages((m) => [
      ...m,
      { id: tempUserId, role: "user", content: text, images: previewImages },
      { id: tempAssistantId, role: "assistant", content: "", streaming: true },
    ]);

    let assistantText = "";
    let serverAsstId = tempAssistantId;

    try {
      await sendMessageStream(
        id,
        { text, roomId: activeRoomId, imageUrls: imageUrls.length ? imageUrls : undefined },
        {
          onMeta: (meta) => {
            serverAsstId = meta.assistantMsgId;
            setMessages((m) =>
              m.map((x) =>
                x.id === tempUserId
                  ? { ...x, id: meta.userMsgId }
                  : x.id === tempAssistantId
                  ? { ...x, id: meta.assistantMsgId }
                  : x,
              ),
            );
          },
          onDelta: (chunk) => {
            assistantText += chunk;
            setMessages((m) =>
              m.map((x) => (x.id === serverAsstId ? { ...x, content: assistantText, streaming: true } : x)),
            );
          },
          onError: (msg) => setErr(msg),
          onDone: async () => {
            setMessages((m) =>
              m.map((x) => (x.id === serverAsstId ? { ...x, streaming: false } : x)),
            );
            // teraz wywołaj rendery jakie skill zażądał w ```render``` blokach
            const blocks = extractRenderBlocks(assistantText);
            if (blocks.length > 0 && id) {
              const renders: Render[] = [];
              for (const b of blocks) {
                try {
                  const r = await api.renderImage(id, {
                    prompt: b.prompt,
                    type: b.type,
                    aspectRatio: b.aspect,
                    messageId: serverAsstId,
                    roomId: activeRoomId,
                  });
                  renders.push({
                    id: r.id,
                    project_id: id,
                    room_id: activeRoomId,
                    message_id: serverAsstId,
                    type: b.type,
                    prompt: b.prompt,
                    image_key: r.key,
                    url: r.url,
                    created_at: Math.floor(Date.now() / 1000),
                  });
                  setRendersByMsg((m) => ({ ...m, [serverAsstId]: [...(m[serverAsstId] ?? []), renders[renders.length - 1]] }));
                } catch (e: any) {
                  setErr(`Render: ${e.message ?? e}`);
                }
              }
            }
          },
        },
      );
    } catch (e: any) {
      setErr(String(e.message ?? e));
    } finally {
      setStreaming(false);
    }
  };

  if (err && !project) {
    return (
      <main className="p-4">
        <p className="text-red-700">{err}</p>
      </main>
    );
  }
  if (!project) {
    return (
      <main className="flex h-screen items-center justify-center">
        <Spinner />
      </main>
    );
  }

  return (
    <>
      <TopBar
        title={project.name}
        subtitle={
          rooms.length > 0
            ? rooms.find((r) => r.id === activeRoomId)?.name ?? "Cały projekt"
            : project.style ?? "Cały projekt"
        }
        back="/"
      />

      {rooms.length > 1 ? (
        <div className="sticky top-[57px] z-10 border-b border-walnut-100 bg-cream-50/95 backdrop-blur dark:bg-walnut-900/95 dark:border-walnut-800">
          <div className="mx-auto max-w-2xl overflow-x-auto px-3 py-2">
            <div className="flex gap-2">
              <Pill active={!activeRoomId} onClick={() => setActiveRoomId(null)}>
                Cały projekt
              </Pill>
              {rooms.map((r) => (
                <Pill key={r.id} active={activeRoomId === r.id} onClick={() => setActiveRoomId(r.id)}>
                  {r.name}
                </Pill>
              ))}
            </div>
          </div>
        </div>
      ) : null}

      <div ref={scrollRef} className="mx-auto max-w-2xl space-y-3 px-3 py-4 pb-40">
        {messages.length === 0 ? (
          <div className="rounded-2xl border border-dashed border-walnut-200 p-6 text-center text-walnut-500 dark:border-walnut-700">
            <p className="font-medium text-walnut-700 dark:text-cream-100">Zacznij od opisania pomieszczenia</p>
            <p className="mt-1 text-sm">
              np. <em>"salon 25m², okno panoramiczne na południe, styl japandi"</em>
              <br />Możesz załączyć zdjęcie lub szkic.
            </p>
          </div>
        ) : null}
        {messages.map((m) => (
          <ChatMessage
            key={m.id}
            msg={{
              ...m,
              renders: (rendersByMsg[m.id] ?? []).map((r) => ({ id: r.id, url: r.url, type: r.type })),
            }}
          />
        ))}
        {err ? <p className="rounded-xl bg-red-50 px-3 py-2 text-sm text-red-700">{err}</p> : null}
      </div>

      <div className="fixed bottom-16 left-0 right-0 z-10 border-t border-walnut-100 bg-cream-50/95 backdrop-blur dark:bg-walnut-900/95 dark:border-walnut-800">
        <div className="mx-auto max-w-2xl px-3 py-2">
          {pendingPhotos.length > 0 ? (
            <div className="mb-2 flex gap-2 overflow-x-auto">
              {pendingPhotos.map((p, i) => (
                <div key={i} className="relative h-16 w-16 shrink-0">
                  <img src={p.previewUrl} className="h-full w-full rounded-lg object-cover" alt="" />
                  <button
                    onClick={() => setPendingPhotos((ps) => ps.filter((_, idx) => idx !== i))}
                    className="absolute -right-1 -top-1 rounded-full bg-walnut-700 px-1.5 text-xs text-cream-50"
                  >
                    ✕
                  </button>
                </div>
              ))}
            </div>
          ) : null}
          <div className="flex items-end gap-2">
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              hidden
              onChange={(e) => {
                const f = e.target.files?.[0];
                if (f) handleFile(f);
                e.target.value = "";
              }}
            />
            <Button
              variant="ghost"
              size="md"
              onClick={() => fileInputRef.current?.click()}
              aria-label="Załącz zdjęcie"
              disabled={streaming}
            >
              <svg className="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48" />
              </svg>
            </Button>
            <Textarea
              rows={1}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  send();
                }
              }}
              placeholder="Napisz wiadomość..."
              className="min-h-[44px] max-h-32 flex-1"
              disabled={streaming}
            />
            <Button onClick={send} disabled={streaming || (!input.trim() && pendingPhotos.length === 0)}>
              {streaming ? <Spinner /> : "→"}
            </Button>
          </div>
        </div>
      </div>
    </>
  );
}

function Pill({ active, onClick, children }: { active: boolean; onClick: () => void; children: React.ReactNode }) {
  return (
    <button
      onClick={onClick}
      className={`whitespace-nowrap rounded-full border px-3 py-1 text-sm ${
        active
          ? "border-walnut-500 bg-walnut-600 text-cream-50"
          : "border-walnut-200 dark:border-walnut-700"
      }`}
    >
      {children}
    </button>
  );
}
