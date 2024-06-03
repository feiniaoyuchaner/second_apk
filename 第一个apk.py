# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:14:22 2024

@author: runmu
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class SimpleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Press the button')
        button = Button(text='Click Me', on_press=self.on_button_click)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def on_button_click(self, instance):
        self.label.text = 'Hello, World!'

if __name__ == '__main__':
    SimpleApp().run()
