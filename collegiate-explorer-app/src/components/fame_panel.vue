<template>
  <el-container style="height: 295px;">
    <div class="fame_tab_chart_title">Hall of Fame</div>
    <el-aside width="300px">

    </el-aside>
    <el-main style="width: 90%; height: 100%; padding-bottom: 0px; padding-top: 0px;">

    </el-main>
  </el-container>
</template>


<script>
  export default {
    props: {
      fame_obj: {
        type: Object,
        required: true,
      }
    }
  }
</script>


<style scoped>
  .fame_tab_chart_title {
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    padding-left: 4%;
    font-size: 25px;
    width: 27%;
    height: 40px;
  }

  .score_tab_desc_title {
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    font-size: 25px;
    width: 90%;
  }

  .niche_desc {
    float: left;
    font-size: 18px;
    color: azure;
    padding-top: 10px;
    padding-left: 40px;
    width: 90%;
    text-align: left;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    text-align: left;
    margin-bottom: 20px;
  }


  .highlight_val {
    color: darkorange;
    font-size: 18px;
    font-weight: 600;
    text-decoration: underline;
  }
</style>