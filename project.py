from tkinter import*
from tkinter import messagebox
import csv

#กำหนดตัวแปรต่างๆ
mywin = Tk()
mywin.title('Cafe Cafe')
mywin.configure(background='pink')
mywin.minsize(1000,580)
mywin.maxsize(1000,580)
label = Label(mywin)
price_drink = 40
price_cake = 60
display = StringVar()
myinput = IntVar()
total = IntVar()

#ไว้แสดงผล
head1 = Label(mywin,fg = "black", text="Choose a menu",font="consolas 18",background='lime', width=20)
head1.place(x=90,y=100)

lb = Label(mywin, text = 'Enter numbers of menus',width=33, font="consolas 12",background='pink')
lb.place(x=70, y=150)

inp = Entry(mywin, textvariable=myinput, width=40)
inp.place(x=100, y=180)
inp.focus()

head2 = Label(mywin,fg = "blue", text="Drink",font="consolas 18",background='lime', width=8)
head2.place(x=50,y=220)
head3 = Label(mywin,fg = "blue", text="Cake",font="consolas 18",background='lime', width=8)
head3.place(x=350,y=220)

lbb = Label(mywin,text="Product price",font="consolas 16",background='lime', width=21)
lbb.place(x=700,y=100)
lbl= Label(mywin, textvariable=display, width=20, bg="skyblue",font="consolas 18")
lbl.place(x=700, y=150)
lbb3 = Label(mywin,text="Total price",font="consolas 16",background='lime', width=21)
lbb3.place(x=700,y=350)
lb2= Label(mywin, textvariable=total, width=20, bg="skyblue",font="consolas 18")
lb2.place(x=700, y=400)

#command
def convert_drink():
    input_no = myinput.get()
    if input_no > 0:
        price = input_no * price_drink
        display.set('{}'.format(price))
        
    else:
        display.set('0')
        

def convert_cake():
    input_no = myinput.get()
    if input_no > 0:
        price = input_no * price_cake
        display.set('{}'.format(price))
    else:
        display.set('0')
           
def how():
    global h
    messagebox.showinfo("วิธีการสั่งซื้อ่","1)ป้อนจำนวนที่ต้องการสั่ง"+"\n"+"2)กดเลือกเมนู"+"\n"+"3)โปรแกรมจะแสดงราคาของสินค้านั้น"+"\n"+"4)กด Save เพื่อเก็บค่าไว้"+"\n"+"5)เมื่อสิ้นสุดการสั่งให้กด End"+"\n"+"6)โปรแกรมจะแสดงราคาทั้งหมด")
h = Button(mywin, text="How to order",command=how, bg='red',font="consolas 10", width=15)
h.place(x=35,y=30)

def filewrite():
    try:
        with open('price.csv',"a") as fw:
            writer = csv.writer(fw,lineterminator='\n')
            writer.writerow( [display.get()] )
    except IOError as e:
        print(e)
        
def fileread():
    try:
        with open('price.csv',"r") as fr:
            reader = csv.reader(fr)
            mylist = list(reader)
        sum = 0                
        for colomn in mylist:
            sum += eval(colomn[0])
            total.set('{} THB'.format(sum))
    except IOError as e:
        print(e)

#button menu   
bt1 = Button(mywin, text='Iced coffee', width=18, bg='yellow', font="consolas 12", command=convert_drink)
bt1.place(x=20, y=280)
bt2 = Button(mywin, text='Iced cappuccino', width=18, bg='yellow', font="consolas 12", command=convert_drink)
bt2.place(x=20, y=320)
bt3 = Button(mywin, text='Iced cocoa', width=18, bg='yellow', font="consolas 12", command=convert_drink)
bt3.place(x=20, y=360)
bt4 = Button(mywin, text='Iced green tea', width=18, bg='yellow', font="consolas 12", command=convert_drink)
bt4.place(x=20, y=400)
bt5 = Button(mywin, text='Iced tea', width=18, bg='yellow', font="consolas 12", command=convert_drink)
bt5.place(x=20, y=440)
bt6 = Button(mywin, text='Chocolate cake', width=18, bg='yellow', font="consolas 12", command=convert_cake)
bt6.place(x=320, y=280)
bt7 = Button(mywin, text='Strawberry cake', width=18, bg='yellow', font="consolas 12", command=convert_cake)
bt7.place(x=320, y=320)
bt8 = Button(mywin, text='Orange cake', width=18, bg='yellow', font="consolas 12", command=convert_cake)
bt8.place(x=320, y=360)
bt9 = Button(mywin, text='Green tea cake', width=18, bg='yellow', font="consolas 12", command=convert_cake)
bt9.place(x=320, y=400)

#ปุ่มไว็ใช้เชื่อมต่อค่า list
btsv = Button(mywin, text='Save', command = filewrite, width = 13)
btsv.place(x=780, y=200)
btt = Button(mywin, text='End', command = fileread, width = 13)
btt.place(x=780, y=240)
bt = Button(mywin, text='Close', command = mywin.destroy, width = 13)
bt.place(x=780, y=450)

mywin.mainloop()

