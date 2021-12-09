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
  
}
</script>
