import json

f = open("config.json")
data = json.loads(f.read())
f.close()

back_color = data['back_color']
fruit_color = data['fruit_color']   
block_color = data['block_color']
cell_size = data['cell_size']
block_cells = data['block_cells']
table_size = data['table_size']
height = data['height']
width = data['width']
snakes = data['snakes']
sx = data['sx']
sy = data['sy']
