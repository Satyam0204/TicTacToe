from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread

player = 1
turn = 0

def win(winner):
    messagebox.showinfo('Tic Tac Toe', winner+" wins!!" )
    root.destroy()

def check():
    
    
    
    
    b1=bt1['text']
    b2=bt2['text']
    b3=bt3['text']
    b4=bt4['text']
    b5=bt5['text']
    b6=bt6['text']
    b7=bt7['text']
    b8=bt8['text']
    b9=bt9['text']
    
    if (b1==b2 and b2==b3 and b1 =='O') or (b1==b2 and b2==b3 and b1 =='X'):
        bt1.config(bg="green")
        bt2.config(bg="green")
        bt3.config(bg="green")
        win(b1)
    if (b4==b5 and b5==b6 and b4 =='O') or (b4==b5 and b5==b6 and b4 =='X'):
        bt4.config(bg="green")
        bt5.config(bg="green")
        bt6.config(bg="green")
        win(b4)
    if (b7==b8 and b8==b9 and b7 =='O') or (b7==b8 and b8==b9 and b7 =='X'):
        bt7.config(bg="green")
        bt8.config(bg="green")
        bt9.config(bg="green")
        win(b7)
    if (b1==b4 and b4==b7 and b1 =='O') or (b1==b4 and b4==b7 and b1 =='X'):
        bt1.config(bg="green")
        bt4.config(bg="green")
        bt7.config(bg="green")
        win(b1)
    if (b2==b5 and b5==b8 and b2 =='O') or (b2==b5 and b5==b8 and b2 =='X'):
        bt2.config(bg="green")
        bt5.config(bg="green")       
        bt8.config(bg="green")
        win(b2)
    if (b3==b6 and b6==b9 and b3 =='O') or (b3==b6 and b6==b9 and b3 =='X'):
        bt3.config(bg="green")
        bt6.config(bg="green")
        bt9.config(bg="green")
        win(b3)
    if (b1==b5 and b5==b9 and b1 =='O') or (b1==b5 and b5==b9 and b1 =='X'):
        bt1.config(bg="green")
        bt5.config(bg="green")
        bt9.config(bg="green")
        win(b1)
    if (b3==b5 and b5==b7 and b3 =='O') or (b3==b5 and b5==b7 and b3 =='X'):
        bt3.config(bg="green")
        bt5.config(bg="green")
        bt7.config(bg="green")
        win(b3)
    elif turn ==5:
        messagebox.showinfo('Tic Tac Toe', "its a tie")
        
def clicked1():
    global player
    global turn
    if (bt1['text']==" "):
        if (player == 1):
            player=2
            turn += 1
            bt1['text']='O'
            send_play(1)
        check()

def clicked2():
    global player
    global turn
    if (bt2['text']==" "):
        if (player == 1):
            player=2
            turn += 1
            bt2['text']='O'
            send_play(2)
        check()
        
def clicked3():
    global player
    global turn
    if (bt3['text']==" "):
        if (player == 1):
            player=2
            turn += 1
            bt3['text']='O'
            send_play(3)
        check()
        
def clicked4():
    global player
    global turn
    if (bt4['text']==" "):
        if (player == 1):
            player=2
            turn += 1
            bt4['text']='O'
            send_play(4)
        check()
        
def clicked5():
    global player
    global turn
    if (bt5['text']==" "):
        if player == 1:
            player=2
            turn += 1
            bt5['text']='O'
            send_play(5)
        check()
        
def clicked6():
    global player
    global turn
    if (bt6['text']==" "):
        if( player == 1):
            player=2
            turn += 1
            bt6['text']='O'
            send_play(6)
        check()
        
def clicked7():
    global player
    global turn
    if (bt7['text']==" "):
        if (player == 1):
            player=2
            turn += 1
            bt7['text']='O'
            send_play(7)
        check()
        
def clicked8():
    global player
    global turn
    if (bt8['text']==" "):
        if (player == 1):
            player=2
            turn += 1
            bt8['text']='O'
            send_play(8)
        check()
        
def clicked9():
    global player
    global turn
    if (bt9['text']==" "):
        if (player == 1):
            player=2
            turn += 1
            bt9['text']='O'
            send_play(9)
        check()

def send_play(n):
    n = str(n)
    n = n.encode() 
    c.send(n)
    
def handle_play(n):
    global player
    n = n-1
    button_list [n]["text"] = "X"
    player = 1

def apply_play(p):
    p = p.decode()
    p = int(p)
    handle_play(p)

root = Tk()

root.title('Server: tic tac toe')


lb1 = Label(root, text='player1: O', font=('Helvetica','15'))
lb1.grid(row=0, column=0)    

button_list = list()

bt1=Button(root, text=" ",width = 6, height = 3,font=('Helvetica',20),command = clicked1)


bt2=Button(root, text=" ",width = 6, height = 3,font=('Helvetica',20),command = clicked2)


bt3=Button(root, text=" ",width = 6, height = 3,font=('Helvetica',20),command = clicked3)


bt4=Button(root, text=" ",width = 6, height = 3,font=('Helvetica',20),command = clicked4)


bt5=Button(root, text=" ",width = 6, height = 3,font=('Helvetica',20),command = clicked5)


bt6=Button(root, text=" ",width = 6, height = 3,font=('Helvetica',20),command = clicked6)


bt7=Button(root, text=" ",width = 6, height = 3,font=('Helvetica',20),command = clicked7)


bt8=Button(root, text=" ",width = 6, height = 3,font=('Helvetica',20),command = clicked8)


bt9=Button(root, text=" ",width = 6, height = 3,font=('Helvetica',20),command = clicked9)

bt1.grid(row = 0, column=1)
bt2.grid(row = 0, column=2)
bt3.grid(row = 0, column=3)

bt4.grid(row = 1, column=1)
bt5.grid(row = 1, column=2)
bt6.grid(row = 1, column=3)

bt7.grid(row = 2, column=1)
bt8.grid(row = 2, column=2)
bt9.grid(row = 2, column=3)


button_list.append(bt1)
button_list.append(bt2)
button_list.append(bt3)
button_list.append(bt4)
button_list.append(bt5)
button_list.append(bt6)
button_list.append(bt7)
button_list.append(bt8)
button_list.append(bt9)

s = socket(AF_INET,SOCK_STREAM)


s.bind(('192.168.29.77', 5050))
s.listen(5)
c=None

def handle_client():
    global player
    global c
    player = 1
    c,ad = s.accept()
    receive = Thread(target = receive_message, args = [c,])
    receive.start()
    
def receive_message(c):
    while True:
        p = c.recv(10)
        apply_play(p)

acc = Thread(target=handle_client)
acc.start()
    
root.mainloop()