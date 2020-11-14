<template>
  <el-container style="height: 300px;">
    <div class="fame_tab_title">Sentimental Analysis</div>
    <el-container style="width: 45%;">
      <el-main v-if='sentimental_tags_obj' >
        <el-tag :key="tag.name" v-for="tag in sentimental_tags_obj.positive_info.data"
          :type="tag.value > 4 ? 'success' : tag.value > 2 ? 'none' : 'info'"
          :effect="tag.value > 6 ? 'dark' : tag.value > 3 ? 'light' : 'plain'"
          :size="tag.value > 7 ? 'medium' : tag.value > 2 ? 'small' : 'mini'">
          {{tag.name}}
        </el-tag>
      </el-main>
      <el-footer class="left_footer">
        <el-tooltip class="item" effect="light" placement="top-start" v-if='sentimental_tags_obj'>
          <div slot="content">
            <span>the constituent of reviewers is </span><br />
            <span>{{gen_content(sentimental_tags_obj.positive_info.people)}}</span>
          </div>
          <div class='positive' :style="{width: sentimental_tags_obj.positive_info.percent}">
            <span
              style="float: left; font-size: 30px; color: rgba(255, 255, 255, 0.7); padding-top: 10px; padding-left: 10px;">
              {{sentimental_tags_obj.positive_info.percent}}
              <span
                style="font-size: 20px; color: rgba(255, 255, 255, 0.3);">[{{sentimental_tags_obj.positive_info.total}}
                reviews]</span>
            </span>
          </div>
        </el-tooltip>
        <el-tooltip class="item" effect="light" placement="top-start" v-if='sentimental_tags_obj'>
          <div slot="content">
            <span>the constituent of reviewers is </span><br />
            <span>{{gen_content(sentimental_tags_obj.negative_info.people)}}</span>
          </div>
          <div class='negative' :style="{width: sentimental_tags_obj.negative_info.percent}">
            <span
              style="float: right; font-size: 30px; color: rgba(255, 255, 255, 0.7); padding-top: 10px; padding-right: 10px;">
              <span
                style="font-size: 20px; color: rgba(255, 255, 255, 0.3); ">[{{sentimental_tags_obj.negative_info.total}}
                reviews]</span>
              {{sentimental_tags_obj.negative_info.percent}}
            </span>
          </div>
        </el-tooltip>
      </el-footer>
    </el-container>

    <el-container style="height: 80%; width: 45%;">
      <el-main v-if='sentimental_tags_obj'>
        <el-tag :key="tag.name" v-for="tag in sentimental_tags_obj.negative_info.data"
          :type="tag.value > 4 ? 'danger' : tag.value > 2 ? 'warning' : 'info'"
          :effect="tag.value > 6 ? 'dark' : tag.value > 3 ? 'light' : 'plain'"
          :size="tag.value > 7 ? 'medium' : tag.value > 2 ? 'small' : 'mini'">
          {{tag.name}}
        </el-tag>
      </el-main>
    </el-container>
  </el-container>
</template>


<script>
  export default {
    props: {
      sentimental_tags_obj: {
        type: Object,
        required: true,
      },

    },

    data() {
      return {

      }

    },
    methods: {
      onWordHover(value) {
        console.log(value)
      },
      gen_content(obj) {
        return 'freshman : ' + (obj.freshman == undefined ? '0%' : obj.freshman) + " | sophomore : "
          + (obj.sophomore == undefined ? '0%' : obj.sophomore) + " | junior : " + (obj.junior == undefined ? '0%' : obj.junior) + " | senior : " + (obj.senior == undefined ? '0%' : obj.senior) +
          " | alum : " + (obj.alum == undefined ? '0%' : obj.alum) + " | other : " + (obj.other == undefined ? '0%' : obj.other);
      },

    },
  }
</script>


<style scoped>
  .fame_tab_title {
    color: rgb(255, 255, 255);
    font-family: "microsoft yahei";
    padding-left: 4%;
    font-size: 25px;
    float: left;
  }

  .tag {
    font-family: "microsoft yahei";
    cursor: pointer;
    font-size: 35px;
  }

  .el-tag {
    margin-top: 5px;
    margin-left: 5px;
  }

  .el-main::-webkit-scrollbar {
    width: 0;
  }


  .left_footer {
    width: 194%;
  }

  .el-footer {
    padding-left: 0px;
    margin-bottom: 0px;
    padding-bottom: 0px;
  }

  .positive {
    background-color: rgba(142, 206, 142, 0.5);
    height: 100%;
    float: left;

  }

  .negative {
    height: 100%;
    background-color: rgba(192, 134, 134, 0.5);
    float: right;
  }
</style>