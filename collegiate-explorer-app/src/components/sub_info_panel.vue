<template>

  <el-container style="height: 255px;" v-if="sub_info_obj">
    <el-tabs tab-position="left" v-model="activeName" @tab-click="testssss">
      <el-tab-pane label="Subjective Statistic" disabled name='index'>
      </el-tab-pane>
      <el-tab-pane label="Niche Review" name="niche">
        <el-container style="padding-left: 5%;">
          <el-main class="niche-panel">
            <div class="sub_desc">In order to find most suitable school for every students,
              we analysis different aspect of review text information on <img
                :src="require('../assets/images/niche-logo.png')" width="30px" style="vertical-align: sub;">
              Niche website. Aiming at this goal, a systematic investigation and study was
              carried out on following aspects: </div>
            <el-row v-for="item in sub_info_obj.niche_ranking" :key='item.item'>
              <el-col :span="4">
                <span style="color: rgb(255, 255, 255); font-size: 18px;">{{item.item}}</span>
              </el-col>
              <el-col :span="5">
                <el-rate v-model="item.score" :icon-classes="iconClasses"
                  style="display: inline; pointer-events: none; cursor: default;" void-icon-class="icon-rate-face-off"
                  :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
                </el-rate>
              </el-col>
              <el-col :span="4">
                <span style="color: rgb(255, 255, 255); font-size: 18px;">{{item.label}}</span>
              </el-col>
            </el-row>
            <div style="float:right; position: relative; top: -70px; left: -150px;">
              <span style="color: rgb(255, 255, 255); font-size: 18px;">Over all Ranking : </span>
              <span class="highlight_val">{{sub_info_obj.over_all_ranking}}</span>
            </div>
          </el-main>
        </el-container>
      </el-tab-pane>
      <el-tab-pane label="Named Title" name='title'>
        <el-container style="padding-left: 5%;">
          <el-main class="niche-panel">
            <div class="sub_desc">See Where this school lands in our other rankingd to get a bigger
              picture of the institution's offereings.
            </div>
            <el-row v-for="title in sub_info_obj.title_list" :key='title.item' style="padding-top: 10px;">
              <el-col :span="3">
                <span style="color: rgb(255, 255, 255); font-size: 18px;"><i class="el-icon-star-on"
                    style="color: darkorange;"></i> #{{title.ranking}}</span>
              </el-col>
              <el-col :span="2">
                <span style="padding-left: 10px; font-size: 18px; color: darkgray;">in</span>
              </el-col>
              <el-col :span="12">
                <span style="color: rgb(255, 255, 255); font-size: 18px;">{{title.item}}</span>
              </el-col>
              <el-col :span="5">
                <div style="color:darkgray; font-size: 16px; 
                overflow: hidden; width: 90%;
                text-overflow: ellipsis;
                white-space: nowrap;">({{title.desc}})</div>
              </el-col>
            </el-row>

          </el-main>
        </el-container>
      </el-tab-pane>
      <el-tab-pane label="..." name='dontknow' disabled>
        Nothing here
      </el-tab-pane>
    </el-tabs>
  </el-container>

</template>


<script>

  export default {
    props: {
      sub_info_obj: {
        type: Object,
        required: true,
      }
    },
    data() {
      return {
        activeName: 'niche',
        iconClasses: ['icon-rate-face-1', 'icon-rate-face-2', 'icon-rate-face-3'],
        iconColors: ['#99A9BF', '#F7BA2A', '#FF9900']
      }
    },
    mounted() {
    },
    methods: {
      testssss(e) {
        if (e.label === 'Niche Review') {
          console.log(e.currentTarget)
        }
      }
    },
  }
</script>


<style scoped>
  @import "../assets/fonts/style.css";

  .icon-android {
    font-size: 24px;
    color: darkorchid;
  }

  .el-tabs>>>.el-tabs__item {
    color: rgb(255, 255, 255);
    text-align: right;
    font-family: "microsoft yahei";
    font-size: 25px;
    top: 20px;
  }

  .el-tabs>>>.el-tabs__item:hover {
    color: darkorange;
    cursor: grab;
  }

  .el-tabs>>>.el-tabs__item.is-active {
    color: darkorange;
  }

  .el-tabs>>>.el-tabs__active-bar {
    top: 20px;
    background-color: darkorange;
  }

  .el-tabs {
    padding-left: 3%;
    height: 100%;
  }


  .el-link {
    color: rgb(255, 255, 255);
    font-size: 18px;
  }

  .sub_desc {
    width: 100%;
    color: rgb(255, 255, 255);
    font-size: 18px;
    padding-bottom: 10px;
  }

  .niche-panel {
    width: 710px;
    height: 100%;
    padding-top: 0px;
    padding-bottom: 0px;
  }


  .highlight_val {
    color: #ff8c00;
    font-size: 22px;
    font-weight: 600;
    vertical-align: sub;
  }
</style>