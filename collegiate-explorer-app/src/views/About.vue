<template>
  <el-container id="app">
    <div id="cover"></div>
    <el-header>
      <Header></Header>
    </el-header>
    <el-main id="index_title">
      <Title :title_obj="title"></Title>
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
  import Footer from '../components/footer.vue'
  export default {
    components: {
      Header,
      Title,
      Footer,
    },
    data() {
      return {
        title: {
          main_title: "About Page",
          sub_title: "Filling The Blank",
          desc: "some descriptive words some descriptive words some  <br> descriptive words some descriptive words some descriptive words some descriptive words"
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

  body {
    color: azure;
    background-image: url('../assets/images/gray_64.png');
  }
</style>