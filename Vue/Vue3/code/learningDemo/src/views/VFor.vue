<template>
  <div>
    <p v-for="num in numbers" :key="num">段落{{ num }}：{{ words[num - 1] }}</p>
  </div>
  <div>
    <a v-for="(wide, index) of wides" :key="index" :href="wide"
      >网址{{ index }}: {{ wide }}
      <p
    /></a>
  </div>
  <div>
    <ol>
      <li v-for="(value, name, index) in book" :key="index">{{ name }} ：{{ value }}</li>
    </ol>
  </div>
  <div>
    <p v-for="n in 5" :key="n">这是{{ n }}</p>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'

const numbers = ref([1, 2, 3, 4, 5])
const words = ref(['一', '二', '三', '四', '五'])

const wides = ref(['www.baidu.com', 'www.alibaba.com', 'www.qq.com'])

const book = reactive({
  name: 'Vue指南',
  price: 68.99,
  author: 'xxx',
})
</script>
