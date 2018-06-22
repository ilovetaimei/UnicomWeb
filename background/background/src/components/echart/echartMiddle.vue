<template>
    <div :style="{width:'195px',height:'253px'}" id="myEchart" ref=""></div>
</template>
<script>
import echarts from "../../../node_modules/echarts";
export default {
  name: "myEchart",
  data() {
    return {
      chart: "",
      //指定图标的数据和配置
      optionData: [
        { value: 0 },
        // { value: 234, name: "联盟广告" },
        // { value: 135, name: "视频广告" },
        { value: 100 }
      ]
    };
  },
  mounted() {
    this.initEchart();
  },
  methods: {
    initEchart: function() {
      //初始化echarts实列，获取dom
      this.chart = this.$echarts.init(document.getElementById("myEchart"));
      this.chart.setOption({
        tooltip: {
          trigger: "axis",
          formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          x: "left"
          // data: ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"]
        },
        series: [
          {
            name: "访问来源",
            type: "pie",
            radius: ["75%", "55%"],
            avoidLabelOverlap: false,
            label: {
              normal: {
                show: false,
                position: "center"
              },
              emphasis: {
                show: false,
                textStyle: {
                  fontSize: "30",
                  fontWeight: "bold"
                }
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            },
            data: this.optionData
          }
        ],
        color: {
          type: "radial",
          x: 1,
          y: 1,
          r: 1.4,
          colorStops: [
            {
              offset: 0,
              color: "#C86DD7  " // 0% 处的颜色
            },
            {
              offset: 0.5,
              color: "#3023AE" // 100% 处的颜色
            }
            // {
            //     color:"red"
            // },
          ],
          globalCoord: false // 缺省为 false,
        }
      });
    }
  }
};
</script>

