<template>
  <q-page class="flex flex-center">
    <theme></theme>
    <div style="position:relative">
   <img src="https://i.loli.net/2021/11/25/IoNVuORKSp7d3ga.jpg">
   <el-button style="background:none;width:150px;height:40px;position:absolute;right: 52%;top:67%;boarder:none;font-size:24px" @click="addRoutes1"></el-button>
   <img/>
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
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://s2.loli.net/2021/12/13/E4opxB8MgkFWzRJ.gif') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
  },
    methods: {
    addRoutes1 () {
      this.$router.push('/page1')
    },
    }
}

</script>

<style>
.up {
  margin-left: -4%;
  margin-top: 3%;
}
</style>
