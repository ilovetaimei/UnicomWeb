<template>
  <div id="app">
    <router-view> </router-view>
  </div>
</template>

<script>

import Vue from 'vue';
import iView from 'iview';
Vue.use(iView);
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  
}
</style>
