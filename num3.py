import tkinter as tk
import random
from pygame import mixer


window = tk.Tk()
window.geometry("500x400")
window.title("Content Warning")
window.resizable(height = False, width = False)
bg_img = tk.PhotoImage(file = 'background.png')
lbl_bg = tk.Label(window, image = bg_img)
lbl_bg.place(x = 0, y = 0, relwidth = 1, relheight = 1)

title_label = tk.Label(window, text = 'KEY GENERATOR',
                       font = ('Arial', 20, 'bold'),
                       bg = "#1a1a1a", fg = 'red')
title_label.place(x = 110, y = 20)
ANIMATING = True
COLORS = ['red', 'blue', 'white', 'pink', 'yellow'] 


def music_play():
    mixer.init()
    mixer.music.load('Music content.mp3')
    mixer.music.play(-1)


def close():
    window.destroy()
    

def title_animation():
    if ANIMATING:
        color_now = random.choice(COLORS)
        title_label.config(fg = color_now)
        interval = random.randint(300, 600)
        window.after(interval, title_animation)

    
def generate():
    amount = 0
    KEY_BLOCKS = 3
    AMOUNT_KEY_BLOCK = 4
    INTERVAL_RIGHT = 35
    INTERVAL_LEFT = 45
    alphabet = {
        "A": 1, "B": 2, "C": 3, "D": 4, "F": 5, "G": 6,
        "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, 
        "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
        "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24,
        "Z": 25, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8" :8, "9": 9, "0": 0
    }
    symb_list = set(alphabet.keys())
    key = []
    while amount != KEY_BLOCKS:
        total_sum = 0
        random_elements = random.choices(list(symb_list), k = AMOUNT_KEY_BLOCK)
        for element in random_elements:
            if element in alphabet:
                total_sum += alphabet[element]
        if total_sum < INTERVAL_LEFT and total_sum > INTERVAL_RIGHT:
            key_part = ''.join(random_elements)
            key.append(key_part)
            amount += 1
    text_label = f'{str(key[0])}-{str(key[1])}-{str(key[2])}'
    label_key['text'] = text_label    
                
            
            
button_exit = tk.Button(height = 1, width = 7, bg = "#b51111",
text = 'Close', font=('Arial', 15, 'bold'), command = close)
button_exit.place(x = 410,y = 0)

label_welcome =tk. Label(width = 45, 
text = "Добро пожаловать! Сгенерировать ключ можно ниже",
font=('Arial', 13, 'bold'), bg = "#ffffff")
label_welcome.place(x=20, y=150)


label_key = tk.Label(width = 20, 
font = ('Arial', 13, 'bold'), bg = "#A29F9F")
label_key.place(x=130, y=200)


button_generate = tk.Button(height = 1, width = 10, bg = "#fffb21",
text = 'Generate key', font=('Arial', 13, 'bold'), command = generate)
button_generate.place(x=180, y=250)


if __name__ == "__main__":
    music_play()
    title_animation()
    window.mainloop()