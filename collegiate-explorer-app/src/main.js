import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'vue-g2'
import 'element-ui/lib/theme-chalk/index.css'

import './assets/images/gray_64.png'
import './assets/styles/global.css'
import router from './router'

Vue.use(ElementUI, { size: 'small', zIndex: 3000 });
Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
