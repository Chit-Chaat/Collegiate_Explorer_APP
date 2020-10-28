<template>
  <div id="cc_recm_res">
    <el-row :gutter="20" v-for="(row, i) in dividedList" :key='i'>
      <el-col :span="8" v-for="(item, j) in row" :key="j">
        <Item :item="item" :key="item.id"></Item>
      </el-col>
    </el-row>
    <el-pagination background layout="prev, pager, next" :page-size="10" :total="50">
    </el-pagination>
  </div>
</template>

<script>
  import Item from './item.vue'
  import axios from "axios"
  export default {
    components: {
      Item,
    },
    data() {
      return {
        result_list: [],
        recommendationApiPrefix: "/recommendation/",
      }
    },
    mounted() {
      this.getRecommendation()
    },
    computed: {
      dividedList: function () {
        var result_list = this.result_list;
        var arrTemp = [];
        var index = 0;
        var sectionCount = 3;
        for (var i = 0; i < result_list.length; i++) {
          index = parseInt(i / sectionCount);
          if (arrTemp.length <= index) {
            arrTemp.push([]);
          }
          arrTemp[index].push(result_list[i]);
        }
        return arrTemp;
      }
    },
    methods: {
      getRecommendation() {
        axios({
          method: "GET",
          url: this.$hostname + this.recommendationApiPrefix
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.data instanceof Array) {
                this.result_list = result.data.data;
              } else {
                this.result_list = Object.values(result.data.data);
              }
              this.$options.methods.sendTips.bind(this)(
                "Load Recommendation Data Successfully."
              );
            }
          },
          error => {
            this.$options.methods.sendAlert.bind(this)(
              "Something wrong about the request"
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

    },

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
  }

  .el-row:last-child {
    margin-bottom: 0;
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