from PIL import Image
import pytesseract
from config.pathes import IMAGE_PATH, FRAME_PATH


def verifyCode(driver,type,value):
    '''
    :param driver: 实例化webdriver
    :param type: id,class,name,css,xpath...
    :param value: 元素
    :return: 识别二维码字符串
    '''
    driver.save_screenshot(IMAGE_PATH)  #截取当前网页
    location = driver.location(type,value)  #获取验证码x,y轴坐标
    size = driver.size(type,value)  #获取验证码的长宽
    coderange = (int(location['x']),int(location['y']),int(location['x']+ size['width']),
               int(location['y']+size['height'])) #截取位置坐标
    i = Image.open(IMAGE_PATH)
    img1 = i.crop(coderange)
    img1.save(IMAGE_PATH)
    i2 = Image.open(IMAGE_PATH)
    imgry = i2.convert('L')  #灰度
    threshold = 100
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)
    i3 = imgry.point(table, '1')
    # sharpness = ImageEnhance.Contrast(i3)  # 对比度增强
    # i3 = sharpness.enhance(3.0)
    i3.save(FRAME_PATH)
    i4 = Image.open(FRAME_PATH)
    data = i4.getdata()#去掉多余的黑点
    w, h = i4.size
    black_point = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            mid_pixel = data[w * y + x]
            if mid_pixel < 50:
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                # 判断上下左右的黑色像素点总个数
                if top_pixel < 10:
                    black_point += 1
                if left_pixel < 10:
                    black_point += 1
                if down_pixel < 10:
                    black_point += 1
                if right_pixel < 10:
                    black_point += 1
                if black_point < 1:
                    i4.putpixel((x, y), 255)
                black_point = 0
    for x in range(1, w - 1):#去子上的白点
        for y in range(1, h - 1):
            if x < 2 or y < 2:
                i4.putpixel((x - 1, y - 1), 255)
            if x > w - 3 or y > h - 3:
                i4.putpixel((x + 1, y + 1), 255)
    i4.save(FRAME_PATH)
    i5 = Image.open(FRAME_PATH)
    text = pytesseract.image_to_string(i5).strip() #识别验证码
    return  text

