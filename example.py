import random
import time
from ttygrid import Grid

def main():
    grid = Grid()
    colors = {
        '0': 'green',
        '1': 'black',
    }
    while True:
        cells = grid.get_all_cells()
        for cell in cells:
            symbol = random.choice(['0', '1'])
            cell.symb = symbol
            cell.set_metadata('color', colors[symbol])
            grid.draw_cells(cell)
        grid.clear_term()
        print(grid)
        time.sleep(0.1)

if __name__ == "__main__":
    main()