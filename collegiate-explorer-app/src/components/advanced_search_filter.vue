<template>
  <div>
    <el-card>
      <el-row>
        <el-col :span="2" style="color: yellowgreen">
          Selected:
        </el-col>
        <el-col :span="20" style="margin-left: 10px;">
          <el-tag v-if="this.selectTags.area !== ''" closable size="small" @close="handle_close(0)">
            {{this.selectTags.area}}
          </el-tag>
          <el-tag v-if="this.selectTags.major !== ''" closable size="small" @close="handle_close(1)">
            {{this.selectTags.major}}
          </el-tag>
          <el-tag v-if="this.selectTags.tuition !== ''" closable size="small" @close="handle_close(2)">
            {{this.selectTags.tuition}}
          </el-tag>
          <el-tag v-if="this.selectTags.act !== ''" closable size="small" @close="handle_close(3)">
            ACT: {{this.selectTags.act}}
          </el-tag>
          <el-tag v-if="this.selectTags.sat !== ''" closable size="small" @close="handle_close(4)">
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
          <el-button type="text" @click="select_key(act_score,3)" style="font-size: 15px; text-decoration: underline;">
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
          <el-button type="text" @click="select_key(sat_score,4)" style="font-size: 15px; text-decoration: underline;">
            SAT Range: {{sat_score}}
          </el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="23" style="text-align: right;">
          <el-button-group>
            <el-button icon="el-icon-refresh-right" @click="reset">Rest All</el-button>
            <el-button @click="go_search">Search<i class="el-icon-search el-icon--right"></i></el-button>
          </el-button-group>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
  import axios from "axios"
  export default {
    data() {
      return {
        initFilterApiPrefix: "/search/init",
        areas: [],
        marjors: [],
        tuitions: [],
        selectTags: {
          area: '',
          major: '',
          tuition: '',
          act: '',
          sat: '',
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
      },
      handle_close(tag) {
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
      },
      reset(e) {
        this.selectTags.area = ''
        this.selectTags.major = ''
        this.selectTags.tuition = ''
        this.selectTags.act = ''
        this.selectTags.sat = ''
        this.$message({
          message: 'All filters have been cleared.',
          type: 'success'
        });
        e.target.blur() // auto unfocused
      },
      go_search() {
        this.$emit('toggle', this.selectTags)
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
