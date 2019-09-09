import pygame, sys
from network import Network


def main():
    pygame.init()
    network = Network('localhost', 12345)
    network.start()
    import consts
    from game_manager import GameManager
    from snake import Snake

    screen = pygame.display.set_mode((consts.height, consts.width))
    screen.fill(consts.back_color)
    game = GameManager(consts.table_size, screen, consts.sx, consts.sy, consts.block_cells)
    snakes = list()
    for snake in consts.snakes:
        snakes.append(Snake(snake['keys'], game, (snake['sx'], snake['sy']), snake['color'], snake['direction']))

    while True:
        events = pygame.event.get()
        keys = []
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys.append(event.unicode)
        network.send_data(keys)
        keys = network.get_data()
        game.handle(keys)
        pygame.time.wait(100)


if __name__ == '__main__':
    main()
