<template>
  <el-container id="app">
    <div id="cover"></div>
    <el-header>
      <Header></Header>
    </el-header>
    <el-main id="index_title">
      <Title :title_obj="title"></Title>
    </el-main>
    <el-main id="index_search_box">
      <SearchBox></SearchBox>
    </el-main>
    <el-divider>EXPLORE YOUR FINDINGS</el-divider>
    <el-main id="index_recommend_res">
      <Recommend></Recommend>
    </el-main>
    <el-divider></el-divider>
    <el-footer>
      <Footer></Footer>
    </el-footer>
  </el-container>
</template>

<script>
  import Header from '../components/header.vue'
  import Title from '../components/title.vue'
  import SearchBox from '../components/search_box.vue'
  import Recommend from '../components/recommend_res.vue'
  import Footer from '../components/footer.vue'
  export default {
    name: 'index',
    components: {
      Header,
      Title,
      SearchBox,
      Recommend,
      Footer,
    },
    data() {
      return {
        title: {
          main_title: "Collegiate Explorer",
          sub_title: "Knowledge Graph",
          desc: "Using Knowledge Graph techniques help you find the most suitable school, and start your new life."
        }
      }
    }
  }
</script>

<style scoped>
  #app {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
  }

  #cover {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background-color: #999;
    opacity: 0.20;
    z-index: -1;
  }

  .el-header {
    text-align: center;
    height: 100px !important;
  }

  .el-footer{
    height: 100% !important;
    bottom: 0;
  }
  .el-main {
    color: #333;
    text-align: center;
    padding-top: 0px;
    padding-bottom: 0px;
  }

  .el-divider {
    width: 92%;
    margin-left: 4%;
    height: 2px;
  }

  #index_title {
    line-height: 120px;
  }

  #index_search_box {
    line-height: 80px;
  }

  body {
    color: azure;
    background-image: url('../assets/images/gray_64.png');
  }
</style>