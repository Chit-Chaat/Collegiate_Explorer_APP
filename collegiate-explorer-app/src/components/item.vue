<template>
  <div class='cc_item'>
    <el-card class="box-card" :body-style="{ height:'200px' }">
      <div slot="header" class="clearfix">
        <div class='title'><img :src="require('../assets/images/' + item.logo)" width="25px"><span
            class='school_name'>{{item.name}}</span>
        </div>
        <div style="display: inline;">
          <el-button class="go_detail_btn" size="medium" type="text"><i class="el-icon-link"></i>Link</el-button>
        </div>
      </div>
      <div class="location"><i class="el-icon-map-location"></i>{{item.address}} | <i
          class="el-icon-chat-line-square"></i>{{item.review}} reviews</div>
      <div class="desc">{{item.desc}}</div>
      <el-divider content-position="right">Other</el-divider>
      <div class="other">
        <div class="ratingA">Niche:
          <el-rate v-model="item.rating.A" disabled void-icon-class="el-icon-medal" :icon-classes="iconClasses" :colors="iconColors" style="display: inline;"
            :score-template="item.rating.A_val">
          </el-rate>
        </div>
        <div class="ratingB">CC:
          <el-rate v-model="item.rating.B" disabled void-icon-class="el-icon-medal" :icon-classes="iconClasses" :colors="iconColors" style="display: inline;"
            :score-template="item.rating.B_val">
          </el-rate>
        </div>
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
        currentDate: new Date(),
        iconClasses: ["el-icon-medal-1","el-icon-medal-1", "el-icon-medal-1"],
        iconColors: ['#99A9BF', '#F7BA2A', '#FF9900']
      };
    },
    methods: {
      
    },
  }
</script>

<style scoped>
  .el-divider {
    margin: 10px 0;
  }

  .cc_item {
    text-align: left;
  }

  .go_detail_btn {
    float: right;
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
    padding-left: 10px;
    font-size: 20px;
    top: -5px;
  }

  .location {
    margin-top: -15px;
    font-size: 14 px;
    color: darkgray;
  }

  .desc {
    margin-top: 5px;
    font-size: 14 px;
    color: rgb(105, 103, 103);
  }

  .ratingA {
    display: inline;
  }
  .ratingB {
    padding-left: 5px;
    display: inline;
  }
</style>