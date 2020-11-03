<template>
  <div class='cc_item'>
    <el-card class="box-card" :body-style="{ height:'200px' }">
      <div slot="header" class="clearfix">
        <div class='title'><img :src="require('../assets/images/logo/' + item.logo)" width="25px">
          <el-link class='school_name' :underline="false"
            @click="$router.push({ name: 'Detail', params: { schoolId: item.id }})">
            {{item.name}}</el-link>
        </div>
        <div style="display: inline;">
          <el-button class="go_detail_btn" size="medium" type="text"
            @click="$router.push({ name: 'Detail', params: { schoolId: item.id }})">
            Detail<i class="el-icon-more-outline"></i></el-button>
        </div>
      </div>
      <div class="location"><i class="el-icon-map-location"></i>{{item.address}} </div>
      <div class="phone_and_review"><i class="el-icon-phone-outline"></i> {{item.telephone}} 213-477-5744 | <i class="el-icon-thumb"></i> <el-link :href="item.link">{{item.link}}</el-link></div>
      <div class="desc">{{item.desc}}</div>
      <el-divider content-position="right">Facts</el-divider>
      <div class="other">
        <el-row>
          <el-col :sm="20" :lg="12">
            <div class="ratingNiche"><img :src="require('../assets/images/qs_logo.png')" width="20px"> QS:
              <el-rate v-model="item.rating.QS" :icon-classes="iconClasses" void-icon-class="el-icon-medal"
                :colors="iconColors" style="display: inline; pointer-events: none; cursor: default;">
              </el-rate>
            </div>
          </el-col>
          <el-col :sm="16" :lg="12">
            <div class="ratingCC">
              <el-tooltip content="College Confidential" placement="bottom" effect="light"><img
                  :src="require('../assets/images/cc-logo.jpg')" width="20px">
              </el-tooltip> CC:
              <el-rate v-model="item.rating.CC" :icon-classes="iconClasses" void-icon-class="el-icon-medal"
                :colors="iconColors" style="display: inline; pointer-events: none; cursor: default;">
              </el-rate>
            </div>
          </el-col>
        </el-row>
        <el-row>
          <el-col :sm="20" :lg="13">
            <div class="num_info">School Type:
              <i class="el-icon-school" style="color: darkolivegreen;font-size: 18px;"></i><span class="num_info_val">
                {{item.school_type}}</span></div>
          </el-col>
          <el-col :sm="15" :lg="8">
            <div class="num_info">Tuition:
              <i class="el-icon-bank-card" style="color: slategrey;font-size: 18px;"></i><span class="num_info_val">
                {{item.tuition}}</span></div>
          </el-col>
          <el-col :sm="17" :lg="13">
            <div class="num_info">ACT Range:
              <i class="el-icon-finished" style="color: lightgreen; font-size: 18px;"></i><span class="num_info_val">
                {{item.ACT}}</span></div>
          </el-col>
          <el-col :sm="17" :lg="11">
            <div class="num_info">Acceptance Rate:
              <i class="el-icon-s-data" style="color: orange; height: 5px; font-size: 18px;"></i><span
                class="num_info_val"> {{item.acceptance_rate}}</span></div>
          </el-col>
        </el-row>
      </div>
    </el-card>
  </div>
</template>

<script>
  export default {
    props: {
      item: {
        type: Object,
        required: true,
      }
    },
    data() {
      return {
        iconClasses: ["el-icon-medal-1", "el-icon-medal-1", "el-icon-medal-1"],
        iconColors: ['#99A9BF', '#F7BA2A', '#FF9900']
      };
    },
    methods: {

    },
  }
</script>

<style scoped>
  .el-col {
    margin-bottom: 8px;
  }

  .el-col :last-child {
    margin-bottom: 0;
  }

  .el-divider {
    margin: 10px 0;
  }

  .cc_item {
    text-align: left;
  }

  .go_detail_btn {
    float: right;
    padding-top: 5px;
  }

  .clearfix {
    height: 25px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 100%;
  }

  .title {
    display: inline;
  }

  .school_name {
    display: inline-block;
    position: relative;
    padding-left: 5px;
    font-size: 20px;
    width: 66%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-top: -18px;
  }

  .location {
    margin-top: -15px;
    font-size: 14 px;
    color: darkgray;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .phone_and_review{
    font-size: 14 px;
    color: darkgray;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .desc {
    margin-top: 5px;
    font-size: 14 px;
    color: rgb(105, 103, 103);
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 4;
  }

  .ratingNiche {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
  }

  .ratingCC {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
  }

  .num_info {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    color: darkgray;
  }

  .num_info_val {
    color: black;
    font-weight: normal;
  }
</style>