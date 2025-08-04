# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:43:49 2020

@author: Lenovo
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(5, 2, 1)
            d = 30.
            Ellipse(pos=(touch.x - d / 3, touch.y - d / 5), size=(d, d))


class MyPaintApp(App):

    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()