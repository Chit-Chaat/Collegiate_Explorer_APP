<template>

  <el-container style="height: 295px;" v-if="score_obj">
    <div class="score_tab_chart_title">Score Statistics</div>
    <el-aside width="300px" v-if="score_obj.score_data">
      <g2-radar :is-show-area="true" :show-legend="true" :axis-name="{score:'Score'}"
        :axisColor="{ lineColor: 'rgb(240, 255, 255)', labelColor: 'rgb(240, 255, 255)' }" :data="score_obj.score_data"
        style="height: 260px; width: 100%;">
      </g2-radar>
    </el-aside>
    <el-main style="width: 90%; height: 100%; padding-bottom: 0px; padding-top: 0px;">
      <div class="score_tab_desc_title">
        Students who received offer have the following characteristics:</div>
      <div class="score_desc" v-if="score_obj.score_desc">For these students, most
        of their SAT math score is
        <span class="highlight_val">{{score_obj.score_desc.cc.sat.math}}</span>, SAT reading is <span
          class="highlight_val">{{score_obj.score_desc.cc.sat.reading}}</span>
        and SAT writing is <span class="highlight_val">{{score_obj.score_desc.cc.sat.writing}}</span>. Also their ACT
        score midpoint is
        <span class="highlight_val">{{score_obj.score_desc.cc.act}}</span>. The avg of GPA is <span
          class="highlight_val">{{score_obj.score_desc.cc.gpa}}</span>.
        From this aspect, candidates who got these scores or had a better performance in other fields will be admitted.
        <br /><br />
        <div style="padding-left: 200px">--- All data from
          <img :src="require('../assets/images/cc-logo.jpg')" width="20px">
          <el-link :underline="false">College Confidential (CC) </el-link> <br/>
          & <img :src="require('../assets/images/qs_logo.png')" width="20px" style="vertical-align: sub;">
          <el-link :underline="false">TopUniversities (QS Ranking) </el-link>
        </div>
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
    width: 17%;
  }

  .score_tab_desc_title {
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    font-size: 25px;
    width: 90%;
  }

  .el-link {
    color: rgb(255, 255, 255);
    font-size: 18px;
  }

  .score_desc {
    float: left;
    font-size: 18px;
    color: azure;
    padding-top: 10px;
    padding-left: 40px;
    width: 70%;
    height: 65%;
    text-align: left;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    text-align: left;
    margin-bottom: 20px;
    -webkit-box-orient: vertical;
    overflow: hidden;

  }


  .highlight_val {
    color: #ff8c00;
    font-size: 18px;
    font-weight: 600;
    text-decoration: underline;
  }
</style>