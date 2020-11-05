<template>
  <div id="cc_searchbox">
    <el-row style="margin-bottom: 0px;">
      <el-col :span="6">
        <div style="visibility: hidden;">dont delete me</div>
      </el-col>
      <el-col :span="10">
        <div class="common_searchobox">
          <el-input placeholder="knowledge graph" v-model="content">
            <el-select v-model="search_type" slot="prepend" placeholder="SEARCH TYPE" style="width: 140px;">
              <el-option label="PRIVATE" value="private"></el-option>
              <el-option label="PUBLIC" value="public"></el-option>
              <el-option label="PROGRAMS" value="public"></el-option>
              <el-option label="OTHER" value="other"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search" @click="advancedSearch">Search</el-button>
          </el-input>
        </div>
      </el-col>
      <el-col :span="3">
        <div class="advanced_searchobox">
          <el-link id="filter_bth" icon="el-icon-edit" @click="toggleFilter"><b><u>More Filter</u></b></el-link>
        </div>
      </el-col>
    </el-row>
    <el-row v-bind:style="{ 'line-height': filter_row_height + 'px' }">
      <el-col :span="4">
        <div style="visibility: hidden;">dont delete me</div>
      </el-col>
      <el-col :span="15">
        <Advanced_Search_Filter v-bind:style="{ display: show_or_not  }"
         @toggleBasic="filterSearch" @toggleNiche='filterSearch'></Advanced_Search_Filter>
      </el-col>
    </el-row>
    <el-row id="recommend_search_tag" :gutter="10">
      <el-col :span="6">
        <div style="visibility: hidden;">dont delete me</div>
      </el-col>
      <el-col :span="1.5" v-for="tag in recommend_search_tags" :key="tag.name">
        <el-button :type="tag.type" size="mini" plain @click="toggleTagSearch(tag.name)">
          {{tag.name}}
        </el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  let clicked = false
  import Advanced_Search_Filter from './advanced_search_filter.vue'
  import axios from "axios"
  export default {
    components: {
      Advanced_Search_Filter,
    },
    data() {
      return {
        recommendTagListApiPrefix: "/recommendation/tags/",
        searhApiPrefix: "/search/query",
        searchByTagApiPrefix: "/search/tag/",
        content: '',
        search_type: '',
        recommend_search_tags: [],
        filter_content: {},
        filter_row_height: '5',
        show_or_not: 'none',
      }
    },
    created() {
      this.getTagList()
    },
    methods: {
      toggleFilter(e) {
        clicked = !clicked
        if (clicked) {
          this.filter_row_height = '40'
          this.show_or_not = 'block'
        } else {
          this.filter_row_height = '5'
          this.show_or_not = 'none'
        }
      },
      toggleTagSearch(tag_name) {
        axios({
          method: "GET",
          url: this.$hostname + this.searchByTagApiPrefix + tag_name
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.$store.commit("updateResultSolt", result.data.data);
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }
          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with the Ranking Historical Data."
            );
          }
        );
      },
      advancedSearch() {
        var params = new URLSearchParams();
        params.append('content', this.content);
        params.append('search_type', this.search_type)
        params.append('filter_content', JSON.stringify(this.filter_content))
        axios({
          method: "POST",
          url: this.$hostname + this.searhApiPrefix,
          data: params
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.$store.commit("updateResultSolt", result.data.data);
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }
          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with the Ranking Historical Data."
            );
          }
        );
      },
      filterSearch(tags){
        this.filter_content = tags
        this.advancedSearch()
        this.toggleFilter()
      },
      getTagList() {
        axios({
          method: "GET",
          url: this.$hostname + this.recommendTagListApiPrefix
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.code == 200) {
                this.recommend_search_tags = result.data.data;
              } else {
                this.$options.methods.sendErrorMsg.bind(this)(result.data.msg);
              }
            }
          },
          error => {
            this.$options.methods.sendErrorMsg.bind(this)(
              "Something wrong with the Ranking Historical Data."
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

    }
  }
</script>

<style scoped>
  #cc_searchbox {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    width: 100%;
    height: 100%;

  }

  .common_searchobox {
    font-size: 15px;
  }

  .common_searchobox .el-input .el-input__inner {
    height: 40px;
  }

  .el-row {
    line-height: 40px;
  }

  #recommend_search_tag {
    text-align: left;
  }

  #filter_bth {
    color: azure;
    font-size: 16px;
  }

  .advanced_search_filter {
    display: block;
  }

  #filter_row {
    line-height: var(--row_height);
  }
</style>