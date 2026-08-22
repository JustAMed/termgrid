from termcolor import colored
import shutil
from typing import Any
from collections.abc import Callable


class Cell:
    def __init__(self, x: int, y: int, symb: str | None = None, metadata: dict[str, Any] | None = None) -> None:
        """Initialize a cell.

        Args:
            x: The horizontal coordinate of the cell.
            y: The vertical coordinate of the cell.
            symb: The value displayed by the cell.
            metadata: Optional metadata associated with the cell.
        """
        self.x = x
        self.y = y
        self.symb = symb
        self.metadata = metadata if metadata is not None else {"color": "white"}
    
    def __str__(self) -> str:
        return f"{self.symb} at ({self.x}, {self.y})"
    
    def get_metadata(self, field: str | None = None):
        """Get field of metadata if given, otherwise return all fields"""
        if field is not None:
            return self.metadata.get(field, None)
        return self.metadata
    
    def set_metadata(self, field: str, parameter: Any):
        """Set a metadata field to a value."""
        self.metadata[field] = parameter

    
# Y = rows
# X = cols

class Grid:
    def __str__(self) -> str:
        return self.render()

    def __init__(self, rows: int = 80, cols: int = 40, mode: str = "fit") -> None:
        """Initialize a Grid.

        Args:
            rows: The number of rows in the grid.
            cols: The number of columns in the grid.
            mode: Either "fit" to use the terminal dimensions,
                or "custom" to use the specified rows and columns.
        """
        if mode not in ['fit', 'custom']:
            raise ValueError(f"Mode must be 'custom' or 'fit', '{mode}' is not a valid mode")
        
        if not self.are_positive_ints(rows, cols):
            raise ValueError("rows and cols must be positive integers")
        
        if mode == "fit":
            self.cols, self.rows = shutil.get_terminal_size((cols, rows))
        else:
            self.cols = cols
            self.rows = rows
        
        self.cell_map = self.gen_cell_map(self.rows, self.cols)           

    def show_size(self) -> None:
        """Print the size of the grid"""
        print(f"Lines: {self.rows}\nColumns: {self.cols}")

    @staticmethod
    def clear_term() -> None:
        """Clear the terminal"""
        print("\033[H\033[J", end="")

    @staticmethod
    def are_positive_ints(*values: int) -> bool:
        """Return True if all values passed in are positive ints"""
        for value in values:
            if not isinstance(value, int) or isinstance(value, bool) or value < 1:
                return False
        return True        

    def get_cell(self, x: int, y: int) -> Cell:
        """Return Cell object at position (x, y)"""
        if (x, y) not in self.cell_map:
            raise ValueError(f"x:{x}, y:{y} is out of bounds")
        return self.cell_map[(x, y)]
    
    def validate_cell(self, cell: Cell) -> None:
        """Raise a ValueError if Cell not in grid"""
        if (cell.x, cell.y) not in self.cell_map:
            raise ValueError(f"x:{cell.x}, y:{cell.y} is out of bounds")

    def get_all_cells(self, include_empty: bool = True) -> list[Cell]:
        """Get a list of all Cell objects in the grid. If empty is false, all empty cells are ignored."""
        cells = []
        for y in range(self.rows):
            for x in range(self.cols):
                cell = self.cell_map[(x, y)]
                if include_empty or cell.symb is not None:
                    cells.append(cell)
        return cells
    
    def draw_cells(self, *cells: Cell) -> "Grid":
        """Draw the given cells onto the grid"""
        for cell in cells:
            self.validate_cell(cell)
            self.cell_map[(cell.x, cell.y)] = cell
        return self
    
    def clear(self) -> "Grid":
        """Clear the grid and return it"""
        self.cell_map = self.gen_cell_map(self.rows, self.cols)
        return self
    
    def redraw_frame(self, cell_map: dict[tuple[int, int], Cell]) -> "Grid":
        """Redraw the entire frame"""
        self.cell_map = cell_map
        return self

    @staticmethod
    def gen_cell_map(rows: int, cols: int, default_value: Any = None, default_metadata: dict[str, Any] | None = None) -> dict[tuple[int, int], Cell]:
        """Generate a cell map of rows x cols dimensions, with each value being the default_value parameter""" 
        cell_map = {}
        for y in range(rows):
            for x in range(cols):
                cell_map[(x, y)] = Cell(x, y, default_value, default_metadata)

        return cell_map

    def default_render(self, cell: Cell) -> str | None:
        """Return metadata field \'color\' of cell"""
        return cell.get_metadata('color')

    def render(self, render_function: Callable = default_render) -> str:
        """Returns a formatted version of the grid suitable for printing. Colors are decided by passed in render_function, which takes in a Cell and outputs a str for a color"""
        lines = []
        for y in range(self.rows):
            line = []
            for x in range(self.cols):
                cell = self.cell_map[(x, y)]
                color = render_function(self, cell)
                if color:
                    line.append(colored(cell.symb, color))
                else:
                    line.append(cell.symb or " ")
            lines.append("".join(line))
        return "\n".join(lines)