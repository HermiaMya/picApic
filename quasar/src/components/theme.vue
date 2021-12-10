<template>
<div>
  <div class="box-body">主题切换</div>
  <button @click="change(1)">切换到紫色主题</button>
  <button @click="change(2)">切换到蓝色主题</button>
</div>
</template>
<script>
import "../assets/css/index.css";
import "../assets/css/index1.css"
export default {
  name: "theme",
  data(){
        return{
          body_now:null
        }
  },
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://i.loli.net/2021/11/24/5kA2cdmWuKjJMDT.gif') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
  },
  methods:{
          change:function (type) {
            if(type == 1){
              document.getElementById('style').setAttribute("href","../src/assets/css/one.css");
              localStorage.setItem("style","../src/assets/css/index.css");
            }else if(type == 2){
              document.getElementById('style').setAttribute("href","../src/assets/css/two.css");
              localStorage.setItem("style","../src/assets/css/index1.css");
            }
          }
        }

}