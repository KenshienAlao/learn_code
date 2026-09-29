export interface Question {
  id: string;
  number: number;
  title: string;
  inputText: string;
  outputText: string;
  tipText: string;
  starterCode: string;
  solutionCode: string;
  fullCode: string;
}

export interface Heading {
  level: number;
  title: string;
  id: string;
}

export interface TopicNavRef {
  slug: string;
  navTitle: string;
}

export interface Topic {
  key: string;
  slug: string;
  path: string;
  navTitle: string;
  title: string;
  description: string;
  markdown: string;
  headings: Heading[];
  questions: Question[];
  prev: TopicNavRef | null;
  next: TopicNavRef | null;
}

export type Theme = "light" | "dark" | "system";
export type FontSize = "normal" | "large" | "xlarge";
