import kivy
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.dropdown  import DropDown
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button  import Button
from kivy.uix.spinner  import Spinner
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, BooleanProperty
from kivy.properties import StringProperty
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

keywords = [['키워드11', '키워드22', '키워드33', '키워드44'],
        ['키워드A', '키워드B', '키워드C', '키워드D']]

class WindowManager(ScreenManager):
    pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
    #font_name = fontName
    
    values_dict = {'서울':['종로구', '중구', '용산구', '성동구', '광진구', '동대문구','중랑구','성북구','강북구','도봉구','노원구','은평구','서대문구','마포구','양천구','강서구','구로구','금천구','영등포구','동작구','관악구','서초구','강남구','송파구','강동구'],
              '부산':['중구', '서구', '동구']}
    
    sub_values = ListProperty()
    
    #지역 keyword가져오기
    def getKeyword(self):
        sm = self.manager
        maint = self.ids.main_drop.text
        subt = self.ids.sub_drop.text
        if maint + '_' +subt == '서울_종로구':
            sm.get_screen('result').ids.key1.text = keywords[0][0]
            sm.get_screen('result').ids.key2.text = keywords[0][1]
            sm.get_screen('result').ids.key3.text = keywords[0][2]
            sm.get_screen('result').ids.key4.text = keywords[0][3]

    #지역을 모두 선택했는지 확인(안했을시 알림창 팝업)/ 선택한 지역에 해당하는 키워드를 DB로부터 가져옴
    def convert2r(self):
        sm = self.manager
        popup = Popup(title ='Alert!!', content=Label(text='지역을 선택해주세요!',font_name = fontName),
size_hint=(None, None), size=(400, 200))
        if self.ids.sub_drop.text =='시/군/구 선택' or self.ids.main_drop.text == self.ids.sub_drop.text:
            popup.open()
        else:
            self.getKeyword()
            sm.current = 'result'
    
    #종료
    def onExit(self):
        App.get_running_app().stop()

    #maindrop과 subdrop
    def values_update(self,text):
        self.sub_values = self.values_dict[text]
        if text != '시/군/구 선택' :
            self.ids.sub_drop.text = text
         
        
            

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)

    #screen change
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