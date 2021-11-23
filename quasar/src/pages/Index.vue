<template>
  <q-page class="flex flex-center">
    <el-upload
      :show-file-list="false"
      :on-success="handleAvatarSuccess"
      :before-upload="beforeAvatarUpload"
      class="avatar-uploader"
      action="https://jsonplaceholder.typicode.com/posts/"
    >
      <img v-if="imageUrl" :src="imageUrl" class="avatar" />
      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>
  </q-page>
</template>
<script>
export default {
  name: "PageIndex",
  data() {
    return {
      imageUrl: "",
    };
  },
}
</script>
