import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'vue-g2'
import 'element-ui/lib/theme-chalk/index.css'

import './assets/images/gray_64.png'
import './assets/styles/global.css'
import router from './router'
import axios from 'axios'
import Vuex from 'vuex'

Vue.use(ElementUI, { size: 'small', zIndex: 3000 });
Vue.config.productionTip = false
Vue.prototype.$hostname = 'http://localhost:8000'
Vue.use(Vuex)

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.withCredentials = true
axios.defaults.baseURL = Vue.prototype.$hostname

const store = new Vuex.Store({
  state:{
    results: []
  },
  mutations:{
    updateResultSolt(state, new_val){
      state.results = new_val
    }
  }
})

new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App)
})
