<template>
  <div id="cc_header">
    <el-link id="title" @click="$router.push('/index')" :underline="false">DSCI 558</el-link>
    <div id="cc_tabs">
      <el-link @click="$router.push('/user_profile')" :underline="false">User Profile</el-link>
      <el-divider direction="vertical"></el-divider>
      <el-link @click="$router.push('/sql')" :underline="false">SPARQL</el-link>
      <el-divider direction="vertical"></el-divider>
      <el-link @click="$router.push('/about')" :underline="false">About</el-link>
    </div>
    <el-divider id="title_divider"></el-divider>
    <div id="cc_team">
      <el-link :underline="false">Aaron Yang <i class="el-icon-news"></i></el-link>
      <el-divider direction="vertical"></el-divider>
      <el-link :underline="false">Kevin Tran <i class="el-icon-news"></i></el-link>
      <el-divider direction="vertical"></el-divider>
      <el-link :underline="false">Ryan Ball <i class="el-icon-news"></i></el-link>
    </div>
  </div>
</template>

<script>
  export default {

  };
</script>

<style scoped>
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

  #title {
    padding-left: 40px;
    font-size: 36px;
    color: rgb(255, 255, 255);
    font-weight: bold;
    display: inline;
  }

  #cc_tabs {
    display: inline;
    padding-left: 40px;
  }

  #cc_tabs .el-link {
    padding-left: 15px;
    color: rgb(255, 255, 255);
    font-size: 20px;
    padding-right: 20px;
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

  #cc_team .el-link {
    padding-left: 15px;
    color: rgb(255, 255, 255);
    padding-right: 5px;
    font-size: 15px;
  }

</style>