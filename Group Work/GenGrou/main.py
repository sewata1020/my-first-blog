#main
import tkinter as tk
import subprocess as sb
import game

#start画面
root = tk.Tk()
root.title('shooting')
root.geometry('800x500')
root.resizable(width=False,height=False)   

#スタート画面用フレーム
start = tk.Frame(root,bd=2,relief="ridge")
start.pack()

game = game.game()

#ゲームスタートボタン
button = tk.Button(start,text='START!',width=50,command=game.game()) 
button.bind("<Button-1>",game.game())
button.pack()


root.mainloop()