#coding:utf-8
import os
def get_curdir():
    return os.getcwd()

#测试代码不能直接写，需要写在如下结构中
if __name__=="_main_":  #_name_是Python内置的1个专有变量
    print(get_curdir())
    print(os.getcwd())
