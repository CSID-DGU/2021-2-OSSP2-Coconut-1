import kivy
kivy.require('1.0.7')
from os.path import dirname
from os.path import join
from kivy.lang import Builder
from kivy.app import App

kv_file = 'test.kv'
Builder.load_file(join(dirname(__file__), kv_file)) 

class Test1App(App):
    pass


if __name__ == '__main__':
    Test1App().run()