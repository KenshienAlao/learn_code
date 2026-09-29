import React from "react";
import { CodeBlock } from "./CodeBlock";
import { IconLink } from "./Icons";

interface MarkdownRendererProps {
  content: string;
}

export const MarkdownRenderer: React.FC<MarkdownRendererProps> = ({
  content,
}) => {
  const lines = content.split("\n");
  const elements: React.ReactNode[] = [];

  let i = 0;
  let keyCount = 0;

  while (i < lines.length) {
    const line = lines[i];

    if (line.trim().startsWith("```")) {
      const lang = line.trim().slice(3).trim() || "text";
      const codeLines: string[] = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith("```")) {
        codeLines.push(lines[i]);
        i++;
      }
      i++;
      elements.push(
        <CodeBlock
          key={`code-${keyCount++}`}
          code={codeLines.join("\n")}
          language={lang}
        />,
      );
      continue;
    }

    if (line.trim().startsWith("|") && line.trim().endsWith("|")) {
      const tableLines: string[] = [];
      while (i < lines.length && lines[i].trim().startsWith("|")) {
        tableLines.push(lines[i]);
        i++;
      }

      if (tableLines.length >= 2) {
        const headerCells = tableLines[0]
          .split("|")
          .slice(1, -1)
          .map((c) => c.trim());
        const bodyRows = tableLines.slice(2).map((row) =>
          row
            .split("|")
            .slice(1, -1)
            .map((c) => c.trim()),
        );

        elements.push(
          <div
            key={`table-${keyCount++}`}
            className="my-6 overflow-x-auto rounded-none border border-border"
          >
            <table className="w-full text-left text-sm border-collapse">
              <thead className="bg-code-header text-body font-semibold border-b border-border">
                <tr>
                  {headerCells.map((h, hIdx) => (
                    <th key={`th-${hIdx}`} className="py-2.5 px-4">
                      {renderInline(h)}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody className="divide-y divide-border-subtle text-body">
                {bodyRows.map((row, rIdx) => (
                  <tr key={`tr-${rIdx}`} className="hover:bg-surface-hover">
                    {row.map((cell, cIdx) => (
                      <td key={`td-${cIdx}`} className="py-2 px-4">
                        {renderInline(cell)}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>,
        );
        continue;
      }
    }

    if (line.trim() === "---") {
      elements.push(
        <hr
          key={`hr-${keyCount++}`}
          className="my-8 border-t border-border-subtle"
        />,
      );
      i++;
      continue;
    }

    if (line.startsWith("# ")) {
      const title = line.slice(2).trim();
      elements.push(
        <h1
          key={`h1-${keyCount++}`}
          className="text-3xl font-extrabold tracking-tight text-primary mb-4"
        >
          {title}
        </h1>,
      );
      i++;
      continue;
    }

    if (line.startsWith("## ")) {
      const heading = line.slice(3).trim();
      const slug = heading
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/(^-|-$)/g, "");

      elements.push(
        <div
          key={`h2-wrap-${keyCount++}`}
          className="group relative mt-10 mb-4"
        >
          <h2
            id={slug}
            className="text-xl sm:text-2xl font-bold tracking-tight text-primary flex items-center gap-2"
          >
            <span>{heading}</span>
            <a
              href={`#${slug}`}
              className="text-muted hover:text-accent opacity-0 group-hover:opacity-100 focus:opacity-100 transition-opacity p-1 rounded-none"
              aria-label={`Link to ${heading}`}
            >
              <IconLink />
            </a>
          </h2>
        </div>,
      );
      i++;
      continue;
    }

    if (line.startsWith("### ")) {
      const heading = line.slice(4).trim();
      elements.push(
        <h3
          key={`h3-${keyCount++}`}
          className="text-lg font-semibold text-primary mt-6 mb-2"
        >
          {heading}
        </h3>,
      );
      i++;
      continue;
    }

    if (line.trim().startsWith("![") && line.trim().endsWith(")")) {
      const imgMatch = line.trim().match(/^!\[([^\]]*)\]\(([^)]+)\)$/);
      if (imgMatch) {
        const alt = imgMatch[1];
        const src = imgMatch[2];
        elements.push(
          <figure
            key={`img-${keyCount++}`}
            className="my-6 flex flex-col items-center"
          >
            <div className="rounded-none border border-code-border bg-code-bg p-2 shadow-none overflow-hidden max-w-full">
              <img
                src={src}
                alt={alt}
                loading="lazy"
                className="max-h-90 w-auto object-contain rounded-none"
              />
            </div>
            {alt && (
              <figcaption className="mt-2 text-xs text-muted text-center font-medium">
                {alt}
              </figcaption>
            )}
          </figure>,
        );
        i++;
        continue;
      }
    }

    if (line.trim().startsWith("- ") || line.trim().startsWith("* ")) {
      const bulletLines: string[] = [];
      while (
        i < lines.length &&
        (lines[i].trim().startsWith("- ") || lines[i].trim().startsWith("* "))
      ) {
        bulletLines.push(lines[i].trim().slice(2));
        i++;
      }

      elements.push(
        <ul
          key={`ul-${keyCount++}`}
          className="my-4 pl-6 list-disc space-y-1.5 text-body"
        >
          {bulletLines.map((b, bIdx) => (
            <li key={`li-${bIdx}`} className="leading-relaxed">
              {renderInline(b)}
            </li>
          ))}
        </ul>,
      );
      continue;
    }

    if (!line.trim()) {
      i++;
      continue;
    }

    const paragraphLines: string[] = [];
    while (
      i < lines.length &&
      lines[i].trim() &&
      !lines[i].startsWith("#") &&
      !lines[i].trim().startsWith("```") &&
      !lines[i].trim().startsWith("|") &&
      !lines[i].trim().startsWith("- ") &&
      !lines[i].trim().startsWith("* ") &&
      !lines[i].trim().startsWith("![") &&
      lines[i].trim() !== "---"
    ) {
      paragraphLines.push(lines[i]);
      i++;
    }

    elements.push(
      <p key={`p-${keyCount++}`} className="my-3 text-body leading-relaxed">
        {renderInline(paragraphLines.join(" "))}
      </p>,
    );
  }

  return <div className="markdown-content">{elements}</div>;
};

function renderInline(text: string): React.ReactNode {
  const tokens: React.ReactNode[] = [];
  const regex = /(`[^`]+`|\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\))/g;
  let lastIndex = 0;
  let match: RegExpExecArray | null;

  while ((match = regex.exec(text)) !== null) {
    if (match.index > lastIndex) {
      tokens.push(text.slice(lastIndex, match.index));
    }

    const token = match[0];
    if (token.startsWith("`")) {
      tokens.push(
        <code
          key={match.index}
          className="px-1.5 py-0.5 rounded-none text-xs font-mono bg-code-bg text-code-text border border-code-border"
        >
          {token.slice(1, -1)}
        </code>,
      );
    } else if (token.startsWith("**")) {
      tokens.push(
        <strong key={match.index} className="font-semibold text-primary">
          {token.slice(2, -2)}
        </strong>,
      );
    } else if (token.startsWith("[")) {
      const linkMatch = token.match(/\[([^\]]+)\]\(([^)]+)\)/);
      if (linkMatch) {
        const label = linkMatch[1];
        let href = linkMatch[2];

        const questionMatch = href.match(/question_0?(\d+)\.py/);
        if (questionMatch) {
          href = `#question-${parseInt(questionMatch[1], 10)}`;
        }

        tokens.push(
          <a
            key={match.index}
            href={href}
            onClick={(e) => {
              if (href.startsWith("#")) {
                e.preventDefault();
                const targetId = href.slice(1);
                document
                  .getElementById(targetId)
                  ?.scrollIntoView({ behavior: "smooth" });
              }
            }}
            className="text-accent hover:underline font-medium"
          >
            {label}
          </a>,
        );
      }
    }

    lastIndex = regex.lastIndex;
  }

  if (lastIndex < text.length) {
    tokens.push(text.slice(lastIndex));
  }

  return tokens;
}
