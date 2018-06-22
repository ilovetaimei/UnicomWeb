<template>
  <div class="container">
    <h1 @click=" showCover">{{ msg }}</h1>  
    <!-- 遮罩层 -->
     <div class="qwrap" v-if="modal1">
                   <Queen></Queen>
    </div>

  </div>
</template>

<script src="@/resource/js/test.js"></script>
<style scoped>
    .qwrap{
        width: 1000px;
        height: 500px;
        display: block;
        margin-top: 100px;
    }
</style>

