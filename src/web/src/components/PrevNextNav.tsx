import React from "react";
import type { TopicNavRef } from "../types";
import { IconArrowBack, IconArrowForward } from "./Icons";

interface PrevNextNavProps {
  prev: TopicNavRef | null;
  next: TopicNavRef | null;
  onNavigate: (slug: string) => void;
}

export const PrevNextNav: React.FC<PrevNextNavProps> = ({
  prev,
  next,
  onNavigate,
}) => {
  if (!prev && !next) return null;

  return (
    <nav
      aria-label="Previous and Next Lessons"
      className="mt-12 pt-6 border-t border-border-subtle grid grid-cols-1 sm:grid-cols-2 gap-4"
    >
      {prev ? (
        <a
          href={`/${prev.slug}`}
          onClick={(e) => {
            e.preventDefault();
            onNavigate(prev.slug);
          }}
          className="flex flex-col items-start p-4 rounded-none border border-border hover:border-accent hover:bg-surface-hover transition-colors min-h-14 group"
        >
          <span className="flex items-center gap-1.5 text-xs font-semibold text-muted uppercase tracking-wider mb-1">
            <IconArrowBack />
            <span>Previous</span>
          </span>
          <span className="text-base font-semibold text-primary group-hover:text-accent">
            {prev.navTitle}
          </span>
        </a>
      ) : (
        <div />
      )}

      {next ? (
        <a
          href={`/${next.slug}`}
          onClick={(e) => {
            e.preventDefault();
            onNavigate(next.slug);
          }}
          className="flex flex-col items-end p-4 rounded-none border border-border hover:border-accent hover:bg-surface-hover transition-colors min-h-14 group text-right"
        >
          <span className="flex items-center gap-1.5 text-xs font-semibold text-muted uppercase tracking-wider mb-1">
            <span>Next</span>
            <IconArrowForward />
          </span>
          <span className="text-base font-semibold text-primary group-hover:text-accent">
            {next.navTitle}
          </span>
        </a>
      ) : (
        <div />
      )}
    </nav>
  );
};