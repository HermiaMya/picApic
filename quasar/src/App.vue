<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>

export default {
  name: 'App',
  created() {
  var style = localStorage.getItem("style");
  if(style){
    document.getElementById('style').setAttribute("href",style); //实现将主题保存在内存中刷新浏览器不改变
  }
}
  
}
</script>
