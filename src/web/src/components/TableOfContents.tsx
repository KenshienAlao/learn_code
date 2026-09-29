import React, { useEffect, useState } from "react";
import type { Heading, Question } from "../types";
import { IconClose, IconChevronDown, IconChevronUp } from "./Icons";
import { useTocObserver } from "./TocObserverContext";

interface TableOfContentsProps {
  headings: Heading[];
  questions?: Question[];
  topicKey: string;
  isMobileDrawer?: boolean;
  onCloseDrawer?: () => void;
}

export const TableOfContents: React.FC<TableOfContentsProps> = ({
  headings,
  questions,
  topicKey,
  isMobileDrawer = false,
  onCloseDrawer,
}) => {
  const { activeId, activeQuestionId, registerElements, resetForTopic } = useTocObserver();
  const [questionsExpanded, setQuestionsExpanded] = useState(true);

  useEffect(() => {
    resetForTopic(topicKey);
  }, [topicKey, resetForTopic]);

  useEffect(() => {
    const elements: Array<{ id: string; type: "heading" | "question"; element: Element }> = [];

    headings
      .filter((h) => h.title !== "Practice")
      .filter((h, idx, arr) => arr.findIndex((x) => x.id === h.id) === idx)
      .forEach((h) => {
        const el = document.getElementById(h.id);
        if (el) elements.push({ id: h.id, type: "heading", element: el });
      });

    (questions || []).forEach((q) => {
      const el = document.getElementById(`question-${q.number}`);
      if (el) elements.push({ id: `question-${q.number}`, type: "question", element: el });
    });

    registerElements(elements);
  }, [headings, questions, registerElements]);

  const handleScrollTo = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: "smooth" });
      if (isMobileDrawer && onCloseDrawer) {
        onCloseDrawer();
      }
    }
  };

  const filteredHeadings = headings
    .filter((h) => h.title !== "Practice")
    .filter((h, idx, arr) => arr.findIndex((x) => x.id === h.id) === idx);

  return (
    <aside
      aria-label="Table of contents"
      className={`${
        isMobileDrawer
          ? "p-4 space-y-2"
          : "w-60 shrink-0 py-6 pl-6 hidden xl:block overflow-y-auto max-h-[calc(100vh-3.5rem)] sticky top-14"
      }`}
    >
      {isMobileDrawer && (
        <div className="flex items-center justify-between pb-3 mb-2 border-b border-border-subtle">
          <span className="font-semibold text-sm tracking-wider uppercase text-muted">
            On this page
          </span>
          <button
            type="button"
            onClick={onCloseDrawer}
            aria-label="Close table of contents"
            className="p-1 rounded-md text-muted hover:text-primary"
          >
            <IconClose />
          </button>
        </div>
      )}

      <div>
        {!isMobileDrawer && (
          <h2 className="px-2 pb-2 text-xs font-bold uppercase tracking-wider text-muted">
            On This Page
          </h2>
        )}
        <ul className="space-y-1 text-xs">
          {filteredHeadings.map((h) => {
            const isActive = activeId === h.id;

            return (
              <li key={h.id}>
                <a
                  href={`#${h.id}`}
                  onClick={(e) => {
                    e.preventDefault();
                    handleScrollTo(h.id);
                  }}
                  className={`block py-1.5 px-2 rounded-md transition-all ${
                    isActive
                      ? "text-accent font-semibold bg-accent-subtle"
                      : "text-secondary hover:text-primary"
                  }`}
                >
                  {h.title}
                </a>
              </li>
            );
          })}

          {questions && questions.length > 0 && (
            <>
              <li className="mt-4">
                <button
                  type="button"
                  onClick={() => setQuestionsExpanded(!questionsExpanded)}
                  aria-expanded={questionsExpanded}
                  className="flex items-center gap-2 w-full px-2 py-1.5 text-left text-xs font-bold uppercase tracking-wider text-muted hover:text-primary"
                >
                  <span>Questions</span>
                  {questionsExpanded ? (
                    <IconChevronUp className="w-4 h-4 shrink-0" />
                  ) : (
                    <IconChevronDown className="w-4 h-4 shrink-0" />
                  )}
                </button>
              </li>
              {questionsExpanded &&
                questions.map((q) => {
                  const questionId = `question-${q.number}`;
                  const isActive = activeQuestionId === questionId;

                  return (
                    <li key={q.id}>
                      <a
                        href={`#${questionId}`}
                        onClick={(e) => {
                          e.preventDefault();
                          handleScrollTo(questionId);
                        }}
                        className={`block px-4 py-1 text-xs transition-colors ${
                          isActive
                            ? "text-accent font-semibold bg-accent-subtle"
                            : "text-secondary hover:text-primary"
                        }`}
                      >
                        Q{q.number}: {q.title}
                      </a>
                    </li>
                  );
                })}
            </>
          )}
        </ul>
      </div>
    </aside>
  );
};