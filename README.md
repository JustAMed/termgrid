# ttygrid
ttygrid is a grid-based framework for building terminal simulations, games, and visualizations.
- [ttygrid on PyPi](https://pypi.org/project/ttygrid/)
![TTYGrid Demo](assets/showcase.gif)

## Features
- Grid class and cell class
- Functions to get and set cells
- Inbuilt coloring for different symbols using `termcolor`
- Auto adjust to terminal size using `shutil`
##  v0.2 is out! 

## Quick Start Guide
You can install `ttygrid` using pip using:

```
pip install ttygrid
```

Alternatively, you could use:

```
pip3 install ttygrid
```

Once installed, import with

```
from ttygrid import Grid, Cell
```

## Example
```
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
```

## Documentation
### Grid()

 ```
 Grid(rows=80, cols=40, mode="fit", grid=None)
 ```

Creates a new ttygrid grid instance that can be manipulated using the library.

#### Args
- `rows` (int) - If mode is "custom", the number of rows in the grid. If mode is "fit", the default number of rows in the grid if `shutil.get_terminal_size()` fails to determine terminal size. Default value 80.

- `cols` (int) - If mode is "custom", the number of cols in the grid. If mode is "fit", the default number of cols in the grid if `shutil.get_terminal_size()` fails to determine terminal size. Default value 40.

- `mode` (str) - Can be either "fit" or "custom" (case-sensitive). If mode is "custom", the dimensions of the grid are given through `rows` and `cols`. If mode is "fit", the dimensions are given through `shutil.get_terminal_size()`, with `rows` and `cols` as fallback. Default value "fit"

---
### render()
```
def render(render_function=default_render)
```

Returns the rendered table. Pass in a render_function to customize rendering. By default, the color is the color field in cell metadata.
---
### __str__() (Grid)
```
print(grid)
```

Prints the formatted grid to the terminal.

---
### show_size()
```
show_size(grid)
```

Prints the number of Lines (rows) and Columns (cols) in the grid. To get them programmatically, use grid.rows and grid.cols instead.

---
### clear_term()
```
clear_term()
```

Clears the terminal. Typically used before printing new frames.

---
### get_cell()
```
get_cell(col, row)
```

Returns the Cell object located at the coordinates (col, row)
Raises ValueError if cell does not exist.

---
### validate_cell()
```
validate_cell(cell)
```

Raises ValueError if cell coordinates not found in grid

---
### get_all_cells()
```
get_all_cells(empty=True)
```

Get a list of all cells in the grid. 
If `empty` is True, empty cells are also included.
If `empty` is False, empty cells are not included.
The default value is True

---
### draw_cells()
```
draw_cells(*cells)
```

Draws all valid cells passed as arguments onto the grid.

---
### clear()
```
clear()
```

Clears the grid (resets it to all cells being None)

---
### redraw_frame()
```
redraw_frame(cell_map)
```

The grid is redrawn using `cell_map`.
Effectively, the value of the grid is now `cell_map`.
A `cell_map` value not made of cells or having irregular sides compared to original grid.rows and grid.cols, results in undefined behaviour.
It is best to first call `get_all_cells()` and pass in modified values of the call to `redraw_frame()`

---

## Cell Class

### Cell()
```
Cell(x, y, symb=None, metadata=None)
```
Args:

- x - the x (col) position of the Cell
- y - the y (row) position of the Cell
- symb - the symbol represented by the cell. A value of None indicates an empty cell.
- metadata - the metadata associated with the cell. by default, only one field, 'color' is present, set to white.

---
### __str__()
```
print(cell)
```

Prints the cell position and symbol

---
### get_metadata()
```
get_metadata(field=None)
```

Sets a specific field. If field is None, returns the metadata dictionary

---
### set_metadata()
```
set_metadata(field, parameter)
```

Sets a specific metadata field.

---

## Known Issues

- Extra newline after print (Scheduled to be fixed in v0.2)

---

## Roadmap

- Drawing primitives
- Demos
- Customizable status bar for simulation


