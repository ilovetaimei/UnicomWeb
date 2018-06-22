<template>
    <div class="search">
        <!-- 搜索框 -->
        <huk></huk>
        <!-- 时间查询 -->
        <div class="date">
             <el-radio v-model="radio" label="1">天</el-radio>
             <el-radio v-model="radio" label="2">周</el-radio>
             <el-radio v-model="radio" label="3">月</el-radio>
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
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item,i) in data" :key="i">
                        <td>{{item.date}}</td>
                        <td>{{item.county}}</td>
                        <td>{{item.IP}}</td>
                        <td>{{item.defer}}</td>
                        <td>{{item.peak}}</td>
                        <td>{{item.loss}}</td>
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
      :total="data.length">
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
      //默认每页数据量
      pagesize: 10,
      //当前页码
      currentPage: 4,
      //查询的页码
      start: 1,
      //默认数据总数
      totalCount: 1000,
      data: [
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公1",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公2司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公3司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公4司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公6司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公7司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分8公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区1分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南2区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南3区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分4公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分5公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区6分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区6分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南7区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.1483.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区9分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区2分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区3分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区4分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区5分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区5分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区6分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区1分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区2分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区4分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区6分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区3分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区6分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区6分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区8分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区3分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区9分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区2分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区5分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区8分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区9分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区1分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区2分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区3分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区4分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区5分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区6分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区7分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区8分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区9分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区1分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区12分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.143.611",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公123司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分4公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分5公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区66分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区78分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分89公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2018-06-07",
          county: "南区分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "10ms",
          loss: "0.001%"
        },
        {
          date: "2019-06-07",
          county: "分公司",
          IP: "10.7.143.6",
          defer: "1ms",
          peak: "1000000ms",
          loss: "0.001%"
        }
      ]
    };
  },
  components: {
    huk
  },
  methods: {
    getDate() {
      this.$axios({
        url: ""
      });
    },
    //   每页多少条数据
    handleSizeChange(val) {
      console.log(val);
      this.pageSize = val;
    },
    //当前页码
    handleCurrentChange(val) {
      console.log(val);
      this.currentPage = val;
    }
  }
};
</script>

<style>
@import "../../assets/css/polling.css";
</style>

