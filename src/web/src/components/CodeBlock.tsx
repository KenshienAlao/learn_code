import React, { useState } from "react";
import { IconCopy, IconCheck } from "./Icons";

interface CodeBlockProps {
  code: string;
  language?: string;
  filename?: string;
}

function highlightPython(code: string): React.ReactNode[] {
  const lines = code.split("\n");

  return lines.map((line, lineIndex) => {
    const tokens: React.ReactNode[] = [];
    let i = 0;

    while (i < line.length) {
      if (line[i] === "#") {
        tokens.push(
          <span key={`c-${i}`} className="text-code-dim italic">
            {line.slice(i)}
          </span>,
        );
        // eslint-disable-next-line no-useless-assignment
        i = line.length;
        break;
      }

      if (
        line.slice(i, i + 3) === '"""' ||
        line.slice(i, i + 3) === "'''" ||
        (i > 0 &&
          line[i - 1]?.toLowerCase() === "f" &&
          (line.slice(i, i + 3) === '"""' || line.slice(i, i + 3) === "'''"))
      ) {
        const quote = line.slice(i, i + 3);
        const endIdx = line.indexOf(quote, i + 3);
        if (endIdx !== -1) {
          const str = line.slice(i, endIdx + 3);
          tokens.push(
            <span key={`tqs-${i}`} className="text-code-string">
              {str}
            </span>,
          );
          i = endIdx + 3;
          continue;
        } else {
          tokens.push(
            <span key={`tqs-${i}`} className="text-code-string">
              {line.slice(i)}
            </span>,
          );
          break;
        }
      }

      if (line[i] === '"' || line[i] === "'") {
        const quote = line[i];
        let j = i + 1;
        while (j < line.length && line[j] !== quote) {
          if (line[j] === "\\") j++;
          j++;
        }
        const str = line.slice(i, j + 1);
        tokens.push(
          <span key={`s-${i}`} className="text-code-string">
            {str}
          </span>,
        );
        i = j + 1;
        continue;
      }

      const wordMatch = line.slice(i).match(/^[a-zA-Z_][a-zA-Z0-9_]*/);
      if (wordMatch) {
        const word = wordMatch[0];
        const keywords = [
          "def",
          "class",
          "if",
          "elif",
          "else",
          "for",
          "while",
          "return",
          "in",
          "import",
          "from",
          "as",
          "try",
          "except",
          "finally",
          "raise",
          "with",
          "pass",
          "break",
          "continue",
          "lambda",
          "yield",
          "not",
          "and",
          "or",
          "is",
          "None",
          "True",
          "False",
        ];
        const builtins = [
          "print",
          "len",
          "range",
          "int",
          "float",
          "str",
          "bool",
          "list",
          "dict",
          "set",
          "tuple",
          "type",
          "divmod",
          "enumerate",
          "zip",
          "sum",
          "min",
          "max",
        ];

        if (keywords.includes(word)) {
          tokens.push(
            <span key={`kw-${i}`} className="text-code-keyword font-semibold">
              {word}
            </span>,
          );
        } else if (builtins.includes(word)) {
          tokens.push(
            <span key={`b-${i}`} className="text-code-builtin">
              {word}
            </span>,
          );
        } else {
          tokens.push(word);
        }
        i += word.length;
        continue;
      }

      const numMatch = line.slice(i).match(/^[0-9]+(\.[0-9]+)?/);
      if (numMatch) {
        tokens.push(
          <span key={`n-${i}`} className="text-code-number">
            {numMatch[0]}
          </span>,
        );
        i += numMatch[0].length;
        continue;
      }

      tokens.push(line[i]);
      i++;
    }

    return (
      <div key={`line-${lineIndex}`} className="table-row leading-relaxed">
        <span className="table-cell select-none pr-4 text-right text-code-dim text-xs w-8">
          {lineIndex + 1}
        </span>
        <span className="table-cell">
          {tokens.length > 0 ? tokens : "\u00A0"}
        </span>
      </div>
    );
  });
}

export const CodeBlock: React.FC<CodeBlockProps> = ({
  code,
  language = "python",
  filename,
}) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      alert("Unable to copy code. Please select and copy it manually.");
    }
  };

  return (
    <div className="relative group my-4 rounded-none border border-code-border bg-code-bg text-code-text overflow-hidden">
      <div className="flex items-center justify-between px-4 py-2 bg-code-header border-b border-code-border text-xs font-mono text-code-dim">
        <span className="font-medium tracking-wide uppercase">
          {filename || language}
        </span>
        <button
          type="button"
          onClick={handleCopy}
          aria-label={copied ? "Copied to clipboard" : "Copy code"}
          className="flex items-center justify-center h-10 w-10 min-h-0 min-w-0 rounded-none bg-transparent hover:bg-accent hover:text-accent-fg transition-colors text-code-text active:scale-95"
        >
          {copied ? (
            <>
              <IconCheck className="text-accent" />
            </>
          ) : (
            <IconCopy className="text-code-dim" />
          )}
        </button>
      </div>

      <pre
        className="p-4 overflow-x-auto text-[0.875rem] font-mono leading-relaxed"
        tabIndex={0}
      >
        <code className="table w-full">
          {language === "python" || language === "py"
            ? highlightPython(code)
            : code}
        </code>
      </pre>
    </div>
  );
};
