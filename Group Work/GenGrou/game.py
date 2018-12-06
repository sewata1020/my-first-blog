#ゲーム本体
import tkinter as tk

window = tk.Tk()
window.geometry('800x500')
window.resizable(width=False,height=False)     

def motion(mouse):
    
    canvas.delete("player")
    canvas.create_rectangle(mouse.x-20,mouse.y-20,mouse.x+20,mouse.y+20,fill="white",tag="player")

def game():
    canvas = tk.Canvas(window,bd=2,relief="ridge")
    canvas.pack()
    window.bind("<Motion>",motion)
    window.mainloop()    
