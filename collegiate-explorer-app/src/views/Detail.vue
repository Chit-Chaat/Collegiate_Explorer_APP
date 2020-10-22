<template>
  <el-container id="app">
    <div id="cover"></div>
    <el-header>
      <Header></Header>
    </el-header>
    <el-main id="index_title">
      <Title :title_obj="title_info"></Title>
    </el-main>

    <el-container style="height: 500px;">
      <el-main>
        <el-carousel height="250px" direction="vertical" :autoplay="true">
          <el-carousel-item v-for="img in head_imgs" :key="img">
            <img :src="require('../assets/images' + img)">
          </el-carousel-item>
        </el-carousel>
        <div class='ranking_chart'>
          <g2-area :padding="['auto', 30]" :data="ranking_data" :axis-name="{name:'Years', value:'Ranking'}"
            :axisColor="{ lineColor: 'rgb(240, 255, 255)', labelColor: 'rgb(240, 255, 255)' }"
            :single-color="{areaColor: 'l(270) 0:#855001 1:#FF9900', lineColor: '#FF9900'}"
            style="height: 200px; width: 100%;">
          </g2-area>
        </div>
      </el-main>
      <el-aside width="40%">Table</el-aside>
    </el-container>

    <el-divider></el-divider>
    <el-container>
      <el-container style="height: 300px;">
        <el-aside width="300px">Chart</el-aside>
        <el-main class="new-main">Desc</el-main>
      </el-container>
    </el-container>

    <el-divider></el-divider>
    <el-container>
      <el-container style="height: 300px;">
        <el-aside width="300px">Chart</el-aside>
        <el-main class="new-main">Desc</el-main>
      </el-container>
    </el-container>

    <el-divider></el-divider>
    <el-footer>
      <Footer></Footer>
    </el-footer>
  </el-container>
</template>

<script>
  import Header from '../components/header.vue'
  import Title from '../components/detail_title.vue'
  import Footer from '../components/footer.vue'

  export default {
    components: {
      Header,
      Title,
      Footer,
    },
    props: {
      schoolId: {
        type: String,
        required: true,
      }
    },
    data() {
      return {
        head_imgs: [],
        title_info: {},
        ranking_data: [
          { name: '1997', value: 37 },
          { name: '2007', value: 35 },
          { name: '2017', value: 30 },
          { name: '2020', value: 33 }
        ],
      }
    },
    mounted() {
      this.head_imgs = ['/usc/1.png', '/usc/2.png', '/usc/3.png']
      this.title_info = {
        main_title: "University of Southern California (USC)",
        duration: '4-Years',
        school_type: "Private University",
        location: "Los Angeles, CA",
        school_link: "http://www.usc.edu",
      }
    },
    methods: {
    },
  }
</script>

<style scoped>
  .small {
    max-width: 600px;
    margin: 150px auto;
  }

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

  .el-footer {
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

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  #index_title {
    line-height: 120px;
  }

  body {
    color: rgb(240, 255, 255);
    background-image: url('../assets/images/gray_64.png');
  }

  .ranking_chart {
    height: 230px;
    padding-top: 10px;
    margin-top: 10px;
  }
</style>