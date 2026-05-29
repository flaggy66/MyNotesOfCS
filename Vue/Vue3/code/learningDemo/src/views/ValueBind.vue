<template>
  <h2>valueBinde</h2>
  <div>{{ count }}</div>
  <button @click="increment">+1</button>
</template>

<script lang="ts" setup>
let count = 0

function increment() {
  count++
  console.log(count)
}
</script>
