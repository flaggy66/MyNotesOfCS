<template>
  <!-- if-else -->
  <div v-if="condition1">IF</div>
  <div v-else>ELSE</div>

  <!-- if-else if-else -->
  <div v-if="condition2">IF</div>
  <div v-else-if="condition3">ELSE-IF</div>
  <div v-else>ELSE</div>

  <div v-show="condition4">Show</div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const condition1 = ref(true)
const condition2 = ref(false)
const condition3 = ref(true)

const condition4 = ref(true)
</script>
