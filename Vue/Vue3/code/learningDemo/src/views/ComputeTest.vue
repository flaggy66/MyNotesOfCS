<template>
  <div>
    <h2>ComputedTest</h2>
    <h3>{{ count }}</h3>
    <button @click="increment">+1</button>
    <p>Is it a multiple of 3? {{ result }}</p>
  </div>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'

const count = ref(1)

// const result = computed(() => {
//   return count.value % 3 === 0 ? 'YES' : 'NO'
// })

const result = computed({
  get(previous) {
    if (previous === 'NO') {
      console.log('上一个值是NO')
    }
    return count.value % 3 === 0 ? 'YES' : 'NO'
  },
  set(newValue) {
    // 如果result的值被设为YES，则count赋值为0
    if (newValue === 'YES') {
      count.value = 0
    }
  },
})

function increment() {
  count.value++
  // 当计数到9时，手动设置result的值为YES
  if (count.value === 9) {
    result.value = 'YES'
  }
}
</script>
