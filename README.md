# ttygrid
ttygrid is a WIP grid based system for terminal-based grid simulations.
[ttygrid on PyPi](https://pypi.org/project/ttygrid/)

## Features
- Grid class and cell class
- Functions to get and set cells
- Inbuilt coloring for different symbols using `termcolor`
- Auto adjust to terminal size using `shutil`
##  v0.1 is out! 

## Quick Start Guide
You can install `ttygrid` using pip using:

``pip install ttygrid`` 

Alternatively, you could use:

``pip3 install ttygrid``

Once installed, import with

`from ttygrid import Grid, Cell`

## Documentation
### Grid()

 ```
 Grid(rows=80, cols=40, mode="fit", grid=None, color_map=COLORS)
 ```

Creates a new ttygrid grid instance that can be manipulated using the library.

#### Args
- `rows` (int) - If mode is "custom", the number of rows in the grid. If mode is "fit", the default number of rows in the grid if `shutil.get_terminal_size()` fails to determine terminal size. Default value 80.

- `cols` (int) - If mode is "custom", the number of cols in the grid. If mode is "fit", the default number of cols in the grid if `shutil.get_terminal_size()` fails to determine terminal size. Default value 40.

- `mode` (str) - Can be either "fit" or "custom" (case-sensitive). If mode is "custom", the dimensions of the grid are given through `rows` and `cols`. If mode is "fit", the dimensions are given through `shutil.get_terminal_size()`, with `rows` and `cols` as fallback. Default value "fit"

- `color_map` (dict[str, str]) - A dict with keys as cell symbols and values as colors recognized by `termcolor.colored()`. The default value is:
```
COLORS = {
        '0': "green",
        '1': "black",
        '2': "yellow",
        '3': "blue",
        '4': "light_yellow",
    }
```
---
### __str__()
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

Clears the grid. Should be used in conjunction with print()
---
### get_cell()
```
get_cell(col, row)
```

Returns the value of the cell located at the coordinates (col, row)
Raises ValueEroor if cell does not exist.
---




