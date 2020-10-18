<template>
  <div>
    <el-card>
      <el-row>
        <el-col :span="2" style="color: yellowgreen">
          Selected:
        </el-col>
        <el-col :span="20" style="margin-left: 10px;">
          <el-tag v-if="this.selectTags.area !== ''" closable size="small" @close="handleClose(0)">
            {{this.selectTags.area}}
          </el-tag>
          <el-tag v-if="this.selectTags.major !== ''" closable size="small" @close="handleClose(1)">
            {{this.selectTags.major}}
          </el-tag>
          <el-tag v-if="this.selectTags.tuition !== ''" closable size="small" @close="handleClose(2)">
            {{this.selectTags.tuition}}
          </el-tag>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="2" style="color: yellowgreen">
          Area:
        </el-col>
        <el-col :span="20">
          <el-button type="text" v-for="area in areas" :key="area" size="medium" @click="selectKey(area,0)">{{area}}
          </el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="2" style="color: yellowgreen">
          Major：
        </el-col>
        <el-col :span="20">
          <el-button type="text" v-for="major in marjors" :key="major" size="medium" @click="selectKey(major,1)">
            {{major}}
          </el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="2" style="color: yellowgreen">
          Tuition：
        </el-col>
        <el-col :span="20">
          <el-button type="text" v-for="tuition in tuitions" :key="tuition" size="medium" @click="selectKey(tuition,2)">
            {{tuition}}
          </el-button>
          <span style="color: darkgray;">[per semester]</span>
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
  export default {
    data() {
      return {
        areas: [
          'New England', 'Mid East', 'Great Lakes',
          'Plains', 'Southeast', 'Southwest',
          'Rocky Mountains', 'Far West', 'Outlying areas'],

        marjors: [
          'Humanities',
          'Natural sciences or mathematics',
          'Social sciences ',
          'Architecture or urban planning',
          'Art and design',
          'Business',
          'Dentistry',
          'Education',
          'Engineering',
          'Law',
          'Medicine',
          'Music, theatre, or dance',
          'Nursing',
          'Pharmacy',
          'Public health',
          'Public policy',
          'Social work',
          'Other'],


        tuitions: ['>= $5k', '>= $10k', '>= $15k'],

        selectTags: {
          area: '',
          major: 'Engineering',
          tuition: '',
        }
      }
    },
    methods: {
      selectKey(tag, key) {
        if (key === 0)
          this.selectTags.area = tag
        else if (key === 1)
          this.selectTags.major = tag
        else
          this.selectTags.tuition = tag
      },
      handleClose(tag) {
        if (tag === 0)
          this.selectTags.area = ''
        else if (tag === 1)
          this.selectTags.major = ''
        else
          this.selectTags.tuition = ''
      },
      reset(e) {
        this.selectTags.area = ''
        this.selectTags.major = ''
        this.selectTags.tuition = ''
        this.$message({
          message: 'All filters have been cleared.',
          type: 'success'
        });
        e.target.blur() // auto unfocused
      },
      go_search() {
        let text = this.selectTags.area + '/' + this.selectTags.major + '/' + this.selectTags.tuition
        console.log(text)
        this.$message({
          message: 'Going to send request.',
          type: 'success'
        });
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