<template>
  <div id="cc_recm_res">
    <el-row :gutter="20">
      <el-col :span="8">
        <div class="grid-content bg-purple">A</div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple-light">B</div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple">C</div>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="8">
        <div class="grid-content bg-purple">D</div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple-light">E</div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple">F</div>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="8">
        <div class="grid-content bg-purple">G</div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple-light">H</div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple">I</div>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="8">
        <div class="grid-content bg-purple">G</div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple-light">H</div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple">I</div>
      </el-col>
    </el-row>
    <el-pagination background layout="prev, pager, next" :total="50">
    </el-pagination>
  </div>
</template>

<script>
  import Item from './item.vue'
  export default {
    components: {
      Item,
    },
    data() {
      return {
        todos: [
          { text: '学习 JavaScript' },
          { text: '学习 Vue' },
          { text: '整个牛项目' },
          { text: '循环的例子' },
          { text: '循环的文本' },
          { text: '循环的文本1' },
          { text: '循环的文本2' },
          { text: '循环的文本3' }
        ]
      }
    }
  }

</script>

<style scoped>
  #cc_recm_res {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    height: 100%;
    width: 100%;
  }

  .el-row {
    margin-bottom: 20px;

    &:last-child {
      margin-bottom: 0;
    }
  }

  .el-col {
    border-radius: 4px;
  }

  .bg-purple-dark {
    background: #99a9bf;
  }

  .bg-purple {
    background: #d3dce6;
  }

  .bg-purple-light {
    background: #e5e9f2;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 220px;
  }
</style>