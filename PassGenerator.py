from cgitb import text
from logging import root
import random
from tkinter import *
from tkinter.tix import COLUMN

root = Tk()
root.title('Random Password Generator')
root.minsize(width=400, height=300)


def generate_pass(length, special_chars_allowed):
    chars_with_special = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_./?'
    chars_without_special = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''

    if(special_chars_allowed == 1):
        for _ in range(length):
            password += random.choice(chars_with_special)
    else:
        for _ in range(length):
            password += random.choice(chars_without_special)

    return password

def is_legit(password, special_chars_allowed):
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '.' '/', '?']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    abc = 'a b c d e f g h i g k l m n o p q r s t u v w x y z'
    abc_upper_case = abc.upper()
    abc_arr = abc.split()
    abc_upper_case_arr = abc_upper_case.split()
    num_cnt = 0
    lower_case_char = 0
    upper_case_char = 0

    if (special_chars_allowed == 1):
        special_cnt = 0 
        for _ in range(len(password)):
            if password[_] in special_chars:
                special_cnt = 1
            if password[_] in numbers:
                num_cnt = 1
            if password[_] in abc_arr:
                lower_case_char = 1
            if password[_] in abc_upper_case_arr:
                upper_case_char = 1
            if (special_cnt == 1) and (num_cnt == 1) and (lower_case_char == 1) and (upper_case_char == 1):
                return 1
        return 0
    else:
        for _ in range(len(password)):
            if password[_] in numbers:
                num_cnt = 1
            if password[_] in abc_arr:
                lower_case_char = 1
            if password[_] in abc_upper_case_arr:
                upper_case_char = 1
            if (num_cnt == 1) and (lower_case_char == 1) and (upper_case_char == 1):
                return 1
        return 0
        

def password_generator():
    length_of_password = int(len_of_pass.get())
    special_chars_allowed = int(radio.get())
    legit = 0
    while(legit == 0):
        password = generate_pass(length_of_password, special_chars_allowed)
        assert len(password) >= 4 , 'password must be at least 4 characters'
        legit = is_legit(password, special_chars_allowed)

    p.set(password)



#labels
len_of_pass = StringVar()
L1 = Label(root, text='PASSWORD LENGTH', padx=10, pady= 3, font= ('Helvetica', 10)).pack()
length_field = Entry(root, textvariable=len_of_pass).pack()
L2 = Label(root, text='SPECIAL CHARACTERS', padx=10, pady=3, font= ('Helvetica', 10)).pack()

#radio buttons
radio = StringVar()
radio.set('YES')
yes = Radiobutton(root, text = 'YES',font= ('Helvetica', 8), variable=radio, value= 1).pack()
no = Radiobutton(root, text = 'NO',font= ('Helvetica', 8), variable=radio, value=0).pack()


#define buttons
generate_button = Button(root, text='GENERATE PASSWORD',padx=10, pady=3, fg= 'black',font= ('Helvetica', 10), command=password_generator).pack(pady=10)
#printing the generated password
p=StringVar() 
ans = Entry(root, text = '',font= ('Helvetica', 14), bd = 0, state='readonly',justify='center', textvariable= p).pack(pady=20, padx=10)


root.mainloop()