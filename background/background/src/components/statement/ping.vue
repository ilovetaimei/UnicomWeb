<template>
    <div class="search">
        <!-- 搜索框 -->
        <huk></huk>
        <!-- 时间查询 -->
        <div class="date">
             <el-radio  v-model="radio" label="1"><span v-on:click="clickDay(day)">天</span></el-radio>
             <el-radio v-model="radio" label="2"><span @click="clickWeek(week)">周</span> </el-radio>
             <el-radio v-model="radio" label="3"><span @click="clickMonth(month)">月</span> </el-radio>
        </div>
        <!-- 表格数据 -->
        <div class="tab1">
            <table>
                <thead>
                    <tr>
                        <th>日期</th>
                        <th>区县分公司</th>
                        <th>设备IP</th>
                        <th>平均延迟</th>
                        <th>峰值延迟</th>
                        <th>丢包率</th>
                        <th>操作</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(v,i) in dateData" :key="i">
                        <td>{{v.date}}</td>
                        <td>{{v.filiale}}</td>
                        <td>{{v.ip}}</td>
                        <td>{{v.avgdelay}}0.0001</td>
                        <td>{{v.maxdelay}}</td>
                        <td>{{v.lostpercent}}0.0003%</td>
                        <td>
                        <span>查看设备</span>
                    </td>
                    </tr>
                      <tr>
                        <td>2018-06-21</td>
                        <td>浦东</td>
                        <td>192.168.86.11	</td>
                        <td>0.63683986663818360.0001</td>
                        <td>0.8444786071777344</td>
                        <td>0.0003%</td>
                        <td>
                        <span>查看设备</span>
                    </td>
                    </tr>
                </tbody>
            </table>
            <tfoot>
                <tr>
                    <td></td>
                </tr>
            </tfoot>
        </div>
     
  
  <div class="block">
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"   
      :page-sizes="[10, 20, 30, 40]"
      :page-size="pagesize"
      layout="total, sizes, prev, pager, next, jumper"
      :total="totalCount">
    </el-pagination>
  </div>

    </div>
</template>
<script>
import huk from "../../components/input/input";
export default {
  data() {
    return {
      radio: true,
      day: "day",
      week: "week",
      month: "month",
      // 接收数据的数组
      dateData: [],
      //当前页码
      currentPage: 1,
      //默认数据总数
      totalCount: 1000,
      //默认每页数据量
      pagesize: 10,
      //查询的页码
      page: 1,
      pageNum: 1
    };
  },
  components: {
    huk
  },
  methods: {
    getDate() {
      this.$axios({
        url: "http://10.6.201.24:8000/pingreportdata/"
      }).then(res => {
        this.dateData = res.data;
      });
    },
    //控制煤业的数据条数
    handleSizeChange(val) {
      console.log(val);
    },
    //当前页码
    handleCurrentChange(val) {
      console.log(val);
    },
    //天周月的数据
    clickDay(info) {
      // alert(info);
      this.$router.push({
        path: "/statement/ping/",
        query: { type: info }
      });
      this.$axios({
        url:
          "http://10.6.201.24:8000/pingreportdata/?type=" +
          this.$route.query.type
      }).then(res => {
        // console.log("这是天的数据" + res.data);
        this.dateData = res.data;
      });
    },
    clickWeek(info) {
      // alert(info);
      this.$router.push({
        path: "/statement/ping/",
        query: { type: info }
      });
      this.$axios({
        url:
          "http://10.6.201.24:8000/pingreportdata/?type=" +
          this.$route.query.type
      }).then(res => {
        // console.log("这是周的数据" + res.data);
        this.dateData = res.data;
      });
    },
    clickMonth(info) {
      // alert(info);
      this.$router.push({
        path: "/statement/ping/",
        query: { type: info }
      });
      this.$axios({
        url:
          "http://10.6.201.24:8000/pingreportdata/?type=" +
          this.$route.query.type
      }).then(res => {
        // console.log("这是月的数据" + res.data);
        this.dateData = res.data;
      });
    }
  },
  created() {
    this.getDate();
  }
};
</script>

<style>
@import "../../assets/css/polling.css";
</style>

