"use client";
import Link from "next/link";

export function TopBar({
  title,
  subtitle,
  back,
  right,
}: {
  title: string;
  subtitle?: string;
  back?: string;
  right?: React.ReactNode;
}) {
  return (
    <header className="sticky top-0 z-20 border-b border-walnut-100 bg-cream-50/95 backdrop-blur dark:bg-walnut-900/95 dark:border-walnut-800 pt-safe">
      <div className="mx-auto flex max-w-2xl items-center gap-2 px-4 py-3">
        {back ? (
          <Link href={back} aria-label="Wstecz" className="-ml-2 rounded-lg p-1.5 hover:bg-walnut-100 dark:hover:bg-walnut-800">
            <svg className="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <polyline points="15 18 9 12 15 6" />
            </svg>
          </Link>
        ) : null}
        <div className="min-w-0 flex-1">
          <h1 className="truncate text-base font-semibold">{title}</h1>
          {subtitle ? <p className="truncate text-xs text-walnut-500 dark:text-walnut-400">{subtitle}</p> : null}
        </div>
        {right}
      </div>
    </header>
  );
}
