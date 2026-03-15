// types.ts
export interface ScriptConfig {
  name: string;
  description: string;
  args: { [key: string]: string };
}

export interface ScriptResult {
  success: boolean;
  output: string;
  error?: string;
}

export type ScriptFunction = (config: ScriptConfig) => Promise<ScriptResult>;

export interface DevOpsScript {
  id: string;
  name: string;
  description: string;
  run: ScriptFunction;
}

export enum ScriptStatus {
  PENDING = 'pending',
  RUNNING = 'running',
  SUCCESS = 'success',
  FAILURE = 'failure',
}