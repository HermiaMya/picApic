<template>
  <q-page class="flex flex-center">
    <theme></theme>
    <div class="up">
      <upload></upload>
      <submenu3></submenu3>
    </div>
  </q-page>
</template>
  


<script>
import upload from '../components/upload.vue';
import theme from '../components/theme.vue'
import submenu3 from '../components/submenu3.vue'
export default {
  name: "PageIndex",
  components: {
    upload,
    theme,
    submenu3
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