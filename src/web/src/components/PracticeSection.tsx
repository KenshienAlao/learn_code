import React, { useState } from "react";
import type { Question } from "../types";
import { CodeBlock } from "./CodeBlock";

interface PracticeSectionProps {
  questions: Question[];
}

export const PracticeSection: React.FC<PracticeSectionProps> = ({
  questions,
}) => {
  const [activeTabByQuestion, setActiveTabByQuestion] = useState<
    Record<string, "starter" | "solution">
  >({});

  const setTab = (qId: string, tab: "starter" | "solution") => {
    setActiveTabByQuestion((prev) => ({ ...prev, [qId]: tab }));
  };

  return (
    <section id="practice" className="mt-12 pt-8 border-t border-border-subtle">
      <div className="mb-6">
        <h2 className="text-2xl font-bold tracking-tight text-primary">
          Practice Questions
        </h2>
        <p className="text-sm text-secondary mt-1">
          Complete the coding challenges below. Each problem is self-contained
          and runnable without user input. Try the starter code before checking
          the solution.
        </p>
      </div>

      <div className="space-y-8">
        {questions.map((q) => {
          const activeTab = activeTabByQuestion[q.id] || "starter";

          return (
            <div
              key={q.id}
              id={`question-${q.number}`}
              className="border border-border rounded-none p-5 bg-surface-hover"
            >
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-border-subtle">
                <div className="flex items-center gap-2">
                  <span className="inline-flex items-center justify-center w-7 h-7 rounded-full bg-accent-subtle text-accent text-xs font-bold">
                    Q{q.number}
                  </span>
                  <h3 className="text-base font-semibold text-primary">
                    {q.title}
                  </h3>
                </div>
                <div className="inline-flex rounded-none bg-surface-hover p-0.5 text-xs font-medium">
                  <button
                    type="button"
                    onClick={() => setTab(q.id, "starter")}
                    className={`px-3 py-1.5 rounded-none transition-colors ${
                      activeTab === "starter"
                        ? "bg-surface text-primary"
                        : "text-secondary hover:text-primary"
                    }`}
                  >
                    Starter
                  </button>
                  <button
                    type="button"
                    onClick={() => setTab(q.id, "solution")}
                    className={`px-3 py-1.5 rounded-none transition-colors ${
                      activeTab === "solution"
                        ? "bg-accent text-accent-fg"
                        : "text-secondary hover:text-primary"
                    }`}
                  >
                    Solution
                  </button>
                </div>
              </div>

              <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                {q.inputText && (
                  <div className="p-3 rounded-none bg-surface border border-border">
                    <span className="font-semibold text-muted uppercase tracking-wider block mb-1">
                      Expected Input
                    </span>
                    <pre className="font-mono text-body whitespace-pre-wrap">
                      {q.inputText}
                    </pre>
                  </div>
                )}
                {q.outputText && (
                  <div className="p-3 rounded-none bg-surface border border-border">
                    <span className="font-semibold text-muted uppercase tracking-wider block mb-1">
                      Expected Output
                    </span>
                    <pre className="font-mono text-body whitespace-pre-wrap">
                      {q.outputText}
                    </pre>
                  </div>
                )}
              </div>

              {q.tipText && (
                <div className="mt-3 flex items-start gap-2 p-3 text-xs bg-warning-bg text-warning border border-warning-border rounded-none">
                  <p>
                    <strong className="font-semibold">Tip: </strong>
                    {q.tipText}
                  </p>
                </div>
              )}

              <div className="mt-4">
                {activeTab === "starter" ? (
                  <CodeBlock
                    code={q.starterCode || q.fullCode}
                    language="python"
                    filename={`question_${q.number.toString().padStart(2, "0")}.py (Starter)`}
                  />
                ) : (
                  <CodeBlock
                    code={q.solutionCode || q.fullCode}
                    language="python"
                    filename={`question_${q.number.toString().padStart(2, "0")}.py (Solution)`}
                  />
                )}
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
};
