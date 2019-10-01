from kivy.core.window import Window
import sys, os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.widget import Canvas
import board as b
import move as m
import randombot
import minmax as minimax


class MyCongklakDisplay(FloatLayout):
    Board = b.Board()
    Mode = ""
    Turn = m.SOUTH_TURN
    Difficulty = 2

    def init(self, _mode):
        self.remove_start_screen()
        self.Mode = _mode

    def start(self):
        self.set_info_lbl()
        self.draw_board()

        if (self.Mode == "RvP"):
            self.remove_difficulty_lay()
    
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
        self.Turn = _turn
        self.boardLay.remove_widget(self.boardLay.turnLay)
        self.set_turn_lbl(_turn)
        self.initiate_play()

    def initiate_play(self):
        print(self.Mode)
        print(self.Turn == m.NORTH_TURN)
        if ((self.Mode == "MvP" or self.Mode == "RvP") and self.Turn == m.NORTH_TURN):
            print("bot turn")
            Clock.schedule_once(self.player_2_move, 1)
        elif (self.Mode == "MvR" and self.Turn == m.SOUTH_TURN):
            Clock.schedule_once(self.player_1_bot_move, 1)
        elif (self.Mode == "MvR" and self.Turn == m.NORTH_TURN):
            Clock.schedule_once(self.player_2_move, 1)

    def player_1_move(self, hole_id):
        if (self.Board.checkAllSouthHouseEmpty()):
            self.Turn = b.NORTH_STOREHOUSE
            Clock.schedule_once(self.player_2_move, 1)
        else:
            if ((self.Mode == "MvP" or self.Mode == "RvP") and self.Turn == m.SOUTH_TURN and self.Board[hole_id]!=0 ): #player move
                if (hole_id < 7):
                    self.Board, self.Turn = m.move(self.Board, m.SOUTH_TURN, hole_id)
                
            self.set_turn_lbl(self.Turn)
            self.draw_board()
            if (m.winCondition(self.Board)):
                self.add_win_lay()
            else:
                if (self.Turn != m.SOUTH_TURN):
                    Clock.schedule_once(self.player_2_move, 1)
    
    def player_1_bot_move(self, dt):
        if (self.Mode == "MvR"): #minimax bot
            bot_move = minimax.best_move(self.Board, self.Turn, self.Difficulty)
            self.Board, self.Turn = m.move(self.Board, m.SOUTH_TURN, bot_move)

            self.set_turn_lbl(self.Turn)
            self.draw_board()
            if (m.winCondition(self.Board)):
                self.add_win_lay()
            else:
                if (self.Turn != m.SOUTH_TURN):
                    Clock.schedule_once(self.player_2_move, 1)
                else:
                    Clock.schedule_once(self.player_1_bot_move, 1)

    def player_2_move(self, dt):
        if (self.Mode == "RvP" or self.Mode == "MvR"): #random bot
            bot_move = randombot.random_move(self.Board, self.Turn)
        else: #minimax bot
            bot_move = minimax.best_move(self.Board, self.Turn, self.Difficulty)

        print("Bot move: " + str(bot_move))
        self.Board, self.Turn = m.move(self.Board, m.NORTH_TURN, bot_move)
        self.set_turn_lbl(self.Turn)
        self.draw_board()
        
        if (m.winCondition(self.Board)):
            self.add_win_lay()
        else:
            if (self.Turn == m.NORTH_TURN):
                Clock.schedule_once(self.player_2_move, 1)
            elif (self.Mode == "MvR"):
                Clock.schedule_once(self.player_1_bot_move, 1)

    def add_win_lay(self):
        if (self.Mode == "MvP" or self.Mode == "RvP"):
            _south = "Player"
            if (self.Mode == "MvP"):
                _south = "Minimax Bot"
            else:
                _south = "Random Bot"
        else: #Minimax vs Random
            _south = "Minimax Bot"
            _north = "Random Bot"

        if (minimax.evaluation(self.Board, b.SOUTH_STOREHOUSE) > 0):
            _text = _south + " WINS"
        elif (minimax.evaluation(self.Board, b.SOUTH_STOREHOUSE) < 0):
            _text = _north + " WINS"
        else:
            _text = "IT'S A TIE"

        self.boardLay.add_widget( Label(text=_text, font_size=50, color=(0,0,0,1)) )
    
    def set_difficulty(self, depth):
        self.Difficulty = depth

    def remove_difficulty_lay(self):
        self.boardLay.remove_widget(self.boardLay.diffImg)
        self.boardLay.remove_widget(self.boardLay.diffLay)

class CongklakApp(App):
    def build(self):
        return MyCongklakDisplay()

# test = MyCongklakDisplay()
# test.player_1_move(0)
# test.player_2_move()