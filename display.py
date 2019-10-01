from kivy.core.window import Window
import sys, os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory

class MyCongklakDisplay(FloatLayout):
    seed_y = [-0.15, 0.15]
    seed_x = [0.3,0.2,0.1,0,-0.1,-0.2,-0.3]

    def start(self, mode):
        self.remove_start_screen()

        if (mode == "MvP"):
            _text = ("Bot Minimax vs Player")
        elif (mode == "RvP"):
            _text = ("Bot Random vs Player")
        else: #mode=="MvR"
            _text = ("Bot Minimax vs Bot Random")
        
        self.boardLay.modeLbl.text = _text
    
    def remove_start_screen(self):
        self.remove_widget(self.startLay)
        self.remove_widget(self.backImg)

    def set_hole_lbl(self, hole_id, number):
        self.ids.get(self.get_lbl_id(hole_id)).text = str(number)

    def get_lbl_id(self, hole_id):       
        return "_" + str(hole_id)

class CongklakApp(App):
    def build(self):
        return MyCongklakDisplay()