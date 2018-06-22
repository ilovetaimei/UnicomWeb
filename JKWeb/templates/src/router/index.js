import Vue from 'vue'
import Router from 'vue-router'
import Host from '@/components/Host'
// import queen from '@/components/queen'
import Net from '@/components/Net'
import test from '@/components/test'
import mainframe from '@/components/main-frame'
import BusinessMonitoring from '@/components/BusinessMonitoring'

Vue.use(Router);
export default new Router({
  routes: [
    {
      path: '/',
      name: 'mainframe',
      component: mainframe
    },
    {
      path: '/index',
      name: 'BusinessMonitoring',
      component: BusinessMonitoring
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    // {
    //   path: '/queen',
    //   name: 'queen',
    //   component: queen
    // },
    {
      path: '/net',
      name: 'Net',
      component: Net
    },
    {
      path: '/host',
      name: 'Host',
      component: Host
    },
    // {
    //   path: '/mainframe',
    //   name: 'mainframe',
    //   component: mainframe
    // },
  ]
})
