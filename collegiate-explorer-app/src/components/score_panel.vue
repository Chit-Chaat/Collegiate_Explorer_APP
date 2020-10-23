<template>

  <el-container style="height: 295px;">
    <div class="score_tab_chart_title">ACT&SAT</div>
    <el-aside width="300px">
      <g2-radar :is-show-area="true" :show-legend="true" :axis-name="{niche:'Niche', cc:'CollegeConfidential'}"
        :axisColor="{ lineColor: 'rgb(240, 255, 255)', labelColor: 'rgb(240, 255, 255)' }" :data="score_obj.score_data"
        style="height: 260px; width: 100%;">
      </g2-radar>
    </el-aside>
    <el-main style="width: 90%; height: 100%; padding-bottom: 0px; padding-top: 0px;">
      <div class="score_tab_desc_title">
        <img :src="require('../assets/images/niche-logo2.png')" width="30px"> Niche Site said:</div>
      <div class="niche_desc" v-if="score_obj.score_desc.niche">For the student who got an offer from this school,
        their SAT score range is
        <span class="highlight_val">{{score_obj.score_desc.niche.sat_range}}</span>, and their ACT score range is
        <span class="highlight_val">{{score_obj.score_desc.niche.act_range}}</span>.
      </div>
      <div class="score_tab_desc_title">
        <img :src="require('../assets/images/cc-logo.jpg')" width="30px"> College Confidential said:</div>
      <div class="niche_desc" v-if="score_obj.score_desc.cc">For the student who got an offer from this school, most
        of their SAT math score is
        <span class="highlight_val">{{score_obj.score_desc.cc.sat.math}}</span>, SAT reading is <span
          class="highlight_val">{{score_obj.score_desc.cc.sat.reading}}</span>
        and SAT writing is <span class="highlight_val">{{score_obj.score_desc.cc.sat.writing}}</span>. Also their ACT
        score midpoint is
        <span class="highlight_val">{{score_obj.score_desc.cc.act}}</span>. The avg of GPA is <span
          class="highlight_val">{{score_obj.score_desc.cc.gpa}}</span>.
      </div>
    </el-main>
  </el-container>

</template>


<script>

  export default {
    props: {
      score_obj: {
        type: Object,
        required: true,
      }
    }
  }
</script>


<style scoped>
  .score_tab_chart_title {
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    padding-left: 4%;
    font-size: 25px;
  }

  .score_tab_desc_title {
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    font-size: 25px;
    width: 90%;
  }

  .niche_desc {
    float: left;
    font-size: 18px;
    color: azure;
    padding-top: 10px;
    padding-left: 40px;
    width: 90%;
    text-align: left;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    text-align: left;
    margin-bottom: 20px;
  }


  .highlight_val {
    color: darkorange;
    font-size: 18px;
    font-weight: 600;
    text-decoration: underline;
  }
</style>