<template>
  <div id="cc_searchbox">
    <el-row style="margin-bottom: 0px;">
      <el-col :span="6">
        <div style="visibility: hidden;">dont delete me</div>
      </el-col>
      <el-col :span="10">
        <div class="common_searchobox">
          <el-input placeholder="knowledge graph" v-model="content">
            <el-select v-model="school_type" slot="prepend" placeholder="SCHOOL TYPE" style="width: 140px;">
              <el-option label="PRIVATE" value="1"></el-option>
              <el-option label="PUBLIC" value="2"></el-option>
              <el-option label="COMMUNITY" value="3"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search">Search</el-button>
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
        <Advanced_Search_Filter v-bind:style="{ display: show_or_not  }"></Advanced_Search_Filter>
      </el-col>
    </el-row>
    <el-row id="recommend_search_tag" :gutter="10">
      <el-col :span="6">
        <div style="visibility: hidden;">dont delete me</div>
      </el-col>
      <el-col :span="1.5" v-for="tag in recommend_search_tags" :key="tag.name">
        <el-tag :type="tag.type" round @click="toggleTagSearch(tag.name)">
          {{tag.name}}
        </el-tag>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  let clicked = false
  import Advanced_Search_Filter from './advanced_search_filter.vue'
  export default {
    components: {
      Advanced_Search_Filter,
    },
    data() {
      return {
        content: '',
        school_type: '',
        filter_row_height: '5',
        show_or_not: 'none',
        recommend_search_tags: [
          { name: 'USC', type: 'primary', link: '' },
          { name: 'Best CS in LA', type: 'success', link: '' },
          { name: 'xxxxxxxxxxx', type: 'info', link: '' },
          { name: 'Top 10 DS programs', type: 'warning', link: '' },
          { name: '#Don\'t go there', type: 'danger', link: '' }
        ]
      }
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
      toggleTagSearch(s){
        this.$message({
          message: 'Going to send request and query ' + s,
          type: 'success'
        });
      }

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