from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, DictProperty
from kivy.lang import Builder
from os.path import dirname
from os.path import join


kv_file = 'test.kv'
Builder.load_file(join(dirname(__file__), kv_file)) 

class windowManager(ScreenManager):
    pass

class MainScreen(Screen):
    values_dict = {'Group1':['Screen1', 'Screen2'],
              'Group2':['Screen3', 'Screen4']}

    sub_values = ListProperty()

    def values_update(self,text):
        self.sub_values = self.values_dict[text]
        if text != 'Select group type':
            self.ids.sub_drop.text = 'select ' + text + ' screen'
            return 'select ' + text + ' screen'

    def open_screen(self, text):        
        if text != 'select ' + self.ids.main_drop.text + ' screen':
            sm = self.manager
            sm.current = text

class Screen1(Screen):    
    def open_screen(self):        
        sm = self.manager
        sm.current = 'main'

class Screen2(Screen):
    def open_screen(self):        
        sm = self.manager
        sm.current = 'main'

class Screen3(Screen):
    def open_screen(self):        
        sm = self.manager
        sm.current = 'main'

class Screen4(Screen):
    def open_screen(self):        
        sm = self.manager
        sm.current = 'main'

class appln(App):                
    def build(self):    
        return windowManager()            

if __name__=="__main__":
    appln().run()