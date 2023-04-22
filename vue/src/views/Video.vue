<template>
  <div style="padding: 10px">

    <!--    功能区域-->
    <div style="margin: 10px 0; text-align: left">
      <el-button type="primary" @click="add">新增</el-button>
      <el-button type="primary" @click="load">刷新</el-button>
    </div>

    <!--    表格区域-->
    <el-table
        v-loading="loading"
        :data="tableData"
        border
        stripe
        style="width: 100%">
      <el-table-column
          prop="id"
          label="ID"
          width="100px"
          sortable
      >
      </el-table-column>
      <el-table-column
          prop="filename"
          label="文件名"
          width="300px"
      >
      </el-table-column>
      <el-table-column
          prop="time"
          label="上传时间"
          width="400px"
          sortable
      >
      </el-table-column>
      <el-table-column
          prop="state"
          label="当前状态"
          width="100px"
      >
        <template #default="scope">
          <span v-if="scope.row.state === 1"><el-tag type="danger">未处理</el-tag></span>
          <span v-if="scope.row.state === 2"><el-tag type="warning">处理中</el-tag></span>
          <span v-if="scope.row.state === 3"><el-tag type="success">已完成</el-tag></span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template #default="scope">
          <el-button size="small" type="primary" plain @click="originScan(scope.row.origin)">原图</el-button>
          <el-button size="small" type="primary" plain @click="detect(scope.row)" :disabled="scope.row.state !== 1">处理</el-button>
          <el-button size="small" type="primary" plain @click="targetScan(scope.row.target)" :disabled="scope.row.state !== 3">查看</el-button>
          <el-button size="small" type="primary" plain @click="download(scope.row.target, scope.row.filename)" :disabled="scope.row.state !== 3">下载</el-button>
          <el-popconfirm title="确定删除吗？" @confirm="handleDelete(scope.row.id)">
            <template #reference>
              <el-button size="small" type="danger">删除</el-button>
            </template>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>

    <!--    分页组件-->
    <div style="margin: 10px 0">
      <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[5, 10, 20]"
          :page-size="pageSize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
      </el-pagination>
    </div>

    <!--    新增 弹出框-->
    <el-dialog title="新增" v-model="dialogVisible1" width="30%">
      <el-upload
          class="avatar-uploader"
          action="http://localhost:5000/api/upload/uploadPicture"
          :show-file-list="false"
          :on-success="handleAvatarSuccess"
          :data="{
            'username': user.username,
            'userId': user.id
          }"
      ><el-button type="primary">选择图片</el-button>
      </el-upload>
    </el-dialog>

    <!--    原图 弹出框-->
    <el-dialog title="查看原图" v-model="dialogVisible2" width="30%">
      <el-image  :src="originScanUrl" fit="fill" />
    </el-dialog>

    <!--    结果图 弹出框-->
    <el-dialog title="查看结果" v-model="dialogVisible3" width="30%">
      <el-image  :src="targetScanUrl" fit="fill" />
    </el-dialog>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "Video",
  data() {
    return {
      user: {},
      loading: true,
      dialogVisible1: false, // 新增
      dialogVisible2: false, // 原图
      dialogVisible3: false, // 检测结果
      originScanUrl: "",
      targetScanUrl: "",
      currentPage: 1,
      pageSize: 10,
      total: 0,
      tableData: [{
        id:'',
        filename:'',
        time:'',
        state:'',
      }],
    }
  },
  created() {
    let str = sessionStorage.getItem("user")
    this.user = JSON.parse(str).data
    this.load()
  },
  methods: {
    handleAvatarSuccess(res){
      this.$message.success("上传成功")
      this.dialogVisible1 = false
      this.load()
    },
    load() {
      this.loading = true
      request.get("/picture/tableData", {
        params: {
          pageNum: this.currentPage,
          pageSize: this.pageSize,
          userId: this.user.id,
        }
      }).then(res => {
        this.loading = false
        this.tableData = res.data.result
        this.total = res.data.total
      })
    },
    add() {
      this.dialogVisible1 = true
    },
    originScan(url){
      this.dialogVisible2 = true
      this.originScanUrl = url
    },
    targetScan(url){
      this.dialogVisible3 = true
      this.targetScanUrl = url
    },
    download(url, filename){
      fetch (url)
          .then ( (response) => response.blob ())
          .then ( (blob) => {
            // 创建 blob 链接
            const url = window.URL.createObjectURL (blob);
            const link = document.createElement ('a');
            link.href = url;
            link.setAttribute ('download', 'result-'+filename);
            // 添加到网页
            document.body.appendChild (link);
            // 开始下载
            link.click ();
            // 清理并移除链接
            link.parentNode.removeChild (link);
          });
    },
    handleDelete(id) {
      request.delete("/picture/delete", {params: {picId: id}}).then(res => {
        if (res.data.code === '0') {
          this.$message({
            type: "success",
            message: "删除成功"
          })
        } else {
          this.$message({
            type: "error",
            message: res.data.msg
          })
        }
        this.load()  // 删除之后重新加载表格的数据
      })
    },
    detect(row){
      request.post("/yolo/picture", {
        source: row.origin,
        picId: row.id,
      }).then(res=>{
        console.log(res)
      })
      this.load() // 刷新表格的数据

    },
    handleSizeChange(pageSize) {   // 改变当前每页的个数触发
      this.pageSize = pageSize
      this.load()
    },
    handleCurrentChange(pageNum) {  // 改变当前页码触发
      this.currentPage = pageNum
      this.load()
    }
  }
}
</script>

<style scoped>

</style>