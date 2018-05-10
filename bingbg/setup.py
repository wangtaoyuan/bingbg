# encoding:utf-8
'''
Created on 2017年8月18日

@author: wangtaoyuan
'''
from distutils.core import setup
import py2exe
import os
import sys

path = os.path.abspath(os.path.dirname(sys.argv[0]))



setup(
    console=['downloadbg.py'],
    windows=[{"script":"downloadbg.py","icon_resources":[(1,path + r"\icon\bingbg.ico")]}]
      )