<template>
  <div id="cc_detail_title">
    <div id="detail_main_title">{{title_obj.main_title}} <i class="el-icon-medal-1" style="color: #FF9900;"></i></div>
    <div id="detail_sub_title">{{title_obj.duration}} {{title_obj.school_type}} | {{title_obj.location}} |
      <i class="el-icon-link"></i><el-link :href="title_obj.school_link" :underline='false' style="padding-bottom: 4px;">
        {{title_obj.school_link}}</el-link>
    </div>
  </div>

</template>

<script>
  export default {
    props: {
      title_obj: {
        type: Object,
        required: true,
      }
    }
  }
</script>

<style scoped>
  #cc_detail_title {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    padding-left: 40px;

  }

  #detail_main_title {
    padding-top: 30px;
    line-height: 50px;
    font-size: 30px;
    padding-bottom: 10px;
  }

  #detail_sub_title {
    line-height: 20px;
    font-size: 18px;
    padding-top: 0px;
    padding-bottom: 30px;
    color: gainsboro;
  }

  .el-link.el-link--default {
    color: gainsboro;
    font-size: 18px;
    
  }
</style>