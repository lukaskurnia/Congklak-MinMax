from kivy.core.window import Window
import sys, os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
import board as b

class MyCongklakDisplay(FloatLayout):
    Board = b.Board()
    mode = ""

    def start(self, _mode):
        self.remove_start_screen()

        self.mode = _mode
        if (self.mode == "MvP"):
            _text = ("Bot Minimax vs Player")
        elif (self.mode == "RvP"):
            _text = ("Bot Random vs Player")
        else: #self.mode=="MvR"
            _text = ("Bot Minimax vs Bot Random")
        
        self.boardLay.modeLbl.text = _text
        self.draw_board()
    
    def remove_start_screen(self):
        self.remove_widget(self.startLay)
        self.remove_widget(self.backImg)

    def draw_board(self):
        i = 0
        for hole in self.Board.board:
            self.set_hole_lbl(i, hole)
            i += 1

    def set_hole_lbl(self, hole_id, number):
        self.ids.get(self.get_lbl_id(hole_id)).text = str(number)

    def get_lbl_id(self, hole_id):       
        return "_" + str(hole_id)

    def player_move(self, hole_id):
        print(hole_id)
    
    def test(self):
        print("AA")

class CongklakApp(App):
    def build(self):
        return MyCongklakDisplay()