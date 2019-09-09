import consts


class Snake:
    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):

        nx = self.get_head()[0] + self.dx[self.direction]
        ny = self.get_head()[1] + self.dy[self.direction]

        nx = self.val(nx)
        ny = self.val(ny)

        cell = self.game.get_cell((nx, ny))

        if not cell or cell.color != consts.back_color and cell.color != consts.fruit_color:
            self.game.kill(self)
            return

        self.cells.append((nx, ny))

        if cell.color != consts.fruit_color:
            self.game.get_cell(self.cells.pop(0)).set_color(consts.back_color)

        cell.set_color(self.color)

    def handle(self, keys):
        for key in keys:
            if key not in self.keys:
                continue

            next_dir = self.keys[key]
            cur_dir = self.direction

            st = {next_dir, cur_dir}

            if st == {'UP', 'DOWN'} or st == {'LEFT', 'RIGHT'}:
                continue

            self.direction = next_dir
            break
