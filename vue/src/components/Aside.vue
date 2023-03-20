<template>
  <div style="background-color: #545c64">
    <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        style="width: 200px; min-height: calc(100vh - 50px)"
        :default-active="path"
        router
    >
      <el-menu-item index="/system/picture" style="text-align: center;" ><i class="el-icon-share"></i>图片识别</el-menu-item>
      <el-menu-item index="/system/video" style="text-align: center"><i class="el-icon-platform-eleme"></i>视频识别</el-menu-item>
      <el-menu-item index="/system/instant" style="text-align: center"><i class="el-icon-user-solid"></i>实时识别</el-menu-item>
      <el-menu-item index="/system/log" style="text-align: center"><i class="el-icon-star-on"></i>历史记录</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import request from '@/utils/request';
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Aside",
  data() {
    return {
      user: {},
      path: this.$route.path   // 设置默认高亮的菜单
    }
  },
  created() {
    let userStr = sessionStorage.getItem("user") || "{}"
    this.user = JSON.parse(userStr)
    // 请求服务端，确认当前登录用户的 合法信息
    // request.get("/user/" + this.user.id).then(res => {
    //   if (res.code === '0') {
    //     this.user = res.data
    //   }
    // })
  }
}
</script>

<style scoped>
* {
  font-weight: bold;
}
el-menu-item {
  background-color: #222222;
}
.item {
  margin-top: 10px;
  margin-right: 40px;
  text-align: center;
}
</style>