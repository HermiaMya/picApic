<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      conTop: {
        backgroundImage: 'url(' + require('./picture/back.jpg') + ')',
        backgroundRepeat: 'no-repeat',
      }

    }
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://i.loli.net/2021/11/21/rqbItuoyf74shde.jpg')";
  }

}
</script>
