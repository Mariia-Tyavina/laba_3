from tkinter import*
import random

window = Tk()
window.geometry("500x400")
window.resizable(height=False, width=False)
bg_img = PhotoImage(file='background.png')

lbl_bg = Label(window, image=bg_img)
lbl_bg.place(x=0, y=0,relwidth=1, relheight=1)


def close():
    window.destroy()
    
    
def generate():
    amount = 0
    INTERVAL_RIGHT = 35
    INTERVAL_LEFT = 45
    alphabet ={
        "A": 1, "B": 2, "C": 3, "D": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
        "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
        "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25,
        "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8" :8, "9": 9, "0": 0
    }
    symb_list = {
        'A','B','C','D','E','F','G','H','I','J','K','L',
        'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        '1','2','3','4','5','6','7','8','9','0'
    }
    key = []
    while amount != 3:
        total_sum = 0
        random_elements = random.choices(list(symb_list), k=4)
        for element in random_elements:
            if element in alphabet:
                total_sum += alphabet[element]
        if total_sum < INTERVAL_LEFT and total_sum > INTERVAL_RIGHT:
            key_part = ''.join(random_elements)
            key.append(key_part)
            amount += 1
    text_label = f'{str(key[0])}-{str(key[1])}-{str(key[2])}'
    label_key['text'] = text_label    
                
            
            
button_exit = Button(height=1, width=7, bg="#b51111",
text='Close', font=('Arial', 15, 'bold'), command = close)
button_exit.place(x=410,y=0)

label_welcome = Label(width=45, text="Добро пожаловать! Сгенерировать ключ можно ниже",
font=('Arial', 13, 'bold'), bg="#ffffff")
label_welcome.place(x=20,y=150)


label_key = Label(width=20, font=('Arial', 13, 'bold'), bg="#A29F9F")
label_key.place(x=130,y=200)


button_generate = Button(height=1, width=10, bg="#fffb21",
text='Generate key', font=('Arial', 13, 'bold'), command = generate)
button_generate.place(x=180,y=250)

window.mainloop()