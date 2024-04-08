import tkinter as tk

window = tk.Tk()

window.title("Disappearing Text App")
window.geometry('520x300')


def clear_input():
    user_entry.delete('1.0', 'end-1c')

def check_user_writing(event):
    input = user_entry.get("1.0",'end-1c')
    print(input)
    if input == "":
        user_entry.after(5000, clear_input)
        

user_entry = tk.Text(window, height=19, width=65)
user_entry.pack()
user_entry.bind('<Key>', check_user_writing)
user_entry.focus_set()
check_user_writing(user_entry)



    

window.mainloop()