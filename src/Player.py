class Player:
    def __init__(self, canvas_player, board, displayWin_function, one_tile_size):
        self.player = canvas_player
        self.x = board.start_position[0]
        self.y = board.start_position[1]
        self.maze = board.maze
        self.field_size = board.field_size
        self.canvas = board.canvas
        self.one_tile_size = one_tile_size
        self.displayWin = displayWin_function
        self.target = board.end_position

        self.won = False

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.won:
            return

        if new_x < 0 or new_x >= self.field_size[0] or new_y < 0 or new_y >= self.field_size[1]:
            # Borders
            return

        if self.maze[new_y][new_x] == 0:
            # Wall
            return

        self.canvas.move(self.player, dx * self.one_tile_size, dy * self.one_tile_size)

        self.x = new_x
        self.y = new_y

        if new_x == self.target[0] and new_y == self.target[1]:
            self.won = True
            self.displayWin()
