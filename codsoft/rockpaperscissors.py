import tkinter as tk
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

def play(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Instructions label
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instructions_label.pack(pady=10)

# Buttons for player choices
rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
