<template>
  <q-page class="flex flex-center">
    <theme></theme>
    <div class="uupp">
        <el-form
          :model="dataForm"
          ref="dataForm"
          label-width="80px"
          style="width=800px;"
        >
        <el-form-item :class="{ hide: hideUpload }">
          <div class="up">
            <div style="float:left">
              <el-upload
                ref="upload"
                action="#"
                :file-list="dataForm.imgFileList"
                list-type="picture-card"
                :on-preview="handlePictureCardPreview"
                :on-change="OnChange"
                :on-remove="handleRemove"
                :on-exceed="handleExceed"
                :limit="1"
                :class="{ hide: hideUpload }"
                accept="image/jpeg,image/png"
                :auto-upload="false"
              >
                <i class="el-icon-plus"></i>
                <div class="el-upload__tip" slot="tip">
                  只能上传jpg/png文件，最多上传1张且单张图片不超过5M
                </div>
              </el-upload>
            </div>
            <div style="float:right">
              <el-avatar shape="square" :size="320":src="url"></el-avatar>
            </div>
          </div>
          <el-dialog :visible.sync="dialogVisible" append-to-body>
            <img width="100%" :src="dialogImageUrl" alt="" />
          </el-dialog>
        </el-form-item>
        <el-form-item style="float:center">
          <el-button type="primary" @click="submitUpload()">确定</el-button>
        </el-form-item>
        </el-form>
      <submenu1 style="float:center"></submenu1>
    </div>
  </q-page>
</template>
  


<script>
import theme from '../components/theme.vue'
import submenu1 from '../components/submenu1.vue'
export default {
  name: "Page1",
  components: {
    theme,
    submenu1
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://i.loli.net/2021/11/24/5kA2cdmWuKjJMDT.gif') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
  },
  methods: {
		speak(msg){
      console.log(msg);//我是子组件发送的消息！
    },
    handleRemove(file, fileList) {
      this.hideUpload = fileList.length >= this.limitCount;
    },
    handleChange(fileList) {
      this.hideUpload = fileList.length >= this.limitCount;
      this.hideUpload = true; //此时值为ture时 才会执行隐藏
    },
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
      }
      return isJPG && isLt2M;
    },
    submitUpload () {
      let formData = new FormData(); //  用FormData存放上传文件
      this.dataForm.imgFileList.forEach((file) => {
        console.log(file.raw);
        console.log(file.size);
        formData.append("file", file.raw);
      });
      // 以下代码可以根据实际情况自己来实现
      this.$http({
        url: this.uploadUrl,
        method: "post",
        data: formData,
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }).then(({ data }) => {
        if (data && data.code === 0) {
          // for (var i = 0; i < data.imgNameList.length; i++) {
          //   this.imgNameList.push(data.imgNameList[i].name);
          //   this.imgSize.push(data.imgNameList[i].size);
          // }
          // this.dataFormSubmit();
          // 上传其他表格信息
          this.$refs.upload.clearFiles();
        } else {
          this.$message.error(data.msg);
        }
      });
    },
    //预览图片时
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    OnChange (file, fileList) {
      // const isType = file.type === "image/jpeg" || "image/png";
      const isLt100M = file.size / 1024 / 1024 < 1024;

      // if (!isType) {
      //   this.$message.error("上传头像图片只能是 JPG 格式!");
      //   fileList.pop();
      // }
      if (!isLt100M) {
        this.$message.error("请检查，上传文件大小不能超过1G!");
        fileList.pop();
      }
      this.dataForm.imgFileList.push(file);
      this.hideUpload = fileList.length >= this.limit;
    },
    //删除图片时
    handleRemove (file, fileList) {
      if (file.id) {
        console.log("删除了已被上传过的图片");
        console.log(file.id);
        this.deleteImgFileList.push(file.id);
      }
      this.dataForm.imgFileList = fileList;
      this.hideUpload = fileList.length >= this.limit;
    },
    //文件超出个数限制时
    handleExceed (files, fileList) {
      this.$message.warning(
        `当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length
        } 个文件`
      );
    },
  },
  data(){
    return {
      dataForm: {
        imgFileList: [],
      },

      //图片上传的参数
      visible: false,
      uploadUrl: "",
      dialogImageUrl: "",
      dialogVisible: false,
      limit: 1,
      hideUpload: false, //是否显示上传图片的加号
      deleteImgFileList: [], //存已被删除了的图片的id
    }
  }

}
</script>

<style>
.uupp .up {
  margin-left: -8%;
  margin-top: 5%;
}
.uupp .q-pa-md {
    padding: 0px 100px;
}
.uupp .avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.uupp .avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.uupp .el-upload--picture-card {
  width: 320px;
  height: 320px;
  line-height: 300px;
  background: none;
}
.hide .el-upload--picture-card {
  display: none;
}
.uupp .el-upload-list--picture-card .el-upload-list__item {
  overflow: hidden;
  background-color: #fff;
  border: 1px solid #c0ccda;
  border-radius: 6px;
  box-sizing: border-box;
  width: 300px;
  height: auto;
  margin: 0 8px 8px 0;
  display: inline-flex;
}
.uupp .avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 500px;
  height: 500px;
  line-height: 500px;
  text-align: center;
}
.uupp .avatar {
  width: 500px;
  height: 500px;
  display: block;
}
.uupp .el-button {
    width: 250px;
    height: 36px;
    display: inline-block;
    line-height: 1;
    white-space: nowrap;
    cursor: pointer;
    opacity: 80%;
    background:rgb(233,152,186);
    border: 1px solid rgb(233,152,186);
    color: #606266;
    -webkit-appearance: none;
    text-align: center;
    box-sizing: border-box;
    outline: 0;
    margin: 0 auto;
    transition: .1s;
    font-weight: 500;
    padding: 12px 20px;
    font-size: 14px;
    border-radius: 4px;
    margin-left: 175px;
}
.uupp .q-tab-panel {
    padding: 2px;
}
.uupp .q-panel > div {
    height: 100%;
    width: 150%;
}
.el-avatar {
    display: inline-block;
    box-sizing: border-box;
    text-align: center;
    color: #fff;
    background:transparent;
    border: 1px solid #c0ccda;
    width: 40px;
    height: 40px;
    line-height: 40px;
    font-size: 14px;
    border-radius: 6px;
}
</style>