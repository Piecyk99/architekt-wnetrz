"use client";
import clsx from "clsx";
import type { ButtonHTMLAttributes, HTMLAttributes, InputHTMLAttributes, TextareaHTMLAttributes } from "react";

export function Button({
  variant = "primary",
  size = "md",
  className,
  ...rest
}: ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "primary" | "secondary" | "ghost" | "danger";
  size?: "sm" | "md" | "lg";
}) {
  const base = "inline-flex items-center justify-center gap-2 rounded-xl font-medium transition active:scale-[0.98] disabled:opacity-50 disabled:active:scale-100";
  const variants = {
    primary: "bg-walnut-600 text-cream-50 hover:bg-walnut-700",
    secondary: "bg-walnut-100 text-walnut-800 hover:bg-walnut-200 dark:bg-walnut-800 dark:text-cream-100 dark:hover:bg-walnut-700",
    ghost: "text-walnut-700 hover:bg-walnut-100 dark:text-cream-100 dark:hover:bg-walnut-800",
    danger: "bg-red-600 text-white hover:bg-red-700",
  };
  const sizes = {
    sm: "px-3 py-1.5 text-sm",
    md: "px-4 py-2.5 text-base",
    lg: "px-5 py-3 text-lg",
  };
  return <button className={clsx(base, variants[variant], sizes[size], className)} {...rest} />;
}

export function Input(props: InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      {...props}
      className={clsx(
        "w-full rounded-xl border border-walnut-200 bg-white px-4 py-2.5 text-base outline-none focus:border-walnut-500 dark:bg-walnut-900 dark:border-walnut-700 dark:text-cream-50",
        props.className,
      )}
    />
  );
}

export function Textarea(props: TextareaHTMLAttributes<HTMLTextAreaElement>) {
  return (
    <textarea
      {...props}
      className={clsx(
        "w-full rounded-xl border border-walnut-200 bg-white px-4 py-2.5 text-base outline-none focus:border-walnut-500 resize-none dark:bg-walnut-900 dark:border-walnut-700 dark:text-cream-50",
        props.className,
      )}
    />
  );
}

export function Card(props: HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      {...props}
      className={clsx(
        "rounded-2xl border border-walnut-100 bg-white p-4 shadow-sm dark:bg-walnut-900 dark:border-walnut-800",
        props.className,
      )}
    />
  );
}

export function Label({ children, htmlFor }: { children: React.ReactNode; htmlFor?: string }) {
  return (
    <label htmlFor={htmlFor} className="mb-1.5 block text-sm font-medium text-walnut-700 dark:text-cream-200">
      {children}
    </label>
  );
}

export function Spinner({ className }: { className?: string }) {
  return (
    <svg className={clsx("h-5 w-5 animate-spin", className)} viewBox="0 0 24 24" fill="none">
      <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="3" opacity="0.25" />
      <path d="M12 2a10 10 0 0 1 10 10" stroke="currentColor" strokeWidth="3" strokeLinecap="round" />
    </svg>
  );
}

export function formatPLN(gr: number): string {
  return `${(gr / 100).toLocaleString("pl-PL", { maximumFractionDigits: 0 })} zł`;
}
