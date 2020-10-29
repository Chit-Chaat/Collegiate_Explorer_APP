<template>
  <div id="cc_recm_res">
    <el-row :gutter="20" v-for="(row, i) in dividedList" :key='i'>
      <el-col :span="8" v-for="(item, j) in row" :key="j">
        <Item :item="item" :key="item.id"></Item>
      </el-col>
    </el-row>
    <el-pagination background layout="prev, pager, next" :current-page.sync="currentPage" :hide-on-single-page=true
      :page-size="pageSize" :total="this.$store.state.results.length">
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
        currentPage: 1,
        pageSize: 3,
        recommendationApiPrefix: "/recommendation/",
      }
    },
    mounted() {
      this.getRecommendation()
    },
    computed: {
      dividedList: function () {
        var result_list = this.splitArray(this.$store.state.results);
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
              if (result.data.code == 200) {
                this.$store.commit("updateResultSolt", result.data.data);
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
              this.$options.methods.sendTips.bind(this)(
                "Everythong looks good now."
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
      splitArray(arr) {
        let whole_size = this.$store.state.results.length;
        let start = Math.min((this.currentPage - 1) * this.pageSize, whole_size);
        let end = Math.min(this.currentPage * this.pageSize, whole_size);
        return arr.slice(start, end)
      },
      sendTips(msg) {
        const h = this.$createElement;
        this.$notify.success({
          title: 'Success',
          message: h('p', { style: 'font-size:12px' }, msg),
          duration: 2000
        });
      },
      sendAlert(msg) {
        this.$notify.warning({
          title: 'Warning',
          message: h('p', { style: 'font-size:12px' }, msg),
          duration: 2000
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