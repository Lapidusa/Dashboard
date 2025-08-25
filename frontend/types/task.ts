export type Status = 0 | 1 | 2;

export type Task = {
  id?: string;
  title: string;
  description: string;
  is_hidden?: boolean;
  status?: Status;
  position?: number;
}
