<template>
  <q-page class="flex flex-center">
    <div class="tup">
    <theme></theme>
    <div class="up">
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
              <el-avatar shape="square" :size="320" :src="url"></el-avatar>
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
    </div>
    </div>
  </q-page>
</template>
  


<script>
import theme from '../components/theme.vue'
export default {
  name: "PageIndex",
  components: {
    theme
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://i.loli.net/2021/11/24/5kA2cdmWuKjJMDT.gif') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
  },
  methods: {

		getchannel(data){
          this.tab = data
          console.log(this.tab)
    },
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    handleChange(fileList) {
      this.hideUpload = fileList.length >= this.limitCount;
      this.hideUpload = true; //此时值为ture时 才会执行隐藏
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
        console.log(this.dataForm.tab);
        formData.append("file", file.raw);
      });
      // 以下代码可以根据实际情况自己来实现
      axios({
        url: this.uploadUrl,
        method: "post",
        data: formData,
        responseType:'blob',
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
        console.log("ok")
        this.url=window.URL.createObjectURL(data.image_url);
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
      uploadUrl: "http:127.0.0.1:8000/pixel/main.html",
      dialogImageUrl: "",
      dialogVisible: false,
      limit: 1,
      hideUpload: false, //是否显示上传图片的加号
      deleteImgFileList: [], //存已被删除了的图片的id
      url:""
    }
  }

}
</script>

<style>
.up {
  margin-left: -4%;
  margin-top: 3%;
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
.el-button {
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
  margin-left: 185px;
}
</style>