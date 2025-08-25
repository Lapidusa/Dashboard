import { useTask } from "./useTask";
import {useTaskStore} from "../stores/taskStore";

let socket: WebSocket | null = null;
const urlWebsocket: string = import.meta.env.VITE_API_WEBSOCKET;
export const useTaskWebSocket = () => {
  const taskStore = useTaskStore()

  const connect = (url: string = urlWebsocket) => {
    socket = new WebSocket(url);

    socket.onmessage = async (event) => {
      const data = event.data;

      if (data === "tasks_updated") {
        await taskStore.fetchTasks()
      }
    };
  };

  return { connect };
};
