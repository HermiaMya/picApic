from django.shortcuts import render,HttpResponse
from django.http import JsonResponse  #接口返回的是json，需要引入的信息
from django.views.decorators.csrf import csrf_exempt
from isort import file   #post接口需要引入的信息
from .faceswap import run_face_swap
import json
import cv2
import dlib
import numpy as np
from .faceBlendCommon import getLandmarksFromOne, calculateDelaunayTriangles, warpTriangle, getLandmarks
import re
import io
import requests
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import os


def find_url(string):
    """Find if a string contains an URL"""
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    if len(url) > 0:
        return True

def read_url_or_local_image(path):
    # 如果传入的是图片url，获取url图片信息
    if find_url(path):
        r = requests.get(path)
        pil_im = Image.open(io.BytesIO(r.content))
    else:
        pil_im = Image.open(path)
    # 返回转换成灰度图的图片
    return cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

def face_swap_in1pic(image, output_filename, mode=''):
    # img = read_url_or_local_image(image)
    image = image.get_raw_uri() #类型转为url
    image = read_url_or_local_image(image)

    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    imgWarped = np.copy(img)

    # 载入dlib库中的面部识别器
    # 如果mode为空，调用dlib中默认的面部识别器
    if mode == '':
        detector = dlib.get_frontal_face_detector()
    # 否则，调用cnn面部识别器
    else:
        detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    points1, points2 = getLandmarksFromOne(detector, predictor, img, mode)
    # 计算面部点阵的凸包（即脸的轮廓）
    hullIndex = cv2.convexHull(np.array(points2).astype(np.int32),
                               returnPoints=False)  # add .astype(np.int32) to fix TypeError: data type = 9 not supported
    # 把轮廓点存起来
    hull1 = []
    hull2 = []
    for i in range(0, len(hullIndex)):
        hull1.append(points1[hullIndex[i][0]])
        hull2.append(points2[hullIndex[i][0]])

    # 为图片2计算一个面罩，把原先图片2中的脸盖住
    hull8U2 = []
    for i in range(0, len(hull2)):
        hull8U2.append((hull2[i][0], hull2[i][1]))
    mask2 = np.zeros(img.shape, dtype=img.dtype)
    cv2.fillConvexPoly(mask2, np.int32(hull8U2), (255, 255, 255))
    # 为图片1计算一个面罩，把原先图片2中的脸盖住
    hull8U1 = []
    for i in range(0, len(hull1)):
        hull8U1.append((hull1[i][0], hull1[i][1]))
    mask1 = np.zeros(img.shape, dtype=img.dtype)
    cv2.fillConvexPoly(mask1, np.int32(hull8U1), (255, 255, 255))

    # 找到图片2中的脸的面心
    m2 = cv2.moments(mask2[:, :, 1])
    center2 = (int(m2['m10'] / m2['m00']), int(m2['m01'] / m2['m00']))
    # 找到图片1中的脸的面心
    m1 = cv2.moments(mask1[:, :, 1])
    center1 = (int(m1['m10'] / m1['m00']), int(m1['m01'] / m1['m00']))
    # 把图2中的脸狄洛尼三角剖分
    sizeImg = img.shape
    rect = (0, 0, sizeImg[1], sizeImg[0])
    dt2 = calculateDelaunayTriangles(rect, hull2)
    dt1 = calculateDelaunayTriangles(rect, hull1)
    # 如果无法划分，退出程序
    if len(dt1) == 0 or len(dt2) == 0:
        quit()
    # 储存分出的一个个三角形
    tris1 = []
    tris2 = []
    for i in range(0, len(dt2)):
        tri1 = []
        tri2 = []
        for j in range(0, 3):
            tri1.append(hull1[dt2[i][j]])
            tri2.append(hull2[dt2[i][j]])
            tris1.append(tri1)
            tris2.append(tri2)
    # 将这图1的脸上的一个个小三角形通过仿射变换投影到图2的脸上
    for i in range(0, len(tris1)):
        warpTriangle(img, imgWarped, tris1[i], tris2[i])
    # 储存分出的一个个三角形
    tris1 = []
    tris2 = []
    for i in range(0, len(dt1)):
        tri1 = []
        tri2 = []
        for j in range(0, 3):
            tri1.append(hull1[dt1[i][j]])
            tri2.append(hull2[dt1[i][j]])
            tris1.append(tri1)
            tris2.append(tri2)
    for i in range(0, len(tris2)):
        warpTriangle(img, imgWarped, tris2[i], tris1[i])
    # 把图1的脸无缝缝合进图2
    output = cv2.seamlessClone(np.uint8(imgWarped), img, mask2, center2, cv2.NORMAL_CLONE)
    output = cv2.seamlessClone(np.uint8(imgWarped), output, mask1, center1, cv2.NORMAL_CLONE)
    # 输出结果
    cv2.imwrite(output_filename, output)


def run_face_swap(from_image, to_image = "image//panda.jpg", output_filename='images//result3.jpg', mode=''):
    if to_image == '':
        face_swap_in1pic(from_image, output_filename, mode)
        exit()

    img1 = read_url_or_local_image(from_image)
    img2 = read_url_or_local_image(to_image)
    # img1 = cv2.cvtColor(np.array(from_image), cv2.COLOR_RGB2BGR)
    # img2 = cv2.cvtColor(np.array(to_image), cv2.COLOR_RGB2BGR)
    # 复制图片2，以保证原来的图片不会被后续的操作改变
    img1Warped = np.copy(img2)
    # 载入dlib库中的面部识别器
    # 如果mode为空，调用dlib中默认的面部识别器
    if mode == '':
        detector = dlib.get_frontal_face_detector()
    # 否则，调用cnn面部识别器
    # else:
    #     detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    # 识别图片中的面部点阵信息
    points1 = getLandmarks(detector, predictor, img1, mode)
    points2 = getLandmarks(detector, predictor, img2, mode)
    # 计算面部点阵的凸包（即脸的轮廓）
    hullIndex = cv2.convexHull(np.array(points2).astype(np.int32),
                               returnPoints=False)  # add .astype(np.int32) to fix TypeError: data type = 9 not supported
    # 把轮廓点存起来
    hull1 = []
    hull2 = []
    for i in range(0, len(hullIndex)):
        hull1.append(points1[hullIndex[i][0]])
        hull2.append(points2[hullIndex[i][0]])
    # 为图片2计算一个面罩，把原先图片2中的脸盖住
    hull8U = []
    for i in range(0, len(hull2)):
        hull8U.append((hull2[i][0], hull2[i][1]))
    mask = np.zeros(img2.shape, dtype=img2.dtype)
    cv2.fillConvexPoly(mask, np.int32(hull8U), (255, 255, 255))
    # 找到面心
    m = cv2.moments(mask[:, :, 1])
    center = (int(m['m10'] / m['m00']), int(m['m01'] / m['m00']))
    # 把图2中的脸狄洛尼三角剖分
    sizeImg2 = img2.shape
    rect = (0, 0, sizeImg2[1], sizeImg2[0])
    dt = calculateDelaunayTriangles(rect, hull2)
    # 如果无法划分，退出程序
    if len(dt) == 0:
        quit()
    # 储存分出的一个个三角形
    tris1 = []
    tris2 = []
    for i in range(0, len(dt)):
        tri1 = []
        tri2 = []
        for j in range(0, 3):
            tri1.append(hull1[dt[i][j]])
            tri2.append(hull2[dt[i][j]])
            tris1.append(tri1)
            tris2.append(tri2)
    # 将这图1的脸上的一个个小三角形通过仿射变换投影到图2的脸上
    for i in range(0, len(tris1)):
        warpTriangle(img1, img1Warped, tris1[i], tris2[i])
    # 把图1的脸无缝缝合进图2
    output = cv2.seamlessClone(np.uint8(img1Warped), img2, mask, center, cv2.NORMAL_CLONE)
    # 输出结果
    cv2.imwrite(output_filename, output)
    output_filename = output_filename.replace('//', '\\')
    # output_filename = os.path.join(os.getcwd(), output_filename)
    return output_filename

def search_form(request):
    return render(request, 'main.html')

def upload(request):
    myFile = None
    strr = 'start'
    if request.method == 'GET':
        return render(request, 'main.html')
    if request.method == "POST":
        myFile = request.FILES.get("myFile", None)
        if myFile != None:
            # 传入的图片我只改了，一张图片的那个函数
            # 两张图片的需要你改
            # 还有就是，两个函数的返回的图片
            # 返回值传回前端
            # print(os.getcwd())
            if not os.path.exists('image'):
                os.mkdir('image')
            with open(os.path.join(os.getcwd(), 'image', myFile.name), 'wb') as fw:
                # 分块读取
                for ck in myFile.chunks():
                    fw.write(ck)

            strr = 'image//'+myFile.name
            strr = run_face_swap(strr, 'image//panda.jpg', 'image//result3.jpg')

            # text = {}
            # text['test'] = 'yes'
            # return HttpResponse("Yes")
        else:
            text = {}
            text['test'] = 'noo'
            return HttpResponse("NOOO")
    text = {}
    text['test'] = strr
    return render(request, 'main.html', text)

# if __name__ == "__main__":
#     # 普通模式
#     # 单张照片
#     # run_face_swap('','','images//result.jpg')
#     # 两张照片
#     run_face_swap('images//example.jpg', 'images//blackguy.jpg', 'images//result.jpg')
#
#     # 卷积神经网络模式
#     # 单张照片
#     # run_face_swap('images//tongtong.jpg','','images//result.jpg','cnn')
#     # 两张照片
#     # run_face_swap('images//example.jpg','images//blackguy.jpg','images//result.jpg','cnn')