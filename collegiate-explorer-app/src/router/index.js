import Vue from 'vue'
import Router from 'vue-router'
import Index from '../views/Index'
import UserProfile from '../views/UserProfile'
import Detail from '../views/Detail'
import SPARQL from '../views/SPARQL'
import About from '../views/About'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Index
    }, {
      path: '/index',
      name: 'Index',
      component: Index
    }, {
      path: '/user_profile',
      name: 'user_profile',
      component: UserProfile
    },{
      path: '/detail/:schoolId',
      name: 'Detail',
      component: Detail,
      props: true
    }, {
      path: '/sql',
      name: 'SPARQL',
      component: SPARQL
    }, {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})