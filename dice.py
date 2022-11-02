import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import random
import itertools

window=tk.Tk()
window.title("Dice!")
# window.geometry("250x350")
window.configure(bg="#eee")



intro = tk.Label(
    window,
    text="Welcome To The Dice!",
    # bg="#FF0000",
    fg="#3f51b5",
    font = ('Georgia', 14, 'bold')
)
intro.grid(row=0,column=0,columnspan=4,sticky="we",pady=5)
invite = tk.Label(
    window,
    text="Click To Roll A Dice ...",
    # bg="#FF0000",
    fg="#323133",
    font = ('', 8, 'bold')
)
invite.grid(row=1,column=0,columnspan=4,sticky="w",padx=(10,0),pady=5)


first_img_path ="0.png"
second_img_path ="0.png"


first_dice_image = ImageTk.PhotoImage(Image.open(first_img_path))
first_dice_label = tk.Label(window,image=first_dice_image)
first_dice_label.grid(row=2,column=0,sticky="w",pady=5)

second_dice_image = ImageTk.PhotoImage(Image.open(second_img_path))
second_dice_label = tk.Label(window,image=second_dice_image)
second_dice_label.grid(row=2,column=1,sticky="e",pady=5)

label_result = tk.Label(
window,
text="You Didn't Rolled Any Dices!",
)

def roll_dice():
    dice_numbers = list(range(1,7))
    combinations = list(itertools.product(dice_numbers, repeat= 2))
    rolled_dice = random.choice(combinations)
    return rolled_dice
def update_dice(*args):
    rolled_dice = list(roll_dice())
    print(rolled_dice)

    new_img1_path =f"{rolled_dice[0]}.png"
    new_img2_path =f"{rolled_dice[1]}.png"

    new_dice_img1 = ImageTk.PhotoImage(Image.open(new_img1_path))
    new_dice_img2 = ImageTk.PhotoImage(Image.open(new_img2_path))
    
    first_dice_label.configure(image =new_dice_img1)
    second_dice_label.configure(image =new_dice_img2)

    first_dice_label.image = new_dice_img1
    second_dice_label.image = new_dice_img2

    label_result["text"] = f"Your Dices Are : {rolled_dice[0]} And {rolled_dice[1]}  "




roll_button = ttk.Button(
    window,
    text="Roll A Dice!",
    command=update_dice,
)

label_result.grid(row=4,column=0,columnspan=2,sticky="we")

roll_button.grid(row=5,column=0,columnspan=2,sticky="we",padx=8,pady=(5,5))


window.bind("<Return>",update_dice)
window.mainloop() 