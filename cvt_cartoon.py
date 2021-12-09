import cv2


def cvt_cartoon(img, num_down_up=2, num_bilateral=7, blur_size=7, blockSize=9, adaptive_C=2):
    # 1. Apply bilateral filters to reduce the image's color palette
    img_color = img
    for _ in range(num_down_up):
        img_color = cv2.pyrDown(img_color)
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)
    for _ in range(num_down_up):
        img_color = cv2.pyrUp(img_color)
    # 2. Convert original color image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 3. Apply intermediate blur to reduce image noise in grayscale images
    img_blur = cv2.medianBlur(img_gray, blur_size)
    # 4. Create edge masks from grayscale images using adaptive thresholding
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=blockSize,
                                     C=adaptive_C)
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    # 5. Merge the color image in step 1 with the edge mask in step 4
    img_color.resize(img.shape)
    result = cv2.bitwise_and(img_color, img_edge)
    return result


if __name__ == '__main__':
    import os

    for name in os.listdir('test_images'):
        src = cv2.imread(os.path.join('test_images', name))
        dst = cvt_cartoon(src)
        cv2.imshow('src', src)
        cv2.imshow('dst', dst)
        cv2.waitKey()
        cv2.destroyAllWindows()
