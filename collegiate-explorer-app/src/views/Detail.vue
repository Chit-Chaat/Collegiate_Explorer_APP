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
        <el-carousel height="245px" direction="vertical" :autoplay="true">
          <el-carousel-item v-for="img in head_imgs" :key="img">
            <img :src="require('../assets/images' + img)">
          </el-carousel-item>
        </el-carousel>
        <div class='location_chart' v-if="location_data">
          <div class="chart_title">School Location</div>
          <static-map :google-api-key="apiKey" format="png" :markers="location_data.markers" 
          :zoom="zoom" :center="location_data.center" :size="size" type="roadmap" language="en"></static-map>
        </div>
      </el-main>
      <el-aside width="40%" style="line-height: 200px;">
        <HeadCard :desc_obj="desc_info"></HeadCard>
      </el-aside>
    </el-container>

    <el-divider></el-divider>
    <FamePanel :fame_obj="fame_info"></FamePanel>

    <el-divider></el-divider>
    <ScorePanel :score_obj="score_info"></ScorePanel>

    <el-divider></el-divider>
    <PopularMajorPanel></PopularMajorPanel>

    <el-divider></el-divider>
    <SimilarSchoolPanel :similar_school_obj="similar_school_info"></SimilarSchoolPanel>

    <el-divider></el-divider>
    <el-footer>
      <Footer></Footer>
    </el-footer>
  </el-container>
</template>

<script>
  import axios from "axios"
  import Header from '../components/header.vue'
  import Title from '../components/detail_title.vue'
  import Footer from '../components/footer.vue'
  import HeadCard from '../components/detail_head_card.vue'
  import ScorePanel from '../components/score_panel.vue'
  import SimilarSchoolPanel from '../components/similar_school_panel.vue'
  import PopularMajorPanel from '../components/popular_major_panel.vue'
  import FamePanel from "../components/fame_panel.vue"
  import StaticMap from 'vue-static-map';
  export default {
    components: {
      Header,
      Title,
      Footer,
      HeadCard,
      ScorePanel,
      SimilarSchoolPanel,
      PopularMajorPanel,
      FamePanel,
      StaticMap,
    },
    props: {
      schoolId: {
        type: String,
        required: true,
      }
    },
    data() {
      return {
        localtionDataApiPrefix: "/detail/location/",
        basicInfoApiPrefix: "/detail/",
        scoreInfoApiPrefix: "/detail/score/",
        similarSchoolApiPrefix: "/detail/similar/",
        fameInfoApiPrefix: "/detail/fame/",
        head_imgs: [],
        title_info: {},
        desc_info: {},
        location_data: {
          markers:[],
          center:{}
        },
        score_info: {},
        popular_major_info: {},
        similar_school_info: [],
        fame_info: {},
        apiKey: 'AIzaSyBe0n3z7qndMX9owX_5rySTLivp7ZSMYvA',
        size: [640, 200],
        zoom: 12,
      }
    },
    computed: {

    },
    created() {
      this.getLocationData()
      this.getBasicInfo()
      this.getScoreData()
      this.getSimilarSchoolList()
      this.getFameInfo()
    },
    mounted() {
      this.head_imgs = ['/usc/1.png', '/usc/2.png', '/usc/3.png']
    },
    methods: {
      getBasicInfo() {
        axios({
          method: "GET",
          url: this.$hostname + this.basicInfoApiPrefix + this.$route.params.schoolId
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.title_info = result.data.data.title_info;
                this.desc_info = result.data.data.desc_info;
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }
          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with the basic deatil info."
            );
          }
        );
      },
      getFameInfo() {
        axios({
          method: "GET",
          url: this.$hostname + this.fameInfoApiPrefix + this.$route.params.schoolId
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.fame_info = result.data.data;
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }
          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with the fame info."
            );
          }
        );
      },
      getLocationData() {
        axios({
          method: "GET",
          url: this.$hostname + this.localtionDataApiPrefix + this.$route.params.schoolId
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.location_data = JSON.parse(JSON.stringify(result.data.data));
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }

          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with the Ranking Historical Data."
            );
          }
        );
      },
      getScoreData() {
        axios({
          method: "GET",
          url: this.$hostname + this.scoreInfoApiPrefix + this.$route.params.schoolId
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.score_info = result.data.data;
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }
          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with the score Data."
            );
          }
        );
      },
      getSimilarSchoolList() {
        axios({
          method: "GET",
          url: this.$hostname + this.similarSchoolApiPrefix + this.$route.params.schoolId
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.similar_school_info = result.data.data;
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }

          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with the similar school list."
            );
          }
        );
      },
      sendTips(msg) {
        const h = this.$createElement;
        this.$notify.success({
          title: 'Success',
          message: h('p', { style: 'font-size:12px' }, msg),
          duration: 1500
        });
      },
      sendAlert(msg) {
        this.$notify.warning({
          title: 'Warning',
          message: h('p', { style: 'font-size:12px' }, msg),
          duration: 1500
        });
      },
      sendSuccessMsg(msg) {
        const h = this.$createElement;
        this.$message.success({
          type: 'Success',
          message: msg
        });
      },
      sendErrorMsg(msg) {
        this.$message.warning({
          type: 'Warning',
          message: msg
        });
      },
    },
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

  #index_title {
    line-height: 120px;
  }

  body {
    color: rgb(240, 255, 255);
    background-image: url('../assets/images/gray_64.png');
  }

  .location_chart {
    height: 230px;
    width: 100%;
    padding-top: 0px;
    margin-top: 5px;
  }
  .location_chart > img {
    width: 100%;
    height: 212px;
  }

  .chart_title{
    width: 60%;
    height: 10%;
    float: left;
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    padding-left: 4%;
    font-size: 25px;
    padding-bottom: 15px;
  }
</style>