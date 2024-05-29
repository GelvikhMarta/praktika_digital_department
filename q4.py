
from kivy.uix.actionbar import Label
from kivy.uix.actionbar import Button
from kivy.uix.actionbar import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.pickers import MDModalDatePicker
from kivy.uix.actionbar import Spinner
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
import scripts 
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

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
        self.boxlayout.clear_widgets
        self.bl = GridLayout(orientation='lr-tb',cols=2,padding = 5, spacing = 5, row_default_height = 10)
        self.boxal = BoxLayout(orientation='horizontal',size_hint=(1,.15))
        self.lalala = BoxLayout(orientation='vertical',size_hint_y = .05)
        self.u = 0
        self.k = 0
        self.text = ''
        biba = 0
        self.boxlayout.add_widget(self.lalala)
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
        self.bl.clear_widgets()
        self.k = 0
        self.u = 0
        self.lalala.remove_widget(self.laba)
        self.manager.transition.direction = 'left'
        self.manager.current = 'main'
    def on_press_baba(self, *args):
        arr = self.abiba.print_tr(baba)       
        if self.k == 0:
            self.laba = Label(
                text = baba,
                size_hint=(1,.1),
            )
            self.lalala.add_widget(self.laba)
            self.k = 1
        if self.u == 0:
            for i in range(len(arr)-1):
                boxl = BoxLayout(orientation='horizontal',spacing = 5, padding=5,size_hint_x=.35)
                label = Label(
                    text = (arr[i]),
                    halign = 'center',
                    valign = 'center'
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
        self.boxlayout.clear_widgets
        arr = []
    def on_press_change(self,instance):
         self.array = self.calculation.list_rowid_tr(baba)
         self.u = 0
         global biba
         biba = self.array[instance.my_id]
         self.bl.clear_widgets()
         self.boxlayout.clear_widgets
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
        self.boxl = BoxLayout(orientation='horizontal',size_hint_y=.1)
        self.abeba = scripts.DatabaseService
        self.pido = ''
        self.pedo = ''
        self.time = 0
        self.sets = 0
        self.reps = 0
        self.weight = 0
        self.kirgiziya = ''
        self.pudo = Train
        spiner = Spinner(
            text="Мышцы",
            values = (self.abeba.find_muscles()),
            background_color=[0, 1.5, 3, 1],
            pos_hint = {'center_x': .5},
            size_hint_x=.8,
            font_size=14
            )
        self.boxl.add_widget(spiner)
        self.gl = GridLayout(cols = 2, pos_hint = {'center_x': .5})
        self.bl.add_widget(self.gl)
        buttin = Button(
            text = 'Назад',
            size_hint_x = .2,
            padding = 400,
            #on_press = self.on_press_back
        )
        self.boxl.add_widget(buttin)
        self.bl.add_widget(self.boxl)
        self.add_widget(self.bl)
        spiner.bind(text=self.show_selected_value)

    def show_selected_value(self,spinner, text):
        self.pedo = text
        self.gl.clear_widgets()
        box1 = BoxLayout(orientation='vertical')
        gl1 = GridLayout(cols = 2,row_default_height=10)
        gl1.clear_widgets()
        self.time = 0
        self.sets = 0
        self.reps = 0
        self.weight = 0
        lab = Label(
            text = 'Время'
        )
        gl1.add_widget(lab)
        ch_box = CheckBox()
        ch_box.bind(active = self.on_ch_box_active_time)
        gl1.add_widget(ch_box)
        lab = Label(
            text = 'Подходы',

        )
        gl1.add_widget(lab)
        ch_box2 = CheckBox()
        ch_box2.bind(active = self.on_ch_box_active_sets)
        gl1.add_widget(ch_box2)
        lab = Label(
            text = 'Повторы',

        )
        gl1.add_widget(lab)
        ch_box3 = CheckBox()
        ch_box3.bind(active = self.on_ch_box_active_reps)
        gl1.add_widget(ch_box3)
        lab = Label(
            text = 'Вес',
        )
        gl1.add_widget(lab)
        ch_box4 = CheckBox()
        ch_box4.bind(active = self.on_ch_box_active_weight)
        gl1.add_widget(ch_box4)
        self.gl.add_widget(gl1)
        self.button_ex = Button(
            text = 'Вывести упражнения',
            on_press = self.print_ex,
            size_hint_x=2
            )
        self.gl.add_widget(self.button_ex)
    def on_ch_box_active_time(self,checkbox,value):
        if value:
            self.time = 1
        else:
            self.time = 0
    def on_ch_box_active_sets(self,checkbox,value):
        if value:
            self.sets = 1
        else:
            self.sets = 0
    def on_ch_box_active_reps(self,checkbox,value):
        if value:
            self.reps = 1
        else:
            self.reps = 0
    def on_ch_box_active_weight(self,checkbox,value):
        if value:
            self.weight = 1
        else:
            self.weight = 0
    def print_ex(self, *args):
        arrar = [0] * 5
        arrar[0] = str(self.pedo)
        self.gl.remove_widget(self.button_ex)
        if self.time != 0 or self.sets != 0 or self.reps != 0 or self.weight != 0:
            arrar[1] = self.time
            arrar[2] = self.sets
            arrar[3] = self.reps
            arrar[4] = self.weight
        arra = self.abeba.find_ex_spec(arrar)
        print(arrar)
        box2 = BoxLayout(orientation='vertical',size_hint_x=2)
        for i in range(len(arra)):
            button = Button(
                text = f'{arra[i][0]}',
                on_press=self.on_press_new_ex_tr
            )
            box2.add_widget(button)
        arra = []
        self.gl.add_widget(box2)
    def on_press_new_ex_tr(self,instance):
        text = str(instance.text)
        self.pedo = text
        print(text)
        self.pido = ''
        self.bl.clear_widgets()
        self.gl.clear_widgets()
        boba = BoxLayout(orientation='horizontal',size_hint_y = .15)
        goga = GridLayout(cols = 2)
        label = Label(
            text = text
        )
        self.bl.add_widget(label)
        if self.abeba.print_boolean_ex(0,text) == 1: # Время
                self.pido = text
                self.TI1 = TextInput(
                        text = '',
                        size = (300,40),
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
                goga.add_widget(lab)
                goga.add_widget(self.TI1)
        if self.abeba.print_boolean_ex(1,text) == 1: # Подходы
                self.pido = text
                self.TI2 = TextInput(
                        text = '',
                        size = (300,40),
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
                goga.add_widget(lab)
                goga.add_widget(self.TI2)
        if self.abeba.print_boolean_ex(2,text) == 1: # Повторы
                self.pido = text
                self.TI3 = TextInput(
                        text = '',
                        size_hint = (None,None),
                        size = (300,40),
                        font_size = 14,
                        input_filter='int' 
                        )
                lab = Label(
                        text = 'Повторы:',
                        size = (100,40),
                        size_hint = (None,None),
                        )
                self.r = 0
                goga.add_widget(lab)
                goga.add_widget(self.TI3)
        if self.abeba.print_boolean_ex(3,text) == 1: # Вес 
                self.TI4 = TextInput(
                        text = '',
                        size = (300,40),
                        size_hint = (None,None),
                        font_size = 14, 
                        input_filter='int'
                        )
                lab = Label(
                        text = 'Вес:',
                        size = (100,40),
                        size_hint = (None,None),
                        )
                goga.add_widget(lab)
                goga.add_widget(self.TI4)
        else: 
            print('zhopa')
        button = Button(
            text = 'Подтвердить',
            on_press = self.on_press_create
        )
        boba.add_widget(button)
        button = Button(
            text = 'ДОМОЙ',
            on_press=self.on_press_menu
        )
        boba.add_widget(button)
        self.bl.add_widget(goga)
        self.bl.add_widget(boba)     
    def on_press_create(self, *args):
        self.bl.clear_widgets()
        spiner = Spinner(
            text="Мышцы",
            values = (self.abeba.find_muscles()),
            background_color=[0, 1.5, 3, 1],
            pos_hint = {'center_x': .5},
            size_hint=(None, None),
            size = (550, 40),
            font_size=12
            )
        """spiner = Spinner(
            text="Мышцы",
            values = (self.abeba.get_names()),
            background_color=[0, 1.5, 3, 1],
            pos_hint = {'center_x': .5},
            size_hint=(None, None),
            size = (550, 40),
            font_size=12
            )"""
        self.bl.add_widget(spiner)
        self.gl = GridLayout(cols = 2, pos_hint = {'center_x': .5})
        self.bl.add_widget(self.gl)
        buttin = Button(
            text = 'Подтвердить упражнение',
            size_hint=(None,None),
            size = (200,40),
            pos_hint = {'center_x':.5},
            padding = 400,
            #on_press = self.on_press_create
        )
        self.bl.add_widget(buttin)
        spiner.bind(text=self.show_selected_value)
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

    def on_press_menu(self,*args):
        self.clear_widgets()
        self.bl = BoxLayout(orientation='vertical',spacing = 10)
        self.boxl = BoxLayout(orientation='horizontal',size_hint_y=.1)
        self.pido = ''
        self.pedo = ''
        self.time = 0
        self.sets = 0
        self.reps = 0
        self.weight = 0
        spiner = Spinner(
            text="Мышцы",
            values = (self.abeba.find_muscles()),
            background_color=[0, 1.5, 3, 1],
            pos_hint = {'center_x': .5},
            size_hint_x=.8,
            font_size=14
            )
        self.boxl.add_widget(spiner)
        self.gl = GridLayout(cols = 2, pos_hint = {'center_x': .5})
        self.bl.add_widget(self.gl)
        buttin = Button(
            text = 'Назад',
            size_hint_x = .2,
            padding = 400,
            #on_press = self.on_press_back
        )
        self.boxl.add_widget(buttin)
        self.bl.add_widget(self.boxl)
        self.add_widget(self.bl)
        spiner.bind(text=self.show_selected_value)
        self.manager.transition.direction = 'left'
        self.manager.current = 'main'

class Exercises(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        self.ababa = scripts.DatabaseService()
        self.bl = BoxLayout(orientation='horizontal',size_hint_y=.1)
        self.box = BoxLayout(orientation='vertical')
        self.box1 = BoxLayout(orientation='vertical',padding = 3, spacing = 3)
        self.a = int(self.ababa.get_count())
        self.b = scripts.Calculation()
        self.c = self.b.list_rowid_ex() 
        self.a_max = 16
        self.a_min = 0
        self.hulio = 0
        for i in range(self.a_min,self.a_max):
            a = str(self.c[i])
            if scripts.get_ex(a) != None:
                label = Button(
                    text = (self.ababa.get_names()[i]),
                    on_press=self.on_press,
                )
                self.box1.add_widget(label)
            else:
                button = Button(
                    text = '+'
                )
                self.box1.add_widget(button)
        button = Button(
                text = 'Назад',
                on_press = self.on_press_back
            )
        self.bl.add_widget(button)
        button = Button(
            text = 'Домой',
            on_press=self.on_press_menu
        )
        self.bl.add_widget(button)      
        button = Button(
            text = 'Далее',
            on_press = self.on_press_next
        )
        self.bl.add_widget(button)
        self.box.add_widget(self.box1)
        self.box.add_widget(self.bl)
        self.add_widget(self.box)
    def on_press_back(self, *args):
        print('zaza')    
    def on_press(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main'
    def on_press_menu(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'main'
        
    def on_press_next(self, *args):
        self.a_max += 16
        self.a_min += 16
        self.box1.clear_widgets()
        if self.hulio < self.a:
            for i in range(self.a_min,self.a_max):
                self.hulio += 1
                print(self.c[i])
                a = str(self.c[i])
                if scripts.get_ex(a) != None:
                    label = Button(
                        text = (self.ababa.get_names()[i]),
                        on_press=self.on_press,
                    )
                    self.box1.add_widget(label)
                if i == (self.a-1):
                    button = Button(
                        text = '+',
                        on_press=self.on_press_exer
                    )
                    self.box1.add_widget(button)
                    break                       
    def on_press_back(self, *args):
        if self.a_min != 0:
            self.a_max -= 16
            self.a_min -= 16
        self.box1.clear_widgets()
        self.hulio -=16
        if self.hulio < self.a:
            for i in range(self.a_min,self.a_max):
                self.hulio += 1
                print(self.c[i])
                a = str(self.c[i])
                if scripts.get_ex(a) != None:
                    print('KAKAHA')
                    label = Button(
                        text = (self.ababa.get_names()[i]),
                        on_press=self.on_press,
                    )
                    self.box1.add_widget(label)
                if i == (self.a-1):
                    button = Button(
                        text = '+',
                        on_press=self.on_press_exer
                    )
                    self.box1.add_widget(button)
                    break                     
    def on_press_exer(self,*args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'NewEx'

class NewEx(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.bl = BoxLayout(orientation='vertical',spacing = 10)
        boxlayout = BoxLayout(orientation='vertical',size_hint_y=.8)
        self.bd_service = scripts.DatabaseService
        self.time = 0
        self.sets = 0
        self.reps = 0
        self.weight = 0
        self.pudo = Train()
        self.spiner = TextInput(
            text="Упражнение",
            )
        boxlayout.add_widget(self.spiner)
        self.ti = TextInput(
            text = 'Какая группа мышц',
        )
        boxlayout.add_widget(self.ti)
        self.bl.add_widget(boxlayout)
        self.gl = GridLayout(cols = 2, pos_hint = {'center_x': .5})
        label = Label(
            text = "Время",
            width= 200
        )
        self.gl.add_widget(label)
        checkbox1 = CheckBox()
        checkbox1.bind(active = self.on_checkbox_active_time)
        self.gl.add_widget(checkbox1)
        label = Label(
            text = "Подходы",
            width= 200
        )
        self.gl.add_widget(label)
        checkbox2 = CheckBox()
        checkbox2.bind(active = self.on_checkbox_active_sets)
        self.gl.add_widget(checkbox2)
        label = Label(
            text = "Повторы",
            width= 200
        )
        self.gl.add_widget(label)
        checkbox3 = CheckBox()
        checkbox3.bind(active = self.on_checkbox_active_reps)
        self.gl.add_widget(checkbox3)
        label = Label(
            text = "Вес",
            width= 200
        )
        self.gl.add_widget(label)
        checkbox4 = CheckBox()
        checkbox4.bind(active = self.on_checkbox_active_weight)
        self.gl.add_widget(checkbox4)
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
    
    def on_checkbox_active_time(self,checkbox,value):
        if value:
            self.time = 1
        else:
            self.time = 0
        print(f'Время - {self.time}')
    def on_checkbox_active_reps(self,checkbox,value):
        if value:
            self.reps = 1
        else:
            self.reps = 0
        print(f'Повторы - {self.reps}')
    def on_checkbox_active_sets(self,checkbox,value):
        if value:
            self.sets = 1
        else:
            self.sets = 0
        print(f'Подходы - {self.sets}')
    def on_checkbox_active_weight(self,checkbox,value):
        if value:
            self.weight = 1
        else:
            self.weight = 0
        print(f'Вес - {self.weight}')
    def on_press_create(self,*args):   
        arrar = []
        arrar.append(self.spiner.text)
        arrar.append(self.time)
        arrar.append(self.sets)
        arrar.append(self.reps)
        arrar.append(self.weight)
        arrar.append(self.ti.text)
        arrar.append('Серёга пират')
        self.bd_service.insert_ex(arrar)
        self.manager.transition.direction = 'left'
        self.manager.current = 'main'

class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        sm = ScreenManager()
        sm.add_widget(MainMenu(name = 'main'))
        sm.add_widget(Train(name = 'Train'))
        sm.add_widget(Exercises(name = 'Exercises'))
        sm.add_widget(ExerciseTrain(name = 'ExerciseTrain'))
        sm.add_widget(NewEx(name = 'NewEx'))
        return sm


if __name__ == '__main__':
    global baba,biba,boba  
    boba = ''  
    baba = 'baba'
    a = ''
    Example().run()