<template>
  <div style="height: 60px; line-height: 50px; border-bottom: 1px solid #ccc; display: flex;">
    <img src="../assets/login_logo.jpg" style="margin-left: 30px" alt="">
    <img src="" alt="">
    <div style="flex: 1"></div>
    <div style="width: 100px">
      <el-dropdown>
        <span class="el-dropdown-link">
          <el-avatar :size="30" :src="user.head" style="position: relative; top: 10px" @click="print"></el-avatar>
           {{ user.username }}
          <i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="$router.push('/system/person')">个人信息</el-dropdown-item>
            <el-dropdown-item @click="$router.push('/login')">退出系统</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Header",
  data() {
    return {
      user: {}
    }
  },
  created() {
    this.user = JSON.parse(sessionStorage.getItem('user')).data
  },
  methods: {
    print(){
      console.log(this.user)
    }
  }
}
</script>

<style scoped>

</style>