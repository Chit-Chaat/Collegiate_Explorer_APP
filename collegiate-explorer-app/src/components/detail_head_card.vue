<template>
  <div class='right_card'>
    <div class="upper_part">
      <div class="quick_fact">Quick Fact: <span class="title">{{desc_obj.title}}</span></div>
      <div class="location"><i class="el-icon-map-location"></i> {{desc_obj.location}}</div>
      <div class="admission">
        <el-row :gutter="10" style="margin-bottom: 15px;">
          <el-col :span="7">
            <div class="acceptance_title">Acceptance Rate:</div>
          </el-col>
          <el-col :span="5" v-if="desc_obj.admission">
            <div class="acceptance_val">
              {{desc_obj.admission.acceptance_rate}}</div>
          </el-col>
          <el-col :span="6">
            <div class="ddl_title"> Apply DeadLine:</div>
          </el-col>
          <el-col :span="6" v-if="desc_obj.admission">
            <div class="acceptance_ddl">{{desc_obj.admission.application_ddl}}</div>
          </el-col>
        </el-row>
        <el-row :gutter="10" style="margin-bottom: 15px;">
          <el-col :span="7">
            <div class="acceptance_title">Application Fee:</div>
          </el-col>
          <el-col :span="7">
            <div class="salary_val">
              ${{desc_obj.app_fee}} <span style="color: darkgray; font-size: 12px; font-weight: 400;">
                /program</span></div>
          </el-col>
          
          <el-col :span="10"> </el-col>
        </el-row>
  
        <el-row :gutter="10" style="margin-bottom: 15px;">
          <el-col :span="7">
            <div class="acceptance_title">Basic Tuition: </div>
          </el-col>
          <el-col :span="10">
            <div class="salary_val"  v-if="desc_obj.cost">
              ${{desc_obj.cost.net_price}} <span class="hidden_val">/year </span></div>
          </el-col>
          
          <el-col :span="7"></el-col>
        </el-row>

      </div>
    </div>
    <div class="lower_part">
      <el-collapse v-model="default_open_tab" accordion class="lower_collapse">
        <el-collapse-item title="Scores" name="1">
          <div class='text_item'>Average SAT Score:</div>
          <div class='text_item' v-if="desc_obj.avg_score" style="padding-left: 10px;">
            Reading: <span class="tab_val"> {{desc_obj.avg_score.reading}}</span> | Math: <span class="tab_val">
              {{desc_obj.avg_score.math}}</span> | ACT Composite: <span class="tab_val">
              {{desc_obj.avg_score.composite}}</span>
          </div>
        </el-collapse-item>
        <el-collapse-item title="Students" name="2">
          <div class='text_item'>This university has</div>
          <div class='text_item' v-if="desc_obj.students" style="padding-left: 10px;">
            Undergraduate: <span class="tab_val"> {{desc_obj.students.undergraduate}}</span> | Graduate: <span
              class="tab_val"> {{desc_obj.students.graduate}}</span>
          </div>
        </el-collapse-item>
        <el-collapse-item title="Statistics" name="3">
          <div class='text_item' v-if="desc_obj.stat" style="padding-left: 10px;">
            Graduation Rate: <span class="tab_val"> {{desc_obj.stat.graduation_rate}}</span> <span class="hidden_val">× 100% </span>
          </div>
          <div class='text_item' v-if="desc_obj.stat" style="padding-left: 10px;">
            Freshman Retention: <span class="tab_val"> {{desc_obj.stat.freshman_retention}} </span> <span class="hidden_val">× 100% </span>
          </div>
        </el-collapse-item>
        <el-collapse-item title="Salary" name="4">
          <div class='text_item' v-if="desc_obj.stat" style="padding-left: 10px;">
            Employment Rate: <span class="tab_val"> {{desc_obj.stat.employment_rate}} </span>
          </div>
          <div class='text_item' v-if="desc_obj.stat" style="padding-left: 10px;">
            Median Of Salary: <span class="tab_val"> ${{desc_obj.stat.median_salary}} </span> <span class="hidden_val">/ year (after 6 years)</span>
          </div>
        </el-collapse-item>
      </el-collapse>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      desc_obj: {
        type: Object,
        required: true,
      }
    },
    data() {
      return {
        default_open_tab: '1'
      };
    }
  }
</script>

<style scoped>
  .right_card {
    width: 96%;
    height: 100%;
  }

  .upper_part {
    background-color: #FFF;
    height: 40%;

  }

  .lower_part {
    background-color: #FFF;
    height: 60%;
  }

  .lower_collapse {
    width: 90%;
    padding-left: 5%;
    padding-right: 5%;
  }

  .quick_fact {
    line-height: 30px;
    padding-left: 28px;
    font-size: 23px;
    color: darkorange;
    padding-top: 10px;
  }

  .title {
    font-size: 13px;
    color: darkgray;
  }

  .location {
    line-height: 30px;
    font-size: 15px;
    padding-left: 28px;
  }

  .admission {
    padding-top: 5px;
    width: 100%;
    height: 100px;

  }

  .bg-purple {
    background: #d3dce6;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }

  .text_item {
    width: 90%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .acceptance_title {
    line-height: 20px;
    padding-left: 30px;
    width: 75%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .tuition_title{
    line-height: 20px;
    margin-left: -40px;
    width: 90%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .ddl_title {
    padding-left: 45px;
    width: 90%;
    line-height: 20px;
    margin-left: -35px;
    margin-right: 20px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .acceptance_val {
    line-height: 20px;
    color: darkorange;
    font-size: 20px;
    margin-top: -3px;
    font-weight: 600;
  }

  .acceptance_ddl {
    width: 100%;
    line-height: 20px;
    color: darkorange;
    font-size: 20px;
    margin-top: -3px;
    font-weight: 600;
    margin-left: -15%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .salary_tip {
    line-height: 20px;
    width: 75%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-left: -43px;
  }

  .salary_val {
    line-height: 20px;
    color: darkorange;
    font-size: 20px;
    margin-top: -3px;
    font-weight: 600;
  }

  .tuition_val{
    line-height: 20px;
    color: darkorange;
    font-size: 20px;
    margin-top: -3px;
    margin-left: -33px;
    font-weight: 600;
  }

  .hidden_val {
    color: darkgray;
    font-size: 12px;
    font-weight: 400;
    width: 20px !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    white-space: nowrap !important;
  }

  .tab_val {
    color: darkorange;
    font-size: 12px;
    font-weight: 600;
  }
</style>
