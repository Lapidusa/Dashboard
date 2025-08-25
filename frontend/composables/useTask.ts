import {useApi} from "./api";
import {apiRoutes} from "./api-routes";
import type {Task} from "../types/task";

export const useTask = () => {
  const api = useApi();

  const getTasks = async () => {
    try {
      const res = await api.get(apiRoutes.task())
      return res.data;
    }catch (error) {
      throw error;
    }
  }

  const addTask = async (task: Task) => {
    try {
      const res = await api.post(apiRoutes.task("create-task"), task);
      return res.data;
    }catch (error) {
      throw error;
    }
  }

  const updateTask = async (task: Task) => {
    if (!task.id) {
      return 'Нет id';
    }
    try {
      const res = await api.put(apiRoutes.task(`${task.id}`), task);
      return res.data;
    }catch (error) {
      throw error;
    }
  }

  const hideTask = async (taskId: string) => {
    try {
      const res = await api.delete(apiRoutes.task(`soft-delete-task/${taskId}`));
      return res.data;
    }catch (error) {
      throw error;
    }
  }

  const restoreTask = async (taskId: string) => {
    try {
      const res = await api.patch(apiRoutes.task(`restore-task/${taskId}`));
      return res.data;
    }catch (error) {
      throw error;
    }
  }

  const deleteTask = async (taskId: string) => {
    try {
      const res = await api.delete(apiRoutes.task(`${taskId}`));
      return res.data;
    }catch (error) {
      throw error;
    }
  }

  return {
    getTasks,
    addTask,
    updateTask,
    hideTask,
    restoreTask,
    deleteTask
  };
}
