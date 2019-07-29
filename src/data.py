#！ python 3.6
# Create Date: 2019-07-29
# Author: Scc_hy 
# Function: 画图所需文件

# 加载包 
import random 
import numpy as np  
import time 
import cv2 
import copy 


__doc__ = """
split to three class or function 
1- get_data function 获取随机列表，用于排序  
2- get_time_info class 用于记录排序的时间
3- get_figure2draw class 画图
"""


def get_data(Length_of_list):
    """
    获取随机列表，用于排序
    :param: Length_of_list int 随机列表的长度
    """
    data = list(range(Length_of_list))
    random.shuffle(data)
    return data


class get_time_info():
    """
    用于记录排序的时间
    """
    def start_timer(self):
        """
        设置start_flg  
        开始计时，获取开始时间
        """
        self.start_flag = True 
        self.start = time.time() 
        return self.start 

    def stop_timer(self):
        """
        设置start_flg  
        停止计时，输出运行时间
        """
        self.start_flag = False 
        return self.time

    def get_time(self):
        """
        依据start_flg  
        计算出运行时间
        """
        if self.start_flag:
            self.time = time.time() - self.start 
        return self.time

    
class get_figure2draw():
    """
    1- 初始化OpenCV图像: GetColor & get_figure
    2- 交换位置并画图： swap
    3- 重新设置(交换位置后)条形图的高和颜色： _set_figure
    4- 画出图形： Visualize 
    5- 突出交换的条形图： Mark

    """
    WHITE = (255, 255, 255)
    RED = (0, 0, 255)
    BLACK = (0, 0, 0)
    YELLOW = (0, 127, 255)
    MAX_IM_SIZE = 500
    gt = get_time_info()

    def __init__(self, data, sort_title = 'Sort_type' 
                     , time_interval = 1):
        self.length = len(data) 
        self.data = data
        self.sort_title = sort_title
        self.set_time_interval(time_interval)

        ## 初始化变量
        self.start = self.gt.start_timer()
        self.get_figure()



    def set_time_interval(self, time_interval):
        """
        设置 cv2.waitKey( time_interval )
        """
        self.time_interval = time_interval


    def GetColor(self, val, TOTAL):
        """
        根据列表的值的大小上 由浅到深的颜色
        :param: val  数组对应值 data[idx] (排序的数)
        :param: TOTAL  
        """
        # 获取颜色
        return (120 + val * 255 // (2 * TOTAL), 255 - val * 255 // (2 * TOTAL), 0)


    def get_figure(self):
        """
        设置初始图像  
        给条形图上色

        try：
            data = get_data(10)
            data = list(range(10))
            _bar_width = 5
            g2dr = get_figure2draw(data)
            g2dr.get_figure()
            cv2.imshow('data list' , g2dr.figure)
            cv2.waitKey(0)
        """
        _bar_width = 5 
        self._bar_width = _bar_width
        figure = np.full((self.length * _bar_width, self.length * _bar_width, 3), 255, dtype = np.uint8)
        
        size = _bar_width * self.length
        self.im_size = size if size < self.MAX_IM_SIZE else self.MAX_IM_SIZE

        for i in range(self.length):
            val = self.data[i]
            ## 上色 
            figure[-1 - val * _bar_width :,
                   i * _bar_width:i * _bar_width+_bar_width] = self.GetColor(val, self.length)
        
        self.figure = figure


    def Mark(self, img, marks, color):
        """
        设置颜色  
        突出调换的列  
        :param: img  figure.copy() 
            figure：  
            # global values Length * _bar_width 维度, Length * _bar_width 行, 3列  
            # figure = np.full((20 * _bar_width, 20 * _bar_width, 3), 255, dtype = np.uint8)
        :param: marks  
        :param: color   要设置的颜色 
            WHITE = (255, 255, 255)
            RED = (0, 0, 255)
            BLACK = (0, 0, 0)
            YELLOW = (0, 127, 255)
        data[idx] global value
        """
        for idx in marks:
            min_col = idx * self._bar_width
            max_col = min_col + self._bar_width
            min_row = -1- self.data[idx] * self._bar_width
            ## 条形图位置
            img[min_row:, min_col:max_col] = color  


    def _set_figure(self, idx, val):
        """
        重新设置(交换位置后)条形图的高和颜色 
        :param: idx int 数组index  
        :param: val  数组对应值 data[idx]
        """
        
        # 锁定条形图两边位置
        min_col = idx * self._bar_width 
        max_col = min_col + self._bar_width 
        min_row = -1 - val *self._bar_width 
        # 100维度 100行 3列
        self.figure[:, min_col:max_col] = self.WHITE
        self.figure[min_row:, min_col:max_col] = self.GetColor(val, self.length)


    def Visualize(self, mark1 = None, mark2 = None):
        """
        显示图像   
        figure：  
            # global values Length * _bar_width 维度, Length * _bar_width 行, 3列  
            # figure = np.full((20 * _bar_width, 20 * _bar_width, 3), 255, dtype = np.uint8)  
        im_size：  
            # size = _bar_width * length 
            # im_size = size if size < MAX_IM_SIZE else MAX_IM_SIZE
            # MAX_IM_SIZE = 500
        
        """
        img = self.figure.copy()
        if mark2:
            self.Mark(img, mark2, self.YELLOW)
        if mark1:
            self.Mark(img, mark1, self.RED) # 长的置为红色并向后移动

        img = cv2.resize(img, (self.im_size, self.im_size))

        # 暂时先不管 
        self.time = self.gt.get_time()
        cv2.putText(img, "{} Time: {:.2f}s".format(self.sort_title, self.time)
                    ,(20, 20), cv2.FONT_HERSHEY_PLAIN, 1, self.YELLOW, 1)
     
        cv2.imshow(self.sort_title , img)
        """
        waitKey的功能是不断刷新图像，时间频率为delay ,单位ms 
        返回值为当前键盘按键值 
        1- 是在一个给定的时间内(单位ms)等待用户按键触发
        如果用户没有按下键盘，则接着等待(循环)
        waitKey(0) 表示程序无线等待用户的按键事件
        一般在imgshow的时候，如果设置waitKey(0),代表按任意键继续
        2- 显示视频时，延迟时间需要设置为 大于0的参数
        """
        cv2.waitKey(self.time_interval)

    ## 排序余姚用到的位置处理函数
    def swap(self, idx1, idx2):
        """
        交换 idx1, idx2 的值
        并画刷新图 
        """
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        # 交换位置 重新设置(交换位置后)条形图的高和颜色
        self._set_figure(idx1, self.data[idx1])
        self._set_figure(idx2, self.data[idx2])
        self.Visualize((idx1, idx2))

    def set_val(self, idx, val):
        """
        :param: idx 位置   
        :param: val 值  
        data[idx] = val 
        """
        self.data[idx] = val 
        self._set_figure(idx, val)
        self.Visualize((idx,))
