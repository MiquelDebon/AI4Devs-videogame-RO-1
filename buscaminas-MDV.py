import tkinter as tk
import random
import time

# --- Configuración ---
BOARD_SIZE = 10
NUM_MINES = 10
CELL_SIZE = 30

# --- Clase Celda ---
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0

# --- Clase Juego Buscaminas ---
class Minesweeper:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.reset_game()

    def reset_game(self):
        self.board = [[Cell(r, c) for c in range(BOARD_SIZE)] for r in range(BOARD_SIZE)]
        self.buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.start_time = None
        self.timer_running = False
        self.flags_remaining = NUM_MINES

        if hasattr(self, 'frame_board'):
            self.frame_board.destroy()
        if hasattr(self, 'top_frame'):
            self.top_frame.destroy()

        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack()

        self.timer_label = tk.Label(self.top_frame, text="Time: 0", font=('Arial', 12))
        self.timer_label.pack(side=tk.LEFT, padx=10)

        self.flag_label = tk.Label(self.top_frame, text=f"Flags: {self.flags_remaining}", font=('Arial', 12))
        self.flag_label.pack(side=tk.RIGHT, padx=10)

        self.frame_board = tk.Frame(self.master)
        self.frame_board.pack()

        self.place_mines()
        self.calculate_adjacents()
        self.create_buttons()

        self.update_timer()

    def place_mines(self):
        placed = 0
        while placed < NUM_MINES:
            r = random.randint(0, BOARD_SIZE - 1)
            c = random.randint(0, BOARD_SIZE - 1)
            cell = self.board[r][c]
            if not cell.is_mine:
                cell.is_mine = True
                placed += 1

    def calculate_adjacents(self):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                if self.board[r][c].is_mine:
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                            if self.board[nr][nc].is_mine:
                                count += 1
                self.board[r][c].adjacent_mines = count

    def create_buttons(self):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                btn = tk.Button(self.frame_board, width=2, height=1, font=('Arial', 14),
                                command=lambda r=r, c=c: self.reveal(r, c))
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.toggle_flag(r, c))
                btn.grid(row=r, column=c, ipadx=5, ipady=5)
                self.buttons[r][c] = btn

    def reveal(self, r, c):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True

        cell = self.board[r][c]
        btn = self.buttons[r][c]

        if cell.is_revealed or cell.is_flagged:
            return

        cell.is_revealed = True
        if cell.is_mine:
            btn.config(text='💣', bg='red')
            self.game_over(False)
            return

        btn.config(relief=tk.SUNKEN, state=tk.DISABLED, bg='#d3d3d3')

        if cell.adjacent_mines > 0:
            btn.config(text=str(cell.adjacent_mines))
        else:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
                        self.reveal(nr, nc)

        self.check_win()

    def toggle_flag(self, r, c):
        cell = self.board[r][c]
        btn = self.buttons[r][c]
        if cell.is_revealed:
            return
        if cell.is_flagged:
            cell.is_flagged = False
            btn.config(text='')
            self.flags_remaining += 1
        else:
            if self.flags_remaining > 0:
                cell.is_flagged = True
                btn.config(text='🚩')
                self.flags_remaining -= 1
        self.flag_label.config(text=f"Flags: {self.flags_remaining}")

    def check_win(self):
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                cell = self.board[r][c]
                if not cell.is_mine and not cell.is_revealed:
                    return
        self.game_over(True)

    def game_over(self, won):
        self.timer_running = False
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                cell = self.board[r][c]
                btn = self.buttons[r][c]
                if cell.is_mine and not cell.is_flagged:
                    btn.config(text='💣')
                btn.config(state=tk.DISABLED)

        msg = "You Win!" if won else "Game Over!"
        result = tk.messagebox.showinfo("Result", msg)
        if result:
            self.reset_game()

    def update_timer(self):
        if self.timer_running:
            elapsed = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed}")
        self.master.after(1000, self.update_timer)

# --- Ejecutar Juego ---
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Buscaminas")
    root.resizable(False, False)
    tk.messagebox = tk.messagebox if hasattr(tk, 'messagebox') else __import__('tkinter.messagebox').messagebox
    game = Minesweeper(root)
    root.mainloop()
