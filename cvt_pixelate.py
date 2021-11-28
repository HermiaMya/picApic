import cv2


def _two_element_tuple(int_or_tuple):
    if isinstance(int_or_tuple, (list, tuple)):
        if len(int_or_tuple) != 2:
            raise ValueError('Must be a tuple or list with 2 elements: {}'.format(int_or_tuple))
        return int(int_or_tuple[0]), int(int_or_tuple[1])
    if isinstance(int_or_tuple, int) and int_or_tuple > 0:
        return int(int_or_tuple), int(int_or_tuple)
    raise ValueError('Must be a positive int, a tuple or list with 2 elements')


def cvt_pixelate(img, pixel_size=1, use_radio=False, radio=None):
    img_height, img_width = img.shape[:2]
    if use_radio:
        if not radio or not hasattr(radio, '__len__') or len(radio) != 2:
            raise ValueError('radio must be a tuple with 2 radio number')
        pixel_width = img_width * radio[0]
        pixel_height = img_height * radio[1]
    else:
        pixel_width, pixel_height = _two_element_tuple(pixel_size)
    assert img_width >= pixel_width and img_height >= pixel_height, 'size of image should be larger than pixel'

    tmp_width = int(round(img_width / pixel_width))
    tmp_height = int(round(img_height / pixel_height))
    # Resize smoothly down to (tmp_width, tmp_height) pixels
    tmp = cv2.resize(img, (tmp_width, tmp_height), interpolation=cv2.INTER_LINEAR)
    # Scale back up using NEAREST to original size
    result = cv2.resize(tmp, (img_width, img_height), interpolation=cv2.INTER_NEAREST)
    return result


if __name__ == '__main__':
    import os

    for name in os.listdir('test_images'):
        src = cv2.imread(os.path.join('test_images', name))
        dst = cvt_pixelate(src, use_radio=True, radio=(0.01, 0.01))
        cv2.imshow('src', src)
        cv2.imshow('dst', dst)
        cv2.waitKey()
        cv2.destroyAllWindows()
