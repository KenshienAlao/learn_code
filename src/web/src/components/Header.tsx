import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import type { Topic, Theme, FontSize } from "../types";
import { IconHamburger, IconSearch, IconList, IconSettings } from "./Icons";
import SearchModal from "./SearchModal";

interface HeaderProps {
  topics: Topic[];
  theme: Theme;
  onThemeChange: (theme: Theme) => void;
  fontSize: FontSize;
  onFontSizeChange: (size: FontSize) => void;
  onSelectTopic: (topic: Topic) => void;
  onOpenTopicDrawer: () => void;
  onOpenTocDrawer: () => void;
}

const headerButton =
  "flex items-center justify-center h-12 w-12 text-slate-200 hover:bg-accent hover:text-accent-fg transition-colors";

export const Header: React.FC<HeaderProps> = ({
  topics,
  onSelectTopic,
  onOpenTopicDrawer,
  onOpenTocDrawer,
}) => {
  const [searchOpen, setSearchOpen] = useState(false);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setSearchOpen((prev) => !prev);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  return (
    <>
      <header className="sticky top-0 z-40 w-full h-12 bg-header border-b border-border-subtle">
        <div className="max-w-7xl mx-auto flex items-center justify-between h-full px-4">
          <div className="flex items-center gap-1">
            <button
              type="button"
              onClick={onOpenTopicDrawer}
              aria-label="Open topics menu"
              className={`${headerButton} lg:hidden`}
            >
              <span
                className="transition-transform duration-150 ease-out"
                aria-hidden="true"
              >
                <IconHamburger />
              </span>
            </button>

            <button
              type="button"
              onClick={() => setSearchOpen(true)}
              aria-label="Search lessons (Ctrl+K)"
              className={headerButton}
            >
              <IconSearch className="shrink-0" />
            </button>
          </div>

          <div className="flex items-center gap-1">
            <button
              type="button"
              onClick={onOpenTocDrawer}
              aria-label="Table of contents"
              className={`${headerButton} xl:hidden`}
            >
              <IconList />
            </button>
            <Link to="/settings" aria-label="Settings" className={headerButton}>
              <IconSettings />
            </Link>
          </div>
        </div>
      </header>

      {searchOpen && (
        <SearchModal
          topics={topics}
          onSelectTopic={onSelectTopic}
          onClose={() => setSearchOpen(false)}
        />
      )}
    </>
  );
};

export default Header;
