<template>
  <el-container id="app">
    <div id="cover">
      <el-header>
        <Header></Header>
      </el-header>
      <el-main id="index_title">
        <Title></Title>
      </el-main>
      <el-main id="index_search_box">
        <SearchBox></SearchBox>
      </el-main>
      <el-main id="index_recommend_res">
        <Recommend></Recommend>
      </el-main>
      <el-footer>
        <Footer></Footer>
      </el-footer>
    </div>

  </el-container>
</template>

<script>
  import Header from './components/header.vue'
  import Title from './components/title.vue'
  import SearchBox from './components/search_box.vue'
  import Recommend from './components/recommend_res.vue'
  import Footer from './components/footer.vue'
  export default {
    name: 'app',
    components: {
      Header,
      Title,
      SearchBox,
      Recommend,
      Footer,

    },
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
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
    opacity: 0.95;
    z-index: -1;
  }

  .el-header {
    text-align: center;
    height: 100px !important;
  }

  .el-main {
    background-color: #6bcc90;
    color: #333;
    text-align: center;
    line-height: 160px;
    padding-top: 0px;
    padding-bottom: 0px;
  }

  #index_title {
    line-height: 120px;
  }

  #index_search_box {
    line-height: 80px;
  }

  #index_recommend_res {
    line-height: 500px;
  }

  .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    height: 100px !important;
  }

  body {
    color: azure;
    background-image: url('./assets/images/gray_64.png');
  }
</style>