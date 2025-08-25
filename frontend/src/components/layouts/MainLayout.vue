<script setup lang="ts">
import Board from "../board/Board.vue";
</script>

<template>
  <main class="main">
    <div class="main__container container">
      <h2 class="main__title">
        Задачи
      </h2>
      <Board />
    </div>
  </main>
</template>

<style scoped lang="sass">
@use '../../../assets/styles/variables' as *
@use '../../../assets/styles/mixins' as *

$header-height: 59px

.main
  margin-top: $header-height
  background: var(--background-dark)
  text-align: center
  color: var(--font-color)
  min-height: calc(100vh - $header-height)
  padding: $padding-xl 0 $padding-xl 0

  &__container
    display: flex
    flex-direction: column
    gap: $gap-m

  &__title
    @include text-h2
</style>
