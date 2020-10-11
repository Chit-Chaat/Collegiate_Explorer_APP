<template>
  <div id="cc_searchbox">
    <el-row>
      <el-col :span="6">
        <div style="visibility: hidden;">dont delete me</div>
      </el-col>
      <el-col :span="10">
        <div class="common_searchobox">
          <el-input placeholder="knowledge graph" v-model="content">
            <el-select v-model="school_type" slot="prepend" placeholder="SCHOOL TYPE">
              <el-option label="PRIVATE" value="1"></el-option>
              <el-option label="PUBLIC" value="2"></el-option>
              <el-option label="COMMUNITY" value="2"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search">Search</el-button>
          </el-input>
        </div>
      </el-col>
      <el-col :span="3">
        <div class="advanced_searchobox">
          <el-link id="filter_bth"icon="el-icon-edit" ><b><u>More Filter</u></b></el-link>
          <Advanced_Search_Filter style="display:none"></Advanced_Search_Filter>
        </div>
      </el-col>
    </el-row>
    <el-row id="recommend_search_tag" :gutter="10">
      <el-col :span="6">
        <div style="visibility: hidden;">dont delete me</div>
      </el-col>
      <el-col :span="1" v-for="tag in tags" :key="tag.name">
        <el-link   :type="tag.type">
          {{tag.name}}
        </el-link>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import Advanced_Search_Filter from './advanced_search_filter.vue'
  export default {
    components: {
      Advanced_Search_Filter,
    },
    data() {
      return {
        content: '',
        school_type: '',
        tags: [
          { name: 'Tag1', type: '' },
          { name: 'Tag2', type: 'success' },
          { name: 'Tag3', type: 'info' },
          { name: 'Tag4', type: 'warning' },
          { name: 'Tag5', type: 'danger' }
        ]
      }
    }
  }
</script>

<style>
  #cc_searchbox {
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    width: 100%;
    height: 100%;

  }

  .common_searchobox {
    font-size: 14px;
  }

  .common_searchobox .el-input .el-input__inner {
    height: 40px;
  }

  .el-input-group__prepend {
    width: 100px;
  }

  .el-row {
    line-height: 40px;
  }

  #recommend_search_tag {
    text-align: left;
  }

  #filter_bth{
    color: azure;
    font-size: 16px;
  }
</style>