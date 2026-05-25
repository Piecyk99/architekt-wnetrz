"use client";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export function Markdown({ children }: { children: string }) {
  return (
    <div className="prose-chat">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: ({ node, ...p }) => <a {...p} target="_blank" rel="noopener noreferrer" />,
          code: ({ node, className, children, ...p }) => {
            const inline = !className?.startsWith("language-");
            if (inline) {
              return (
                <code className={className} {...p}>
                  {children}
                </code>
              );
            }
            return (
              <code className={className} {...p}>
                {children}
              </code>
            );
          },
        }}
      >
        {children}
      </ReactMarkdown>
    </div>
  );
}
