import React from "react";
import type { Topic } from "../types";
import { IconClose } from "./Icons";

interface TopicNavigationProps {
  topics: Topic[];
  currentTopic: Topic;
  onSelectTopic: (topic: Topic) => void;
  open?: boolean;
  isMobileDrawer?: boolean;
  onCloseDrawer?: () => void;
}

export const TopicNavigation: React.FC<TopicNavigationProps> = ({
  topics,
  currentTopic,
  onSelectTopic,
  open = true,
  isMobileDrawer = false,
  onCloseDrawer,
}) => {
  const topicItems = (
    <ul role="list">
      {topics.map((t, idx) => {
        const isActive = t.slug === currentTopic.slug;

        return (
          <li key={t.slug}>
            <a
              href={t.path}
              onClick={(e) => {
                e.preventDefault();
                onSelectTopic(t);
                if (isMobileDrawer && onCloseDrawer) onCloseDrawer();
              }}
              aria-current={isActive ? "page" : undefined}
              className={`flex items-center gap-2 px-4 py-2 text-sm border-b border-border-subtle transition-colors ${
                isActive
                  ? "bg-accent text-accent-fg font-semibold"
                  : "text-body hover:bg-surface-hover"
              }`}
            >
              <span
                className={`w-6 shrink-0 tabular-nums ${isActive ? "text-accent-fg" : "text-muted"}`}
              >
                {idx + 1}.
              </span>
              <span className="truncate">{t.navTitle}</span>
            </a>
          </li>
        );
      })}
    </ul>
  );

  if (isMobileDrawer) {
    return (
      <nav aria-label="Topics">
        <div className="flex items-center justify-between h-12 px-4 bg-page border-b border-border-subtle text-primary">
          <span className="text-sm font-semibold">Topics</span>
          <button
            type="button"
            onClick={onCloseDrawer}
            aria-label="Close menu"
            className="h-12 w-12 flex items-center justify-center hover:bg-surface-hover transition-colors"
          >
            <IconClose />
          </button>
        </div>
        {topicItems}
      </nav>
    );
  }

  return (
    <nav
      id="topics-panel"
      aria-label="Topics"
      aria-hidden={!open}
      className={`hidden lg:block shrink-0 sticky top-12 h-[calc(100vh-3rem)] overflow-y-auto overflow-x-hidden bg-surface border-r border-border-subtle transition-[width] duration-200 ${
        open ? "w-64" : "w-0 invisible"
      }`}
    >
      <div className="w-64">{topicItems}</div>
    </nav>
  );
};
