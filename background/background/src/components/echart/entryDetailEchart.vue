<template>
    <div :style="{width:'100%',height:'280px'}" id="meshDetailEchart"></div>
</template>
<script>
import echarts from "../../../node_modules/echarts";
export default {
  name: "meshDetailEchart",
  data() {
    return {
      chart: "",
      maxData: [35, 45, 20, 45, 35, 90, 65, 90, 65, 108, 43, 65, 200],
      minData: [78, 95, 45, 85, 45, 155, 105, 130, 125, 145, 105, 130, 105],
      aveData: [35, 70, 80, 40, 80, 40, 140, 80, 120, 90, 130, 60, 90],
      gateData: [
        "00:00",
        "02:00",
        "04:00",
        "06:00",
        "08:00",
        "10:00",
        "12:00",
        "14:00",
        "16:00",
        "18:00",
        "20:00",
        "22:00",
        "24:00"
      ]
    };
  },
  mounted() {
    this.initEchart3();
  },
  methods: {
    initEchart3() {
      //舒适化echart实例，获取Dom
      this.chart = this.$echarts.init(
        document.getElementById("meshDetailEchart")
      );

      this.chart.setOption({
        tooltip: {
          trigger: "axis"
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            magicType: { show: true, type: ["line", "bar"] },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        calculable: true,
        legend: {
          data: [
            "MIN",
            "MAX",
            "MVE"
            // {
            //   name: ["MIN", "MAX", "MVE"]
            // }
          ],
          textStyle: {
            color: "#fff",
            fontWeight: 200
          }
        },
        xAxis: [
          {
            type: "category",
            data: this.gateData,
            // x轴刻度对齐方式
            boundaryGap: true,
            // 柱子宽度
            // barWidth: 50,
            // 字体颜色
            axisLabel: {
              show: true,
              textStyle: {
                color: "#fff"
              }
            },
            axisLine: {
              lineStyle: {
                color: "#6F7DA6",
                width: 1
              }
            }
          }
        ],
        yAxis: [
          {
            type: "value",
            name: "流量/Mbps",
            splitLine: {
              show: true,
              lineStyle: {
                color: ["rgba(155,155,155,0.3)"]
              }
            }, //去除网格线
            axisLabel: {
              formatter: "{value}"
            },
            // 字体颜色
            axisLabel: {
              show: true,
              textStyle: {
                color: "#fff"
              }
            },
            axisLine: {
              lineStyle: {
                color: "#6F7DA6",
                width: 1
              }
            },
            nameTextStyle: {
              color: ["#fff"]
            },
            splitNumber: 10,
            max: 200,
            min: 0
          },
          {
            type: "value",
            name: "AVE",
            axisLabel: {
              formatter: "{value}"
            },
            // 坐标轴颜色
            axisLine: {
              lineStyle: {
                color: "#6F7DA6",
                width: 1
              }
            },
            nameTextStyle: {
              color: ["#fff"]
            }
          }
        ],
        series: [
          {
            name: "MVE",
            type: "line",
            smooth: true,
            itemStyle: {
              normal: {
                areaStyle: { type: "default" },
                color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                  { offset: 0, color: "#221972 " },
                  // { offset: 0.5, color: "#C3536B" },
                  { offset: 1, color: "#72347C" }
                ]),
                barBorderRadius: 10
              },
              emphasis: {
                barBorderRadius: 10
              }
            },
            data: this.aveData,
            color: ["#72347C"]
          },
          {
            name: "MIN",
            type: "bar",
            data: this.maxData,
            color: ["#98CA49"],
            barWidth: 10,
            itemStyle: {
              normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                  { offset: 0, color: "#98CA49 " },
                  { offset: 0.5, color: "#7AB135" },
                  { offset: 1, color: "#8FE13C" }
                ]),
                barBorderRadius: [10, 10, 0, 0]
              },
              emphasis: {
                // barBorderRadius: 10
              }
            }
          },
          {
            name: "MAX",
            type: "bar",
            data: this.minData,
            color: ["#C3536B"],
            barWidth: 10,
            itemStyle: {
              normal: {
                color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                  { offset: 0, color: "#EF90A4 " },
                  { offset: 0.5, color: "#C3536B" },
                  { offset: 1, color: "#EF90A4" }
                ]),
                barBorderRadius: [10, 10, 0, 0]
              },
              emphasis: {
                barBorderRadius: 10
              }
            }
          }
        ]
      });
      // 自适应
      window.onresize = this.chart.resize();
    }
  },
  created() {}
};
</script>
