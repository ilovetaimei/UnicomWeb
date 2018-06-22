// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
//引入elementui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App'
import router from './router'

Vue.use(ElementUI);
Vue.config.productionTip = false

//引入vue-happy-scroll
import {
  HappyScroll
} from 'vue-happy-scroll'
//自定义组件名
Vue.component('happy-scroll', HappyScroll)
// 引入css
import 'vue-happy-scroll/docs/happy-scroll.css'

// 引入echarts
import echarts from 'echarts'
Vue.prototype.$echarts = echarts
// 引入axios
import axios from '../node_modules/axios'
// 全局注册axios
Vue.prototype.$axios = axios


var vue = new Vue({
  el: '#app',
  router,
  components: {
    App
  },
  template: '<App/>',

})
