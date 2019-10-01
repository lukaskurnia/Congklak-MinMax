from kivy.core.window import Window
import sys, os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import board as b
import move as m
import randombot
import minmax as minimax


class MyCongklakDisplay(FloatLayout):
    Board = b.Board()
    Mode = ""
    Turn = m.SOUTH_TURN
    Difficulty = 5

    def init(self, _mode):
        self.remove_start_screen()
        self.Mode = _mode

    def start(self):
        self.set_info_lbl()
        self.draw_board()
    
    def remove_start_screen(self):
        self.remove_widget(self.startLay)
        self.remove_widget(self.backImg)

    def draw_board(self):
        i = 0
        for hole in self.Board.board:
            self.set_hole_lbl(i, hole)
            i += 1

    def set_info_lbl(self):
        _text = ""

        if (self.Mode == "MvP"):
            _text = "Bot Minimax vs Player"
        elif (self.Mode == "RvP"):
            _text = "Bot Random vs Player"
        else: #self.Mode=="MvR"
            _text = "Bot Minimax vs Bot Random"
        self.boardLay.gamemodeLbl.text = _text

        player1 = ""
        player2 = ""

        if ((self.Mode == "MvP") or (self.Mode == "RvP")):
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
            if (self.Mode == 'MvP' or self.Mode == 'RvP'):
                _text = "Player"
            else:
                _text = "Bot Minimax"
        else: #NORTH_TURN
            if (self.Mode == 'MvP' or self.Mode == 'RvP'):
                _text = "Bot"
            else:
                _text = "Bot Random"

        self.boardLay.turnLbl.text = _text +  " Turn"

    def set_first_turn(self, _turn):
        self.boardLay.remove_widget(self.boardLay.turnLay)
        self.set_turn_lbl(_turn)

    def player_1_move(self, hole_id):
        if ((self.Mode == "MvP" or self.Mode == "RvP") and self.Turn == m.SOUTH_TURN): #player move
            if (hole_id < 7):
                self.Board, self.Turn = m.move(self.Board, m.SOUTH_TURN, hole_id)
        self.set_turn_lbl(self.Turn)
        self.Board.printBoard()
        self.draw_board()
        if (m.winCondition(self.Board)):
            self.add_win_lay()
        else:
            if (self.Turn != m.SOUTH_TURN):
                self.player_2_move()
                # Clock.schedule_once(lambda dt: self.player_2_move, 0.1)
            elif (self.Mode == "MvR"):
                self.player_1_move(minimax.best_move(self.Board,self.Turn, self.Difficulty))

    def player_2_move(self):
        print("A")
        if (self.Mode == "RvP" or self.Mode == "MvR"): #random bot
            bot_move = randombot.random_move(self.Board, self.Turn)
        else: #minimax bot
            bot_move = minimax.best_move(self.Board, self.Turn, self.Difficulty)

        print("Bot move: " + str(bot_move))
        new_board, next_turn = m.move(self.Board, m.SOUTH_TURN, bot_move)
        new_board.printBoard()
        self.set_turn_lbl(self.Turn)
        self.draw_board()
        
        if (m.winCondition(self.Board)):
            self.add_win_lay()
        # else:
        #     if (self.Turn != m.NORTH_TURN):
        #         self.player_1_move()
        #     else:
        #         self.player_2_move()

    def add_win_lay(self):
        self.boardLay.add_widget( Label(text="WIN", font_size=50) )
        print("END GAME")

class CongklakApp(App):
    def build(self):
        return MyCongklakDisplay()

# test = MyCongklakDisplay()
# test.player_1_move(0)
# test.player_2_move()