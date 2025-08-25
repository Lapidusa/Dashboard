<script setup lang="ts">
import type {Task} from "../../../types/task";
import {useTaskStore} from "../../../stores/taskStore";
import {ref} from "vue";

const props = defineProps<{
  data: Task,
  isDragging: boolean,
}>()

const modalStatus = ref<boolean>(false);

const taskStore = useTaskStore()

function toggleModal(){
  modalStatus.value = !modalStatus.value;
}

const editTask = async (e: Event) => {
  e.preventDefault()
  await taskStore.updateTask(props.data)
  toggleModal()
}

const hideTask = async () => {
  await taskStore.hideTask(props.data.id!)
}

const showTask = async () => {
  await taskStore.restoreTask(props.data.id!)
}

const deleteTask = async () => {
  await taskStore.deleteTask(props.data.id!)
}
</script>

<template>
  <div class="task-card" v-bind="$attrs">
    <div class="task-card__data">
      <button v-if="isDragging" class="task-card__drag-handle drag-handle" :aria-label="`Перетащить задачу ${data.title}`">⋮⋮</button>
      <div class="task-card__wrapper">
        <h3 class="task-card__title">{{ data.title }}</h3>
        <p class="task-card__description">{{ data.description }}</p>
      </div>
    </div>
    <div class="task-card__actions">
      <div class="task-card__actions-main" v-if="isDragging">
        <button @click="toggleModal" class="task-card__button" :aria-label="`Изменить задачу ${data.title}`">
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M20.8477 1.87868C19.6761 0.707109 17.7766 0.707105 16.605 1.87868L2.44744 16.0363C2.02864 16.4551 1.74317 16.9885 1.62702 17.5692L1.03995 20.5046C0.760062 21.904 1.9939 23.1379 3.39334 22.858L6.32868 22.2709C6.90945 22.1548 7.44285 21.8693 7.86165 21.4505L22.0192 7.29289C23.1908 6.12132 23.1908 4.22183 22.0192 3.05025L20.8477 1.87868ZM18.0192 3.29289C18.4098 2.90237 19.0429 2.90237 19.4335 3.29289L20.605 4.46447C20.9956 4.85499 20.9956 5.48815 20.605 5.87868L17.9334 8.55027L15.3477 5.96448L18.0192 3.29289ZM13.9334 7.3787L3.86165 17.4505C3.72205 17.5901 3.6269 17.7679 3.58818 17.9615L3.00111 20.8968L5.93645 20.3097C6.13004 20.271 6.30784 20.1759 6.44744 20.0363L16.5192 9.96448L13.9334 7.3787Z" fill="currentColor"/></svg>
        </button>

        <button @click="hideTask()" class="task-card__button" :aria-label="`Скрыть задачу ${data.title}`">
          <svg  viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 4L9.87868 9.87868M20 20L14.1213 14.1213M9.87868 9.87868C9.33579 10.4216 9 11.1716 9 12C9 13.6569 10.3431 15 12 15C12.8284 15 13.5784 14.6642 14.1213 14.1213M9.87868 9.87868L14.1213 14.1213M6.76821 6.76821C4.72843 8.09899 2.96378 10.026 2 11.9998C3.74646 15.5764 8.12201 19 11.9998 19C13.7376 19 15.5753 18.3124 17.2317 17.2317M9.76138 5.34717C10.5114 5.12316 11.2649 5 12.0005 5C15.8782 5 20.2531 8.42398 22 12.0002C21.448 13.1302 20.6336 14.2449 19.6554 15.2412" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>

      <div class="task-card__actions-aside" v-else>
        <button @click="deleteTask" class="task-card__button" :aria-label="`Удалить задачу ${data.title}`">
          <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g id="ic_fluent_delete_48_regular" fill="currentColor" fill-rule="nonzero"><path d="M24,7.25 C27.1017853,7.25 29.629937,9.70601719 29.7458479,12.7794443 L29.75,13 L37,13 C37.6903559,13 38.25,13.5596441 38.25,14.25 C38.25,14.8972087 37.7581253,15.4295339 37.1278052,15.4935464 L37,15.5 L35.909,15.5 L34.2058308,38.0698451 C34.0385226,40.2866784 32.1910211,42 29.9678833,42 L18.0321167,42 C15.8089789,42 13.9614774,40.2866784 13.7941692,38.0698451 L12.09,15.5 L11,15.5 C10.3527913,15.5 9.8204661,15.0081253 9.75645361,14.3778052 L9.75,14.25 C9.75,13.6027913 10.2418747,13.0704661 10.8721948,13.0064536 L11,13 L18.25,13 C18.25,9.82436269 20.8243627,7.25 24,7.25 Z M33.4021054,15.5 L14.5978946,15.5 L16.2870795,37.8817009 C16.3559711,38.7945146 17.116707,39.5 18.0321167,39.5 L29.9678833,39.5 C30.883293,39.5 31.6440289,38.7945146 31.7129205,37.8817009 L33.4021054,15.5 Z M27.25,20.75 C27.8972087,20.75 28.4295339,21.2418747 28.4935464,21.8721948 L28.5,22 L28.5,33 C28.5,33.6903559 27.9403559,34.25 27.25,34.25 C26.6027913,34.25 26.0704661,33.7581253 26.0064536,33.1278052 L26,33 L26,22 C26,21.3096441 26.5596441,20.75 27.25,20.75 Z M20.75,20.75 C21.3972087,20.75 21.9295339,21.2418747 21.9935464,21.8721948 L22,22 L22,33 C22,33.6903559 21.4403559,34.25 20.75,34.25 C20.1027913,34.25 19.5704661,33.7581253 19.5064536,33.1278052 L19.5,33 L19.5,22 C19.5,21.3096441 20.0596441,20.75 20.75,20.75 Z M24,9.75 C22.2669685,9.75 20.8507541,11.1064548 20.7551448,12.8155761 L20.75,13 L27.25,13 C27.25,11.2050746 25.7949254,9.75 24,9.75 Z"></path></g></g></svg>
        </button>

        <button @click="showTask" class="task-card__button" :aria-label="`Восстановить задачу ${data.title}`">
          <svg fill="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M14 12c-1.095 0-2-.905-2-2 0-.354.103-.683.268-.973C12.178 9.02 12.092 9 12 9a3.02 3.02 0 0 0-3 3c0 1.642 1.358 3 3 3 1.641 0 3-1.358 3-3 0-.092-.02-.178-.027-.268-.29.165-.619.268-.973.268z"/><path d="M12 5c-7.633 0-9.927 6.617-9.948 6.684L1.946 12l.105.316C2.073 12.383 4.367 19 12 19s9.927-6.617 9.948-6.684l.106-.316-.105-.316C21.927 11.617 19.633 5 12 5zm0 12c-5.351 0-7.424-3.846-7.926-5C4.578 10.842 6.652 7 12 7c5.351 0 7.424 3.846 7.926 5-.504 1.158-2.578 5-7.926 5z"/></svg>
        </button>
      </div>
    </div>
  </div>
  <div v-if="modalStatus" class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" aria-describedby="modal-desc">
    <div class="modal__container">
      <div class="modal__active">
        <div class="modal__title">
          Изменить задачу
        </div>
        <form @submit="editTask" class="modal__form">
          <label for="title" class="modal__label">
            <span>Заголовок</span>
            <input id="title" v-model="data.title" type="text" required placeholder="Введите заголовок">
          </label>

          <label for="title" class="modal__label">
            <span>Описание
              <span class="modal__opacity text-opacity">
                (необязательно)
              </span>
            </span>
            <textarea id="title" v-model="data.description" type="text" />
          </label>
          <button class="modal__button" type="submit">Изменить</button>
        </form>
      </div>
      <button @click="toggleModal" class="modal__close" type="button" aria-label="Закрыть модальное окно">
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

.task-card
  text-align: start
  background: var(--background-opacity)
  padding: $padding-xl
  border-radius: $border-radius
  border-top: 2px solid var(--background-opacity)
  border-left: 2px solid var(--background-opacity)
  transition: $transition
  display: flex
  justify-content: space-between
  align-items: flex-start
  gap: $gap-s
  min-width: 250px

  &:hover
    transform: translateY(-5px)
    box-shadow: var(--shadow-dark)

  &__title
    @include text-h3

  &__button
    @include btn-stroke(var(--background-opacity))
    display: inline-flex

    & svg
      color: var(--background-opacity)
      fill: var(--background-opacity)
    &:hover svg
      color: var(--background-dark)
      fill: var(--background-dark)

  &__data
    word-break: break-all
    display: flex
    gap: $gap-xs
    align-items: flex-start

  &__drag-handle
    white-space: nowrap
    background: none
    border: none
    @include text-base
    cursor: pointer
    color: var(--font-color)
    padding: 4px

  &__actions
    &-main, &-aside
      display: flex
      flex-direction: column
      gap: $gap-xs

    &-main
      & .task-card__button
        & svg
          fill: transparent
</style>
