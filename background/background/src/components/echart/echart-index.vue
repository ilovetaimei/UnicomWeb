<template>
    <div :style="{width:'195px',height:'253px'}" id="echartsDemo" ref="myEchart"></div>
</template>
<script>
import echart from "../../../node_modules/echarts";
export default {
  name: "echartsDemo",
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
    this.initEcharts();
  },
  methods: {
    initEcharts: function() {
      //初始化echarts实列，获取dom
      this.chart = this.$echarts.init(document.getElementById("echartsDemo"));
      this.chart.setOption({
        tooltip: {
          trigger: "axis",
          formatter: "{a} <br/>{b}: {c} ({d}%)"
        },

        series: [
          {
            name: "访问来源",
            type: "pie",
            radius: ["75%", "55%"],
            avoidLabelOverlap: false,
            label: {
              normal: {
                show: true,
                position: "center"
              },
              emphasis: {
                show: false,
                textStyle: {
                  fontSize: "10",
                  fontWeight: "700"
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
