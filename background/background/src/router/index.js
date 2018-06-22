import Vue from 'vue'
import Router from 'vue-router'

//引入首页
import Index from '@/components/index/index.vue'
//引入报表管理
import Ping from '../components/statement/ping'
import Mesh from '../components/statement/mesh'
import Polling from '../components/statement/polling'
import Detail from '../components/statement/detail.vue'
Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [{
      path: "/",
      component: Index
    },
    {
      path: '/index',
      component: Index
    },
    {
      path: '/statement/polling',
      component: Polling
    },
    {
      path: '/statement/mesh',
      component: Mesh
    },
    {
      path: '/statement/ping',
      component: Ping
    },
    {
      path: '/statement/detail',
      component: Detail
    }
  ]
})
