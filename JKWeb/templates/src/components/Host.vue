<template>
  <div class="container">
    <h1 class="title">{{ msg }}</h1>
      
      <div class="table1">
          <div class="title1">{{title1}}</div>
          <Table border :columns="columns1" :data="data1"></Table>
      </div>

      <div class="tab">
            <Tabs value="name1">
              <TabPane label="钦州路" name="name1">
                    <img @click="modal = true" class="logo" src="@/resource/images/logo.png">
              </TabPane>
              <TabPane label="新黄浦" name="name2">标签二的内容</TabPane>
              <TabPane label="包头路" name="name3">标签三的内容</TabPane>
              <TabPane label="标签四" name="name4">标签二的内容</TabPane>
              <TabPane label="标签五" name="name5">标签三的内容</TabPane>
          </Tabs>
      </div>
      <div class="table2">
          <div class="title1">{{title2}}</div>
          <Table border :columns="columns2" :data="data2"></Table>
      </div>


      <div class="table3">
          <div class="title1">{{title3}}</div>
          <Table border :columns="columns3" :data="data3"></Table>
      </div>

       <div class="table4">
          <div class="title1">{{title4}}</div>
          <Table border :columns="columns4" :data="data4"></Table>
      </div>

       <!-- 遮罩层 -->
     <div>
        <Modal   v-model="modal"  title="Host" width = "600px" >
                      <div class="info">
                              <div class="row">
                                     <span>CPU : {{cpuNum}}</span>
                                     <span>内存 : {{ramNum}}</span>
                              </div>
                               <div class="row">
                                     <span>磁盘IO : {{diskNum}}</span>
                                     <span>磁盘空间利用率 : {{diskRate}}</span>
                              </div>
                              <div class="row">
                                     <span>网络延迟 : {{netDelay}}</span>
                              </div>
                              <div class="row">
                                     <span>网卡流量 :</span>
                              </div>

                              <div class="tabWarp">
                                 <Table border :columns="columns5" :data="data5"></Table>
                            </div>
                      </div>
        </Modal>    
   </div>
  </div>
</template>

<script src="@/resource/js/host.js"></script>
<style scoped src="@/resource/css/host.css"></style>
<style>
        .table1>.ivu-table-wrapper .ivu-table{
            font-size: 14px;
        }
         .table2>.ivu-table-wrapper .ivu-table{
            font-size: 14px;
        }
         .table3>.ivu-table-wrapper .ivu-table{
            font-size: 14px;
        }
         .table4>.ivu-table-wrapper .ivu-table{
            font-size: 14px;
        }
        .tab>.ivu-tabs .ivu-tabs-nav-container{
               font-size: 16px;
        }
</style>


