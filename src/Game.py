import tkinter as tk
from Board import Board
from Player import Player

one_tile_size = 30


class Game:
    def __init__(self, field_size):
        self.displayWelcome()

        root = tk.Tk()
        root.title('Где Прога?')
        self.root = root

        self.board = Board(root, field_size, one_tile_size)

        root.geometry(str(field_size[0] * one_tile_size) + 'x' + str(field_size[1] * one_tile_size))
        root.resizable(False, False)

        sx = self.board.start_position[0]
        sy = self.board.start_position[1]

        tx = self.board.end_position[0]
        ty = self.board.end_position[1]

        canvas = self.board.canvas
        self.target_image = tk.PhotoImage(file='images/target.gif', width=one_tile_size, height=one_tile_size) #
        canvas_target = canvas.create_image((tx + 0.5) * one_tile_size, (ty + 0.5) * one_tile_size,
                                            image=self.target_image)

        self.player_image = tk.PhotoImage(file='images/player.gif', width=one_tile_size, height=one_tile_size)  #
        canvas_player = canvas.create_image((sx + 0.5) * one_tile_size, (sy + 0.5) * one_tile_size,
                                            image=self.player_image)
        self.player = Player(canvas_player, self.board, self.displayWin, one_tile_size)

        # Attention! As Y axis is pointed down, we have move(0, -1) for Up and W, and move(0, 1) for Down and S
        root.bind('<Left>', lambda event: self.player.move(-1, 0))
        root.bind('<Right>', lambda event: self.player.move(1, 0))
        root.bind('<Up>', lambda event: self.player.move(0, -1))
        root.bind('<Down>', lambda event: self.player.move(0, 1))

        root.bind('<a>', lambda event: self.player.move(-1, 0))
        root.bind('<d>', lambda event: self.player.move(1, 0))
        root.bind('<w>', lambda event: self.player.move(0, -1))
        root.bind('<s>', lambda event: self.player.move(0, 1))

    def play(self):
        return self.root.mainloop()

    @classmethod
    def displayWelcome(self):
        welcome_window = tk.Tk()
        welcome_window.title('Где Прога? - Введение')
        welcome_text = "Добро пожаловать в игру \"Где Прога?\"!\n" \
                       "Сюжет данной игры предельно прост:\n" \
                       "Вы играете за восьмиклассника Сашу, который совсем недавно поступил в ФТШ.\n" \
                       "У нашего героя через 15 минут начинается первый урок в его новой школе - информатика,\n" \
                       "Однако как это часто бывает с новенькими, он не может найти нужный ему кабинет.\n" \
                       "Ваша задача - помочь Саше найти путь к кабинету информатики и не получить по лбу от учителя.\n" \
                       "\n" \
                       "Управление:\n" \
                       "WASD + стрелочки\n" \
                       "\n" \
                       "Удачи!"
        mes = tk.Message(welcome_window, text=welcome_text, justify='center')
        mes.config(width=600)
        btn = tk.Button(welcome_window, text='Начать игру!', command=welcome_window.destroy)
        mes.pack()
        btn.pack()
        return welcome_window.mainloop()

    @classmethod
    def displayWin(self):
        win_window = tk.Tk()
        win_window.title('Где Прога? - Победа!')
        lbl = tk.Label(win_window, text='Вы победили! '
                                        'Саша успел на занятие и теперь на уроках учит питон и котлин '
                                        '(может всё-таки лучше jav\'у?).')
        btn = tk.Button(win_window, text='Выход', command=exit)
        lbl.pack()
        btn.pack()
        return win_window.mainloop()
