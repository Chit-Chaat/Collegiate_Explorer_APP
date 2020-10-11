<template>
  <div>
    <el-card>
      <el-row :gutter="10">
        <el-col :span="2" style="color: yellowgreen">
          Selected:
        </el-col>
        <el-col :span="2">
          <el-tag v-if="this.selectTags.area !== ''" closable size="small" @close="handleClose(0)">
            {{this.selectTags.area}}
          </el-tag>
          <el-tag v-if="this.selectTags.work !== ''" closable size="small" @close="handleClose(1)">
            {{this.selectTags.work}}
          </el-tag>
          <el-tag v-if="this.selectTags.num !== ''" closable size="small" @close="handleClose(2)">
            {{this.selectTags.num}}
          </el-tag>
        </el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="2" style="color: yellowgreen">
          行业：
        </el-col>
        <el-col :span="8">
          <el-button type="text" v-for="work in works" :key="work" size="medium" @click="selectKey(work,0)">{{work}}
          </el-button>
        </el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="2" style="color: yellowgreen">
          省份：
        </el-col>
        <el-col :span="8">
          <el-button type="text" v-for="area in areas" :key="area" size="medium" @click="selectKey(area,1)">{{area}}
          </el-button>
        </el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="2" style="color: yellowgreen">
          指数：
        </el-col>
        <el-col :span="8">
          <el-button type="text" v-for="num in nums" :key="num" size="medium" @click="selectKey(num,2)">{{num}}
          </el-button>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        areas: ['湖南', '广西', '福建', '广东', '江西', '山东'],

        works: ['工业', '旅游业', '餐饮', '农业'],

        nums: ['>=0.9', '>=0.8', '>=0.6'],

        selectTags: {
          area: '湖南',
          work: '',
          num: '',
        }
      }
    },
    methods: {
      selectKey(tag, key) {
        if (key === 0)
          this.selectTags.work = tag
        else if (key === 1)
          this.selectTags.area = tag
        else
          this.selectTags.num = tag
      },
      handleClose(tag) {
        if (tag === 0)
          this.selectTags.area = ''
        else if (tag === 1)
          this.selectTags.work = ''
        else
          this.selectTags.num = ''
      }
    }
  }
</script>

<style scoped>
  .el-row {
    margin: 0px 0 15px 10px;
  }

  .el-tag {
    margin-right: 10px;
  }

  .el-button--medium {
    padding: 0px 10px;
    font-size: 16px;
    border-radius: 4px;
  }
</style>