<template>
 <div>
    <div class="seek">
        <seek></seek>
    </div>
    <div class="check">
        <span @click="btn">定义查看组别</span>
        <div class="box3"></div>
    </div>
    <div class="nav" v-show="isSubShow">
        <div class="network">
            <div class="title">
                <span>网络类型:</span>
            </div>
            <div class="left-content">
                <ul class="content-ul">
                    <li v-for="(v,i) in networkType" :key="i" @click="change" :class="{current:active}">
                       <span @click="mesh(v.fatherid)"  ref="myMesh">{{v.name}}</span>
                    </li>
                    
                </ul>
            </div>
        </div>
        <div class="branch">
            <div class="title">
                <span>区县分公司:</span>
            </div>
            <div class="left-content">
                <ul class="content-ul">
                    <li v-for="(v,i) in filiale" :key="i"> 
                     <span @click="branch(v.sonid)">{{v.sonname}}</span>
                    </li>
                    
                </ul>
            </div>
        </div>
        <div class="level">
            <div class="title">
                <span>楼层:</span>
            </div>
            <div class="left-content">
                <ul class="content-ul">
                    <li v-for="(v,i) in area" :key="i">
                     <span>{{v.branname}}</span>
                    </li>
                    
                </ul>
            </div>
        </div>
    </div>
    <!-- 表格 -->
    <div class="tab" ref="myData">
        <happy-scroll>
        <table class="table2">
            <thead>
                <tr>
                    <th>序号</th>
                    <th>网络</th>
                    <th>分公司</th>
                    <!-- <th>楼层</th> -->
                    <th>设备名称</th>
                    <th>设备类型</th>
                    <th>端口数量</th>
                    <!-- <th>端口状态</th> -->
                    <th>操作</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(v,i) in data" :key="i">
                    <td>{{i++}}</td>
                    <td>办公网</td>
                    <td>嘉定</td>
                    <!-- <td>12</td> -->
                    <td>{{v.name}}</td>
                    <td>{{v.type}}</td>
                    <td>{{v.portnum}}</td>
                    <!-- <td>异常</td> -->
                    <td>
                        <span @click="look(v.id)">查看端口流量</span>
                    </td>
                </tr>
                <tr >
                    <td>1</td>
                    <td>1</td>
                    <td>2</td>
                    <!-- <td>12</td> -->
                    <td>3</td>
                    <td>4</td>
                    <td>5</td>
                    <!-- <td>异常</td> -->
                    <td>
                        <span @click="look">查看端口流量</span>
                    </td>
                </tr>
            </tbody>
        </table>
        </happy-scroll>
    </div>
 </div>
 
</template>
<script>
import seek from "../../components/input/input-mesh";
export default {
  data() {
    return {
      isSubShow: true,
      msg: false,
      meshData: [],
      networkType: {},
      filiale: [],
      area: [],
      data: [],
      active: false
    };
  },
  created() {
    this.getData();
  },
  methods: {
    btn() {
      this.isSubShow = !this.isSubShow;
      if (this.isSubShow === false) {
        this.$refs.myData.style.height = 540 + "px";
      } else {
        this.$refs.myData.style.height = 310 + "px";
      }
    },
    look(info) {
      this.$router.push({
        path: "/statement/detail",
        query: { id: info }
      });
    },
    mesh(info) {
      this.$router.push({
        path: "/statement/mesh/",
        query: { fartherid: info }
      });
      this.active = true;
      this.getData();
    },
    change() {
      this.active = !this.active;
    },
    getData() {
      this.$axios({
        url:
          "http://10.6.201.24:8000/netreport/?fartherid=" +
          this.$route.query.fartherid
      }).then(res => {
        console.log(res.data);
        this.meshData = res.data;
        this.networkType = res.data[0].networkType;
        this.filiale = res.data[0].filiale;
        this.area = res.data[0].area;
        this.data = res.data[0].data;
        // console.log(res.data);
      });
    },
    branch(info) {
      this.$router.push({
        path: "/statement/mesh/",
        query: {
          sonid: info
        }
      });
      //   console.log(this.$route);
      this.$axios({
        url:
          "http://10.6.201.24:8000/netreport/?sonid=" + this.$route.query.sonid
      }).then(res => {
        this.meshData = res.data;
        this.networkType = res.data[0].networkType;
        this.filiale = res.data[0].filiale;
        this.area = res.data[0].area;
        this.data = res.data[0].data;
        // console.log(res.data);
      });
    }
  },
  components: {
    seek
  }
};
</script>
<style>
@import "../../assets/css/mesh.css";
</style>


