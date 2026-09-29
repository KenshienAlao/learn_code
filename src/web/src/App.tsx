import { createContext, useContext, useState, useEffect } from "react";
import { Routes, Route, useNavigate, Outlet, useLocation } from "react-router-dom";
import rawTopics from "./data/topics.json";
import type { Topic, Theme, FontSize } from "./types";
import { Header } from "./components/Header";
import { TopicNavigation } from "./components/TopicNavigation";
import { TableOfContents } from "./components/TableOfContents";
import { MarkdownRenderer } from "./components/MarkdownRenderer";
import { PracticeSection } from "./components/PracticeSection";
import { PrevNextNav } from "./components/PrevNextNav";
import { ReadingProgress } from "./components/ReadingProgress";
import { SettingsPage } from "./components/SettingsPage";
import { TocObserverProvider } from "./components/TocObserverContext";

const topics = rawTopics as Topic[];

function getTopicFromPath(path: string): Topic {
  const slug = path.replace(/^\/|\/$/g, "");
  return topics.find((t) => t.slug === slug) || topics[0];
}

interface SettingsContextValue {
  theme: Theme;
  setTheme: (theme: Theme) => void;
  fontSize: FontSize;
  setFontSize: (size: FontSize) => void;
}

const SettingsContext = createContext<SettingsContextValue | null>(null);

function SettingsProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>(() => {
    const saved = localStorage.getItem("py-reviewer-theme") as Theme;
    if (saved === "light" || saved === "dark" || saved === "system")
      return saved;
    return "system";
  });

  const [fontSize, setFontSize] = useState<FontSize>(() => {
    const saved = localStorage.getItem("py-reviewer-fontsize") as FontSize;
    return saved === "large" || saved === "xlarge" ? saved : "normal";
  });

  useEffect(() => {
    const root = document.documentElement;
    if (theme === "dark") {
      root.classList.add("dark");
    } else if (theme === "light") {
      root.classList.remove("dark");
    } else {
      const prefersDark = window.matchMedia(
        "(prefers-color-scheme: dark)",
      ).matches;
      if (prefersDark) {
        root.classList.add("dark");
      } else {
        root.classList.remove("dark");
      }
    }
    localStorage.setItem("py-reviewer-theme", theme);
  }, [theme]);

  useEffect(() => {
    if (theme === "system") {
      const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
      const handleChange = () => {
        const root = document.documentElement;
        if (mediaQuery.matches) {
          root.classList.add("dark");
        } else {
          root.classList.remove("dark");
        }
      };
      mediaQuery.addEventListener("change", handleChange);
      return () => mediaQuery.removeEventListener("change", handleChange);
    }
  }, [theme]);

  useEffect(() => {
    if (fontSize === "normal") {
      document.documentElement.removeAttribute("data-font-size");
    } else {
      document.documentElement.setAttribute("data-font-size", fontSize);
    }
    localStorage.setItem("py-reviewer-fontsize", fontSize);
  }, [fontSize]);

  return (
    <SettingsContext.Provider
      value={{ theme, setTheme, fontSize, setFontSize }}
    >
      {children}
    </SettingsContext.Provider>
  );
}

function useSettings() {
  const context = useContext(SettingsContext);
  if (!context) {
    throw new Error("useSettings must be used within a SettingsProvider");
  }
  return context;
}

function ContentLayout() {
  const { theme, setTheme, fontSize, setFontSize } = useSettings();
  const [topicDrawerOpen, setTopicDrawerOpen] = useState(false);
  const [tocDrawerOpen, setTocDrawerOpen] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();

  const currentTopic = getTopicFromPath(location.pathname);

  useEffect(() => {
    document.title = `${currentTopic.title}`;
  }, [currentTopic]);

  const handleSelectTopic = (topic: Topic) => {
    navigate(topic.path, { replace: false });
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <TocObserverProvider>
      <div className="min-h-screen flex flex-col bg-page text-body">
        <a href="#main-content" className="skip-link">
          Skip to main content
        </a>

        <ReadingProgress />

        <Header
          topics={topics}
          theme={theme}
          onThemeChange={setTheme}
          fontSize={fontSize}
          onFontSizeChange={setFontSize}
          onSelectTopic={handleSelectTopic}
          onOpenTopicDrawer={() => setTopicDrawerOpen(true)}
          onOpenTocDrawer={() => setTocDrawerOpen(true)}
        />

        <div className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 flex">
          <TopicNavigation
            topics={topics}
            currentTopic={currentTopic}
            onSelectTopic={handleSelectTopic}
          />

          <main
            id="main-content"
            tabIndex={-1}
            className="flex-1 min-w-0 py-8 lg:px-10 focus:outline-hidden"
          >
            <Outlet />
          </main>

          <TableOfContents
            headings={currentTopic.headings}
            questions={currentTopic.questions}
            topicKey={currentTopic.slug}
          />
        </div>

        <footer className="border-t border-border-subtle py-6 text-center text-xs text-muted">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-2">
            <div className="flex items-center gap-4">
              <a href="#top" className="hover:underline">
                Back to top
              </a>
            </div>
          </div>
        </footer>

        {topicDrawerOpen && (
          <div
            role="dialog"
            aria-modal="true"
            aria-label="Navigation drawer"
            className="fixed inset-0 z-50 flex lg:hidden bg-black/50"
            onClick={() => setTopicDrawerOpen(false)}
          >
            <div
              className="w-4/5 max-w-xs bg-surface h-full shadow-none overflow-y-auto"
              onClick={(e) => e.stopPropagation()}
            >
              <TopicNavigation
                topics={topics}
                currentTopic={currentTopic}
                onSelectTopic={handleSelectTopic}
                isMobileDrawer
                onCloseDrawer={() => setTopicDrawerOpen(false)}
              />
            </div>
          </div>
        )}

        {tocDrawerOpen && (
          <div
            role="dialog"
            aria-modal="true"
            aria-label="Table of contents drawer"
            className="fixed inset-0 z-50 flex justify-end xl:hidden bg-black/50"
            onClick={() => setTocDrawerOpen(false)}
          >
            <div
              className="w-4/5 max-w-xs bg-surface h-full shadow-none overflow-y-auto"
              onClick={(e) => e.stopPropagation()}
            >
              <TableOfContents
                headings={currentTopic.headings}
                questions={currentTopic.questions}
                topicKey={currentTopic.slug}
                isMobileDrawer
                onCloseDrawer={() => setTocDrawerOpen(false)}
              />
            </div>
          </div>
        )}
      </div>
    </TocObserverProvider>
  );
}

function TopicPage() {
  const location = useLocation();
  const currentTopic = getTopicFromPath(location.pathname);

  const handleNavigateBySlug = (slug: string) => {
    if (topics.find((t) => t.slug === slug)) {
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  };

  return (
    <>
      <article className="max-w-[72ch] mx-auto lg:mx-0">
        <MarkdownRenderer content={currentTopic.markdown} />

        {currentTopic.questions.length > 0 && (
          <PracticeSection questions={currentTopic.questions} />
        )}

        <PrevNextNav
          prev={currentTopic.prev}
          next={currentTopic.next}
          onNavigate={handleNavigateBySlug}
        />
      </article>
    </>
  );
}

function SettingsRoute() {
  const navigate = useNavigate();
  const { theme, setTheme, fontSize, setFontSize } = useSettings();

  return (
    <SettingsPage
      theme={theme}
      onThemeChange={setTheme}
      fontSize={fontSize}
      onFontSizeChange={setFontSize}
      onBack={() => navigate(-1)}
    />
  );
}

function SettingsLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-page">{children}</div>
  );
}

export function App() {
  return (
    <SettingsProvider>
      <Routes>
        <Route
          path="/settings"
          element={
            <SettingsLayout>
              <SettingsRoute />
            </SettingsLayout>
          }
        />

        <Route element={<ContentLayout />}>
          <Route path="*" element={<TopicPage />} />
        </Route>
      </Routes>
    </SettingsProvider>
  );
}

export default App;