<template>
  <div class='cc_item'>
    <el-card :body-style="{ padding: '3px'}" shadow="hover">
      <div class="logo_block">
        <img :src="img_path" class="logo" /></div>

      <div class='info'>
        <span>好吃的汉堡</span>
        <!--<div class="bottom clearfix">
          <time class="time">{{ currentDate }}</time>
          <el-button type="text" class="button">操作按钮</el-button>
        </div> -->
      </div>
    </el-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        img_path: "https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        currentDate: new Date()
      };
    }
  }
</script>

<style scoped>
  /* .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }



  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  } */
  .cc_item {
    text-align: left;
  }

  .el-card {
    height: 200px;
  }

  .logo_block {
    display: inline-block;
    padding-left: 0px;
  }

  .logo {
    width: 50%;
  }

  .info {
    display: inline-block;
  }
</style>