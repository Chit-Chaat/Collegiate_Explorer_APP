<template>
  <div id="cc_detail_title">
    <div id="detail_main_title">{{title_obj.main_title}}</div>
    <div id="detail_sub_title">{{title_obj.sub_title}}</div>
    <p>{{title_obj.desc}}</p>
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
    text-align: center;
    font-family: "microsoft yahei";
    
  }
  #detail_main_title{
    line-height: 85px;
    font-size: 40px;
  }
  #detail_sub_title{
    line-height: 40px;
    font-size: 35px;
  }
  p{
    font-size: 15px;
    line-height: 15px;
    padding-bottom: 15px;
  }
</style>