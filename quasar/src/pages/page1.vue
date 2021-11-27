<template>
  <q-page class="flex flex-center">
    <theme></theme>
    <div class="up">
      <upload style="margin-top:50px; margin-left:50px"></upload>
      <submenu1 style="margin-top:50px; margin-left:50px"></submenu1>
    </div>
  </q-page>
</template>
  


<script>
import upload from '../components/upload.vue';
import theme from '../components/theme.vue'
import submenu1 from '../components/submenu1.vue'
export default {
  name: "PageIndex",
  components: {
    upload,
    theme,
    submenu1
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