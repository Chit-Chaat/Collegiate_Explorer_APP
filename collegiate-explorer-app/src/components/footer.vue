<template>
  <div id="cc_footer">
    <el-row :gutter="20">
      <el-col :span="6">
        <div class="title">ABOUT</div>
        <div class="about_desc">This project is for USC DSCI 558 Building Knowledge Graph
          Course.<br /><br />We believe a knowledge graph-related application like this is
          needed for tens of thousands of students across the world since they might have a hard time
          sifting through which college they want to go to. So we hope the app can solve
          this problem.</div>
      </el-col>
      <el-col :span="8">
        <div class="title">SITE MAP</div>
        <el-container>
          <el-aside>
            <el-link :underline="false">Index Page</el-link><br>
            <el-link :underline="false">User Profile</el-link><br>
            <el-link :underline="false">Detail Page</el-link><br>
            <el-link :underline="false">SPARQL</el-link><br>
            <el-link :underline="false">About Page</el-link><br>
            <el-link :underline="false">...</el-link>
            <el-link :underline="false"> </el-link>
            <el-link :underline="false"> </el-link>
          </el-aside>
          <el-main>
            <el-link :underline="false">Best College Dorms</el-link><br>
            <el-link :underline="false">Best College Food</el-link><br>
            <el-link :underline="false">Best Liberal Arts Colleges</el-link><br>
            <el-link :underline="false">Best Value Colleges</el-link><br>
            <el-link :underline="false">Colleges with the Best Academics</el-link><br>
            <el-link :underline="false">Colleges with the Best Student Life</el-link><br>
            <el-link :underline="false">Hardest Colleges to Get Into</el-link><br>
            <el-link :underline="false">Most Diverse Colleges</el-link><br>
            <el-link :underline="false">Most Expensive Colleges</el-link><br>
            <el-link :underline="false">Top Party Schools</el-link><br>
            <el-link :underline="false">Top Private Universities</el-link><br>
            <el-link :underline="false">Top Public Universities</el-link><br>
          </el-main>
        </el-container>
      </el-col>
      <el-col :span="5">
        <div class="title">CONTACT</div>
        <el-row style="width: 100%; padding-right: 0px;">
          <el-col >
            <div class="grid-content bg-purple">Aaron Yang</div>
          </el-col>
          <el-col>
            <div class="grid-content bg-purple"></div>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <div class="grid-content bg-purple">Kevin Tran</div>
          </el-col>
          <el-col>
            <div class="grid-content bg-purple"></div>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <div class="grid-content bg-purple">Ryan Ball</div>
          </el-col>
          <el-col>
            <div class="grid-content bg-purple"></div>
          </el-col>
        </el-row>

      </el-col>
      <el-col :span="4">
        <div class='chit-chat-logo'>
          <img :src="require('../assets/images/chit-chat-logo.png')"
            width="180px; background-color: #999; opacity: 0.10;">
          <div class="social_btn">
            <el-row>
              <a href="https://github.com/Chit-Chaat/Collegiate_Explorer_APP"><img
                  :src="require('../assets/images/github-icon.png')" width="40px;"></a>
              <a href="/"><img :src="require('../assets/images/facebook-icon.png')" width="40px"></a>
              <a href="/"><img :src="require('../assets/images/twitter-icon.png')" width="40px"></a>
              <a href="/"><img :src="require('../assets/images/tiktok-icon.png')" width="40px"></a>
            </el-row>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<style scoped>

.bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  #cc_footer {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    height: 100%;
  }

  .el-row {
    margin-bottom: 20px;
  }

  .el-aside {
    text-align: right;
    width: 30% !important;
  }

  .el-main {
    padding-top: 0px;
    text-align: left;
    width: 68%;
    padding-left: 10%;
  }

  .about_desc {
    color: rgb(189, 187, 187);
    font-size: 15px;
    padding-left: 43px;
    padding-right: 5px;
  }

  .title {
    color: #FFF;
    font-weight: bold;
    padding-left: 30%;
    font-size: 23px;
    padding-bottom: 10px;
  }

  .team_desc {
    color: rgb(189, 187, 187);
    font-size: 15px;
    padding-right: 10px;
  }

  .person_desc {
    padding-left: 15px;

  }

  .skill {
    padding-left: 10px;
  }

  .chit-chat-logo {
    padding-top: 20px;
    width: 200px;
    padding-left: 10px;
  }

  .el-link.el-link--default:hover {
    color: #FFF;
  }

  .el-link.el-link--default {
    color: rgb(204, 200, 200);
    font-size: 13px;

  }

  .social_btn {
    padding-left: 5px;
  }
</style>