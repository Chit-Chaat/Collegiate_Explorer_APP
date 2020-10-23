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
        <div class='ranking_chart'>
          <div style="text-align: left; font-size: 17px; color: azure; padding-left: 20px;">Historical Ranking of
            {{title_info.main_title}}</div>
          <g2-area :padding="['auto', 30]" :data="ranking_data"
            :axis-name="{name:'Years', value:'Ranking', type:'Site'}"
            :axisColor="{ lineColor: 'rgb(240, 255, 255)', labelColor: 'rgb(240, 255, 255)' }"
            style="height: 180px; width: 100%;">
          </g2-area>
        </div>
      </el-main>
      <el-aside width="40%" style="line-height: 200px;">
        <HeadCard :desc_obj="desc_info"></HeadCard>
      </el-aside>
    </el-container>

    <el-divider></el-divider>
    <ScorePanel :score_obj="score_info"></ScorePanel>

    <el-divider></el-divider>
    <FamePanel :fame_obj="fame_info"></FamePanel>

    <el-divider></el-divider>
    <SimilarSchoolPanel></SimilarSchoolPanel>

    <el-divider></el-divider>
    <PopularMajorPanel></PopularMajorPanel>
    <!-- <el-divider></el-divider>
    <el-container>
      <el-container style="height: 300px;">
        <el-aside width="300px">Chart</el-aside>
        <el-main>Desc</el-main>
      </el-container>
    </el-container> just in case, if group member wanna add other info in the detail page-->

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
  import HeadCard from '../components/detail_head_card.vue'
  import ScorePanel from '../components/score_panel.vue'
  import FamePanel from '../components/fame_panel.vue'
  import SimilarSchoolPanel from '../components/similar_school_panel.vue'
  import PopularMajorPanel from '../components/popular_major_panel.vue'
  export default {
    components: {
      Header,
      Title,
      Footer,
      HeadCard,
      ScorePanel,
      FamePanel,
      SimilarSchoolPanel,
      PopularMajorPanel,
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
        desc_info: {},
        ranking_data: [
          { name: '1997', value: 37, type: 'Niche' },
          { name: '2007', value: 35, type: 'Niche' },
          { name: '2018', value: 30, type: 'Niche' },
          { name: '2020', value: 33, type: 'Niche' },
          { name: '1997', value: 40, type: 'CollegeConfidential' },
          { name: '2007', value: 36, type: 'CollegeConfidential' },
          { name: '2018', value: 35, type: 'CollegeConfidential' },
          { name: '2020', value: 39, type: 'CollegeConfidential' },
          { name: '1997', value: 30, type: 'QS News' },
          { name: '2007', value: 32, type: 'QS News' },
          { name: '2018', value: 35, type: 'QS News' },
          { name: '2020', value: 32, type: 'QS News' },
        ],
        score_info: {
          score_data: [],
          score_desc: {},
        },
        fame_info: {},
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
      this.desc_info = {
        title: "University of Southern California",
        location: "University Park Los Angeles, CA 90089",
        avg_score: {
          reading: "700",
          math: "714",
          composite: "32"
        },
        expected_salary: "74,000",
        cost: {
          net_price: '36,161',
          national: "15,523",
          financial_aid: "69%",
          avg_aid_award: "35,953"
        },
        admission: {
          acceptance_rate: '13%',
          application_ddl: 'January 15th'
        },
        students: {
          undergraduate: "20,048",
          graduate: "27,970",
          international: "2,499"
        }
      }
      this.score_info = {
        score_data: [
          { item: 'SAT_reading', niche: 67.5, cc: 60.3 }, // div 10
          { item: 'SAT_writing', niche: 64.6, cc: 50.6 }, // div 10
          { item: 'SAT_math', niche: 71.0, cc: 70.1 }, // div 10
          { item: 'ACT', niche: 64, cc: 68 }, // * 2
          { item: 'GPA', niche: 76, cc: 74 } // * 20
        ],
        score_desc: {
          niche: {
            sat_range: '1390-1540',
            act_range: '32-35',
          },
          cc: {
            sat: {
              reading: 731,
              writing: 656,
              math: 731,
            },
            act: 32,
            gpa: 3.72
          }
        }
      }
      this.fame_info = {}

    },
    methods: {
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

  .ranking_chart {
    height: 230px;
    padding-top: 10px;
    margin-top: 10px;
  }
</style>