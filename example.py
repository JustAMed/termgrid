import random
import time
from ttygrid import Grid

def main():
    grid = Grid()
    while True:
        cells = grid.get_all_cells()
        for cell in cells:
            cell.symb = random.choice(['0', '1'])
            grid.draw_cells(cell)
        grid.clear_term()
        print(grid)
        time.sleep(0.1)

if __name__ == "__main__":
    main()