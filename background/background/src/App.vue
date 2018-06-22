<template>
  <div id="app">
   <el-container>
  <el-header class="el-header">
    基础设施自动化运维管理后台
    <div class="log">
      <span>你好</span>
    </div>
  </el-header>
  <el-container>
    <!-- 侧边导航栏 -->
    <leftnav> </leftnav>
    <el-main ref="myWidth">
      <router-view></router-view>
    </el-main>
  </el-container>
</el-container>
  </div>
</template>

<script>
import leftnav from "./components/left-nav/nav";
export default {
  name: "App",
  data() {
    return {
      isActive: false,
      isActive1: false,
      isActive2: false,
      isSubShow: false
    };
  },
  created() {
    this.$refs.myWidth = window.innerWidth;
  },
  methods: {
    sho() {
      if (this.isSubShow === true) {
        this.isSubShow = false;
      }
    },
    bt() {
      this.isSubShow = !this.isSubShow;
      this.isActive = true;
      this.isActive1 = false;
      this.isActive2 = false;
    },
    btn() {
      this.$router.push({ path: "/statement/polling" });
      this.isActive = true;
      if ((this.isActive = true)) {
        this.isActive1 = false;
        this.isActive2 = false;
      }
    },
    btn1() {
      this.$router.push({ path: "/statement/mesh" });
      this.isActive1 = true;
      if ((this.isActive1 = true)) {
        this.isActive = false;
        this.isActive2 = false;
      }
    },
    btn2() {
      this.$router.push({ path: "/statement/ping" });
      this.isActive2 = true;
      if ((this.isActive2 = true)) {
        this.isActive = false;
        this.isActive1 = false;
      }
    }
  },
  components: {
    leftnav
  }
};
</script>

<style>
@import "./assets/css/app.css";
</style>
