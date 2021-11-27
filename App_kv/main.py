import kivy
from kivy.app import App 
kivy.require('1.9.0')
from kivy.uix.checkbox import CheckBox 
from kivy.uix.dropdown  import DropDown
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button  import Button
from kivy.uix.spinner  import Spinner, SpinnerOption
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, BooleanProperty
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from os.path import dirname
from os.path import join
import get_feature
import get_region




fontName = './HMKMRHD.ttf'
kv_file = 'test11.kv'
Builder.load_file(join(dirname(__file__), kv_file)) 

Window.size = (600, 800)

class WindowManager(ScreenManager):
    pass

class MySpinnerOption(SpinnerOption):
    def __init__(self, **kwargs):
        self.font_name = fontName
        super(MySpinnerOption, self).__init__(**kwargs)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
    
    values_dict = {'강원':['강릉시','고성군','동해시','삼척시','속초시','양구군','양양군','영월군','원주시','인제군','정선군','철원군','춘천시','태백시','평창군','홍천군','화천군','횡성군'],
    '경기':['가평군','고양시','과천시','광명시','광주시','구리시','군포시','김포시','남양주시','동두천시','부천시','성남시','수원시','시흥시','안산시','안성시','안양시','양주시','양평군','여주시','연천군','오산시','용인시','의왕시','의정부시','이천시','파주시','평택시','포천시','하남시','화성시'],
    '경남':['거제시','거창군','고성군','김해시','남해군','마산시','밀양시','사천시','산청군','양산시','의령군','진주시','진해시','창녕군','창원시','통영시','하동군','함안군','함양군','합천군'],
    '경북':['경산시','경주시','고령군','구미시','군위군','김천시','봉화군','상주시','성주군','안동시','영덕군','영양군','영주시','영천시','예천군','을릉도','을진군','의성군','청도군','청송군','칠곡군','포항시'],
    '광주':['광산구','남구','동구','북구','서구'],
    '대구':['남구','달서구','달성군','동구','북구','서구','수성구','중구'],
    '대전':['대덕구','동구','서구','유성구','중구'],
    '부산':['강서구','금정구','기장군','남구','동구','동래구','부산진구','북구','사상구','사하구','서구','수영구','연제구','영도구','중구','해운대구'],
    '서울':['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구'],
    '세종':['세종시'],
    '울산':['남구','동구','북구','울주군','중구'],
    '인천':['강화군','계양구','남동구','동구','미추홀구','부평구','서구','연수구','옹진군','중구'],
    '전남':['강진군','고흥군','곡성군','광양시','구례군','나주시','담양군','목포시','무안군','보성군','순천시','신안군','여수시','영광군','영암군','완도군','장성군','진도군','함평군','해남군','화순군'],
    '전북':['고창군','군산시','김제시','남원시','무주군','부안군','순창군','완주군','익산시','임실군','장수군','전주시','정읍시','진안군'],
    '제주도':['서귀포시','제주시'],
    '충남':['계룡시','공주시','금산군','논산시','당진시','보령시','부여군','서산시','서천군','아산시','연기군','예산군','천안시','청양군','태안군','홍성군'],
    '충북':['괴산군','단양군','보은군','영동군','옥천군','음성군','제천시','증편군','진천군','청주시','충주시']}
    
    sub_values = ListProperty()
    
    #지역 keyword가져오기 / DB에서 지역에 해당하는 main keyword값들 가져올 예정..
    def getKeyword(self):
        sm = self.manager
        maint = self.ids.main_drop.text
        subt = self.ids.sub_drop.text
        features = get_feature.get_f(maint + '_' + subt)
        sm.get_screen('result').ids.key1.text = features[0]
        sm.get_screen('result').ids.key2.text = features[1]
        sm.get_screen('result').ids.key3.text = features[2]
        sm.get_screen('result').ids.key4.text = features[3]
        sm.get_screen('result').ids.key5.text = features[4]
        sm.get_screen('result').ids.key6.text = features[5]
        sm.get_screen('result').ids.key7.text = features[6]
        sm.get_screen('result').ids.key8.text = features[7]
        sm.get_screen('result').ids.key9.text = features[8]
        sm.get_screen('result').ids.key10.text = features[9]

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
        sm = self.manager    
        
    
    key_values=ListProperty()
    region = ListProperty()
    popup = Popup(title ='Alert!!', content=Label(text='최소한 하나의 키워드를 선택해 주세요!',font_name = fontName),
size_hint=(None, None), size=(400, 200))

    #screen change
    def convert2m(self):
        sm = self.manager
        sm.current = 'main'
        

    def convert2t(self,text):
        sm = self.manager
        sm.get_screen('third').ids.CityState2.text = text
        sm.current = 'third'

    def get_keyval(self):
        sm = self.manager
        
        self.key_values.append(sm.get_screen('main').ids.main_drop.text + '_' + sm.get_screen('main').ids.sub_drop.text)
        if self.ids.chk_key1.active:
            self.key_values.append(self.ids.key1.text)
        if self.ids.chk_key2.active:
            self.key_values.append(self.ids.key2.text)
        if self.ids.chk_key3.active:
            self.key_values.append(self.ids.key3.text)
        if self.ids.chk_key4.active:
            self.key_values.append(self.ids.key4.text)
        if self.ids.chk_key5.active:
            self.key_values.append(self.ids.key5.text)
        if self.ids.chk_key6.active:
            self.key_values.append(self.ids.key6.text)
        if self.ids.chk_key7.active:
            self.key_values.append(self.ids.key7.text)
        if self.ids.chk_key8.active:
            self.key_values.append(self.ids.key8.text)
        if self.ids.chk_key9.active:
            self.key_values.append(self.ids.key9.text)
        if self.ids.chk_key10.active:
            self.key_values.append(self.ids.key10.text)
        
        if len(self.key_values)==1:
            self.popup.open()
        else:
            Region = get_region.get_r(self.key_values)
            self.ids.recom.disabled = False
            self.ids.recom1.text=Region[0]
            self.ids.recom2.text=Region[1]
            self.ids.recom3.text=Region[2]
            self.ids.recom4.text=Region[3]
            self.ids.recom5.text=Region[4]

            #추천지역에 값 할당해준후 배열 초기화
            Region.clear()
            self.key_values.clear()
        


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