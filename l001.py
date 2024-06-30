# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
# @Time    : 2024/6/29 16:39
# @Author  : Mark Deng
# @Email   : 1114026501@qq.com
# @File    : l001
# @Software: PyCharm


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from functools import partial
from kivy.core.text import LabelBase
# C:\Windows\Fonts\STSONG.TTF
# 注册位于 C:\Windows\Fonts\ 的宋体
LabelBase.register(name='STSong', fn_regular=r'C:/Windows/Fonts/STSONG.TTF')


class EffectButton(Button):
    def __init__(self, **kwargs):
        super(EffectButton, self).__init__(**kwargs)
        # 设置默认背景颜色
        self.default_background_color = self.background_color

    def on_press(self):
        # 按下时改变背景颜色
        self.background_color = (1, 0, 0, 1)  # 红色

    def on_release(self):
        # 弹起时恢复默认背景颜色
        self.background_color = self.default_background_color


class TestApp(App):
    def build(self):
        layout = FloatLayout()

        rf_btn = Button(text='刷新',
                        on_press=partial(self.say_hello),
                        size_hint=(0.2, 0.1),  # 控制按钮大小
                        pos_hint={'center_x': 0.3, 'center_y': 0.5},  # 控制按钮位置
                        font_name='STSong',
                        font_size=20)

        finish_btn = Button(text='完成',
                            on_press=partial(self.say_hello),
                            size_hint=(0.2, 0.1),  # 控制按钮大小
                            pos_hint={'center_x': 0.6, 'center_y': 0.5},  # 控制按钮位置
                            font_name='STSong',
                            font_size=20)

        # 创建关闭应用的按钮
        close_btn = Button(text='关闭这个应用',
                           on_press=self.close_app,
                           size_hint=(0.2, 0.1),  # 控制按钮大小
                           pos_hint={'right': 1, 'y': 0},  # 控制按钮位置在右下角
                           font_name='STSong',
                           background_color=(1, 0, 0, 1),
                           font_size=20)

        # 将按钮添加到布局中
        layout.add_widget(rf_btn)
        layout.add_widget(finish_btn)
        layout.add_widget(close_btn)

        return layout

    @staticmethod
    def say_hello(*_):
        # 打印问候语到控制台
        print('Hello, world!')

    def close_app(self, _):
        # 停止应用
        self.stop()


if __name__ == '__main__':
    TestApp().run()
