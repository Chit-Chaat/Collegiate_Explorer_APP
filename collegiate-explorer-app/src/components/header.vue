<template>
  <div id="cc_header">
    <span id="title">DSCI 558</span>
    <div id="cc_tabs">
      <span>User Profile</span>
      <el-divider direction="vertical"></el-divider>
      <span>??????????</span>
      <el-divider direction="vertical"></el-divider>
      <span>About</span>
    </div>
    <el-divider id="title_divider"></el-divider>
    <div id="cc_team">
      <span>Aaron Yang</span>
      <el-divider direction="vertical"></el-divider>
      <span>Kevin Tran</span>
      <el-divider direction="vertical"></el-divider>
      <span>Ryan Ball</span>
    </div>
  </div>
</template>

<script>
  export default {

  };
</script>

<style scoped>
  #title {
    padding-left: 40px;
    font-size: 36px;
    color: rgb(255, 255, 255);
    font-weight: bold;
  }

  #cc_tabs {
    display: inline;
    padding-left: 40px;

  }

  #cc_tabs span {
    padding-left: 15px;
    color: rgb(255, 255, 255);
    padding-right: 15px;
    font-weight: 500;
  }

  #title_divider {
    margin-top: 5px;
    height: 2px;
    margin-bottom: 0px;
  }

  #cc_team {
    padding-left: 28px;
  }

  #cc_team span {
    padding-left: 15px;
    color: rgb(255, 255, 255);
    padding-right: 15px;
    font-size: 15px;
  }


  #cc_header {
    padding-top: 20px;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    height: 100%;
    color: rgb(238, 238, 238);
    text-align: left;
    font-size: 20px;
  }
</style>