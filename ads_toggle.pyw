import tkinter as tk
import sys
import os
import subprocess

def on_button_click(flag):
    
    text = ''
    scr = ''
    if flag == 1:
        text = entry1.get().lower()
        scr = "monitor.ahk"
    else:
        text = entry2.get().lower()
        scr = "ads.ahk"

    i = 0 
    with open(scr, "r") as file:
        content = file.readlines()     

    for line in content:
            i = i + 1
            #print(i)
            #print(line)
            if line.strip() == ";checkpoint":
                break
                
    content[i] = text + "::" + "\n"
    res_content = ''
    for line in content:
         res_content = res_content + line 
    
    #print(res_content)
    with open(scr, "w") as file:
        file.write(res_content)
        file.flush()


def on_run_button_click():
     process = subprocess.Popen("monitor.ahk", shell=True)
     root.destroy()
     exit()
    

def get_position_and_size(widget):
    x_position = widget.winfo_x()
    y_position = widget.winfo_y()
    width = widget.winfo_width()
    height = widget.winfo_height()
    print(f"Widget: {widget}, X: {x_position}, Y: {y_position}, Width: {width}, Height: {height}")
    

def on_closing():
    root.destroy()
    sys.exit()



root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("Toggle ADS")

window_width = 450
window_height = 450
root.geometry(f"{window_width}x{window_height}")

label1 = tk.Label(root, text="Start script:")
label1.place(x=150, y=75, width=150, height=30)
entry1 = tk.Entry(root)
entry1.place(x=200, y=100, width=60, height=30)

label2 = tk.Label(root, text="Stop script:")
label2.place(x=150, y=155, width=150, height=30)
entry2 = tk.Entry(root)
entry2.place(x=200, y=180, width=60, height=30)

button1 = tk.Button(root, text="Set", command=lambda: on_button_click(1))
button1.place(x=280, y=100, width=60, height=30)

button2 = tk.Button(root, text="Set", command=lambda: on_button_click(2))
button2.place(x=280, y=180, width=60, height=30)

run_button = tk.Button(root, text="Run", command=on_run_button_click)
run_button.place(x=180, y=235, width=100, height=30)

root.mainloop()