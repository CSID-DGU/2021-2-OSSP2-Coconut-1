import kivy
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.dropdown  import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button  import Button
from kivy.uix.spinner  import Spinner
from kivy.properties import ListProperty, BooleanProperty
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from os.path import dirname
from os.path import join

fontName = './HMKMRHD.ttf'
kv_file = 'test11.kv'
Builder.load_file(join(dirname(__file__), kv_file)) 

Window.size = (600, 700)

items = [
        {"text" : "StateA", "seleceted": 'normal', "input_data":["key1","key2","key3"]},
        {"text" : "StateB", "seleceted": 'normal', "input_data":["keyA","keyB","keyC"]},
        {"text" : "StateC", "seleceted": 'normal', "input_data":["keyD","keyE","keyF"]},
    ]


class windowManager(ScreenManager):
    pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    values_dict = {'City1':['StateA', 'StateB', 'StateC'],
              'City2':['StateD', 'StateE', 'StateF']}

    sub_values = ListProperty()

    def convert2r(self):
        sm = self.manager
        sm.current = 'result'

    def onExit(self):
        App.get_running_app().stop()
    
    def values_update(self,text):
        self.sub_values = self.values_dict[text]
        if text != 'Select City':
            self.ids.sub_drop.text = text
            

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        
    

    #def getState(self):
    #    sm = self.manager
    #    t1 = sm.get_screen('MainScreen').ids.sub_drop.text
    #    return t1
    
    #screen change
    def convert2m(self):
        sm = self.manager
        sm.current = 'main'

    def convert2t(self):
        sm = self.manager
        sm.current = 'third'


class ThirdScreen(Screen):
    
    keyword1 = ObjectProperty(None)
    keyword2 = ObjectProperty(None)
    keyword3 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)

    def convert2m(self):
        sm = self.manager
        sm.current = 'main'

    def convert2r(self):
        sm = self.manager
        sm.current = 'result'


sm = ScreenManager() # transition = NoTransition())
sm.add_widget(MainScreen())
sm.add_widget(ResultScreen())
sm.add_widget(ThirdScreen())
       
class MainApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    MainApp().run()