"use client";
import { Component, ReactNode } from "react";

interface State { hasError: boolean; error?: Error }
interface Props { children: ReactNode; fallback?: ReactNode }

export default class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback ?? (
        <div className="p-6 text-center text-red-500">
          <p className="font-semibold">Something went wrong.</p>
          <p className="text-sm mt-1">{this.state.error?.message}</p>
        </div>
      );
    }
    return this.props.children;
  }
}
