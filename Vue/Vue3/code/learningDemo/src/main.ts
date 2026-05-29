import { createApp, ref } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import RefTest from './views/RefTest.vue'
import ReactiveTest from './views/ReactiveTest.vue'
import ValueBind from './views/ValueBind.vue'
import ComputeTest from './views/ComputeTest.vue'
import VIfVShow from './views/VIf&VShow.vue'
import VFor from './views/VFor.vue'

const app1 = createApp(RefTest)

app1.use(createPinia())
app1.use(router)

app1.mount('#app1')

// const app2 = createApp({
//   // 编写组件选项
//   template: `<div>My name is: {{ name }} .</div>`,
//   data() {
//     return {
//       name: 'Jack',
//     }
//   },
// })

const app2 = createApp(ReactiveTest)

app2.mount('#app2')

const app3 = createApp(ValueBind)

app3.mount('#app3')

const app4 = createApp(ComputeTest)
app4.mount('#app4')

const app5 = createApp(VFor)
app5.mount('#app5')
