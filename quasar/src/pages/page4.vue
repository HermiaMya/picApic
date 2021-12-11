<template>
  <q-page class="flex flex-center">
    <div class="upp">
      <div class="up">
        <el-form
          :model="dataForm"
        ref="dataForm"
          label-width="80px"
          style="width=800px;"
        >
          <el-form-item :class="{ hide: hideUpload }">
          <div class="up">
            <el-upload
              ref="upload"
              action="#"
              :file-list="dataForm.imgFileList"
              list-type="picture-card"
              :on-preview="handlePictureCardPreview"
              :on-change="OnChange"
              :on-remove="handleRemove"
              :on-exceed="handleExceed"
              :class="{ hidee: hideUpload }"
              :limit="1"
              accept="image/jpeg,image/png"
              :auto-upload="false"
            >
            <i class="el-icon-plus"></i>
            <div class="el-upload__tip" slot="tip">
              只能上传jpg/png文件，最多上传1张且单张图片不超过5M
            </div>
            </el-upload>
          </div>
          <el-dialog :visible.sync="dialogVisible" append-to-body>
            <img width="100%" :src="dialogImageUrl" alt="" />
          </el-dialog>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitUpload()">确定</el-button>
          </el-form-item>
        </el-form>
      </div>
      <slider style=""></slider>
    </div>
  </q-page>
</template>
  


<script>
import theme from '../components/theme.vue';
import slider from '../components/slider.vue'
export default {
  name: "Page4",
  components: {
    theme,
    slider
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
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    handleChange(fileList) {
      this.hideUpload = fileList.length >= this.limit;
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

