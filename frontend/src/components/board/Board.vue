<script setup lang="ts">
import { storeToRefs } from "pinia"
import { useTaskStore } from "../../../stores/taskStore"
import {computed, reactive} from "vue";
import TaskCard from "./TaskCard.vue";
import draggable from "vuedraggable"

const taskStore = useTaskStore()
const { tasks, loading, error, openedForm } = storeToRefs(taskStore)

const form = reactive({
  title: "",
  description: ""
})

const tasksByStatus = computed(() => {
  return {
    todo: tasks.value.filter(task => task.status! === 0),
    in_progress: tasks.value.filter(task => task.status! === 1),
    done: tasks.value.filter(task => task.status! === 2),
  }
})

const closeModal = () =>{
  taskStore.closeForm()
}

const addTask = async (e: Event) => {
  e.preventDefault()
  if (!form.title.trim()) return

  await taskStore.addTask({
    title: form.title,
    description: form.description,
  })

  form.title = ""
  form.description = ""
}

const toggleForm = async () => {
  taskStore.toggleForm('add')
  form.title = ""
  form.description = ""
}

const onEnd = async (evt: any) => {
  const task = evt.item._underlying_vm_
  const newStatus = Number(evt.to.dataset.status)
  if (isNaN(newStatus)) {
    console.error('Не удалось определить новый статус')
    return
  }
  try {
    await taskStore.updateTask({ ...task, status: newStatus })
  } catch (e) {
    console.error('Не удалось обновить статус', e)
  }
}
</script>

<template>
  <div class="board">
    <div v-if="loading">Загрузка...</div>
    <div v-else-if="error">Ошибка: {{ error }}</div>
    <template v-if="tasks.length">
      <div class="board__columns">
        <div class="board__column">
          <h3 class="board__title">To Do</h3>
          <draggable
            :list="tasksByStatus.todo"
            group="tasks"
            @end="onEnd"
            item-key="id"
            :data-status="0"
            class="board__draggable"
            handle=".drag-handle"
          >
            <template #item="{ element }">
              <div class="draggable-item">
                <TaskCard :data="element" :is-dragging="true" :key="element.id" />
              </div>
            </template>
          </draggable>
        </div>

        <div class="board__column">
          <h3 class="board__title">In Progress</h3>
          <draggable
            :list="tasksByStatus.in_progress"
            group="tasks"
            @end="onEnd"
            item-key="id"
            :data-status="1"
            class="board__draggable"
            handle=".drag-handle"
          >
          <template #item="{ element }">
            <div class="draggable-item">
              <TaskCard :data="element" :is-dragging="true" :key="element.id" />
            </div>
          </template>
          </draggable>
        </div>

        <div class="board__column">
          <h3 class="board__title">Done</h3>
          <draggable
            :list="tasksByStatus.done"
            group="tasks"
            @end="onEnd"
            item-key="id"
            :data-status="2"
            class="board__draggable"
            handle=".drag-handle"
          >
          <template #item="{ element }">
            <div class="draggable-item">
              <TaskCard :data="element" :is-dragging="true" :key="element.id" />
            </div>
          </template>
          </draggable>
        </div>
      </div>
    </template>
    <div class="board__empty" v-else>
      <h3 class="board__title">Нет задач, добавьте новую задачу</h3>
      <button @click="toggleForm" class="board__button" type="button">Добавить задачу</button>
    </div>
  </div>
  <div v-if="openedForm !== 'none'" class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" aria-describedby="modal-desc">
    <div class="modal__container">
      <div class="modal__active" v-if="openedForm === 'add'">
        <h3 id="modal__title">Создать задачу</h3>
        <form class="modal__form" @submit="addTask">
          <label for="title" class="modal__label">
            <span>Заголовок</span>
            <input id="title" v-model="form.title" type="text" required placeholder="Введите заголовок">
          </label>

          <label for="title" class="modal__label">
            <span>Описание
              <span class="modal__opacity text-opacity">
                (необязательно)
              </span>
            </span>
            <textarea id="title" v-model="form.description" type="text" />
          </label>

          <button type="submit" class="modal__button">
            Создать
          </button>
        </form>
      </div>

      <button @click="closeModal" class="modal__close" type="button" aria-label="Закрыть модальное окно">
        <svg fill="currentColor" viewBox="0 0 36 36" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
          <path class="clr-i-outline clr-i-outline-path-1" d="M19.41,18l8.29-8.29a1,1,0,0,0-1.41-1.41L18,16.59,9.71,8.29A1,1,0,0,0,8.29,9.71L16.59,18,8.29,26.29a1,1,0,1,0,1.41,1.41L18,19.41l8.29,8.29a1,1,0,0,0,1.41-1.41Z"></path>
          <rect x="0" y="0" width="36" height="36" fill-opacity="0"/>
        </svg>
      </button>
    </div>
  </div>
</template>

<style scoped lang="sass">
@use '../../../assets/styles/variables' as *
@use '../../../assets/styles/mixins' as *

.board
  &__columns
    display: flex
    justify-content: space-between
    align-items: flex-start
    gap: $gap-s

    @media (max-width: 1279px)
      flex-direction: column
      align-items: normal

  &__column
    flex: 1
    border-radius: $border-radius
    padding: $padding-xl
    display: flex
    flex-direction: column
    gap: $gap-s
    border-top: 2px solid var(--background-opacity)
    border-left: 2px solid var(--background-opacity)

    &:first-child
      background: var(--todo-background)
      color: var(--font-color)

    &:nth-child(2)
      background: var(--in-progress-background)

    &:last-child
      background: var(--done-background)
  &__title
    @include text-h3
  &__draggable
    display: flex
    flex-direction: column
    gap: $gap-s

  &__empty
    display: flex
    flex-direction: column
    gap: $gap-s
    align-items: center

  &__button
    @include btn-stroke(var(--background-opacity))
    width: auto
    padding: $padding-s $padding-m

</style>
