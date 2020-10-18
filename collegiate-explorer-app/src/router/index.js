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
      name: 'Home page',
      component: Index
    }, {
      path: '/index',
      name: 'Index page',
      component: Index
    }, {
      path: '/user_profile',
      name: '3d user profile',
      component: UserProfile
    },{
      path: '/detail',
      name: 'Detail page',
      component: Detail
    }, {
      path: '/sql',
      name: 'SPARQL query page',
      component: SPARQL
    }, {
      path: '/about',
      name: 'about page',
      component: About
    }
  ]
})