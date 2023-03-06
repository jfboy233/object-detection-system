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
      <el-menu-item index="/home" style="text-align: center;" ><i class="el-icon-share"></i>       数据统计</el-menu-item>
      <el-menu-item index="/Batch" style="text-align: center"><i class="el-icon-platform-eleme"></i>批次管理</el-menu-item>
      <el-menu-item index="/Enroll" style="text-align: center"><i class="el-icon-user-solid"></i>报名管理</el-menu-item>
      <el-menu-item index="/EnrollTable" style="text-align: center"><i class="el-icon-star-on"></i>报名表</el-menu-item>
      <el-menu-item index="/major" style="text-align: center"><i class="el-icon-info"></i>专业管理</el-menu-item>
      <el-menu-item index="/news" style="text-align: center"><i class="el-icon-s-help"></i>招生简章</el-menu-item>
      <el-menu-item index="/question" style="text-align: center"><i class="el-icon-magic-stick"></i>学生提问</el-menu-item>
      <el-menu-item index="/open" style="text-align: center"><i class="el-icon-s-home"></i>公告</el-menu-item>
      <el-submenu  style="text-align: center" index="1" v-if="user.role === 1">
        <template #title ><i class="el-icon-s-platform"></i>系统管理</template>
        <el-menu-item index="/user">用户管理</el-menu-item>
      </el-submenu>
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
    request.get("/user/" + this.user.id).then(res => {
      if (res.code === '0') {
        this.user = res.data
      }
    })
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