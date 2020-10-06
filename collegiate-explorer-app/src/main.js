import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import './assets/images/gray_64.png'
import './assets/styles/global.css'

Vue.use(ElementUI, { size: 'small', zIndex: 3000 });

new Vue({
  el: '#app',
  render: h => h(App)
})
