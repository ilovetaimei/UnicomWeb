<template>
    <div class="input1">
         <input type="text" placeholder="野猪佩奇">
        <div class="seek-txt">
            <span>分类筛选</span>
            <div class="icon1"></div>
        </div>
    </div>
</template>
<style>
.icon1 {
  position: absolute;
  top: 10px;
  right: 24.5px;
  width: 8px;
  height: 8px;
  border-top: 2px solid white;
  border-right: 2px solid white;
  transform: rotate(135deg);
}

.input1 {
  position: relative;
  /* padding-top: 100px; */
}

.input1 input {
  position: relative;
  display: block;
  width: 796px;
  height: 36px;
  border: 1px solid yellow;
  border-radius: 18px;
  text-indent: 171px;
  margin-left: 60px;
  border: pink;
  background-color: #2c3554;
}

.seek-txt {
  border-right: 1px solid #d8d8d8;
  top: 0;
  left: 60px;
  position: absolute;
  width: 168px;
  height: 36px;
  text-align: center;
  line-height: 36px;
  color: white;
}
</style>
