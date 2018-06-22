<template>
   <div class="back">
    <el-aside ref="myHeight">
       <div class="el-img" >
        <img src="" alt="">
       </div>
      <div class="el-nave">
        <happy-scroll size="0">
        <ul class="one-nav">
          <li>
            <div class="icon"></div>
            <router-link to="/index">
              <span @click="sho">首页</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/abnormal">
              <span>异常记录</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="mainframe">
              <span>主机管理</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/network">
              <span>网络设备管理</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/polling">
              <span>自动巡检</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/statement/polling">
              <span @click="bt">报表管理</span>
              
            </router-link>
            <ul class="two-nav" v-show="isSubShow">
                <li>
                  <!-- <router-link to="/statement/polling"> -->
                  <span @click="btn" v-bind:class="{ current: isActive }">巡检报表</span>
                  <!-- </router-link> -->
                </li>
                <li>
                  <!-- <router-link to="/statement/mesh"> -->
                  <span @click="btn1" v-bind:class="{ current: isActive1 }">网络报表</span>
                  <!-- </router-link> -->
                </li>
                <li>
                  <!-- <router-link to="/statement/ping"> -->
                  <span @click="btn2" v-bind:class="{ current: isActive2 }">ping报表</span>
                  <!-- </router-link> -->
                </li>
              </ul>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/business">
              <span>业务管理</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/IP-business">
              <span>IP资源管理</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/circuit">
              <span>电路编码管理</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/blog">
              <span>日志管理</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/alarm">
              <span>报警管理</span>
            </router-link>
          </li>
           <li>
            <div class="icon"></div>
            <router-link to="/system">
              <span>系统设置</span>
            </router-link>
          </li>
        </ul>
        
        </happy-scroll>
     </div>
    </el-aside>
  </div> 
</template>
<script>
export default {
  data() {
    return {
      isActive: false,
      isActive1: false,
      isActive2: false,
      isSubShow: false,
      show: false
    };
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
      this.$router.push({ path: "/statement/mesh/?fartherid=1" });
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
  created() {
    this.$refs.myHeight.style.height = window.innerHeight + "px";
  }
};
</script>
<style>
@import "../../assets/css/app.css";
</style>
