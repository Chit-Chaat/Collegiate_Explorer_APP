<template>
  <el-container style="height: 200px;">
    <el-header class="similar_tab_title">You may also fit for thses following schools</el-header>
    <el-main style="padding-top: 0px; overflow: hidden; margin-left: -20px;">
      <div class="recommand-wrap">
        <div ref="wrapper">
          <ul class="cont" ref="cont">
            <li class="cont-item" v-for="item of similar_school_obj" :key="item.id">
              <div class="cont-img">
                <div class="img"><img :src="require('../assets/images/school_logo.jpg')" width="30px"></div>
                <div class="cont-title"><a :href="item.link">{{item.name}}</a></div>
              </div>
              <el-divider class="divider"></el-divider>
              <div class="cont-desc">
                <el-row>
                  <el-col :sm="20" :lg="15">
                    <div class="ratingNiche"><img :src="require('../assets/images/niche-logo.png')" width="20px"> Niche:
                      <el-rate v-model="item.rating.Niche" :icon-classes="iconClasses" void-icon-class="el-icon-medal"
                        :colors="iconColors" style="display: inline; pointer-events: none; cursor: default;">
                      </el-rate> {{item.rating.Niche}} / 5
                    </div>
                  </el-col>
                  <el-col :sm="16" :lg="15">
                    <div class="ratingCC">
                      <el-tooltip content="College Confidential" placement="bottom" effect="light"><img
                          :src="require('../assets/images/cc-logo.jpg')" width="20px">
                      </el-tooltip> C C:
                      <el-rate v-model="item.rating.CC" :icon-classes="iconClasses" void-icon-class="el-icon-medal"
                        :colors="iconColors"
                        style="display: inline; pointer-events: none; cursor: default; padding-left: 13px;">
                      </el-rate> {{item.rating.CC}} / 5
                    </div>
                  </el-col>
                </el-row>
                <el-row>
                  <el-col :sm="14" :lg="15">
                    <div style="padding-left: 14px; padding-top: 5px;"> Similarity Score:  <div class="highlighted_val">{{item.similarity}} </div></div>
                  </el-col>
                  <el-col :sm="10" :lg="9">
                    <el-button class="go_detail_btn" size="medium" type="text"
                    @click="$router.push({ name: 'Detail', params: { schoolId: item.id }})">
                    <i class="el-icon-bottom-right"></i></el-button>
                  </el-col>
                </el-row>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </el-main>
  </el-container>
</template>


<script>
  import BScroll from 'better-scroll'
  export default {
    props: {
      similar_school_obj: {
        type: Object|Array,
        required: true,
      },

    },
    created() {

    },
    mounted() {

    },
    data() {
      return {
        iconClasses: ["el-icon-medal-1", "el-icon-medal-1", "el-icon-medal-1"],
        iconColors: ['#99A9BF', '#F7BA2A', '#FF9900']
      }
    },
    methods: {
      verScroll() {
        var temp_obj = JSON.parse(JSON.stringify(this.similar_school_obj))
        let width = 0
        if (null === temp_obj || temp_obj.length == 0){
          width = 2100
        }else{
          width = this.similar_school_obj.length * 300
        }
        this.$refs.cont.style.width = width + 'px'
        this.$nextTick(() => {
          if (!this.scroll) {
            this.scroll = new BScroll(this.$refs.wrapper, {
              startX: 0,
              click: true,
              scrollX: true,
              scrollY: false,
              eventPassthrough: 'vertical'
            })
          } else {
            this.scroll.refresh()
          }
        })
      }
    },
    mounted() {
      this.$nextTick(() => {
        let timer = setTimeout(() => {
          if (timer) {
            clearTimeout(timer)
            this.verScroll()
          }
        }, 0)
      })
    },
  
  }
</script>


<style scoped>
  .similar_tab_title {
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    padding-left: 4%;
    font-size: 25px;
    width: 90%;
    height: 40px !important;
  }

  .divider {
    margin: 8px 0;
  }

  .recommand-wrap {
    height: 0;
    width: 100%;
  }

  .recommand-wrap .cont {
    list-style: none;
    white-space: nowrap;
    font-size: 12px;
    text-align: center;
    padding-right: 0.24rem;
    padding-left: 0px;
    width: 100px;
  }

  .recommand-wrap .cont .cont-item {
    position: relative;
    display: inline-block;
    padding: 0.06rem 0 0.2rem;
    width: 20rem;
    height: 9rem;
    margin: 0 0.2rem;
    background-color: #FFF;
  }

  .recommand-wrap .cont .cont-item .cont-img {
    overflow: hidden;
    width: 100%;
    padding-left: 1%;
    padding-top: 3%;
    margin-right: 0px;
  }

  .recommand-wrap .cont .cont-item .cont-img .cont-title {
    display: inline-block;
    font-size: 16px;
    margin-left: 5px;
  }

  .recommand-wrap .cont .cont-item .cont-img .img {
    display: inline-block;
    vertical-align: middle;
  }

  .recommand-wrap .cont .cont-item .cont-desc {
    padding: 1% 2%;
    text-align: left;
    height: 63%;
  }

  .ratingNiche {
    padding-left: 14px;
  }

  .ratingCC {
    padding-left: 14px;
  }

  .highlighted_val {
    line-height: 20px;
    color: darkorange;
    font-size: 16px;
    font-weight: 600;
    display: inline;
    padding-left: 10px;
  }

  .go_detail_btn {
    float: right;
    padding-right: 3px;
    padding-bottom: 0px;
  }

  .el-button--medium {
    color: darkorange;
    font-size: 22px;
    padding-right: 0px;
  }
</style>}