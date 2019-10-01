from kivy.core.window import Window
import sys, os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
import board as b
import move as m

class MyCongklakDisplay(FloatLayout):
    Board = b.Board()
    mode = ""
    turn = 0

    def init(self, _mode):
        self.remove_start_screen()
        self.mode = _mode

    def start(self):
        _text = ""

        if (self.mode == "MvP"):
            _text = "Bot Minimax vs Player"
        elif (self.mode == "RvP"):
            _text = "Bot Random vs Player"
        else: #self.mode=="MvR"
            _text = "Bot Minimax vs Bot Random"
        
        self.boardLay.gamemodeLbl.text = _text
        self.draw_board()
        self.set_info_lbl()
    
    def remove_start_screen(self):
        self.remove_widget(self.startLay)
        self.remove_widget(self.backImg)

    def draw_board(self):
        i = 0
        for hole in self.Board.board:
            self.set_hole_lbl(i, hole)
            i += 1

    def set_info_lbl(self):
        player1 = ""
        player2 = ""

        if ((self.mode == "MvP") or (self.mode == "RvP")):
            player1 = "Player"
            player2 = "Bot"
        else:
            player1 = "Minimax Bot"
            player2 = "Random Bot"

        self.boardLay.player1Lbl.text = player1
        self.boardLay.player2Lbl.text = player2
        
        self.ids.get("chooseplyr1btn").text = player1
        self.ids.get("chooseplyr2btn").text = player2

    def set_hole_lbl(self, hole_id, number):
        self.ids.get("_" + str(hole_id)).text = str(number)

    def set_turn_lbl(self, _turn):
        _text = ""

        if (_turn == m.SOUTH_TURN):
            if (self.mode == 'MvP' or self.mode == 'RvP'):
                _text = "Player"
            else:
                _text = "Bot Minimax"
        else: #NORTH_TURN
            if (self.mode == 'MvP' or self.mode == 'RvP'):
                _text = "Bot"
            else:
                _text = "Bot Random"

        self.boardLay.turnLbl.text = _text +  " Turn"

    def set_first_turn(self, _turn):
        self.boardLay.remove_widget(self.boardLay.turnLay)
        self.set_turn_lbl(_turn)

    def player_1_move(self, hole_id):
        if ((self.mode == "MvP") or (self.mode == "RvP")):
            if (hole_id < 7):
                self.Board, turn = m.move(self.Board, m.SOUTH_TURN, hole_id)
        self.set_turn_lbl(turn)
        self.draw_board()
        if (m.winCondition(self.Board)):
            self.add_win_lay()
        else:
            if (turn != m.SOUTH_TURN):
                self.player_2_move()

    def player_2_move(self):
        print("player 2 move")
    
    def add_win_lay(self):
        print("END GAME")

class CongklakApp(App):
    def build(self):
        return MyCongklakDisplay()