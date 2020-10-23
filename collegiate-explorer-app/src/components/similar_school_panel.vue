<template>
  <el-container style="height: 295px;">
    <div class="similar_tab_title">You may also fit</div>
    <el-main style="width: 90%; height: 100%; padding-bottom: 0px; padding-top: 0px;">

    </el-main>
  </el-container>


</template>


<script>

  export default {
    props: {
      similar_school_obj: {
        type: Object,
        required: false,
      }
    },
    data() {
      return {

      }
    }
  }
</script>


<style scoped>
  .similar_tab_title {
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    padding-left: 4%;
    font-size: 25px;
    width: 60%;
    height: 40px;
  }

  .highlight_val {
    color: darkorange;
    font-size: 18px;
    font-weight: 600;
    text-decoration: underline;
  }
</style>