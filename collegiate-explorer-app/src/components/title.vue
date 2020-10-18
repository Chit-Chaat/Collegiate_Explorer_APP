<template>
  <div id="cc_title">
    <div id="main_title">{{title_obj.main_title}}</div>
    <div id="sub_title">{{title_obj.sub_title}}</div>
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
  #cc_title {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    color: rgb(255, 255, 255);
    text-align: center;
    font-family: "microsoft yahei";
    
  }
  #main_title{
    line-height: 85px;
    font-size: 40px;
  }
  #sub_title{
    line-height: 40px;
    font-size: 35px;
  }
  p{
    font-size: 15px;
    line-height: 15px;
    padding-bottom: 15px;
  }
</style>