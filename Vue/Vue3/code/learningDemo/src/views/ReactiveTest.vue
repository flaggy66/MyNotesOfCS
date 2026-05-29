<template>
  <h2>ReactiveTest</h2>
  <div>{{ count.count }}</div>
  <button @click="increment">+1</button>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'

const count = reactive({ count: 0 })

function increment() {
  count.count++
}

console.log(count)
console.log(count.count)
</script>
