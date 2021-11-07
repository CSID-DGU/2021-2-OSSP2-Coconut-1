import kivy
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.dropdown  import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button  import Button
from kivy.uix.spinner  import Spinner
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from os.path import dirname
from os.path import join

fontName = './HMKMRHD.ttf'
kv_file = 'test11.kv'
Builder.load_file(join(dirname(__file__), kv_file)) 


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

    resource_value = ["mountain", "ocean", "museum"]
    
    def convert2m(self):
        sm = self.manager
        sm.current = 'main'

    def convert2t(self):
        sm = self.manager
        sm.current = 'third'


class ThirdScreen(Screen):
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