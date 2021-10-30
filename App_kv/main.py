# Program to Show how to create a switch 
# import kivy module    
import kivy  
       
# base Class of your App inherits from the App class.    
# app:always refers to the instance of your application   
from kivy.app import App 
     
# this restrict the kivy version i.e  
# below this kivy version you cannot  
# use the app or software  
kivy.require('1.9.0') 
    
# drop-down menu is a list of items that
# appear whenever a piece of text or a
# button is clicked.
# To use drop down you must have ti import it
from kivy.uix.dropdown  import DropDown
    
# module consists the floatlayout  
# to work with FloatLayout first  
# you have to import it  
from kivy.uix.floatlayout import FloatLayout
  
# The Button is a Label with associated actions that
# are triggered when the button is pressed (
# or released after a click / touch).
from kivy.uix.button  import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from os.path import dirname
from os.path import join
  
class CityDropDown(DropDown):
    pass

class StateDropDown(DropDown):
    pass

class NoneDropDown(DropDown):
    pass

class SelectScreen(Screen):
    def convert2r(self):
        sm = self.manager
        sm.current = 'result'
        return

class ResultScreen(Screen):
    def convert2s(self):
        sm = self.manager
        sm.current = 'select'
        return

class WindowManager(ScreenManager):
    pass


fontName = './HMKMRHD.ttf'
kv_file = 'test11.kv'
Builder.load_file(join(dirname(__file__), kv_file))   
   
class windowManager(ScreenManager):
    pass

class MainScreen(Screen):
    pass
    
class ResultScreen(Screen):
    pass
       
class DropdownDemo(FloatLayout):
    '''The code of the application itself.''' 
    
    sm = ScreenManager() 

    def __init__(sm, **kwargs):
          
        '''The button at the opening of the window is created here,
        not in kv
        ''' 
        super(DropdownDemo, sm).__init__(**kwargs)
 

        # Creating a self widget botton
        sm.mainbutton = Button(text ='특별시/광역시',
                                 size_hint=(0.3, 0.1),pos_hint={'center_x': 0.2, 'center_y': 0.9}, font_name = fontName)
        sm.mainbutton2 = Button(text ='도시를 먼저 선택하세요',
                                 size_hint=(0.3, 0.1),pos_hint={'center_x': 0.8, 'center_y': 0.9}, font_name = fontName)
        
        sm.add_widget(SelectScreen(name='select'))
        sm.add_widget(ResultScreen(name='Result'))
        sm.dropdown()



    def dropdown(sm):
        # Added button to FloatLayout so inherits this class 
        sm.dropdown1 = CityDropDown()
        sm.dropdown2 = NoneDropDown()
        sm.add_widget(sm.mainbutton)
        sm.add_widget(sm.mainbutton2)
        # Adding actions 
        # If click 
        sm.mainbutton.bind(on_release = sm.dropdown1.open)
        sm.dropdown1.bind(on_select = lambda\
                           instance, x: setattr(sm.mainbutton, 'text', x))

        sm.mainbutton2.bind(on_release = sm.dropdown2.open)
        sm.dropdown2.bind(on_select = lambda\
                           instance, x: setattr(sm.mainbutton2, 'text', x))
        return sm



class MainApp(App):
    '''The build function returns root,
    here root = DropdownDemo ().
    root can only be called in the kv file.
    ''' 
    def build(self):
        return DropdownDemo()

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(SelectScreen(name='select'))
        sm.add_widget(ResultScreen(name='result'))
        return sm  
   
if __name__ == '__main__':
    MainApp().run()
    #TestApp().run()