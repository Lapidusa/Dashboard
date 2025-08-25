<script setup lang="ts">
import {useTaskStore} from "../../../stores/taskStore";
import {computed, ref} from "vue";
import TaskCard from "../board/TaskCard.vue";

const taskStore = useTaskStore()
const isOpenAside = ref<boolean>(false)
const hiddenTask = computed(() => taskStore.hiddenTasks)
const toggleForm = () =>{
  taskStore.toggleForm('add')
}
const toggleAside = () =>{
  isOpenAside.value = !isOpenAside.value
  isOpenAside.value ? document.body.style.overflow = 'hidden' : document.body.style.overflow = "";
}

</script>

<template>
  <header class="header">
    <div class="header__container container">
      <h1 class="header__title">Kanban Board</h1>
      <nav class="header__nav">
        <button @click="toggleForm" class="header__button" type="button">
          <span class="sr-only">Добавить задачу</span>
          <svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" fill="currentColor">
          <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
          </svg>
        </button>
        <button @click="toggleAside" class="header__button" type="button">
          <span class="sr-only">Посмотреть скрытые задачи</span>
          <svg  viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 4L9.87868 9.87868M20 20L14.1213 14.1213M9.87868 9.87868C9.33579 10.4216 9 11.1716 9 12C9 13.6569 10.3431 15 12 15C12.8284 15 13.5784 14.6642 14.1213 14.1213M9.87868 9.87868L14.1213 14.1213M6.76821 6.76821C4.72843 8.09899 2.96378 10.026 2 11.9998C3.74646 15.5764 8.12201 19 11.9998 19C13.7376 19 15.5753 18.3124 17.2317 17.2317M9.76138 5.34717C10.5114 5.12316 11.2649 5 12.0005 5C15.8782 5 20.2531 8.42398 22 12.0002C21.448 13.1302 20.6336 14.2449 19.6554 15.2412" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </nav>
    </div>
  </header>
  <aside v-if="isOpenAside" class="aside">
    <div class="aside__container">
      <button @click="toggleAside" class="aside__close" type="button" aria-label="Закрыть модальное окно">
        <svg fill="currentColor" viewBox="0 0 36 36" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
          <path class="clr-i-outline clr-i-outline-path-1" d="M19.41,18l8.29-8.29a1,1,0,0,0-1.41-1.41L18,16.59,9.71,8.29A1,1,0,0,0,8.29,9.71L16.59,18,8.29,26.29a1,1,0,1,0,1.41,1.41L18,19.41l8.29,8.29a1,1,0,0,0,1.41-1.41Z"></path>
        </svg>
      </button>
      <div class="aside__active">
        <div v-if="hiddenTask.length" class="aside__task" v-for="task in hiddenTask" :key="task.id">
          <TaskCard :data="task" :is-dragging="false"></TaskCard>
        </div>
        <div v-else>
          <h3 class="aside__title">Нет скрытых задач</h3>
        </div>
      </div>
    </div>
  </aside>
</template>

<style scoped lang="sass">
@use '../../../assets/styles/mixins' as *
@use '../../../assets/styles/variables' as *
.header
  background: var(--background-dark)
  border-bottom: 2px solid var(--border-color)
  padding: 12px 0
  position: fixed
  top: 0
  width: 100%
  z-index: 100

  &__container
    display: flex
    justify-content: space-between
    align-items: center
  &__title
    color: var(--font-color)
    @include text-h1

  &__nav
    display: flex
    align-items: center
    gap: 8px

  &__button
    @include btn-stroke(var(--border-color))
    display: flex
    align-items: center
    justify-content: center

    &:focus-visible
      background: var(--font-color)

      &:first-child svg
        fill: var(--background)

      &:last-child svg
        fill: transparent
        color: var(--background)

    &:first-child svg
      fill: var(--icon-color)
      scale: 1.3

    &:first-child:hover svg
      fill: var(--background)

    &:last-child svg
      fill: transparent
      color: var(--icon-color)

    &:last-child:hover svg
      color: var(--background)

.aside
  position: fixed
  inset: 0
  background: var(--background-dark-opacity)
  z-index: 1000

  &__container
    position: absolute
    top: 0
    right: 0
    height: 100%
    display: flex
    gap: 8px
    align-items: center
    justify-content: end
    width: 100%

    @media (max-width: 665px)
      display: block

  &__active
    background: var(--background-dark)
    padding: $padding-xl
    border-radius: $border-radius
    box-shadow: var(--shadow)
    display: flex
    height: 100%
    flex-direction: column
    gap: $gap-l
    max-width: 50%
    color: var(--font-color)
    overflow-y: auto

    &:has(.aside__title)
      justify-content: center

    @media (max-width: 665px)
      max-width: 100%
      width: 100%
      padding: $padding-2xl
      align-items: center

  &__close
    display: flex
    justify-content: center
    align-items: center
    padding: $padding-xs
    border-radius: $border-radius-full
    border: none
    background: var(--background-dark)
    box-shadow: var(--shadow)
    cursor: pointer
    transition: $transition

    & svg
      fill: var(--font-color)

    &:hover
      background: var(--font-color)

    &:hover svg
      fill: var(--background-dark)

    @media (max-width: 665px)
      position: absolute
      top: $padding-xs
      left: $padding-xs
</style>
