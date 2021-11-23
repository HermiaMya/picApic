<template>
  <q-page class="flex flex-center">
    <theme></theme>
    <div class="up">
      <upload></upload>
    </div>
  </q-page>
</template>
  


<script>
import upload from '../components/upload.vue';
import theme from '../components/theme.vue'
export default {
  name: "PageIndex",
  components: {
    upload,
    theme
  }
}
</script>

<style>
.up {
  margin-left: -5%;
}
</style>
