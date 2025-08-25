<script setup lang="ts">
import MainPage from "./pages/mainPage.vue";
import {onMounted} from "vue";
import {useTaskStore} from "../stores/taskStore";
import {useTaskWebSocket} from "../composables/websocket";

const { connect } = useTaskWebSocket();

const taskStore = useTaskStore()

onMounted(async () =>{
  await taskStore.init()
  connect();
})

</script>

<template>
  <MainPage/>
</template>

<style scoped>

</style>
