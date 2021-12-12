<template>
</template>
<script>
import "../assets/css/index.css";
import "../assets/css/index1.css"
export default {
  name: "theme",
  data(){
        return{
        }
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://i.loli.net/2021/11/24/5kA2cdmWuKjJMDT.gif') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
  }

}