<template>
  <div id="login_page2" style="width: 100%; height: 100vh; overflow: hidden"> <!--  :style="bg" 加背景图片-->
    <div style="width: 500px;height: 600px; margin: 60px auto;background-color: white;display: flex">
      <div style="width: 400px; margin: 100px auto">
        <div><img src="../assets/login_logo.jpg" style="width: 130px; height: auto; margin-top: -120px"/></div>
        <div style="font-size: 30px; text-align: center; padding: 30px 0">欢迎注册</div>
        <el-form ref="form" :model="form" size="normal" :rules="rules">
          <el-form-item prop="email">

            <el-input  v-model="form.email" placeholder="请输入电子邮箱"></el-input>
          </el-form-item>
          <el-form-item prop="username">
            <el-input  v-model="form.username" placeholder="请输入用户名"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input  v-model="form.password" placeholder="请输入密码" show-password></el-input>
          </el-form-item>
          <el-form-item prop="confirm">
            <el-input  v-model="form.confirm" placeholder="请确认密码" show-password></el-input>
          </el-form-item>
          <el-form-item prop="code">
            <div style="display:flex;">
              <el-input  name="code" placeholder="输入验证码" v-model="form.code" style="width: 300px"></el-input>
              <el-button @click="sendCode" :disabled="flag">获取验证码 {{count}}</el-button>
            </div>
          </el-form-item>
          <el-form-item>
            <el-button style="width: 100%" type="primary" @click="register">注册</el-button>
          </el-form-item>
          <el-form-item><el-button type="text" @click="$router.push('/login')">返回登录 >> </el-button></el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "Register",
  data() {
    return {
      flag: false,
      seconds: 60,
      count: '',
      form: {},
      rules: {
        username: [
          {required: true, message: '请输入用户名', trigger: 'blur'},
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'},
        ],
        confirm: [
          {required: true, message: '请确认密码', trigger: 'blur'},
        ],
      }
    }
  },
  methods: {
    sendCode() {
      request.post("/user/sendValidCode",  this.form).then(res => {
        if (res.data.code === '0') {
          this.$message({
            message: "验证码已发送",
            type: "success"
          });
          this.Time()
        } else {
          this.$message({
            message: res.data.msg,
            type: "error"
          });
        }
      })
    },
    countDown() {
      let s = parseInt(this.seconds % 60);
      s = s < 10 ? "0" + s : s
      this.count = '('+s + '秒)'
    },
    Time() {
      const y = setInterval(() => {
        this.seconds -= 1
        this.countDown()
        if (this.seconds < 0) {
          this.flag = false
          this.count = ''
          clearInterval(y)
        } else this.flag = true
      }, 1000);
    },
    register() {
      if (this.form.password !== this.form.confirm) {
        this.$message({
          type: "error",
          message: '2次密码输入不一致！'
        })
        return
      }

      this.$refs['form'].validate((valid) => {
        if (valid) {
          request.post("/user/register", this.form).then(res => {
            if (res.data.code === '0') {
              this.$message({
                type: "success",
                message: "注册成功"
              })
              this.$router.push("/login")  //登录成功之后进行页面的跳转，跳转到主页
            } else {
              this.$message({
                type: "error",
                message: res.data.msg
              })
            }
          })
        }
      })
    }
  }
}
</script>

<style scoped>
#login_page2 {
  background-image: url("../assets/login_bg.jpg");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
}
#left_img2 img{
  width: 100%;
  height: 100%;
}
</style>