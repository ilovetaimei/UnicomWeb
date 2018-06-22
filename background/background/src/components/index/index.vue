<template>
    <div class="content">
        <happy-scroll>
        <!-- 三圆 -->
         <div class="superior">
           <div class="round one">
               <div class="title">
                   <span>网络设备情况</span>
               </div>
               <div class="echart">
                   <echart></echart>
               </div>
               <div class="echart-data">
                  <div class="data-box">
                      <p><span>10</span>台 <span>在线设备</span></p>
                      <p><span>0</span>台 <span>异常设备</span></p>
                      <p>共<span>1000</span>台</p>
                  </div>
               </div>
           </div>
           <div class="round two">
                <div class="title">
                   <span>服务器情况</span>
               </div>
               <div class="echart">
                 <echartMiddle></echartMiddle>
               </div>
               <div class="echart-data">
                  <div class="data-box">
                      <p><span>10</span>台 <span>在线服务器</span></p>
                      <p><span>0</span>台 <span>异常服务器</span></p>
                      <p>共<span>1000</span>台</p>
                  </div>
               </div>
           </div>
           <div class="round three">
                <div class="title">
                   <span>业务情况</span>
               </div>
               <div class="echart">
                  <echartRight></echartRight>
               </div>
               <div class="echart-data">
                  <div class="data-box">
                      <p><span>10</span>台 <span>在线业务</span></p>
                      <p><span>0</span>台 <span>异常业务</span></p>
                      <p>共<span>1000</span>台</p>
                  </div>
               </div>
           </div>
      </div>
       <!-- 表格 -->
       <div class="middle">
           <p class="title">当前异常</p>
           <div class="middle-nav">
                <div class="imge">
                    <img src="../../assets/images/icon_紧急待处理 copy.png" alt="">
                    <img src="../../assets/images/icon_待处理总数 copy.png" alt="">
                    <img src="../../assets/images/icon_异常总数 copy.png" alt="">
                </div>
               <ul>
                   <li v-for="(v,i) in title" :key="i">
                       <span class="term" ><span>{{v.test}}：</span> <span>{{v.total}}</span>项</span>
                   </li>
                   
               </ul>
           </div>
           
           <div class="tab">
                <div class="box1" ref="triangle">
                  <span class="box1-span"></span>
                </div>
               <table class="table1">
                   <thead>
                       <tr>
                          <th>发生时间</th>
                          <th>IP地址</th>
                          <th>关联业务</th>
                          <th>异常情况</th>
                          <th>严重程度</th>
                          <th>操作</th>
                       </tr>
                   </thead>
                   <tbody>
                       <tr v-for="(v,i) in table" :key="i">
                           <td>{{v.date}}</td>
                           <td>{{v.ip}}</td>
                           <td>{{v.service}}</td>
                           <td>{{v.error}}</td>
                           <td>{{v.errgency}}</td>
                           <td class="box">
                               <span>处理</span>
                           </td>
                       </tr>
                   </tbody>
               </table>
           </div>
       </div>
         <!-- 底部模块 -->
        <div class="foot-modul">
            <div class="content one">
                <div class="imge1">
                    <img src="../../assets/images/CPU.png" alt="">
                    <img src="../../assets/images/占比 copy 3.png" alt="">
                    <img src="../../assets/images/峰值.png" alt="">
                </div>
                <p>
                    <span>cpu异常总数:</span>
                    <span>1</span>
                </p>
                 <p>
                    <span>cpu异常占比:</span>
                    <span>10%</span>
                </p>
                 <p>
                    <span>cpu最高占用量:</span>
                    <span>10%</span>
                </p>
            </div>
            <div class="content two">
                <div class="imge1">
                    <img src="../../assets/images/磁盘.png" alt="">
                    <img src="../../assets/images/占比 copy 3.png" alt="">
                    <img src="../../assets/images/峰值.png" alt="">
                </div>
                <p>
                    <span>cpu异常总数:</span>
                    <span>1</span>
                </p>
                 <p>
                    <span>cpu异常占比:</span>
                    <span>10%</span>
                </p>
                 <p>
                    <span>cpu最高占用量:</span>
                    <span>10%</span>
                </p>
            </div>
            <div class="content three">
                <div class="imge1">
                    <img src="../../assets/images/端口.png" alt="">
                    <img src="../../assets/images/占比 copy 3.png" alt="">
                    <img src="../../assets/images/峰值.png" alt="">
                </div>
                <p>
                    <span>cpu异常总数:</span>
                    <span>1</span>
                </p>
                 <p>
                    <span>cpu异常占比:</span>
                    <span>10%</span>
                </p>
                 <p>
                    <span>cpu最高占用量:</span>
                    <span>10%</span>
                </p>
            </div>
        </div>
    </happy-scroll>
    </div>
</template>
<script>
import echart from "../echart/echart-index";
import echartMiddle from "../echart/echartMiddle";
import echartRight from "../echart/echart-right";
export default {
  data() {
    return {
      table: [],
      title: []
    };
  },
  created() {
    this.$axios({
      url: "http://10.6.201.24:8000/index/"
    }).then(res => {
      this.table = res.data;
      this.title = this.table.splice(0, 3);
    });
  },
  components: {
    echart,
    echartMiddle,
    echartRight
  }
};
</script>
<style>
@import "../../assets/css/index.css";
</style>
