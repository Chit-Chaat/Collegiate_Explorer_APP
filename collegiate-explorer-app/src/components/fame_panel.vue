<template>
  <el-container style="height: 255px;">
    <div class="fame_tab_title">Hall of Fame</div>
    <el-aside width="320px">
      <el-card class="box-card">
        <div slot="header" v-if="title">
          <span>{{title}}</span>
        </div>
        <div class="text item" v-if="fame_obj.president">
          <div style="display: inline;">President: </div>
          <el-avatar class="avatar_img" :size="20" @error="errorImgHandler" :src="fame_obj.president.profile">
          </el-avatar>
          {{fame_obj.president.name}}
        </div>
        <div class="text item" v-if="fame_obj.motto">
          <div style="display: inline; padding-right: 22px;">Motto: </div> <span class="highlight_val">
            {{fame_obj.motto.words}}</span>
        </div>
        <div class="text item" v-if="fame_obj.mascot">
          <div style="display: inline; padding-right: 12px;">Mascot: </div>
          <el-avatar class="avatar_img" :size="20" @error="errorImgHandler" :src="fame_obj.mascot.logo"></el-avatar>
          {{fame_obj.mascot.name}}
        </div>
        <div class="text item" v-if="fame_obj.color">
          <div style="display: inline; padding-right: 23px;vertical-align: middle;">Color: </div>
          <div v-for="color in fame_obj.color" :key="color.name" style="display: inline; vertical-align: middle;">
            <el-tooltip class="item" effect="light" :content="color.name" placement="bottom-start">
              <el-color-picker :value="color.rgb" disabled></el-color-picker>&nbsp;
            </el-tooltip>
          </div>
        </div>
      </el-card>
    </el-aside>
    <el-main>
      <el-card class="right-card">
        <div slot="header">
          <span><i class="el-icon-office-building"></i> Affiliations</span>
        </div>
        <div class="text item" v-for="org in fame_obj.affiliations" :key="org.name">
          <el-link :href="org.link">
            <el-avatar class="avatar_img" :size="20" icon="el-icon-house">
            </el-avatar>
            {{org.name}}
          </el-link>
        </div>

      </el-card>
      <el-card class="right-card">
        <div slot="header">
          <span><i class="el-icon-user"></i> Athletics</span>
        </div>
        <div class="text item" v-for="person in fame_obj.athletics" :key="person.name">
          <el-link :href="person.link">
            <el-avatar class="avatar_img" :size="20" icon="el-icon-user-solid">
            </el-avatar>
            {{person.name}}
          </el-link>
        </div>
      </el-card>

    </el-main>
  </el-container>
</template>


<script>
  export default {
    props: {
      fame_obj: {
        type: Object,
        required: false,
      },
      title: {
        type: String,
        required: true,
      }
    },
    methods: {
      errorImgHandler() {
        return true
      }
    }
  }
</script>


<style scoped>
  .fame_tab_title {
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    padding-left: 4%;
    font-size: 25px;
    height: 40px;
    width: 15%;
  }


  .highlight_val {
    color: darkorange;
    font-size: 18px;
    font-weight: 600;
    text-decoration: underline;
  }

  .text {
    font-size: 14px;
    vertical-align: middle;

  }

  .avatar_img {
    vertical-align: middle;
  }

  .item {
    margin-bottom: 15px;
    line-height: 20px;
    vertical-align: middle;
  }

  .item:last-child {
    margin-bottom: 0px;
  }

  .el-main {
    padding: 0 10px;
  }

  .el-card__header>div {
    text-align: center;
  }

  .box-card {
    bottom: 0;
    width: 95%;
    margin-left: 2%;
  }

  .right-card {
    width: 45%;
    display: inline-block;
    margin-left: 1%;
    height: 95%;
  }

  .highlight_val {
    color: darkorange;
    font-size: 15px;
    font-weight: 600;
  }
</style>