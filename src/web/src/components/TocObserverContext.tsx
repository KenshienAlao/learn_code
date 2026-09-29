import {
  createContext,
  useContext,
  useState,
  useEffect,
  useRef,
  useCallback,
  type ReactNode,
} from "react";

type ElementType = "heading" | "question";

interface RegisteredElement {
  id: string;
  type: ElementType;
  element: Element;
}

interface TocObserverValue {
  activeId: string;
  activeQuestionId: string;
  registerElements: (elements: RegisteredElement[]) => void;
  resetForTopic: (topicKey: string) => void;
}

const TocObserverContext = createContext<TocObserverValue | null>(null);
// eslint-disable-next-line react-refresh/only-export-components
export function useTocObserver(): TocObserverValue {
  const ctx = useContext(TocObserverContext);
  if (!ctx) {
    throw new Error("useTocObserver must be used within TocObserverProvider");
  }
  return ctx;
}

interface TocObserverProviderProps {
  children: ReactNode;
}

export function TocObserverProvider({ children }: TocObserverProviderProps) {
  const [activeId, setActiveId] = useState("");
  const [activeQuestionId, setActiveQuestionId] = useState("");
  const observerRef = useRef<IntersectionObserver | null>(null);
  const registeredElementsRef = useRef<Map<string, RegisteredElement>>(new Map());
  const currentTopicKeyRef = useRef<string>("");

  useEffect(() => {
    observerRef.current = new IntersectionObserver(
      (entries) => {
        const intersecting: Array<{ id: string; rect: DOMRect }> = [];

        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            intersecting.push({
              id: entry.target.id,
              rect: entry.boundingClientRect,
            });
          }
        });

        if (intersecting.length === 0) return;

        intersecting.sort((a, b) => a.rect.top - b.rect.top);
        const closest = intersecting[0];

        if (closest.id.startsWith("question-")) {
          setActiveQuestionId((prev) => (prev !== closest.id ? closest.id : prev));
        } else {
          setActiveId((prev) => (prev !== closest.id ? closest.id : prev));
        }
      },
      { rootMargin: "-80px 0% -60% 0%", threshold: 0 },
    );

    return () => observerRef.current?.disconnect();
  }, []);

  const resetForTopic = useCallback((topicKey: string) => {
    if (currentTopicKeyRef.current === topicKey) return;

    if (observerRef.current) {
      registeredElementsRef.current.forEach(({ id }) => {
        const el = document.getElementById(id);
        if (el) observerRef.current!.unobserve(el);
      });
    }

    registeredElementsRef.current.clear();
    currentTopicKeyRef.current = topicKey;
    setActiveId("");
    setActiveQuestionId("");
  }, []);

  const registerElements = useCallback(
    (elements: RegisteredElement[]) => {
      if (!observerRef.current) return;

      elements.forEach(({ id, type, element }) => {
        if (registeredElementsRef.current.has(id)) return;

        observerRef.current!.observe(element);
        registeredElementsRef.current.set(id, { id, type, element });
      });
    },
    [],
  );

  return (
    <TocObserverContext.Provider
      value={{ activeId, activeQuestionId, registerElements, resetForTopic }}
    >
      {children}
    </TocObserverContext.Provider>
  );
}