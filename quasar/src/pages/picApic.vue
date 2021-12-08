<template>
<div>
  <body>
    <div id=background></div>
    <div id=image class="test"></div>
    <div id=options>
        <div id="imagecolor" style="display: flex;margin-left: 50%;"></div>

        <div class=upload>上传ヾ(•ω•`)o
            <input type="file" id="file1" name="file1" onchange="LoadImage()" />
            <audio id="music"><source src="sound/pikapik.mp3"> </audio>
        </div>




    </div>

    <div id=container style="display: inline-block;
    vertical-align: top;width: 75%;margin-left: 26%;">
        <div id=container1>

            <div class=inputname>grayscale灰度</div>
            <input value=0 min=0 max=100 step=any id=grayscale oninput="change1()" type=range>
            <input id="grayscale1" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />
            <audio id="music2"><source src="sound/pika.mp3"> </audio>

            <div class=inputname>blur模糊度</div>
            <input value=0 min=0 max=10 step=any id=blur oninput="change1()" type=range>
            <input id="blur1" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />

            <div class=inputname>brightness亮度</div>
            <input value=100 min=0 max=200 step=any id=brightness oninput="change1()" type=range>
            <input id="brightness1" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />

            <div class=inputname>contrast对比度</div>
            <input value=100 min=0 max=200 step=any id=contrast oninput="change1()" type=range>
            <input id="contrast1" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />
            <div id="reset" style="margin-left:0%;">Reset</div>
            <audio id="music3"><source src="sound/pikachu.mp3"> </audio>


        </div>
        <div id=container2>
            <div class=inputname>hue-rotate色相</div>
            <input value=0 min=0 max=360 step=any id=huerotate oninput="change1()" type=range>
            <input id="hue-rotate" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />

            <div class=inputname>invert反转</div>
            <input value=0 min=0 max=100 step=any id=invert oninput="change1()" type=range>
            <input id="invert1" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />

            <div class=inputname>opacity透明度</div>
            <input value=100 min=0 max=100 step=any id=opacity oninput="change1()" type=range>
            <input id="opacity1" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />

            <div class=inputname>saturate饱和度</div>
            <input value=1 min=0 max=1 step=any id=saturate oninput="change1()" type=range>
            <input id="saturate1" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />

            <div class=inputname>sepia棕色效果</div>
            <input value=0 min=0 max=100 step=any id=sepia oninput="change1()" type=range>
            <input id="sepia1" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />

        </div>
    </div>
    <h2 class="toCanvas"> <a href="javascript:void(0);" class="intoCanvas"> 转成图片 </a></h2>

    <h5>
        <label for="imgW">宽度:</label>
        <input type="number" value="" id="imgW" class="imgw" placeholder="默认是原图宽度" />
        <label for="imgH">高度:</label>
        <input type="number" value="" id="imgH" class="imgh" placeholder="默认是原图高度" />
        <label for="imgFileName">文件名:</label>
        <input type="text" placeholder="文件名" id="imgFileName" class="imgFileName" />
        <select id="sel" class="sel">
		                <option value="png">png</option>
		                <option value="jpeg">jpeg</option>
		                <option value="bmp">bmp</option>
		            </select>
        <button id="save" class="saveimg">确定</button>
    </h5>
  </body>
</div>
</template>
<script>
export default {
  name:"picApic",
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://s2.loli.net/2021/12/07/xshBDeJ8ILH7E5Y.jpg') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
  },
}
</script>

<!--<script type="text/javascript" src="./page/js/jquery-3.6.0.js"></script>
<script type="text/javascript" src="./page/js/index.js"></script>
<script type="text/javascript" src="./page/js/canvas2image.js"></script>
<script type="text/javascript" src="./page/js/html2canvas.min.js"></script>-->

<style>
* {
    margin: 0;
    padding: 0;
}
body {
    background: #fff;
    background-image: url("https://s2.loli.net/2021/12/07/xshBDeJ8ILH7E5Y.jpg");
    /*background-image: -webkit-linear-gradient(top left, #fff, #b4b4b4);
    background-image: linear-gradient(to bottom right, #fff, #b4b4b4);*/
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
    font-family: "huxiaobo";
}
.upload {
    position: relative;
    display: inline-block;
    background: rgb(225, 115, 92);
    border-radius: 16px;
    padding: 4px 12px;
    overflow: hidden;
    color: #fff;
    text-decoration: none;
    text-indent: 0;
    line-height: 20px;
    font-size: 20px;
    width: 230px;
    margin-left: 45%;
    margin-top: 20px;
}
.upload input {
    position: absolute;
    font-size: 100px;
    right: 0;
    top: 0;
    opacity: 0;
}

.upload:hover {
    background: rgb(215, 182, 111);
    color: #000;
    text-decoration: none;
}
#reset,
.inputname {
    color: #000;
    font-family: huxiaobo;
}

#reset:hover{
    background: #ef7126;
    border-color: #218c8d;
}

input[type="range"] {
    background: rgb(225, 115, 92);
    /*------------------------------------------*/
}
#image {
    z-index: 20;
    overflow: hidden;
    float: left;
    width: 98%;
    margin-top: 2%;
    min-height: 400px;
    /*background-image: url(https://yt3.ggpht.com/-V92UP8yaNyQ/AAAAAAAAAAI/AAAAAAAAAAA/zOYDMx8Qk3c/s900-c-k-no/photo.jpg);*/
    background-image: url("https://s2.loli.net/2021/12/07/xshBDeJ8ILH7E5Y.jpg");
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    cursor: -webkit-zoom-in;
    cursor: zoom-in;
    -webkit-transition: width 0.3s linear, height 0.3s linear, background 0.3s linear, box-shadow 0.3s linear;
    transition: width 0.3s linear, height 0.3s linear, background 0.3s linear, box-shadow 0.3s linear;
}

.zoomed {
    background: rgb(225, 115, 92);
    width: 100% !important;
    min-height: 600px !important;
    box-shadow: 0 0 10px rgb(225, 115, 92);
    cursor: -webkit-zoom-out !important;
    cursor: zoom-out !important;
}

#container1 {
    z-index: 0;
    display: inline-block;
    vertical-align: top;
    overflow: hidden;
    margin-right: 2%;
    padding-left: 5px;
    margin-top: 1%;
    width: 33%;
    text-align: left;
    -webkit-transition: width 0.3s linear;
    transition: width 0.3s linear;
}

#container2 {
    margin-top: 1%;
    display: inline-block;
    vertical-align: top;
    margin-left: 0%;
    padding-left: 5px;
    z-index: 0;
    overflow: hidden;
    width: 33%;
    text-align: left;
    -webkit-transition: width 0.3s linear;
    transition: width 0.3s linear;
}

input[type="range"] {
    -webkit-appearance: none;
    outline: none;
    width: 80%;
    height: 4px;
    margin-top: 19px;
    margin-left: 0px;
    border-radius: 5px;
}

.intoCanvas {
    position: relative;
    display: inline-block;
    background: rgb(225, 115, 92);
    border-radius: 16px;
    padding: 4px 12px;
    overflow: hidden;
    color: #fff;
    text-decoration: none;
    text-indent: 0;
    line-height: 20px;
    font-size: 20px;
    width: 230px;
    margin-left: 40%;
    margin-top: 10px;
    font-size: 20px;
    opacity: 80%;
}

.sel {
    position: relative;
    display: inline-block;
    background: rgb(225, 115, 92);
    border-radius: 16px;
    border: none;
    padding-left: 25px;
    overflow: hidden;
    color: #fff;
    text-decoration: none;
    text-indent: 0;
    line-height: 10px;
    font-size: 20px;
    width: 230px;
    height: 30px;
    font-family: huxiaobo;
    margin-top: 20px;
    margin-left: 40%;
    opacity: 80%;
}

.saveimg {
    position: relative;
    display: inline-block;
    background: rgb(225, 115, 92);
    border-radius: 16px;
    border: none;
    overflow: hidden;
    color: #fff;
    text-decoration: none;
    text-indent: 0;
    line-height: 20px;
    font-size: 20px;
    width: 230px;
    margin-top: 20px;
    margin-left: 40%;
    padding: 4px 12px;
    font-family: huxiaobo;
}

label {
    width: 100%;
    min-width: 150px;
    height: 25px;
    float: left;
    margin-left: 26%;
    margin-top: 10px;
    font-family: huxiaobo;
    line-height: 25px;
    font-size: 30px;
    font-weight: 400;
    letter-spacing: 0.1em;
    -webkit-font-smoothing: antialiased;
    border-radius: 2px;
    color: #fff;
    text-shadow: 0 2px 3px #000;
}

.imgw {
    float: left;
    margin-left: 30%;
    margin-top: 10px;
    width: 520px;
}

.imgh {
    float: left;
    margin-left: 30%;
    margin-top: 10px;
    width: 520px;
}

.imgFileName {
    float: left;
    margin-left: 30%;
    margin-top: 10px;
    width: 520px;
}

input[type="number"] {
    font-size: 25px;
    color: rgb(108, 107, 107);
    border: none;
    border-radius: 16px;
    padding-left: 16px;
    font-family: huxiaobo;
    height: 25px;
}

input[type="text"] {
    font-size: 25px;
    height: 25px;
    color: rgb(108, 107, 107);
    border: none;
    border-radius: 16px;
    padding-left: 16px;
    font-family: huxiaobo;
}

.inputname {
    width: 100%;
    min-width: 150px;
    height: 25px;
    margin: 20px auto -5px;
    font-family: huxiaobo;
    line-height: 25px;
    font-size: 30px;
    font-weight: 400;
    letter-spacing: 0.1em;
    -webkit-font-smoothing: antialiased;
    border-radius: 2px;
    color: #fff;
    text-shadow: 0 2px 3px #000;
}

.inputname:first-letter {
    text-transform: uppercase;
    color: rgb(225, 115, 92);
    font-weight: bold;
    font-size: 35px;
}

.inputname:first-of-type {
    margin-top: 20px;
}

input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 15px;
    height: 15px;
    background: rgb(247, 222, 130);
    border: none;
    box-shadow: inset 0 1px 3px rgb(181, 150, 84), 0 0 2px rgb(181, 150, 84);
    border-radius: 50%;
    -webkit-transition: all 0.1s linear;
    transition: all 0.1s linear;
    cursor: pointer;
}

input[type=range]:active::-webkit-slider-thumb {
    -webkit-transform: scale(1.5);
    transform: scale(1.5);
}

input[type=range]::-moz-range-track {
    height: 5px;
    background: rgb(225, 115, 92);
    border-radius: 5px;
}

input[type=range]::-moz-range-thumb {
    width: 10px;
    height: 10px;
    background: #fff;
    border: 5px solid firebrick;
    box-shadow: inset 0 1px 1px rgb(225, 115, 92);
    border-radius: 50%;
    cursor: pointer;
}

input[type=range]:active::-moz-range-thumb {
    transform: scale(1.5);
}

#options {
    width: 66%;
    float: left;
    margin-top: 20px;
    text-align: center;
}
</style>