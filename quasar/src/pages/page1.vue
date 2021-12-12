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
     <div class="q-pa-md" >
    <div class="q-gutter-y-md" style="max-width: 600px">
      <q-card>
        <q-tabs
          v-model="tab"
          dense
          class="bg-primary text-grey-7"
          active-color="primary"
          indicator-color="purple"
          align="justify"
        >
          <q-tab name="meme" label="表情包" />
          <q-tab name="ip" label="多IP联动" />
          <q-tab name="ai" label="AI换脸" />
        </q-tabs>

        <q-tab-panels v-model="tab" animated class="bg-primary text-white">
          <q-tab-panel name="meme">
            <button v-on:click="meme1">
            <img
              src="https://i.loli.net/2021/11/25/WPAU3iMwQGsZ9Oj.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            </button>
            <button v-on:click="meme2">
            <img
              src="https://i.loli.net/2021/11/25/lrS3NR6Z8P7i4LC.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            </button>
            <button v-on:click="meme3">
            <img
              src="https://i.loli.net/2021/11/26/ePQBtmRw2HU1J7a.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            </button>
            <button v-on:click="meme4">
            <img
              src="https://i.loli.net/2021/11/26/rKXtIjnfFPvWLYx.gif"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            </button>
            <button v-on:click="meme5">
            <img
              src="https://i.loli.net/2021/11/26/jWDFoYUBrzsJSuA.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            </button>
          </q-tab-panel>

          <q-tab-panel name="ip">
            <button v-on:click="ip1">
            <img
              src="https://s3.bmp.ovh/imgs/2021/12/d535554cb9a33532.jpeg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            </button>
            <button v-on:click="ip2">
            <img
              src="https://s3.bmp.ovh/imgs/2021/12/b28c23f337121e1c.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            </button>
            <button v-on:click="ip3">
            <img
              src="https://s3.bmp.ovh/imgs/2021/12/99d17e2ae8812ab7.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            </button>
            <button v-on:click="ip4">
            <img
              src="https://s3.bmp.ovh/imgs/2021/12/be2f56180bd22af4.png"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            </button>
          </q-tab-panel>

          <q-tab-panel name="ai">
              <div class="up2" style="float:left;width = 160px">
     <el-upload
    ref="upload"
    action="#"
    :file-list="dataForm.imgFileListTem"
    list-type="picture-card"
    :on-preview="handlePictureCardPreviewTem"
    :on-change="OnChangeTem"
    :on-remove="handleRemoveTem"
     :on-exceed="handleExceed"
    :limit="1"
    :class="{ hide: hideUploadTem }"
    accept="image/jpeg,image/png"
    :auto-upload="false"
    >
     <i class="el-icon-plus"></i>
     </el-upload>
 </div>
            <img
              src="https://i.loli.net/2021/11/26/4RykKnvgwhBboXi.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <img
              src="https://i.loli.net/2021/11/26/Vo8IlULtAhyGPap.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>
  </div>
    </div>
  </q-page>
</template>
  


<script>
import theme from '../components/theme.vue'
export default {
  name: "Page1",
  components: {
    theme,
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://i.loli.net/2021/11/24/5kA2cdmWuKjJMDT.gif') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      
  },
  methods: {
    
	meme1(){
        this.choice="meme1";
    },
    meme2(){
        this.choice="meme2";
    },
    meme3(){
        this.choice="meme3";
    },
    meme4(){
        this.choice="meme4";
    },
    meme5(){
        this.choice="meme5";
    },
    ip1(){
        this.choice="ip1";
    },
    ip2(){
        this.choice="ip2";
    },
    ip3(){
        this.choice="ip3";
    },
    ip4(){
        this.choice="ip4";
    },
    handleRemove(file, fileList) {
      this.hideUpload = fileList.length >= this.limitCount;
    },
    handleChange(fileList) {
      this.hideUpload = fileList.length >= this.limitCount;
      this.hideUpload = true; //此时值为ture时 才会执行隐藏
    },
    handleRemoveTem(file, fileList) {
      this.hideUploadTem = fileList.length >= this.limitCount;
    },
    handleChangeTem(fileList) {
      this.hideUploadTem = fileList.length >= this.limitCount;
      this.hideUploadTem = true; //此时值为ture时 才会执行隐藏
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
      this.dataForm.imgFileListTem.forEach((file) => {
        console.log(file.raw);
        console.log(file.size);
        formData.append("filetem", file.raw);
      });
      formData.append("tab",this.tab);
      formData.append("choice",this.choice);

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
    handlePictureCardPreviewTem (file) {
      this.dialogImageUrlTem = file.url;
      this.dialogVisibleTem = true;
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
    OnChangeTem (file, fileList) {
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
      this.dataForm.imgFileListTem.push(file);
      this.hideUploadTem = fileList.length >= this.limit;
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
    handleRemoveTem (file, fileList) {
      if (file.id) {
        console.log("删除了已被上传过的图片");
        console.log(file.id);
        this.deleteImgFileListTem.push(file.id);
      }
      this.dataForm.imgFileListTem = fileList;
      this.hideUploadTem = fileList.length >= this.limit;
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
        imgFileListTem: [],
      },
      tab: 'meme',
      choice:'',
      //图片上传的参数
      visible: false,
      uploadUrl: "",
      dialogImageUrl: "",
      dialogVisible: false,
      dialogImageUrlTem: "",
      dialogVisibleTem: false,
      limit: 1,
      hideUpload: false,
      hideUploadTem: false, //是否显示上传图片的加号
      deleteImgFileList: [], 
      deleteImgFileListTem: [], //存已被删除了的图片的id
    }
  }

}
</script>

<style>
.q-pa-md .bg-primary {
    background:rgb(234,184,219) !important;
}
.up2 .el-upload-list--picture-card .el-upload-list__item{
    width: 150px !important;
}
.up2 .el-upload--picture-card {
  width: 140px !important;
  height: 140px !important;
  line-height: 140px !important;
  background: none;
}
.uupp.q-pa-md .q-tab-panel {
    padding: 20px;
}
.uupp.q-pa-md .absolute-full, .fullscreen, .fixed-full {
    top: 0px;
    right: 4px;
    bottom: 0;
    left: 4px;
}
.uupp.q-pa-md .q-panel > div {
    height: 100%;
    width: 300%;
}
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