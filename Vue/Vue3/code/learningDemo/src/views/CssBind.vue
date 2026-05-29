<template>
  <!-- 绑定对象 -->
  <div :class="{ active: isActive, header: isHeader, myClass: isMine }"></div>
  <div class="static" :class="{ active: isActive, 'text-danger': hasError }"></div>
  <div :class="classObject1"></div>
  <div :class="classObject2"></div>
  <!-- 绑定数组 -->
  <div :class="[activeClass, errorClass]"></div>

  <!-- 绑定对象 -->
  <div :style="{ color: color, fontSize: fontsize + 'px' }"></div>
  <div :style="styleObject"></div>
  <!-- 绑定数组 -->
  <div :style="[baseStyle, overridingStyle]"></div>
</template>

<script lang="ts" setup>
import { computed, reactive, ref } from 'vue'

const isActive = ref(true)
const isHeader = ref(false)
const isMine = ref(true)
const hasError = ref(false)

const classObject1 = reactive({
  active: true,
  header: false,
  myClass: true,
  'text-danger': true,
})
const classObject2 = computed(() => ({
  active: isActive.value,
  'text-danger': hasError.value,
}))

const activeClass = ref('active')
const errorClass = ref('text-danger')

const color = ref('red')
const fontsize = ref(50)

const styleObject = reactive({
  color: 'blue',
  fontsize: '50px',
})

const baseStyle = reactive({
  color: 'red',
  fontsize: '66px',
})
const overridingStyle = reactive({
  color: 'black',
  fontsize: '30px',
})
</script>
