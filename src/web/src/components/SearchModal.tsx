import React, { useState, useEffect, useRef } from "react";
import type { Topic } from "../types";
import { IconSearch, IconClose } from "./Icons";

interface SearchModalProps {
  topics: Topic[];
  onSelectTopic: (topic: Topic) => void;
  onClose: () => void;
}

export const SearchModal: React.FC<SearchModalProps> = ({
  topics,
  onSelectTopic,
  onClose,
}) => {
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const timer = setTimeout(() => inputRef.current?.focus(), 50);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onClose]);

  const q = query.trim().toLowerCase();

  const results = q
    ? topics.flatMap((t) => {
        const matches: Array<{
          topic: Topic;
          title: string;
          sub?: string;
          anchor?: string;
        }> = [];

        if (
          t.navTitle.toLowerCase().includes(q) ||
          t.description.toLowerCase().includes(q)
        ) {
          matches.push({ topic: t, title: t.title, sub: t.description });
        }

        t.headings.forEach((h) => {
          if (h.title.toLowerCase().includes(q)) {
            matches.push({
              topic: t,
              title: `${t.navTitle} › ${h.title}`,
              anchor: h.id,
            });
          }
        });

        t.questions.forEach((question) => {
          if (question.title.toLowerCase().includes(q)) {
            matches.push({
              topic: t,
              title: `${t.navTitle} › ${question.title}`,
              anchor: `question-${question.number}`,
            });
          }
        });

        return matches;
      })
    : [];

  const handleSelect = (topic: Topic, anchor?: string) => {
    onSelectTopic(topic);
    onClose();
    if (anchor) {
      setTimeout(() => {
        document.getElementById(anchor)?.scrollIntoView({ behavior: "smooth" });
      }, 100);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && results[0]) {
      e.preventDefault();
      handleSelect(results[0].topic, results[0].anchor);
    }
  };

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-label="Site search"
      className="fixed inset-0 z-50 flex items-start justify-center pt-16 px-4 pb-4 bg-black/50"
      onClick={onClose}
    >
      <div
        className="w-full max-w-xl bg-surface border border-border rounded-none shadow-none overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center border-b border-border-subtle">
          <IconSearch className="text-muted mx-3 shrink-0" />
          <input
            ref={inputRef}
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Search topics, headings, questions..."
            className="flex-1 h-14 bg-transparent border-0 text-base text-primary outline-none placeholder:text-muted"
            autoComplete="off"
          />
          <button
            type="button"
            onClick={onClose}
            aria-label="Close search"
            className="h-14 w-12 flex items-center justify-center text-muted hover:bg-accent hover:text-accent-fg transition-colors outline-none focus-visible:ring-2 focus-visible:ring-focus-ring focus-visible:ring-inset"
          >
            <IconClose />
          </button>
        </div>

        <div className="max-h-[60vh] overflow-y-auto">
          {q === "" ? (
            <div className="p-6 text-center">
              <IconSearch
                className="mx-auto text-muted mb-3"
                style={{ width: 32, height: 32 }}
              />
              <p className="text-sm text-secondary">
                Type a keyword to search all lessons and practice questions.
              </p>
              <p className="mt-2 text-xs text-muted">
                Press{" "}
                <kbd className="px-1.5 py-0.5 bg-surface-hover rounded-none text-secondary font-mono">
                  Ctrl K
                </kbd>{" "}
                to open search
              </p>
            </div>
          ) : results.length === 0 ? (
            <div className="p-6 text-center">
              <p className="text-sm text-secondary">
                No results found for &ldquo;{query}&rdquo;.
              </p>
            </div>
          ) : (
            <ul className="divide-y divide-border-subtle">
              {results.map((res, idx) => (
                <li key={idx}>
                  <button
                    type="button"
                    onClick={() => handleSelect(res.topic, res.anchor)}
                    className={`w-full text-left px-4 py-3 hover:bg-surface-hover transition-colors text-sm outline-none focus-visible:bg-surface-hover ${
                      idx === 0 ? "border-l-4 border-accent pl-3" : ""
                    }`}
                  >
                    <div className="font-medium text-primary flex items-center gap-2">
                      {res.anchor && (
                        <span className="text-xs px-1.5 py-0.5 bg-accent-subtle text-accent rounded-none font-mono">
                          {res.anchor.startsWith("question")
                            ? "Question"
                            : "Section"}
                        </span>
                      )}
                      {res.title}
                    </div>
                    {res.sub && (
                      <div className="text-xs text-secondary truncate mt-1">
                        {res.sub}
                      </div>
                    )}
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
        <div className="px-4 py-2 border-t border-border-subtle bg-surface-hover">
          <p className="text-xs text-muted text-center">
            Enter to open first result · Esc to close
          </p>
        </div>
      </div>
    </div>
  );
};

export default SearchModal;
