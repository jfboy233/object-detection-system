<template>
  <el-card style="width: 60%; margin: 10px">
    <el-form ref="form" :model="form" label-width="80px">
      <div style="text-align: center;margin:50px 38%;" >
        <el-form-item>
          <el-upload
              class="avatar-uploader"
              action="http://localhost:5000/api/upload/avatar"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :data="{'username': form.username}"
          >
            <img v-if="form.head" :src="form.head" class="avatar">
            <el-icon v-else class="avatar-uploader-icon" style="border: dashed 1px silver"><Plus/></el-icon>
          </el-upload>
        </el-form-item>
      </div>
      <el-form-item label="邮件">
        <el-input v-model="form.email" disabled></el-input>
      </el-form-item>
      <el-form-item label="用户名">
        <el-input v-model="form.username" v-bind:disabled="!flag"></el-input>
      </el-form-item>
      <el-form-item label="电话">
        <el-input v-model="form.phone" v-bind:disabled="!flag"></el-input>
      </el-form-item>
      <el-form-item label="新的密码">
        <el-input v-model="form.pwd" v-bind:disabled="flag"></el-input>
      </el-form-item>

    </el-form>
    <div style="text-align: center">
      <el-button type="primary" @click="update" v-show="!dialogButtonVisible">保存</el-button>
      <el-button type="danger" @click="change_pwd" v-show="!dialogButtonVisible">修改密码</el-button>
      <el-button type="danger" @click="update_pwd" v-show="dialogButtonVisible">保存密码</el-button>
    </div>
  </el-card>
</template>

<script>
import request from "@/utils/request";

export default {
name: "Person",
data() {
  return {
    form: {},
    uploadParam:{
      open: false,
      // 是否禁用上传
      enableUpload: false,
      // 是否更新已经存在的数据
      updateSupport: 0,
      limit: 3,
      // 上传的地址,这个地方写自己的后台地址
      // url: this.GLOBAL.serverSrc + "/uploadController/uploadImg",
      ContentType:"application/json"
    },
    flag: true,
    dialogButtonVisible: false
  }
},
created() {
  let str = sessionStorage.getItem("user")
  this.form = JSON.parse(str).data
},
methods: {
  handleAvatarSuccess(res) {
    this.form.head = res.head
    this.$message.success("上传成功")
    console.log(this.form)
  },
  change_pwd() {
    this.flag = false
    this.dialogButtonVisible = true
  },
  update_pwd() {
    this.flag = true
    this.dialogButtonVisible = false
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