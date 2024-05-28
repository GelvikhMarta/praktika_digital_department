from kivy.uix.codeinput import TextInput
from kivy.uix.actionbar import Label
from kivy.uix.actionbar import Button
from kivy.uix.actionbar import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.pickers import MDModalDatePicker
from kivy.uix.actionbar import Spinner
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
import scripts 


class MainMenu(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.aboba = scripts.DatabaseService()
        self.baba = ''
        boxlay = BoxLayout(orientation='vertical',spacing = 30, padding = 15)
        label = Label(
            text = 'ДОБРО ПОЖАЛОВАТЬ В БОЙЦОВСКИЙ КЛУБ!'
        )
        boxlay.add_widget(label)
        button = Button(
            text = 'Календарь',
            size_hint_x=.25,
            size_hint_y=.25,
            pos_hint = {'center_x': .5,'center_y': .5},
            on_release = self.show_modal_date_picker,
        )
        boxlay.add_widget(button)
        bitton = Button(
            text = 'Упражнения',
            size_hint_x=.25,
            size_hint_y=.25,
            pos_hint = {'center_x': .5,'center_y': .5},
            on_release = self._on_press_button_new_pasword
        )
        boxlay.add_widget(bitton)
        self.add_widget(boxlay)

    def on_ok(self, instance_date_picker):
        instance_date_picker.dismiss()
        global baba
        baba = instance_date_picker.set_text_full_date()
        if self.aboba.find_train(baba) == 0:
            self.manager.transition.direction = 'right'
            self.manager.current = 'Train'
        else:
            self.manager.transition.direction = 'right'
            self.manager.current = 'Train'
        
    def _on_press_button_new_pasword(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Exercises'

    def show_modal_date_picker(self, *args):
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.open()

class Train(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        self.abiba = scripts.DatabaseService()
        self.calculation = scripts.Calculation()
        self.menu = MainMenu()
        self.text_data = ''
        self.boxlayout = BoxLayout(orientation='vertical',spacing = 10, padding = 20)
        self.bl = GridLayout(orientation='lr-tb',cols=2)
        self.boxal = BoxLayout(orientation='horizontal',size_hint=(1,.2))
        self.u = 0
        self.text = ''
        print(baba)
        global biba
        biba = 0
        button_show = Button(
            text = 'Показать упражнения',
            on_press = self.on_press_baba,
            size_hint=(1, 1),
            )
        self.boxal.add_widget(button_show)
        button_new = Button(
            text = 'Новое упражнение',
            on_press = self.on_press_create,
            size_hint=(1, 1),
        )
        button_home = Button(
            text = 'Выход',
            on_press = self.on_press_quit,
            size_hint = (1,1),
        )
        self.boxlayout.add_widget(self.bl) 
        self.boxal.add_widget(button_new)
        self.boxal.add_widget(button_home)  
        self.boxlayout.add_widget(self.boxal)
        self.add_widget(self.boxlayout)
    def on_press_create(self, *args):
        global biba
        biba = 0
        self.u = 0
        self.bl.clear_widgets()
        self.manager.transition.direction = 'left'
        self.manager.current = 'ExerciseTrain'
    def on_press_quit(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main'
    def on_press_baba(self, *args):
        arr = self.abiba.print_tr(baba)
        if self.u == 0:
            laba = Label(
                text = baba,
                size_hint=(1,.1),
            )
            self.boxlayout.add_widget(laba)
            for i in range(len(arr)-1):
                boxl = BoxLayout(orientation='horizontal',spacing = 5, padding=5,size_hint_x=.35)
                label = Label(
                    text = (arr[i])
                )
                button = Button(
                    text = 'Изменить',
                    on_press=self.on_press_change,
                )
                button.my_id = i
                biton = Button(
                    text = 'Удалить',
                    on_press = self.on_press_delete,
                )
                biton.my_id = i
                self.bl.add_widget(label)
                boxl.add_widget(button)
                boxl.add_widget(biton)
                self.bl.add_widget(boxl)
            
            self.u = 1
    def on_press_change(self,instance):
         self.array = self.calculation.list_rowid_tr(baba)
         self.u = 0
         global biba
         biba = self.array[instance.my_id]
         self.bl.clear_widgets()
         self.manager.transition.direction = 'left'
         self.manager.current = 'ExerciseTrain'
         
    def on_press_delete(self, instance):
        self.array = self.calculation.list_rowid_tr(baba)
        self.abiba.delete_tr(str(self.array[instance.my_id]))
        self.bl.clear_widgets()
        self.u = 0 

class ExerciseTrain(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.bl = BoxLayout(orientation='vertical',spacing = 10)
        self.abeba = scripts.DatabaseService()
        self.pido = ''
        self.pedo = ''
        self.pudo = Train()
        spiner = Spinner(
            text="Упражнение",
            values = (self.abeba.get_names()),
            background_color=[0, 1.5, 3, 1],
            pos_hint = {'center_x': .5},
            size_hint=(None, None),
            size = (550, 40),
            font_size=12
            )
        self.bl.add_widget(spiner)
        self.gl = GridLayout(cols = 2, pos_hint = {'center_x': .85})
        self.bl.add_widget(self.gl)
        buttin = Button(
            text = 'Подтвердить упражнение',
            size_hint=(None,None),
            size = (200,40),
            pos_hint = {'center_x':.5},
            padding = 400,
            on_press = self.on_press_create
        )
        self.bl.add_widget(buttin)
        self.add_widget(self.bl)
        def show_selected_value(spinner, text):
            self.pedo = text
            self.gl.clear_widgets()
            if self.abeba.print_boolean_ex(0,text) == 1: # Время
                self.pido = text
                self.TI1 = TextInput(
                        text = '',
                        size = (100,40),
                        size_hint = (None,None),
                        font_size=14,
                        input_filter='int'
                    )
                lab = Label(
                        text = 'Время:',
                        size = (100,40),
                        size_hint = (None,None),
                        )
                self.r = 0
                self.gl.add_widget(lab)
                self.gl.add_widget(self.TI1)
            if self.abeba.print_boolean_ex(1,text) == 1: # Подходы
                self.pido = text
                self.TI2 = TextInput(
                        text = '',
                        size = (100,40),
                        size_hint = (None,None),
                        font_size = 14,
                        input_filter='int'
                        )
                lab = Label(
                        text = 'Подходы:',
                        size = (100,40),
                        size_hint = (None,None),
                        )
                self.r = 0
                self.gl.add_widget(lab)
                self.gl.add_widget(self.TI2)
            if self.abeba.print_boolean_ex(2,text) == 1: # Повторы
                self.pido = text
                self.TI3 = TextInput(
                        text = '',
                        size = (100,40),
                        size_hint = (None,None),
                        font_size = 14,
                        input_filter='int' 
                        )
                lab = Label(
                        text = 'Повторы:',
                        size = (100,40),
                        size_hint = (None,None),
                        )
                self.r = 0
                self.gl.add_widget(lab)
                self.gl.add_widget(self.TI3)
            if self.abeba.print_boolean_ex(3,text) == 1: # Вес
                self.TI4 = TextInput(
                        text = '',
                        size = (100,40),
                        size_hint = (None,None),
                        font_size = 14, 
                        input_filter='int'
                        )
                lab = Label(
                        text = 'Вес:',
                        size = (100,40),
                        size_hint = (None,None),
                        )
                self.gl.add_widget(lab)
                self.gl.add_widget(self.TI4)
            else: 
                print('fail')
        spiner.bind(text=show_selected_value)

    def on_press_create(self, *args):
        arr = [0] * 6
        if self.abeba.print_boolean_ex(0,self.pido) == 1:    
            arr[0] = int(self.TI1.text)
        if self.abeba.print_boolean_ex(1,self.pido) == 1:
            arr[1] = int(self.TI2.text)
        if self.abeba.print_boolean_ex(2,self.pido) == 1:
            arr[2] = int(self.TI3.text)
        if self.abeba.print_boolean_ex(3,self.pido) == 1:
            arr[3] = int(self.TI4.text)
        arr[4] = baba
        arr[5] = biba
        self.abeba.proverka(arr,self.pedo)
        self.manager.transition.direction = 'right'
        self.manager.current = 'Train'


    def on_press(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'NewExercise'

class Exercises(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        self.ababa = scripts.DatabaseService()
        boxlayout = GridLayout(cols = 2)
        self.a = int(self.ababa.get_count())
        for i in range(self.a):
            label = Button(
                text = (self.ababa.get_names()[i]),
                on_press=self.on_press,
            )
            boxlayout.add_widget(label)
        self.add_widget(boxlayout)
    def on_press(self, *args):
        print(1)

class Example(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name = 'main'))
        sm.add_widget(Train(name = 'Train'))
        sm.add_widget(Exercises(name = 'Exercises'))
        sm.add_widget(ExerciseTrain(name = 'ExerciseTrain'))
        return sm


if __name__ == '__main__':
    global baba,biba    
    baba = 'baba'
    a = ''
    Example().run()