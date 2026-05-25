"use client";
import clsx from "clsx";
import { Markdown } from "./Markdown";
import { mediaUrl } from "@/lib/api";
import { stripFenceBlocks } from "@/lib/stream";

export interface ChatMessageData {
  id: string;
  role: "user" | "assistant";
  content: string;
  images?: string[];
  streaming?: boolean;
  renders?: Array<{ id: string; url: string; type: string }>;
}

export function ChatMessage({ msg }: { msg: ChatMessageData }) {
  const isUser = msg.role === "user";
  const stripped = isUser ? msg.content : stripFenceBlocks(msg.content);

  return (
    <div className={clsx("flex w-full", isUser ? "justify-end" : "justify-start")}>
      <div
        className={clsx(
          "max-w-[88%] rounded-2xl px-4 py-3",
          isUser
            ? "bg-walnut-600 text-cream-50"
            : "bg-white dark:bg-walnut-900 border border-walnut-100 dark:border-walnut-800",
        )}
      >
        {msg.images && msg.images.length > 0 ? (
          <div className="mb-2 flex flex-wrap gap-2">
            {msg.images.map((u, i) => (
              <a key={i} href={mediaUrl(u)} target="_blank" rel="noreferrer">
                <img src={mediaUrl(u)} alt="" className="h-32 w-32 rounded-lg object-cover" />
              </a>
            ))}
          </div>
        ) : null}

        {stripped ? (
          isUser ? (
            <p className="whitespace-pre-wrap text-[15px] leading-relaxed">{stripped}</p>
          ) : (
            <div className={clsx("text-[15px] leading-relaxed", msg.streaming && !stripped && "shimmer")}>
              <Markdown>{stripped || (msg.streaming ? "​" : "")}</Markdown>
            </div>
          )
        ) : msg.streaming ? (
          <div className="shimmer text-walnut-400" />
        ) : null}

        {msg.renders && msg.renders.length > 0 ? (
          <div className="mt-3 grid grid-cols-2 gap-2">
            {msg.renders.map((r) => (
              <a key={r.id} href={r.url} target="_blank" rel="noreferrer">
                <img src={r.url} alt={r.type} className="w-full rounded-lg" />
              </a>
            ))}
          </div>
        ) : null}
      </div>
    </div>
  );
}
