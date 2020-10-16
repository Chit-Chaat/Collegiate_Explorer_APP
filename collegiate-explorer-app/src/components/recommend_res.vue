<template>
  <div id="cc_recm_res">
    <el-row :gutter="20" v-for="(row, i) in dividedList" :key='i'>
      <el-col :span="8" v-for="(cell, j) in row" :key="j">
        <!-- <div class="grid-content bg-purple" :id="'T_'+(i*3+j)">Data-{{cell}}</div> -->
        <Item></Item>
      </el-col>
    </el-row>
    <el-pagination background layout="prev, pager, next" :page-size="10" :total="50">
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
        recommend_list: ['a','b','c','d','e','f','g','h','i'],

      }
    },
    computed: {
      dividedList: function () {
        var recommend_list = this.recommend_list;
        var arrTemp = [];
        var index = 0;
        var sectionCount = 3;
        for (var i = 0; i < recommend_list.length; i++) {
          index = parseInt(i / sectionCount);
          if (arrTemp.length <= index) {
            arrTemp.push([]);
          }
          arrTemp[index].push(recommend_list[i]);
        }
        return arrTemp;
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