<template>
<div>
   
    <!-- 左侧端口导航 -->
    <div class="port-nav" ref="myNav">
      <div class="title">
        <span>端口列表</span>
       
      </div>
       <div class="port-ul">
        <happy-scroll style="height:650px">
        <ul>
          <li v-for="(v,i) in navData" :key="i">
            <span>{{v.port}}</span>
          </li>
        </ul>
        </happy-scroll>
        </div>
    </div>
    <!-- 右侧端口数据 -->
    <div class="port-content" ref="myDetail">
      
      <div class="solid">
        <span>name_01路由器端口流量时段报表</span>
      </div>

      <!-- 时间查询 -->
      <div class="date">
        <!-- 选择间隔 -->
        <div class="section-time">
            <span>选择间隔:</span>
            <div class="time">
              <span></span>
              <!-- <div class="icon4"></div> -->
          <el-col :span="12">
            <el-dropdown trigger="click">
            <span class="el-dropdown-link">
             1小时<i class="el-icon-arrow-down el-icon--right"></i>
            </span>
            <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>10分钟</el-dropdown-item>
            <el-dropdown-item>1小时</el-dropdown-item>
            <el-dropdown-item>1天</el-dropdown-item>
            <el-dropdown-item>1月</el-dropdown-item>
            </el-dropdown-menu>
            </el-dropdown>
          </el-col>
            </div>    
        </div>
        <!-- 起始时间 -->
        <div class="interval"><span>起始时间:</span> 
          <div class="section">
            <span>2018-06-20</span> <span>06:00</span>
          </div> 
        </div> 
        <!-- 结束时间 -->
           <div class="over">
             <span>结束时间:</span>
             <div class="over-time">
               <span>2018-06-20</span> <span>12:00</span>
             </div>
           </div> 
      </div>
      
      <!-- 图表数据 -->
      <div class="echart-title"><span>入口流量</span></div>
      <div class="echart">
        <div class="echart-one">
          <entryDetailEchart></entryDetailEchart>
        </div>
         <div class="echart-title"><span>出口流量</span></div>
        <div class="echart-two">
          <exitEcharts></exitEcharts>
        </div>
      </div>
    </div>  
</div>
</template>
<script>
import entryDetailEchart from "../../components/echart/entryDetailEchart";
import exitEcharts from "../../components/echart/exitEcharts.vue";
export default {
  data() {
    return {
      radio: true,
      navData: []
    };
  },
  methods: {
    getData() {}
  },
  created() {
    this.$axios({
      url: "http://10.6.201.24:8000/netportdetails/?id=" + this.$route.query.id
    }).then(res => {
      this.navData = res.data;
    });
    // 获取窗口大小
    this.$refs.myNav.style.height = window.innerHeight + "px";
    this.$refs.myDetail.style.height = window.innerHeight + "px";
    this.$refs.myDetail.style.width = window.innerWidth + "px";
  },
  components: {
    entryDetailEchart,
    exitEcharts
  }
};
</script>
<style>
@import "../../assets/css/polling.css";
@import "../../assets/css/detail.css";
</style>

