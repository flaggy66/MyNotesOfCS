<template>
  <h2>RefTest</h2>
  <div>{{ count }}</div>
  <button @click="incremnet">+1</button>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const count = ref(0)

function incremnet() {
  count.value++
}

console.log(count)
console.log(count.value)
</script>
