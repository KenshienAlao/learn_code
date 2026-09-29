import React from "react";
import type { Theme, FontSize } from "../types";
import { IconSun, IconMoon, IconMonitor, IconArrowBack } from "./Icons";

interface SettingsPageProps {
  theme: Theme;
  onThemeChange: (theme: Theme) => void;
  fontSize: FontSize;
  onFontSizeChange: (size: FontSize) => void;
  onBack?: () => void;
}

interface Option<T extends string> {
  value: T;
  label: string;
  description: string;
  icon?: React.ReactNode;
}

const THEME_OPTIONS: Array<Option<Theme>> = [
  {
    value: "light",
    label: "Light",
    description: "Always use light mode",
    icon: <IconSun />,
  },
  {
    value: "dark",
    label: "Dark",
    description: "Always use dark mode",
    icon: <IconMoon />,
  },
  {
    value: "system",
    label: "System",
    description: "Match your operating system",
    icon: <IconMonitor />,
  },
];

const FONT_SIZE_OPTIONS: Array<Option<FontSize>> = [
  { value: "normal", label: "Default", description: "Standard text size" },
  { value: "large", label: "Large", description: "Increased text size" },
  { value: "xlarge", label: "Extra large", description: "Maximum text size" },
];

interface OptionGroupProps<T extends string> {
  title: string;
  description: string;
  options: Array<Option<T>>;
  value: T;
  onChange: (value: T) => void;
}

function OptionGroup<T extends string>({
  title,
  description,
  options,
  value,
  onChange,
}: OptionGroupProps<T>) {
  return (
    <section className="mb-8">
      <h2 className="text-base font-semibold text-primary">{title}</h2>
      <p className="text-sm text-secondary mb-3">{description}</p>

      <div
        role="radiogroup"
        aria-label={title}
        className="border border-border divide-y divide-border-subtle rounded-none"
      >
        {options.map((option) => {
          const selected = option.value === value;
          return (
            <button
              key={option.value}
              type="button"
              role="radio"
              aria-checked={selected}
              onClick={() => onChange(option.value)}
              className="w-full flex items-center gap-3 px-4 py-3 text-left hover:bg-surface-hover transition-colors"
            >
              <span
                className={`flex items-center justify-center w-5 h-5 shrink-0 rounded-full border-2 ${
                  selected ? "border-accent" : "border-muted"
                }`}
                aria-hidden="true"
              >
                {selected && (
                  <span className="w-2.5 h-2.5 rounded-full bg-accent" />
                )}
              </span>

              {option.icon && (
                <span className="w-5 h-5 shrink-0 text-muted">
                  {option.icon}
                </span>
              )}

              <span className="flex-1 min-w-0">
                <span className="block text-sm font-medium text-primary">
                  {option.label}
                </span>
                <span className="block text-xs text-secondary">
                  {option.description}
                </span>
              </span>
            </button>
          );
        })}
      </div>
    </section>
  );
}

export const SettingsPage: React.FC<SettingsPageProps> = ({
  theme,
  onThemeChange,
  fontSize,
  onFontSizeChange,
  onBack,
}) => {
  return (
    <div className="min-h-screen bg-page">
      <header className="sticky top-0 z-40 w-full h-12 bg-header border-b border-border-subtle">
        <div className="max-w-2xl mx-auto flex items-center h-full">
          {onBack && (
            <button
              type="button"
              onClick={onBack}
              aria-label="Back"
              className="flex items-center justify-center h-12 w-12 text-slate-200 hover:bg-accent hover:text-accent-fg transition-colors"
            >
              <IconArrowBack />
            </button>
          )}
          <h1 className={`text-base font-semibold text-slate-200 ${onBack ? "" : "px-4"}`}>
            Settings
          </h1>
        </div>
      </header>

      <main className="max-w-2xl mx-auto px-4 sm:px-6 py-8">
        <OptionGroup
          title="Theme"
          description="Choose your preferred color scheme."
          options={THEME_OPTIONS}
          value={theme}
          onChange={onThemeChange}
        />

        <OptionGroup
          title="Font size"
          description="Adjust the text size across the application."
          options={FONT_SIZE_OPTIONS}
          value={fontSize}
          onChange={onFontSizeChange}
        />
      </main>
    </div>
  );
};