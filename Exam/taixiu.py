import random
import tkinter as tk
from tkinter import messagebox

class TaiXiuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tài Xỉu ")
        
        self.player_guess = tk.StringVar()
        self.bet_amount = tk.IntVar()
        
        self.create_widgets()
        
    def roll_dice(self):
        return random.randint(1, 6)

    def tai_xiu(self, player_guess, total):
        if player_guess == "tai" and total >= 11:
            return True
        elif player_guess == "xiu" and total <= 10:
            return True
        return False
    
    def play_game(self):
        guess = self.player_guess.get()
        bet = self.bet_amount.get()
        
        if guess not in ("tai", "xiu"):
            messagebox.showerror("Invalid Input", "Please enter 'tai' or 'xiu'.")
            return
        
        if bet <= 0:
            messagebox.showerror("Invalid Bet", "Bet amount must be greater than 0.")
            return
        
        dice1 = self.roll_dice()
        dice2 = self.roll_dice()
        dice3 = self.roll_dice()
        
        total = dice1 + dice2 + dice3
        
        result_text = f"Dice 1: {dice1}\nDice 2: {dice2}\nDice 3: {dice3}\nTotal: {total}"
        
        if self.tai_xiu(guess, total):
            winnings = bet * 1.98
            result_text += f"\nCongratulations! You guessed correctly.\nYou win {winnings} coins."
        else:
            result_text += "\nSorry, you guessed wrong. You lose your bet."
        
        messagebox.showinfo("Game Result", result_text)

    def create_widgets(self):
        tk.Label(self.root, text="Welcome to Sunwin!", font=("Helvetica", 16)).pack(pady=10)
        
        tk.Label(self.root, text="Enter your guess (tai or xiu):").pack()
        tk.Entry(self.root, textvariable=self.player_guess).pack()
        
        tk.Label(self.root, text="Enter your bet amount:").pack()
        tk.Entry(self.root, textvariable=self.bet_amount).pack()
        
        tk.Button(self.root, text="Roll Dice", command=self.play_game).pack(pady=10)
        
        tk.Label(self.root, text="Note: Tai (11-18) or Xiu (3-10)").pack()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TaiXiuGame(root)
    root.mainloop()
