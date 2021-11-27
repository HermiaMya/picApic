<template>
  <q-page class="flex flex-center">
 
    <div class="up">
      <upload style="margin-left:150px" ></upload>
      <slider style=""></slider>
    </div>
  </q-page>
</template>
  


<script>
import upload from '../components/upload.vue';
import theme from '../components/theme.vue';
import slider from '../components/slider.vue'
export default {
  name: "PageIndex",
  components: {
    upload,
    theme,
    slider
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://i.loli.net/2021/11/24/5kA2cdmWuKjJMDT.gif') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
  }

}
</script>

<style>
.up {
  margin-left: -4%;
  margin-top: 3%;
}
</style>