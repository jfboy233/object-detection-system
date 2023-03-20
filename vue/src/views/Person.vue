<template>
  <el-card style="width: 40%; margin: 10px">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item style="text-align: center" label-width="0">
        <el-upload
            class="avatar-uploader"
            action="http://localhost:5000/files/upload"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
        >
          <img v-if="form.avatar" :src="form.avatar" class="avatar">
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item label="用户名">
        <el-input v-model="form.username" disabled></el-input>
      </el-form-item>
      <el-form-item label="电话">
        <el-input v-model="form.phone"></el-input>
      </el-form-item>
      <el-form-item label="邮件">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
    </el-form>
    <div style="text-align: center">
      <el-button type="primary" @click="update">保存</el-button>
    </div>
  </el-card>
</template>

<script>
import request from "@/utils/request";

export default {
name: "Person",
data() {
  return {
    form: {}
  }
},
created() {
  let str = sessionStorage.getItem("user")
  this.form = JSON.parse(str)
},
methods: {
  handleAvatarSuccess(res) {
    this.form.head = res.data
    this.$message.success("上传成功")
  },
  update() {
    request.put("/user", this.form).then(res => {
      console.log(res)
      if (res.data.code === '0') {
        this.$message({
          type: "success",
          message: "更新成功"
        })
        sessionStorage.setItem("user", JSON.stringify(this.form))
        // 触发Layout更新用户信息
        this.$emit("userInfo")
      } else {
        this.$message({
          type: "error",
          message: res.data.msg
        })
      }
    })
  }
}
}
</script>

<style scoped>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 120px;
  height: 120px;
  line-height: 120px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>