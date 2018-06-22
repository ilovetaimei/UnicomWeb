<template>
    <div class="input1">
         <input type="text" placeholder="hello World">
          <!-- <i class="el-icon-search"></i> -->
        <div class="seek-txt">
           <el-col :span="12">
  
    <el-dropdown trigger="click">
      <span class="el-dropdown-link">
        IP<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>IP</el-dropdown-item>
        <el-dropdown-item>设备名称</el-dropdown-item>
        <el-dropdown-item>设备类型</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </el-col>
        </div>
    </div>
</template>
<style>
/* 搜索框 */
.el-popper[x-placement^="bottom"] {
  left: 349px !important;
}
.el-popper[x-placement^="bottom"] .popper__arrow {
  top: 0px;
  left: 50%;
  margin-right: 3px;
  border-top-width: 0;
  border-bottom-color: #ebeef5;
}
.el-popper[x-placement^="bottom"] {
  top: 104px !important;
}
.el-col-12 {
  position: absolute;
  width: 50%;
  left: 75px;
}
.el-popper[x-placement^="bottom"] {
  background: #2c3554;
  border: none;
  border-radius: 0;
  left: 332px;
}

.el-popper .popper__arrow,
.el-popper .popper__arrow::after {
  border-style: none;
}
.el-dropdown-menu__item:focus,
.el-dropdown-menu__item:not(.is-disabled):hover {
  background-color: #2c3554;
}

.el-dropdown {
  color: #fff;
}
.el-dropdown-menu__item {
  color: #fff;
}

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
  border-radius: 18px;
  text-indent: 171px;
  margin-left: -2px;
  border: pink;
  background-color: #2c3554;
}

.seek-txt {
  border-right: 1px solid #d8d8d8;
  top: 0;
  left: -30px;
  position: absolute;
  width: 168px;
  height: 36px;
  text-align: center;
  line-height: 36px;
  color: white;
}
[class*=" el-icon-"],
[class^="el-icon-"] {
  font-family: element-icons !important;
  speak: none;
  font-style: normal;
  font-weight: 400;
  font-variant: normal;
  text-transform: none;
  line-height: 1;
  vertical-align: baseline;
  display: inline-block;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* position: absolute; */
  top: 4px;
  right: 320px;
  color: #fff;
  font-size: 18px;
}
</style>
