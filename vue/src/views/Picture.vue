<template>
  <div style=" margin-bottom: 80px">
    <el-card>
      <div style="text-align: center;">
        <h2>图片识别</h2>
      </div>
    </el-card>
  </div>
</template>

<script>
import request from "@/utils/request";
export default {
  name: "Picture",
  data() {
    return {
      user: {},
    }
  },
  created() {
    this.user = sessionStorage.getItem("user")
  },
  methods: {

  }

}
</script>

<style scoped>

</style>