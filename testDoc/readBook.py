#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2022-04-12 18:49:46
LastEditTime: 2022-05-10 23:02:29
LastEditors: 560130
Description: 一个闹铃,用来练习阅读。“3-2-1”方法;输入第一次用时，自动开始第二次和第三次计时
FilePath: /pythonitem/testDoc/readBook.py
'''

from pydub import AudioSegment  # 导入此模块实现声音播放功能
from pydub.playback import play
import time  # 导入此模块，获取当前时间


class Alarm:
    def __init__(self) -> None:
        '''
        description:初始化闹铃，保存必要参数 
        param {*}
        return {*}
        '''
        #"/home/gree/wfDocument/gree/wfDocument/其他/练习项目/PythonItem/testDoc/bensound-ukulele.mp3",
        self.sound1 = AudioSegment.from_mp3(
            "/home/gree/MyDocument/MyWorkSpace/pythonitem/testDoc/bensound-ukulele.mp3")
        print("-----------",self.sound1)
        pass

    def set_time(self):
        '''
        description:设定时长,设定“3”的时长,自动生产“2”和“1”
        param {无}
        return {三个时长}
        '''
        pass

    def start_timing(self):
        '''
        description: 开始计时
        param {*}
        return {*}
        '''
        pass

    def bell(self):
        '''
        description:到时间响铃 
        param {开始标志}
        return {无}
        '''
        while True:
            try:
                play(self.sound1)
            except KeyboardInterrupt:
                print("Stopping bell")
                break

    def stop_bell(self):
        '''
        description:可以手动停止闹铃 
        param {停止标志}
        return {无}
        '''
        pass


if __name__ == "__main__":
    a = Alarm()
    print(a.sound1)
    a.bell()