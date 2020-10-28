<template>
  <el-container style="height: 230px;">
    <el-aside width="50%">
      <div class="popular_major_tab_title">Popular Major</div>
      <div class="popular_major_tab_desc">This university has
        <span class="highlight_val">{{majors.length}}</span> majors.<br />
        I dont know what to say, just use some text to filling the blank.<br />
        Hopefully, you guys can figure out what content could be set here. This is
        so annoying, since we dont have enought time to finish this project.
        Now, you can click right tag cloud, which will guide to search related
        major, and explore which university is suit for you.
      </div>
    </el-aside>
    <el-main class="main">
      <svg :width='width' :height='height' @mousemove='listener($event)' style="padding-left: 0px;">
        <a :href="tag.href" v-for='tag in tags' :key='tag.text' style="color: darkorange;">
          <text :x='tag.x' :y='tag.y' :font-size='20 * (600/(600-tag.z))'
            :fill-opacity='((400+tag.z)/600)'>{{tag.text}}</text>
        </a>
      </svg>
    </el-main>
  </el-container>
</template>


<script>
  import axios from "axios"
  export default {
    components: {

    },
    props: {
      popular_major_obj: {
        type: Object | Array,
        required: false,
      }
    },
    data() {
      return {
        width: 500,
        height: 220,
        RADIUS: 200,
        popularMajorPrefix: "/detail/popular_major/",
        speedX: Math.PI / 720,
        speedY: Math.PI / 720,
        tags: [],
        majors: [],
        tagsNum: 10,
      }
    },
    computed: {
      CX() {
        return this.width / 2;
      },
      CY() {
        return this.height / 2;
      },
    },
    watch: {
      majors: function (newValue, oldValue) {
        for (let i = 0; i < this.tags.length; i++) {
          if (typeof this.majors[i] !== 'undefined') {
            let tag = this.tags[i]
            tag.text = this.majors[i].name
            tag.href = this.majors[i].link
          }
        }
      }
    },
    created() {
      this.getPopularMajors()
      let tags = [];
      for (let i = 0; i < this.tagsNum; i++) {
        let tag = {};
        let k = -1 + (2 * (i + 1) - 1) / this.tagsNum;
        let a = Math.acos(k);
        let b = a * Math.sqrt(this.tagsNum * Math.PI)
        tag.text = 'unused_tag_' + i;
        tag.x = this.CX + this.RADIUS * Math.sin(a) * Math.cos(b);
        tag.y = this.CY + this.RADIUS * Math.sin(a) * Math.sin(b);
        tag.z = this.RADIUS * Math.cos(a);
        tag.href = 'https://github.com/Chit-Chaat/Collegiate_Explorer_APP';
        tags.push(tag);
      }
      this.tags = tags;
    },
    mounted() {
      setInterval(() => {
        this.rotateX(this.speedX);
        this.rotateY(this.speedY);
      }, 25)
    },
    methods: {
      getPopularMajors() {
        axios({
          method: "GET",
          url: this.$hostname + this.popularMajorPrefix + this.$route.params.schoolId
        }).then(
          result => {
            if (result.data != null) {
              if (result.data.data instanceof Array) {
                this.majors = result.data.data;
              } else {
                this.majors = Object.values(result.data.data);
              }
              this.$options.methods.sendTips.bind(this)(
                "Load Popular major Data Successfully."
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
      rotateX(speedX) {
        var cos = Math.cos(speedX);
        var sin = Math.sin(speedX);
        for (let tag of this.tags) {
          var y1 = (tag.y - this.CY) * cos - tag.z * sin + this.CY;
          var z1 = tag.z * cos + (tag.y - this.CY) * sin;
          tag.y = y1;
          tag.z = z1;
        }
      },
      rotateY(speedY) {
        var cos = Math.cos(speedY);
        var sin = Math.sin(speedY);
        for (let tag of this.tags) {
          var x1 = (tag.x - this.CX) * cos - tag.z * sin + this.CX;
          var z1 = tag.z * cos + (tag.x - this.CX) * sin;
          tag.x = x1;
          tag.z = z1;
        }
      },
      listener(event) {
        var x = event.clientX - this.CX;
        var y = event.clientY - this.CY;
        this.speedX = x * 0.0001 > 0 ? Math.min(this.RADIUS * 0.00002, x * 0.0001) : Math.max(-this.RADIUS * 0.00002, x * 0.0001);
        this.speedY = y * 0.0001 > 0 ? Math.min(this.RADIUS * 0.00002, y * 0.0001) : Math.max(-this.RADIUS * 0.00002, y * 0.0001);
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

    }

  }
</script>


<style scoped>
  .popular_major_tab_title {
    color: rgb(255, 255, 255);
    text-align: left;
    font-family: "microsoft yahei";
    padding-left: 8%;
    font-size: 25px;
    height: 40px;
  }

  .popular_major_tab_desc {
    height: 82%;
    padding-left: 8%;
    color: rgb(255, 255, 255);
    font-size: 20px;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    -webkit-line-clamp: 2;
  }

  .highlight_val {
    color: darkorange;
    font-size: 18px;
    font-weight: 600;
    text-decoration: underline;
  }

  .main {
    width: 95%;
    height: 100%;
    padding-bottom: 0px;
    padding-top: 0px;
    padding-left: 0px;
  }
</style>