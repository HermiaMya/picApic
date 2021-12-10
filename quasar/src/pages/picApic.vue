<template>
<div>
  <body>
    <div id=background></div>
    <div id=image class="test"></div>
    <div id=options>
        <div id="imagecolor" style="display: flex;margin-left: 50%;"></div>

        <div class=upload>上传ヾ(•ω•`)o
            <input type="file" id="file1" name="file1" onchange="LoadImage()" />
            <audio id="music"><source src="./page/sound/pikapik.mp3"> </audio>
        </div>




    </div>

    <div id=container style="display: inline-block;
    vertical-align: top;width: 75%;margin-left: 26%;">
        <div id=container1>

            <div class=inputname>grayscale灰度</div>
            <input value=0 min=0 max=100 step=any id=grayscale oninput="change1()" type=range>
            <input id="grayscale1" type=number onchange="change2()" style="border: none; border-radius: 16px;padding-left: 8px;" />
            <audio id="music2"><source src="./page/sound/pika.mp3"> </audio>

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
            <audio id="music3"><source src="./page/sound/pikachu.mp3"> </audio>


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
import html2canvas from "html2canvas";
import canvas2image from './page/js/canvas2image';



export default {
  name:"picApic",
  mounted () {
    document.querySelector("body").style.backgroundImage =
      "url('https://i.loli.net/2021/11/24/5kA2cdmWuKjJMDT.gif') ";
      document.querySelector("body").style.backgroundAttachment= 'fixed';
      document.querySelector("body").style.backgroundSize= 'cover';
      var qulity = 100;
      window.onload =function() {
    var audio = document.getElementById('music');
    audio.pause(); //打开页面时无音乐
};

document.getElementById("file1").onchange = function() {
    //function LoadImage(){
    $("#image").css("-webkit-filter", "none");
    $("#image").css("-moz-filter", "none");

    //1 创建文件读取对象
    var reader = new FileReader();

    //文件存储在file表单元素的files属性中，它是一个数组
    //没有返回值，但是读取完毕后，将读取结果存储在对象的result中
    var fil = document.getElementById("file1").files;

    reader.readAsDataURL(fil[0]);
    reader.readas
        //当读取成功后触发
    reader.onload = function() {
        var url = reader.result;
        $("#image").css("background-image", "url(" + url + ")");
        var imageObj = new Image();
        imageObj.src = reader.result;
        imageObj.onload = function() {
            w = imageObj.width;
            h = imageObj.height;
            var audio = document.getElementById('music');
            if (audio.paused) {
                audio.play();
            } else {
                audio.pause();
            }
            var canvas = document.createElement('canvas');

            // 给canvas赋值
            canvas.width = w;
            canvas.height = h;

            // 将图画入canvas
            var ctx = canvas.getContext('2d');
            ctx.drawImage(imageObj, 0, 0);

            var imgData = ctx.getImageData(0, 0, w, h);
            CalculateGray(imgData);
            CalculateBlur();
            CalculateContrast(imgData, w);
            CalculateHuerotate();
            CalculateInversion()
            CalculateAlpha(imgData);
            CalculateSaturation(imgData);
            CalculateSepia();
            CalculateHue(imgData);
        };
    };

};
$(function() {
    $("#reset").click(function() {

        var audio = document.getElementById('music3');
        audio.play();

        $("#grayscale").val(0);
        $("#blur").val(0);
        $("#brightness").val(100);
        $("#contrast").val(100);
        $("#huerotate").val(0);
        $("#invert").val(0);
        $("#opacity").val(100);
        $("#saturate").val(1);
        $("#sepia").val(0);
        $("#image").css("-webkit-filter", "none");
        $("#image").css("-moz-filter", "none");

        var location1 = document.getElementById("grayscale1"),
            location2 = document.getElementById("blur1"),
            location3 = document.getElementById("brightness1"),
            location4 = document.getElementById("contrast1"),
            location5 = document.getElementById("hue-rotate"),
            location6 = document.getElementById("invert1"),
            location7 = document.getElementById("opacity1"),
            location8 = document.getElementById("saturate1"),
            location9 = document.getElementById("sepia1");

        location1.value = 0;
        location2.value = 0;
        location3.value = 100;
        location4.value = 100;
        location5.value = 0;
        location6.value = 0;
        location7.value = 100;
        location8.value = 1;
        location9.value = 0;
    });
});

$(document).ready(function() {
    $("input").on("input", function() {
        var grayscale = $("#grayscale").val(),
            blur = $("#blur").val(),
            brightness = $("#brightness").val(),
            contrast = $("#contrast").val(),
            huerotate = $("#huerotate").val(),
            invert = $("#invert").val(),
            opacity = $("#opacity").val(),
            saturate = $("#saturate").val(),
            sepia = $("#sepia").val();


        $("#image").css({
            "-webkit-filter": "grayscale(" + grayscale + "%)" +
                "blur(" + blur + "px)" + "brightness(" + brightness + "%)" +
                " contrast(" + contrast + "%)" +
                " hue-rotate(" + huerotate + "deg)" +
                " invert(" + invert + "%)" +
                " opacity(" + opacity + "%)" +
                " saturate(" + saturate + ")" +
                " sepia(" + sepia + "%)",

            "filter": "grayscale(" + grayscale + "%)" +
                "blur(" + blur + "px)" + "brightness(" + brightness + "%)" +
                " contrast(" + contrast + "%)" +
                " hue-rotate(" + huerotate + "deg)" +
                " invert(" + invert + "%)" +
                " opacity(" + opacity + "%)" +
                " saturate(" + saturate + ")" +
                " sepia(" + sepia + "%)"
        });

    });

    //放大图片
    $("#image").click(function() {
        $("#image").toggleClass("zoomed");

    });
});


var test = $(".test").get(0); //将jQuery对象转换为dom对象
// 点击转成canvas
$('.toCanvas').click(function(e) {
    // 调用html2canvas插件
    html2canvas(test).then(function(canvas) {
        // canvas宽度
        var canvasWidth = canvas.width;
        // canvas高度
        var canvasHeight = canvas.height;
        // 调用Canvas2Image插件
        var img = Canvas2Image.convertToImage(canvas, canvasWidth, canvasHeight);
        // 点击保存
        $('#save').click(function(e) {
            let type = $('#sel').val(); //图片类型
            let w = $('#imgW').val(); //图片宽度
            let h = $('#imgH').val(); //图片高度
            let f = $('#imgFileName').val(); //图片文件名
            w = (w === '') ? canvasWidth : w; //判断输入宽高是否为空，为空时保持原来的值
            h = (h === '') ? canvasHeight : h;
            // 调用Canvas2Image插件
            Canvas2Image.saveAsImage(canvas, w, h, type, f);
        })
    })
})
  },
  methods:{

//计算灰度
CalculateGray(imgData) {
    var gray = 0;
    for (var i = 0; i < imgData.data.length; i += 4) { //遍历图像矩阵
        var R = imgData.data[i]; //R(0-255)
        var G = imgData.data[i + 1]; //G(0-255)
        var B = imgData.data[i + 2]; //G(0-255)
        var Alpha = imgData.data[i + 3]; //Alpha(0-255)
        //浮点算法
        gray += R * 0.299 + G * 0.587 + B * 0.114;
    }
    var ans = gray / imgData.data.length;
    var location = document.getElementById("grayscale1");
    location.value = parseInt(ans);
    CalculateBrightness(ans);
    $("#grayscale").val(location.value);
},

//计算模糊度
CalculateBlur() {
    var location = document.getElementById("blur1");
    location.value = 0;
},

//计算亮度
CalculateBrightness(ans) {
    var location = document.getElementById("brightness1");
    location.value = parseInt(ans);
    $("#brightness").val(location.value);
},

//计算对比度
CalculateContrast(imgData, w) {
    var gray = new Array();
    var j = 0;
    var contrast = 0;
    var num = 0;

    for (var i = 0; i < imgData.data.length; i += 4) { //遍历图像矩阵

        var R = imgData.data[i]; //R(0-255)
        var G = imgData.data[i + 1]; //G(0-255)
        var B = imgData.data[i + 2]; //G(0-255)
        var Alpha = imgData.data[i + 3]; //Alpha(0-255)
        //浮点算法
        gray[j] = R * 0.299 + G * 0.587 + B * 0.114;
        j = j + 1;

    }
    var width = w;
    var length = gray.length;

    for (var k = 0; k < length; k += 1) {

        if (k == 0) {
            contrast = contrast + Math.pow(gray[k + 1] - gray[k], 2) + Math.pow(gray[k + width] - gray[k], 2);
            num += 2;


        } else if (k == width - 1) {
            contrast = contrast + Math.pow(gray[k - 1] - gray[k], 2) + Math.pow(gray[k + width] - gray[k], 2);
            num += 2;
        } else if (k == length - width) {
            contrast = contrast + Math.pow(gray[k + 1] - gray[k], 2) + Math.pow(gray[k - width] - gray[k], 2);
            num += 2;
        } else if (k == length - 1) {
            contrast = contrast + Math.pow(gray[k - 1] - gray[k], 2) + Math.pow(gray[k - width] - gray[k], 2);
            num += 2;
        } else if (k % width == 0) {
            contrast = contrast + Math.pow(gray[k + 1] - gray[k], 2) + Math.pow(gray[k + width] - gray[k], 2) + Math.pow(gray[k - width] - gray[k], 2);
            num += 3;
        } else if (k % (width - 1) == 0) {
            contrast = contrast + Math.pow(gray[k - 1] - gray[k], 2) + Math.pow(gray[k + width] - gray[k], 2) + Math.pow(gray[k - width] - gray[k], 2);
            num += 3
        } else if (k > 0 && k < width - 1) {
            contrast = contrast + Math.pow(gray[k + 1] - gray[k], 2) + Math.pow(gray[k - 1] - gray[k], 2) + Math.pow(gray[k + width] - gray[k], 2);
            num += 3;
        } else if (k > (length - width) && k < (length - 1)) {
            contrast = contrast + Math.pow(gray[k + 1] - gray[k], 2) + Math.pow(gray[k - 1] - gray[k], 2) + Math.pow(gray[k - width] - gray[k], 2);
            num += 3;
        } else {
            contrast = contrast + Math.pow(gray[k + 1] - gray[k], 2) + Math.pow(gray[k - 1] - gray[k], 2) + Math.pow(gray[k - width] - gray[k], 2) + Math.pow(gray[k + width] - gray[k], 2);
            num += 4;
        }
    }

    var ans = contrast / num;
    ans = Math.floor(ans * 1000) / 1000;
    var location = document.getElementById("contrast1");
    location.value = ans;

},

//计算色相
CalculateHuerotate() {
    var location = document.getElementById("hue-rotate");
    location.value = 0;
},

//计算反转
CalculateInversion() {
    var location = document.getElementById("invert1");
    location.value = 0;
},

//计算透明度
CalculateAlpha(imgData) {
    var sum = 0;
    for (var i = 0; i < imgData.data.length; i += 4) {
        var R = imgData.data[i]; //R(0-255)
        var G = imgData.data[i + 1]; //G(0-255)
        var B = imgData.data[i + 2]; //G(0-255)
        var Alpha = imgData.data[i + 3]; //Alpha(0-255)
        sum += Alpha;
    }
    var ans = sum / imgData.data.length;
    var location = document.getElementById("opacity1");
    location.value = parseInt(ans);
    $("#opacity").val(location.value);
},

//计算平均饱和度
CalculateSaturation(imgData) {
    var gray = 0;
    var num = 0;
    var saturation = 0;
    for (var i = 0; i < imgData.data.length; i += 4) { //遍历图像矩阵
        var R = imgData.data[i]; //R(0-255)
        var G = imgData.data[i + 1]; //G(0-255)
        var B = imgData.data[i + 2]; //G(0-255)
        var Alpha = imgData.data[i + 3]; //Alpha(0-255)
        //浮点算法
        num = num + 1;
        var max = Math.max(R, G, B);
        var min = Math.min(R, G, B);
        var delta = (max - min) / 255;
        if (delta > 0) {
            var value = (max + min) / 255;
            var l = value / 2;
            if (l < 0.5) {
                var s = delta / value;
            } else {
                var s = delta / (2 - value);
            }
            saturation = s + saturation;
        }
    }
    var ans = saturation / num;
    ans = Math.floor(ans * 1000) / 1000;
    var location = document.getElementById("saturate1");
    location.value = ans;
    $("#saturate").val(ans);
},

//计算棕色度
CalculateSepia() {
    var location = document.getElementById("sepia1");
    location.value = 0;
},

//提取主颜色
CalculateHue(imgData) {
    var rgbArray = new Array();
    for (var i = 0; i < imgData.data.length; i += 4) { //遍历图像矩阵
        var R = imgData.data[i]; //R(0-255)
        var G = imgData.data[i + 1]; //G(0-255)
        var B = imgData.data[i + 2]; //G(0-255)
        var Alpha = imgData.data[i + 3]; //Alpha(0-255)
        //浮点算法
        if (Alpha > 125) {
            rgbArray.push([R, G, B, Alpha]);
        }

    }
    console.log(rgbArray);
    GetColor(rgbArray);
},

GetColor(cube) {
    var maxr = cube[0][0],
        minr = cube[0][0],
        maxg = cube[0][1],
        ming = cube[0][1],
        maxb = cube[0][2],
        minb = cube[0][2];
    for (var i = 0; i < cube.length; i++) {
        if (cube[i][0] > maxr) {
            maxr = cube[i][0];
        }
        if (cube[i][0] < minr) {
            minr = cube[i][0];
        }
        if (cube[i][1] > maxg) {
            maxg = cube[i][1];
        }
        if (cube[i][1] < ming) {
            ming = cube[i][1];
        }
        if (cube[i][2] > maxb) {
            maxb = cube[i][2];
        }
        if (cube[i][2] < minb) {
            minb = cube[i][2];
        }
    }

    if ((maxr - minr) < qulity && (maxg - ming) < qulity && (maxb - minb) < qulity) {
        var r = 0,
            g = 0,
            b = 0;
        for (var i = 0; i < cube.length; i++) {
            r += cube[i][0];
            g += cube[i][1];
            b += cube[i][2];
        }
        var divcolor = document.createElement("div");
        divcolor.style.backgroundColor = "rgba(" + r / (cube.length) + "," + g / (cube.length) + "," + b / (cube.length) + ")";
        divcolor.style.width = "20px";
        divcolor.style.height = "20px";
        var html = document.getElementById("imagecolor");
        html.appendChild(divcolor);
    } else {
        var maxrgb = 0;
        var rgbindex = 0;
        var rgbmiddle = 0;

        if ((maxr - minr) > maxrgb) {
            maxrgb = (maxr - minr);
            rgbmiddle = (maxr + minr) / 2
            rgbindex = 0;
        }
        if ((maxg - ming) > maxrgb) {
            maxrgb = (maxg - ming);
            rgbmiddle = (maxg + ming) / 2;
            rgbindex = 1;
        }
        if ((maxb - minb) > maxrgb) {
            maxrgb = (maxb - minb);
            rgbmiddle = (maxb + minb) / 2;
            rgbindex = 2;
        }

        //排序
        cube.sort(function(x, y) {
            return x[rgbindex] - y[rgbindex];
        });
        var cubea = new Array();
        var cubeb = new Array();
        for (var i = 0; i < cube.length; i++) {
            if (cube[i][rgbindex] < rgbmiddle) {
                cubea.push(cube[i]);
            } else {
                cubeb.push(cube[i]);
            }
        }

        GetColor(cubeb);
        GetColor(cubea);
    }
},

change1() {
    var audio = document.getElementById('music2');
    audio.play();

    var grayscale = $("#grayscale").val(),
        blur = $("#blur").val(),
        brightness = $("#brightness").val(),
        contrast = $("#contrast").val(),
        huerotate = $("#huerotate").val(),
        invert = $("#invert").val(),
        opacity = $("#opacity").val(),
        saturate = $("#saturate").val(),
        sepia = $("#sepia").val();

    saturate = Math.floor(saturate * 1000) / 1000;

    var location1 = document.getElementById("grayscale1"),
        location2 = document.getElementById("blur1"),
        location3 = document.getElementById("brightness1"),
        location4 = document.getElementById("contrast1"),
        location5 = document.getElementById("hue-rotate"),
        location6 = document.getElementById("invert1"),
        location7 = document.getElementById("opacity1"),
        location8 = document.getElementById("saturate1"),
        location9 = document.getElementById("sepia1");

    location1.value = parseInt(grayscale);
    location2.value = parseInt(blur);
    location3.value = parseInt(brightness);
    location4.value = parseInt(contrast);
    location5.value = parseInt(huerotate);
    location6.value = parseInt(invert);
    location7.value = parseInt(opacity);
    location8.value = saturate;
    location9.value = parseInt(sepia);

},

change2() {
    var location1 = document.getElementById("grayscale1"),
        location2 = document.getElementById("blur1"),
        location3 = document.getElementById("brightness1"),
        location4 = document.getElementById("contrast1"),
        location5 = document.getElementById("hue-rotate"),
        location6 = document.getElementById("invert1"),
        location7 = document.getElementById("opacity1"),
        location8 = document.getElementById("saturate1"),
        location9 = document.getElementById("sepia1");

    var grayscale = location1.value,
        blur = location2.value,
        brightness = location3.value,
        contrast = location4.value,
        huerotate = location5.value,
        invert = location6.value,
        opacity = location7.value,
        saturate = location8.value,
        sepia = location9.value;

    $("#grayscale").val(grayscale);
    $("#blur").val(blur);
    $("#brightness").val(brightness);
    $("#contrast").val(contrast);
    $("#huerotate").val(huerotate);
    $("#invert").val(invert);
    $("#opacity").val(opacity);
    $("#saturate").val(saturate);
    $("#sepia").val(sepia);

    $("#image").css({
        "-webkit-filter": "grayscale(" + grayscale + "%)" +
            "blur(" + blur + "px)" + "brightness(" + brightness + "%)" +
            " contrast(" + contrast + "%)" +
            " hue-rotate(" + huerotate + "deg)" +
            " invert(" + invert + "%)" +
            " opacity(" + opacity + "%)" +
            " saturate(" + saturate + ")" +
            " sepia(" + sepia + "%)",

        "filter": "grayscale(" + grayscale + "%)" +
            "blur(" + blur + "px)" + "brightness(" + brightness + "%)" +
            " contrast(" + contrast + "%)" +
            " hue-rotate(" + huerotate + "deg)" +
            " invert(" + invert + "%)" +
            " opacity(" + opacity + "%)" +
            " saturate(" + saturate + ")" +
            " sepia(" + sepia + "%)"
    });
},


  }
}
</script>

<!--<script type="text/javascript" src="./page/js/jquery-3.6.0.js"></script>
<script type="text/javascript" src="page/js/index.js"></script>
<script type="text/javascript" src="page/js/canvas2image.js"></script>
<script type="text/javascript" src="page/js/htmlcanvas.min.js"></script>-->

<style>
* {
    margin: 0;
    padding: 0;
}
body {
    background: #fff;
    background-image: url("https://i.loli.net/2021/11/24/5kA2cdmWuKjJMDT.gif");
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
    background-image: url("https://i.loli.net/2021/11/24/5kA2cdmWuKjJMDT.gif");
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