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
  export default {
    components: {
      Item,
    },
    data() {
      return {
        result_list: [{
          id: '1',
          name: 'University of AAAAAA',
          logo: 'school_logo.jpg',
          desc: 'this is desc this is this is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 5,
            B: 3,
            A_val: '5',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '2',
          name: 'University of bbbbbbbb',
          logo: 'school_logo2.jpg',
          desc: 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 2,
            B: 3,
            A_val: '2',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '3',
          name: 'University of cCCCCC',
          logo: 'school_logo.jpg',
          desc: 'this is desc this is this is desc this isthis is des desc this isthis is des desc this isthis is des desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 4,
            B: 3,
            A_val: '4',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '4',
          name: 'University of DDDDDDDDD',
          logo: 'school_logo2.jpg',
          desc: 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 4,
            B: 3,
            A_val: '4',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '5',
          name: 'University of EEEEEEEEEE',
          logo: 'school_logo2.jpg',
          desc: 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 4,
            B: 3,
            A_val: '4',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '6',
          name: 'University of FFFFFFF',
          logo: 'school_logo.jpg',
          desc: 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 4,
            B: 3,
            A_val: '4',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '7',
          name: 'University of FGGGGGGG',
          logo: 'school_logo.jpg',
          desc: 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 4,
            B: 3,
            A_val: '4',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '8',
          name: 'University of HHHHHHH',
          logo: 'school_logo2.jpg',
          desc: 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 4,
            B: 3,
            A_val: '4',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '9',
          name: 'University of IIIIIIIIIIII',
          logo: 'school_logo.jpg',
          desc: 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 4,
            B: 3,
            A_val: '4',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '10',
          name: 'University of JJJJJJJJJJJJJJ',
          logo: 'school_logo.jpg',
          desc: 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 4,
            B: 3,
            A_val: '4',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        },
        {
          id: '11',
          name: 'University of KKKKKKKKKKKKKKK',
          logo: 'school_logo2.jpg',
          desc: 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
          rating: {
            A: 4,
            B: 3,
            A_val: '4',
            B_val: '3'
          },
          review: '3453',
          level: 'A',
          detail: 'detail/school_id',
          address: '1420 22nd W St, Los Angeles, CA, 90007',
          tuition: '$17,234'
        }]

      }
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