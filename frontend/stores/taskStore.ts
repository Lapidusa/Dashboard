import { defineStore } from "pinia"
import { ref } from "vue"
import { useTask } from "../composables/useTask"
import type {Task} from "../types/task";

export const useTaskStore = defineStore("taskStore", () => {
  const tasks = ref<Task[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const hiddenTasks = ref<Task[]>([])

  const openedForm = ref<'none' | 'add' | 'edit' | 'delete'>('none')

  const { getTasks } = useTask()

  const toggleForm = (type: 'add' | 'edit' | 'delete') => {
    openedForm.value = type
  }

  const closeForm = () => {
    openedForm.value = 'none'
  }

  const handleRequest = async (
    fn: () => Promise<void>,
    options: { refresh?: boolean; closeForm?: boolean } = {}
  ) => {
    loading.value = true
    error.value = null
    try {
      await fn()
      if (options.refresh) await fetchTasks()
      if (options.closeForm) closeForm()
    } catch (e: any) {
      error.value = e.message || "Ошибка при выполнении запроса"
    } finally {
      loading.value = false
    }
  }

  const fetchTasks = async () => {
    loading.value = true
    error.value = null
    try {
      const res = await getTasks() as { tasks: Task[] }
      tasks.value = res.tasks.filter(task => !task.is_hidden)
      hiddenTasks.value = res.tasks.filter(task => task.is_hidden)
    } catch (e: any) {
      error.value = "Ошибка загрузки задач"
    } finally {
      loading.value = false
    }
  }

  const addTask = async (task: Task) => {
    await handleRequest(
      async () => { await useTask().addTask(task) },
      { refresh: true, closeForm: true }
    )
  }

  const updateTask = async (task :Task)=>{
    await handleRequest(
      async () => { await useTask().updateTask(task) },
      { refresh: true }
    )
  }

  const hideTask = async (id: string) => {
    await handleRequest(
      async () => { await useTask().hideTask(id) },
      { refresh: true }
    )
  }

  const restoreTask = async (id: string) => {
    await handleRequest(
      async () => { await useTask().restoreTask(id) },
      { refresh: true }
    )
  }

  const deleteTask = async (id: string) => {
    await handleRequest(
      async () => { await useTask().deleteTask(id) },
      { refresh: true }
    )
  }

  const init = async () => {
    if (tasks.value.length === 0) {
      await fetchTasks()
    }
  }

  return {
    tasks,
    loading,
    error,
    openedForm,
    hiddenTasks,
    fetchTasks,
    init,
    toggleForm,
    closeForm,
    addTask,
    updateTask,
    restoreTask,
    deleteTask,
    hideTask
  }
})
