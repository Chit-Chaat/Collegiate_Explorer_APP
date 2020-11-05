<template>
  <div>
    <el-tabs v-model="activeName" type="border-card" @tab-click="handleClick">
      <el-tab-pane name="basic">
        <span slot="label"><i class="el-icon-pie-chart"></i> Area & Major & Score</span>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Selected:
          </el-col>
          <el-col :span="20" style="margin-left: 10px;">
            <el-tag v-if="this.selectTags.area !== ''" closable size="small" @close="handle_close('basic', 0)">
              {{this.selectTags.area}}
            </el-tag>
            <el-tag v-if="this.selectTags.major !== ''" closable size="small" @close="handle_close('basic', 1)">
              {{this.selectTags.major}}
            </el-tag>
            <el-tag v-if="this.selectTags.tuition !== ''" closable size="small" @close="handle_close('basic', 2)">
              {{this.selectTags.tuition}}
            </el-tag>
            <el-tag v-if="this.selectTags.act !== ''" closable size="small" @close="handle_close('basic', 3)">
              ACT: {{this.selectTags.act}}
            </el-tag>
            <el-tag v-if="this.selectTags.sat !== ''" closable size="small" @close="handle_close('basic', 4)">
              SAT: {{this.selectTags.sat}}
            </el-tag>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Area:
          </el-col>
          <el-col :span="20">
            <el-button type="text" v-for="area in areas" :key="area" size="medium" @click="select_key(area,0)">{{area}}
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Major：
          </el-col>
          <el-col :span="20">
            <el-button type="text" v-for="major in marjors" :key="major" size="medium" @click="select_key(major,1)">
              {{major}}
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Tuition：
          </el-col>
          <el-col :span="20">
            <el-button type="text" v-for="tuition in tuitions" :key="tuition" size="medium"
              @click="select_key(tuition,2)">
              {{tuition}}
            </el-button>
            <span style="color: darkgray;">[per semester]</span>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            ACT:
          </el-col>
          <el-col :span="14">
            <el-slider v-model="act_score" range show-stops :marks="act_marks" :min="20" :max="36"
              style="padding-left: 10px;">
            </el-slider>
          </el-col>
          <el-col :span="8" style="color:  darkgray; padding-left: 15px;">
            <el-button type="text" @click="select_key(act_score,3)"
              style="font-size: 15px; text-decoration: underline;">
              ACT Range: {{act_score}}
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            SAT:
          </el-col>
          <el-col :span="14">
            <el-slider v-model="sat_score" range :marks="sat_marks" :min="1000" :max="1600" style="padding-left: 10px;">
            </el-slider>
          </el-col>
          <el-col :span="8" style="color:  darkgray; padding-left: 15px;">
            <el-button type="text" @click="select_key(sat_score,4)"
              style="font-size: 15px; text-decoration: underline;">
              SAT Range: {{sat_score}}
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="23" style="text-align: right;">
            <el-button-group>
              <el-button icon="el-icon-refresh-right" @click="reset($event, 'basic')">Rest Thsi Panel</el-button>
              <el-button @click="go_search($event,'basic')">Search<i class="el-icon-search el-icon--right"></i></el-button>
            </el-button-group>
          </el-col>
        </el-row>
      </el-tab-pane>
      <el-tab-pane name="niche">
        <span slot="label"><img
          :src="require('../assets/images/niche-logo.png')" width="20px" style="vertical-align: sub;"> Niche Ranking</span>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Selected:
          </el-col>
          <el-col :span="20" style="margin-left: 10px;">
            <el-tag v-if="this.nicheRankings.academic !== ''" closable size="small" @close="handle_close('niche',0)">
              ACADEMIC: {{rank_strs[this.nicheRankings.academic]}}
            </el-tag>
            <el-tag v-if="this.nicheRankings.dorms !== ''" closable size="small" @close="handle_close('niche',1)">
              DORNS: {{rank_strs[this.nicheRankings.dorms]}}
            </el-tag>
            <el-tag v-if="this.nicheRankings.food !== ''" closable size="small" @close="handle_close('niche',2)">
              FOOD: {{rank_strs[this.nicheRankings.food]}}
            </el-tag>
            <el-tag v-if="this.nicheRankings.location !== ''" closable size="small" @close="handle_close('niche',3)">
              LOCATION: {{rank_strs[this.nicheRankings.location]}}
            </el-tag>
            <el-tag v-if="this.nicheRankings.safety !== ''" closable size="small" @close="handle_close('niche',4)">
              SAFETY: {{rank_strs[this.nicheRankings.safety]}}
            </el-tag>
            <el-tag v-if="this.nicheRankings.value !== ''" closable size="small" @close="handle_close('niche',5)">
              VALUE: {{rank_strs[this.nicheRankings.value]}}
            </el-tag>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Academic:
          </el-col>
          <el-col :span="14">
            <el-slider v-model="academic_scores" show-stops :show-tooltip='false' :min="0" :max="4"
              style="padding-left: 10px;">
            </el-slider>
          </el-col>
          <el-col :span="8" style="color:  #a9a9a9; padding-left: 15px;">
            <el-button type="text" @click="select_key(academic_scores,5)" style="font-size: 18px;">
              {{rank_strs[academic_scores]}} ! <i class="el-icon-thumb"></i>
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Dorms:
          </el-col>
          <el-col :span="14">
            <el-slider v-model="dorms_scores" show-stops :show-tooltip='false' :min="0" :max="4"
              style="padding-left: 10px;">
            </el-slider>
          </el-col>
          <el-col :span="8" style="color:  #a9a9a9; padding-left: 15px;">
            <el-button type="text" @click="select_key(dorms_scores,6)" style="font-size: 18px;">
              {{rank_strs[dorms_scores]}} ! <i class="el-icon-thumb"></i>
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Food:
          </el-col>
          <el-col :span="14">
            <el-slider v-model="food_scores" show-stops :show-tooltip='false' :min="0" :max="4"
              style="padding-left: 10px;">
            </el-slider>
          </el-col>
          <el-col :span="8" style="color:  #a9a9a9; padding-left: 15px;">
            <el-button type="text" @click="select_key(food_scores,7)" style="font-size: 18px;">
              {{rank_strs[food_scores]}} ! <i class="el-icon-thumb"></i>
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Location:
          </el-col>
          <el-col :span="14">
            <el-slider v-model="location_scores" show-stops :show-tooltip='false' :min="0" :max="4"
              style="padding-left: 10px;">
            </el-slider>
          </el-col>
          <el-col :span="8" style="color:  #a9a9a9; padding-left: 15px;">
            <el-button type="text" @click="select_key(location_scores,8)" style="font-size: 18px;">
              {{rank_strs[location_scores]}} ! <i class="el-icon-thumb"></i>
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Safety:
          </el-col>
          <el-col :span="14">
            <el-slider v-model="safety_scores" show-stops :show-tooltip='false' :min="0" :max="4"
              style="padding-left: 10px;">
            </el-slider>
          </el-col>
          <el-col :span="8" style="color:  #a9a9a9; padding-left: 15px;">
            <el-button type="text" @click="select_key(safety_scores,9)" style="font-size: 18px;">
              {{rank_strs[safety_scores]}} ! <i class="el-icon-thumb"></i>
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="2" style="color: yellowgreen">
            Value:
          </el-col>
          <el-col :span="14">
            <el-slider v-model="value_scores" show-stops :show-tooltip='false' :marks="rank_marks" :min="0" :max="4"
              style="padding-left: 10px;">
            </el-slider>
          </el-col>
          <el-col :span="8" style="color:  #a9a9a9; padding-left: 15px;">
            <el-button type="text" @click="select_key(value_scores,10)" style="font-size: 18px;">
              {{rank_strs[value_scores]}} ! <i class="el-icon-thumb"></i>
            </el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="23" style="text-align: right; padding-top: 10px;">
            <el-button-group>
              <el-button icon="el-icon-refresh-right" @click="reset($event, 'niche')">Rest This Panel</el-button>
              <el-button @click="go_search($event,'niche')">Go Search<i class="el-icon-search el-icon--right"></i></el-button>
            </el-button-group>
          </el-col>
        </el-row>
      </el-tab-pane>

    </el-tabs>
  </div>
</template>

<script>
  import axios from "axios"
  export default {
    data() {
      return {
        initFilterApiPrefix: "/search/init",
        activeName: 'basic',
        areas: [],
        marjors: [],
        tuitions: [],
        selectTags: {
          area: '',
          act: '',
          major: '',
          sat: '',
          tuition: '',
        },
        nicheRankings: {
          academic: '',
          dorms: '',
          food: '',
          location: '',
          safety: '',
          value: ''
        },
        rank_strs: ['Not Important', 'Slightly Important', 'Moderately Important', 'Important', 'Very Important'],
        academic_scores: 4,
        dorms_scores: 3,
        food_scores: 2,
        location_scores: 3,
        safety_scores: 2,
        value_scores: 1,
        rank_marks: {
          0.01: {
            style: {
              'margin-top': '5px',
              color: '#A9A9A9'
            },
            label: this.$createElement('strong', 'Not Important')
          },
          3: {
            style: {
              'margin-top': '5px',
              color: '#1989FA'
            },
            label: this.$createElement('strong', 'Important')
          },
          4: {
            style: {
              'margin-top': '5px',
              'width': '120px',
              color: '#1989FA',
              'font-size': '14px'
            },
            label: this.$createElement('strong', 'Very Important')
          }
        },
        act_score: [28, 32],
        act_marks: {
          30: {
            style: {
              'margin-top': '5px',
              color: '#1989FA'
            },
            label: this.$createElement('strong', '30')
          }
        },
        sat_score: [1500, 1600],
        sat_marks: {
          1550: {
            style: {
              'margin-top': '5px',
              color: '#1989FA'
            },
            label: this.$createElement('strong', '1550')
          }
        }
      }
    },
    mounted() {
      this.getFilterData()
    },
    methods: {
      handleClick(tab, event) {
        // console.log(tab, event);
      },
      getFilterData() {
        axios({
          method: "GET",
          url: this.$hostname + this.initFilterApiPrefix
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.areas = result.data.data.areas;
                this.marjors = result.data.data.marjors;
                this.tuitions = result.data.data.tuitions;
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }
          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with initialize the filter option."
            );
          }
        );
      },
      sendTips(msg) {
        const h = this.$createElement;
        this.$notify.success({
          title: 'Success',
          message: h('p', { style: 'font-size:12px' }, msg),
          duration: 1500
        });
      },
      sendAlert(msg) {
        this.$notify.warning({
          title: 'Warning',
          message: h('p', { style: 'font-size:12px' }, msg),
          duration: 1500
        });
      },
      sendSuccessMsg(msg) {
        const h = this.$createElement;
        this.$message.success({
          type: 'Success',
          message: msg
        });
      },
      sendErrorMsg(msg) {
        this.$message.warning({
          type: 'Warning',
          message: msg
        });
      },
      select_key(tag, key) {
        if (key === 0)
          this.selectTags.area = tag
        else if (key === 1)
          this.selectTags.major = tag
        else if (key === 2)
          this.selectTags.tuition = tag
        else if (key === 3)
          this.selectTags.act = tag
        else if (key === 4)
          this.selectTags.sat = tag
        else if (key === 5)
          this.nicheRankings.academic = tag
        else if (key === 6)
          this.nicheRankings.dorms = tag
        else if (key === 7)
          this.nicheRankings.food = tag
        else if (key === 8)
          this.nicheRankings.location = tag
        else if (key === 9)
          this.nicheRankings.safety = tag
        else if (key === 10)
          this.nicheRankings.value = tag
      },
      handle_close(type, tag) {
        if (type === 'basic') {
          if (tag === 0)
            this.selectTags.area = ''
          else if (tag === 1)
            this.selectTags.major = ''
          else if (tag === 2)
            this.selectTags.tuition = ''
          else if (tag === 3)
            this.selectTags.act = ''
          else if (tag === 4)
            this.selectTags.sat = ''
        } else if (type === 'niche') {
          if (tag === 0)
            this.nicheRankings.academic = ''
          else if (tag === 1)
            this.nicheRankings.dorms = ''
          else if (tag === 2)
            this.nicheRankings.food = ''
          else if (tag === 3)
            this.nicheRankings.location = ''
          else if (tag === 4)
            this.nicheRankings.safety = ''
          else if (tag === 5)
            this.nicheRankings.value = ''
        }
      },
      reset(e, type) {
        if (type === 'basic') {
          this.selectTags.area = ''
          this.selectTags.major = ''
          this.selectTags.tuition = ''
          this.selectTags.act = ''
          this.selectTags.sat = ''
        } else if (type === 'niche') {
          this.nicheRankings.academic = ''
          this.nicheRankings.dorms = ''
          this.nicheRankings.food = ''
          this.nicheRankings.location = ''
          this.nicheRankings.safety = ''
          this.nicheRankings.value = ''
        }
        this.$message({
          message: 'All filters have been cleared.',
          type: 'success'
        });
        e.currentTarget.blur()
      },
      go_search(e,type) {
        if (type === 'basic') {
          this.$emit('toggleBasic', this.selectTags)
        } else if (type === 'niche') {
          this.$emit('toggleNiche', this.nicheRankings)
        }
        this.$message({
          message: 'Http Response is on the way.',
          type: 'success'
        });
        e.currentTarget.blur()
      }
    }
  }
</script>

<style scoped>
  .el-row {
    margin: 0px 0 5px 5px;
  }

  .el-col {
    text-align: left;
  }

  .el-tag {
    margin-right: 10px;
  }

  .el-button--medium {
    padding: 0px 10px;
    font-size: 16px;
    border-radius: 4px;
    margin-left: 0px;
  }
</style>