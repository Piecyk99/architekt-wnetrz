"use client";
import { Suspense } from "react";
import { BottomNav } from "@/components/BottomNav";
import { useProjectId } from "@/lib/projectId";

function NavWrapper() {
  const projectId = useProjectId();
  if (!projectId) return null;
  return <BottomNav projectId={projectId} />;
}

export default function ProjectLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <div className="min-h-screen pb-20">{children}</div>
      <Suspense fallback={null}>
        <NavWrapper />
      </Suspense>
    </>
  );
}
