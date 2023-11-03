import tkinter as tk


class Window(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.geometry(f'{width}x{height}')
        self.title("TicTacToe")
        self.canvas = tk.Canvas(self)
        self.canvas.pack(expand=1, fill=tk.BOTH)
    
    def start(self, grid):
        grid.clear()
        grid.snake.move()
        grid.draw_snake()
        root.after(100, lambda:self.start(grid))

class Snake():
    dirs = ['Up', 'Down', 'Left', 'Right']

    def __init__(self):
        self.chain = [[1,2],[2,2],[3,2]]
        self.dir = 'Right'

    def change_dir(self, event):
        self.dir = event.keysym
    
    def move(self):
        dir_ind = dict(map(lambda i,j:
            (i,j), Snake.dirs, [0, 0, 1, 1]))
        dir_sgn = dict(map(lambda i,j:
            (i,j), Snake.dirs, [-1, 1, -1, 1]))
        for item in self.chain:
            item[dir_ind[self.dir]] = (
                item[dir_ind[self.dir]] + dir_sgn[self.dir]) % 8


class Grid():

    def click(self, event):
        x_ind = (event.x - self.x) // self.size
        y_ind = (event.y - self.y) // self.size
        tag = f'rect{x_ind}{y_ind}'
        self.canvas.itemconfigure(tag, fill='blue') #Grid.color_dict[self.turn%2]
    
    def clear(self):
        for i in range(self.dim):
            for j in range(self.dim):
                tag = f'rect{i}{j}'
                self.canvas.itemconfigure(tag, fill='lightgray')
    
    def draw_snake(self):
        for item in self.snake.chain:
            tag = f'rect{item[1]}{item[0]}'
            self.canvas.itemconfigure(tag, fill='red')
    
    def __init__(self, root, left_top_x, left_top_y, size, dim):
        self.canvas = root.canvas
        self.x = left_top_x
        self.y = left_top_y
        self.size = size
        self.dim = dim
        self.snake = Snake()
        for i in range(dim):
            for j in range(dim):
                tag = f'rect{i}{j}'
                self.canvas.create_rectangle(
                    left_top_x + i * size, left_top_y + j * size,
                    left_top_x + (i + 1) * size, left_top_y + (j + 1) * size,
                    tag=tag)
        self.draw_snake()
        self.canvas.bind('<Button-1>', self.click)
        for item in Snake.dirs:
            root.bind(f'<{item}>', self.snake.change_dir)

if __name__ == "__main__":
    root = Window(800, 600)
    grid = Grid(root, 100, 100, 50, 8)
    root.start(grid)
    root.mainloop()