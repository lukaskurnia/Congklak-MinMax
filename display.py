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

class MyCongklakDisplay(BoxLayout):
    def start(self, mode):
        self.remove_start_screen()

        if (mode == "MvP"):
            text = ("Bot Minimax vs Player")
        elif (mode == "RvP"):
            text = ("Bot Random vs Player")
        else: #mode=="MvR"
            text = ("Bot Minimax vs Bot Random")
        
        self.add_board(text)
    
    def remove_start_screen(self):
        self.remove_widget(self.startLay)

    def add_board(self, _text):
        self.boardLay = FloatLayout()
        self.add_widget(self.boardLay)

        self.boardLay.add_widget(Label(text=_text, font_size= 50, pos_hint={"y":0.4}, ))

        self.boardLay.add_widget( Image(source="Images/board.png") )
        self.boardLay.add_widget(Label(id="7", text="0", font_size= 50, pos_hint={"x":-0.42}))
        self.boardLay.add_widget(Label(id="15",text="0", font_size= 50, pos_hint={"x":0.42}))

        self.boardLay.add_widget(Label(id="0", text="6", font_size= 50, pos_hint={"x":0.3, "y":-0.15}))
        self.boardLay.add_widget(Label(id="1", text="6", font_size= 50, pos_hint={"x":0.2, "y":-0.15}))
        self.boardLay.add_widget(Label(id="2",text="6", font_size= 50, pos_hint={"x":0.1, "y":-0.15}))
        self.boardLay.add_widget(Label(id="3",text="6", font_size= 50, pos_hint={"x":0, "y":-0.15}))
        self.boardLay.add_widget(Label(id="4",text="6", font_size= 50, pos_hint={"x":-0.1, "y":-0.15}))
        self.boardLay.add_widget(Label(id="5",text="6", font_size= 50, pos_hint={"x":-0.2, "y":-0.15}))
        self.boardLay.add_widget(Label(id="6",text="6", font_size= 50, pos_hint={"x":-0.3, "y":-0.15}))
        
        self.boardLay.add_widget(Label(id="8",text="6", font_size= 50, pos_hint={"x":0.3, "y":0.15}))
        self.boardLay.add_widget(Label(id="9",text="6", font_size= 50, pos_hint={"x":0.2, "y":0.15}))
        self.boardLay.add_widget(Label(id="10",text="6", font_size= 50, pos_hint={"x":0.1, "y":0.15}))
        self.boardLay.add_widget(Label(id="11",text="6", font_size= 50, pos_hint={"x":0, "y":0.15}))
        self.boardLay.add_widget(Label(id="12",text="6", font_size= 50, pos_hint={"x":-0.1, "y":0.15}))
        self.boardLay.add_widget(Label(id="13",text="6", font_size= 50, pos_hint={"x":-0.2, "y":0.15}))
        self.boardLay.add_widget(Label(id="14",text="6", font_size= 50, pos_hint={"x":-0.3, "y":0.15}))

class CongklakApp(App):
    def build(self):
        return MyCongklakDisplay()