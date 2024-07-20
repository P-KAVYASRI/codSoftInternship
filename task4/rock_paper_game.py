import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    global games_played, total_games
    if games_played >= total_games:
        messagebox.showinfo("Game Over", "All games completed. Please reset to start again.")
        return
    
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        global user_score
        user_score += 1
    else:
        result = "Computer wins!"
        global computer_score
        computer_score += 1
    
    games_played += 1
    
    # Update the labels with choices and result
    label_user_choice.config(text=f"Your choice: {user_choice}")
    label_computer_choice.config(text=f"Computer's choice: {computer_choice}")
    label_result.config(text=result)
    label_score.config(text=f"Score - You: {user_score}, Computer: {computer_score}")
    label_games_played.config(text=f"Games Played: {games_played}/{total_games}")

# Function to start a new game series
def start_game():
    global total_games, games_played, user_score, computer_score
    try:
        total_games = int(entry_total_games.get())
        if total_games <= 0:
            raise ValueError("Number of games must be greater than 0")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for total games.")
        return
    
    games_played = 0
    user_score = 0
    computer_score = 0
    label_user_choice.config(text="")
    label_computer_choice.config(text="")
    label_result.config(text="")
    label_score.config(text=f"Score - You: {user_score}, Computer: {computer_score}")
    label_games_played.config(text=f"Games Played: {games_played}/{total_games}")

# Function to reset the game
def reset_game():
    entry_total_games.delete(0, tk.END)
    start_game()

# Set up the main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize game variables
user_score = 0
computer_score = 0
games_played = 0
total_games = 0

# Set up the UI components
label_instruction = tk.Label(root, text="Enter number of games:")
label_instruction.pack(pady=5)

entry_total_games = tk.Entry(root)
entry_total_games.pack(pady=5)

button_start = tk.Button(root, text="Start Game", command=start_game)
button_start.pack(pady=10)

button_rock = tk.Button(root, text="Rock", width=10, command=lambda: determine_winner("rock"))
button_rock.pack(pady=5)

button_paper = tk.Button(root, text="Paper", width=10, command=lambda: determine_winner("paper"))
button_paper.pack(pady=5)

button_scissors = tk.Button(root, text="Scissors", width=10, command=lambda: determine_winner("scissors"))
button_scissors.pack(pady=5)

label_user_choice = tk.Label(root, text="")
label_user_choice.pack(pady=5)

label_computer_choice = tk.Label(root, text="")
label_computer_choice.pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=5)

label_score = tk.Label(root, text=f"Score - You: {user_score}, Computer: {computer_score}")
label_score.pack(pady=5)

label_games_played = tk.Label(root, text=f"Games Played: {games_played}/{total_games}")
label_games_played.pack(pady=5)

button_reset = tk.Button(root, text="Reset Game", command=reset_game)
button_reset.pack(pady=10)

# Run the application
root.mainloop()


