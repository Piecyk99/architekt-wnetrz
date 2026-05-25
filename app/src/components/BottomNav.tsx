"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import clsx from "clsx";
import { projectHref } from "@/lib/projectId";

export function BottomNav({ projectId }: { projectId: string }) {
  const pathname = usePathname();
  const tabs = [
    { path: "/project", label: "Czat", icon: ChatIcon },
    { path: "/project/renders", label: "Wizualizacje", icon: ImageIcon },
    { path: "/project/shopping", label: "Zakupy", icon: CartIcon },
    { path: "/project/budget", label: "Budżet", icon: MoneyIcon },
    { path: "/project/notes", label: "Notatki", icon: NoteIcon },
  ];

  return (
    <nav className="fixed bottom-0 left-0 right-0 z-30 border-t border-walnut-100 bg-cream-50/95 backdrop-blur dark:bg-walnut-900/95 dark:border-walnut-800 pb-safe">
      <div className="mx-auto flex max-w-2xl items-stretch justify-around">
        {tabs.map((t) => {
          const isActive =
            t.path === "/project"
              ? pathname === "/project" || pathname === "/project/"
              : pathname.startsWith(t.path);
          const Icon = t.icon;
          return (
            <Link
              key={t.path}
              href={projectHref(t.path, projectId)}
              className={clsx(
                "flex flex-1 flex-col items-center gap-0.5 py-2 text-xs",
                isActive ? "text-walnut-700 dark:text-cream-100" : "text-walnut-400 dark:text-walnut-500",
              )}
            >
              <Icon className="h-5 w-5" />
              <span>{t.label}</span>
            </Link>
          );
        })}
      </div>
    </nav>
  );
}

function ChatIcon(p: { className?: string }) {
  return (
    <svg {...p} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" />
    </svg>
  );
}
function ImageIcon(p: { className?: string }) {
  return (
    <svg {...p} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="3" width="18" height="18" rx="2" ry="2" />
      <circle cx="8.5" cy="8.5" r="1.5" />
      <polyline points="21 15 16 10 5 21" />
    </svg>
  );
}
function CartIcon(p: { className?: string }) {
  return (
    <svg {...p} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="9" cy="21" r="1" />
      <circle cx="20" cy="21" r="1" />
      <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6" />
    </svg>
  );
}
function MoneyIcon(p: { className?: string }) {
  return (
    <svg {...p} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <line x1="12" y1="1" x2="12" y2="23" />
      <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
    </svg>
  );
}
function NoteIcon(p: { className?: string }) {
  return (
    <svg {...p} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
      <polyline points="14 2 14 8 20 8" />
      <line x1="9" y1="13" x2="15" y2="13" />
      <line x1="9" y1="17" x2="13" y2="17" />
    </svg>
  );
}
