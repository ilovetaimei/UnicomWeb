<template>
  <div class="container">
    <h1 >{{ msg }}</h1>  
    <div class="one  handw ">
             <h2>{{title1}}</h2>
             <canvas width="800" height="320" class="treeOne"></canvas>
             <div class="num1 spe" v-if="colorChange" @click=" showCover">  {{num1 }}111 </div>
             <div class="num2 spe">  {{num2}} </div>
             <div class="num3 spe">  {{num3}} </div>
             <div class="num4 spe">  {{num4}} </div>
             <div class="num5 spe">  {{num5}} </div>
    </div>

    <div class="two  handw ">
             <h2>{{title1}}</h2>
             <canvas width="800" height="320" class="treeTwo"></canvas>
             <div class="num1 spe" v-if="colorChange">  {{num1 }} </div>
             <div class="num2 spe">  {{num2}} </div>
             <div class="num3 spe">  {{num3}} </div>
             <div class="num4 spe">  {{num4}} </div>
             <div class="num5 spe">  {{num5}} </div>
    </div>

   <div class="three  handw ">
             <h2>{{title1}}</h2>
             <canvas width="800" height="320" class="treeThree"></canvas>
             <div class="num1 spe"  v-if="colorChange">  {{num1 }} </div>
             <div class="num2 spe">  {{num2}} </div>
             <div class="num3 spe">  {{num3}} </div>
             <div class="num4 spe">  {{num4}} </div>
             <div class="num5 spe">  {{num5}} </div>
    </div>

    <div class="four  handw ">
             <h2>{{title1}}</h2>
             <canvas width="800" height="320" class="treeFour"></canvas>
             <div class="num1 spe" v-if="colorChange">  {{num1 }} </div>
             <div class="num2 spe">  {{num2}} </div>
             <div class="num3 spe">  {{num3}} </div>
             <div class="num4 spe">  {{num4}} </div>
             <div class="num5 spe">  {{num5}} </div>
    </div>

    <!-- 遮罩层 -->
      <!-- <div>
          <Modal   v-model="modal1"
                  title="Common Modal dialog box title "
                  width = "1060px"
                  @on-ok="ok"
                  @on-cancel="cancel">
                    <Queen></Queen>
          </Modal>    
    </div> -->

  <div id="mask" v-if="maskIsShow"> </div>
  <transition name="slide-fade" mode="out-in">
      <div class="cover-wrap" v-if="coverIsShow">
          <div class="cancel" @click="cancel">关闭</div>
            <div class="qwrap">
                <Queen></Queen>
            </div> 
      </div>
  </transition> 

   <!-- <div class="cover"> -->
          <!-- <Queen></Queen> -->
   <!-- </div> -->

  </div>
</template>

<script src="@/resource/js/BusinessMonitoring.js"></script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src="@/resource/css/BusinessMonitoring.css"></style>

