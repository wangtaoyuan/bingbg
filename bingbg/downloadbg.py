# encoding:utf-8
'''
Created on 2017年8月16日
对bing主页的审查
1、审查元素中查找backgroudimage
@author: wangtaoyuan
'''
import urllib2
# import urllib
import requests
import time
import os
import sys
import win32api, win32con,win32gui
url = 'http://cn.bing.com'
#伪装头信息
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'
headers = {'User-Agent':user_agent}
request = urllib2.Request(url, headers)
# request = urllib.request.Request(url)
try:
    content = urllib2.urlopen(url).read()#会抛urllib2.URLError异常
#     content = urllib.request.urlopen(url).read()
except urllib2.URLError, e:
# except urllib.error.URLError as e:
    win32api.MessageBox(0, u"网络连接异常", u"错误提示", win32con.MB_OK)


# head = content.find(r'g_img=') + len(r'g_img={url: "')
# tail = content.find(r'.jpg') + 4
head = content.find(r'g_img=') + len(r'g_img={url: "')
tail = content.find(r'.jpg') + 4
img_url = url + content[head: tail]#对content进行切片取图片的url
time.sleep(1)
print img_url


def downloadpic(image_url, save_path):#下载壁纸函数
    r = requests.get(image_url)
    with open(save_path, "wb") as code:
        code.write(r.content)
        
tday = time.strftime('%Y%m%d',time.localtime()) 

if os.path.isdir(r'E:\background') == False :#创建文件夹，如果不存在
    os.makedirs( r'E:\background')

if (os.path.exists(r'E:\\background\\bing%s.jpg' % tday) ) == False:
    save_path = 'E:\\background\\bing%s.jpg' % tday

    downloadpic(img_url, save_path)#下载壁纸

    win32api.MessageBox(0, u"bing壁纸下载完成\n已下载至E:\\background", u"提示", win32con.MB_OK)
else:
    win32api.MessageBox(0, u"已存在", u"存在", win32con.MB_OK)


#设置壁纸
def set_wallpaper_from_bmp(save_path):
    #.打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    #最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    #最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    #刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,save_path, win32con.SPIF_SENDWININICHANGE)

set_wallpaper_from_bmp(save_path)