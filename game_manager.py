import consts

from cell import Cell


class GameManager:

    def __init__(self, size, screen, sx, sy, block_cells):
        self.screen = screen
        self.size = size
        self.cells = []
        self.sx = sx
        self.sy = sy
        self.snakes = list()
        self.turn = 0
        for i in range(self.size):
            tmp = []
            for j in range(self.size):
                tmp.append(Cell(screen, sx + i * consts.cell_size, sy + j * consts.cell_size))
            self.cells.append(tmp)
        for cell in block_cells:
            self.get_cell(cell).set_color(consts.block_color)

    def add_snake(self, snake):
        self.snakes.append(snake)

    def get_cell(self, pos):
        try:
            return self.cells[pos[0]][pos[1]]
        except:
            return None

    def kill(self, killed_snake):
        self.snakes.remove(killed_snake)

    def get_next_fruit_pos(self):
        ret = -1, -1
        mx = -100

        for i in range(0, self.size):
            for j in range(0, self.size):

                mn = 100000000

                for x in range(0, self.size):
                    for y in range(0, self.size):
                        if self.get_cell((x, y)).color != consts.back_color:
                            mn = min(mn, int(abs(x - i) + abs(y - j)))

                if mn > mx:
                    mx = mn
                    ret = i, j

        return ret

    def handle(self, keys):
        for snake in self.snakes:
            snake.handle(keys)

        for snake in self.snakes:
            snake.next_move()

        self.turn += 1

        if self.turn % 10 == 0:
            self.get_cell(self.get_next_fruit_pos()).set_color(consts.fruit_color)
