from tkinter import *
from tkinter import ttk
import time
import datetime
import functions
from functions import *



def clock_time():
    time=datetime.datetime.now()
    #time=(time.strftime('%H:%M:%S'))
    time=(time.strftime('%Y %m %d \n %H:%M:%S \n %A'))
    #txt.set(time)
    root.after(1000,clock_time)

def btn(numbers):
    global operator
    operator= operator + str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator =''
    txt_input.set('')
    Display.insert(0,'Start Calculating.....')

def equal():
    global operator
    sumup=float(eval(operator))
    txt_input.set(sumup)
    operator= ' '




def Totalcost():
    varme1=mealdicator.get()
    varme2=meal1.get()
    if varme1 == 'Fried Rice':
        varme3=(varme2 * 1.8)
        cost.set(varme3)

    elif varme1 == 'Banku with Tilapia':
        varme3=(varme2 * 2.0)
        cost.set(varme3)

    elif varme1 == 'Riceball':
        varme3=(varme2 * 1.0)
        cost.set(varme3)

    elif varme1 == 'Waakye':
        varme3=(varme2 * 2.0)
        cost.set(varme3)
    else:
        varme3=(varme2 * 0.0)
        cost.set(varme3)

    ####### cost of drink  #########

    vardi1=drinkdicator.get()
    vardi2=drink.get()

    if vardi1 == 'Bottled Water':
        vardi3=(vardi2 * 1.0)
        drink1.set(vardi3)

    elif vardi1 == 'Coca Cola':
        vardi3=(vardi2* 2.0)
        drink1.set(vardi3)

    elif vardi1 == 'Red Wine':
        vardi3=(vardi2 * 2.0)
        drink1.set(vardi3)

    elif vardi1 == 'Heineken':
        vardi3=(vardi2 * 5.0)
        drink1.set(vardi3)
    else:
        vardi3=(vardi2 * 0.0)
        drink1.set(vardi3)



    num1=float(cost.get())
    num2=float(drink.get())
    delivery= (num1+num2) * 0.5

    room=v.get()
    null=0.0
    rvip=10
    rvip1=delivery + rvip


    rnormal=5
    rnormal1=delivery + rnormal

    if room == 1:
        if chk1 ==1:
            servicecost.set(rvip1)
            devcost.set(delivery)
            roomcost.set(10)
        else:
            servicecost.set(null)
            devcost.set(null)
            roomcost.set(10)
    elif room == 2:
        if chk1 ==1:
            servicecost.set(rnormal1)
            devcost.set(delivery)
            roomcost.set(5)
        else:
            servicecost.set(null)
            devcost.set(null)
            roomcost.set(5)

        
    elif room == 3:
        if chk1 ==1:
            servicecost.set(null)
            devcost.set(null)
            roomcost.set(null)
        else:
            servicecost.set(null)
            devcost.set(null)
            roomcost.set(null)




#####################
    num3=float(devcost.get())
    num4=float(roomcost.get())
    num5=float(servicecost.get())

    mytotal=num1 + num2 + num3 + num4 + num5
    totalcost.set(mytotal)

    finaltotal=f'total is $ {mytotal}'
    Display.delete(0,END)
    Display.insert(0,finaltotal)

    num6=totalcost.get()
    if num6 <= '0.0':
        Display.delete(0,END)
        Display.insert(0,'make an order......')





def Convertor():
    var2=var1.get()
    var3=indicator.get()
    if var3 == 'Ghana':
        Display.delete(0,END)
        var4= ('Cedi',var2 * 5.00)
        Display.insert(0,var4)

    elif var3 == 'France':
        Display.delete(0,END)
        var4= ('Euro',var2 * 0.81)
        Display.insert(0,var4)
    
    elif var3 == 'Nigeria':
        Display.delete(0,END)
        var4= ('Naira',var2 * 369.00)
        Display.insert(0,var4)

    elif var3 == 'China':
        Display.delete(0,END)
        var4= ('Yuan',var2 * 0.81)
        Display.insert(0,var4)
    else:
        Display.delete(0,END)
        Display.insert(0,'Error,Select a country!')

def hotel():
    Display.delete(0,END)
    Display.insert(0,'hotel managemnt sys')

def powered():
    Display.delete(0,END)
    Display.insert(0,'Powered by python')

def reset():
    Display.delete(0,END)
    Display.insert(0,'Resetting.....')
    Display.after(2000,hotel)
    Display.after(4000,powered)
    Display.after(6000,rest)
        


def rest():
    clear()
    Display.delete(0,END)
    Display.insert(0,'Hello and welcome....')
    servicecost.set(0.0)
    devcost.set(0.0)
    roomcost.set(0.0)
    mealdicator.set(value='Delicious food')
    indicator.set(value='choose country')
    txtmealqty.delete(END,0)
    txtmealqty.insert(END,0)
    txtdrinkqty.delete(END,0)
    txtdrinkqty.insert(END,0)
    drinkdicator.set(value='Fresh Drinks')
    drink.set(0.0)
    cost.set(0.0)
    chk.set(0.0)
    v.set(3) 
    totalcost.set(0.0)
    drink1.set(0.0)
    meal1.set(0.0)



def clear():
    Display.delete(0,END)
    roomcost.set('')
    totalcost.set('')
    servicecost.set('')
    drink1.set('')
    devcost.set('')
    cost.set('')

    
def stop():
    root.destroy()
           
def exit():
    Display.delete(0,END)
    Display.insert(0,'Thanks for your patronage')
    Display.after(3000,stop)


    


           
        




     

root=Tk()
width_v=root.winfo_screenwidth()
height_v=root.winfo_screenheight()

root.geometry(f'{width_v}x{height_v}')
root.title('Hotel Management System')



#########################screen#################,
Tops=Frame(root,width=1600,height=100,bg='blue',relief=SUNKEN)
Tops.pack(side=TOP)


f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=800,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

f3=Frame(root,width=35,height=700,relief=SUNKEN)
f3.pack(side=LEFT)

f4=Frame(root,width=100,height=700,relief=SUNKEN,bg='red')
f4.pack(side=LEFT)



############# Main Screen #######################
txt_input=StringVar(value='Alabama Hotel..........................')
Display=Entry(Tops,bg='blue',fg='white',bd=50,
font=('arial',87,'bold'),textvariable=txt_input,justify='right')

Display.grid(columnspan=4)


############### Date and Time #######################
#localtime=time.asctime(time.localtime(time.time()))

lblinfo=Label(f2,fg='dark blue',text=clock_time(),anchor=W,font=('arial',20,'bold'),bd=10)
lblinfo.grid(row=0,column=0,columnspan=4)



################ Row 1 #######################################
operator=''
btn7=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='7',command=lambda:btn(7)).grid(row=1,column=0)
btn8=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='8',command=lambda:btn(8)).grid(row=1,column=1)
btn9=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='9',command=lambda:btn(8)).grid(row=1,column=2)
btnc=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='c',bg='green',command=clear).grid(row=1,column=3)


################ Row 2 #######################################
btn4=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='4',command=lambda:btn(4)).grid(row=2,column=0)
btn5=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='5',command=lambda:btn(5)).grid(row=2,column=1)
btn6=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='6',command=lambda:btn(6)).grid(row=2,column=2)
btnplus=Button(f2,font=('arial',20,'bold'),padx=18,pady=5,bd=8,text='+',bg='orange',command=lambda:btn('+')).grid(row=2,column=3)



################ Row 3 #######################################
btn1=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='1',command=lambda:btn(1)).grid(row=3,column=0)
btn2=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='2',command=lambda:btn(2)).grid(row=3,column=1)
btn3=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='3',command=lambda:btn(3)).grid(row=3,column=2)
btnminus=Button(f2,font=('arial',20,'bold'),padx=23,pady=8,bd=8,text='-',bg='orange',command=lambda:btn('-')).grid(row=3,column=3)


################ Row 4 #######################################
btn0=Button(f2,font=('arial',20,'bold'),padx=15,pady=5,bd=8,text='0',command=lambda:btn(0)).grid(row=4,column=0)
btndot=Button(f2,font=('arial',20,'bold'),padx=21,pady=5,bd=8,text='.',bg='orange',command=lambda:btn('.')).grid(row=4,column=1)
btndivision=Button(f2,font=('arial',20,'bold'),padx=20,pady=5,bd=8,text='/',bg='orange',command=lambda:btn('/')).grid(row=4,column=2)
btnmultiply=Button(f2,font=('arial',20,'bold'),padx=19,pady=5,bd=8,text='x',bg='orange',command=lambda:btn('*')).grid(row=4,column=3)


################ Row 5 #######################################
btnequals=Button(f2,font=('arial',20,'bold'),padx=64,pady=2,bd=8,text='=',bg='green',command=equal).grid(row=5,column=0,columnspan=2)
btnopenbracket=Button(f2,font=('arial',20,'bold'),padx=19,pady=2,bd=8,text='(',bg='orange',command=lambda:btn('(')).grid(row=5,column=2)
btnclosebracket=Button(f2,font=('arial',20,'bold'),padx=23,pady=2,bd=8,text=')',bg='orange',command=lambda:btn(')')).grid(row=5,column=3)

########################## Choosing Meal #############################
meal1=IntVar()
mealdicator=StringVar(value='Delicious Meal')

lblmeal=Label(f1,font=('arial',16,'bold'),text='Choose Meal:',anchor=W)
lblmeal.grid(row=0,column=0)
txtmeal=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=mealdicator)
txtmeal['values']=('Fried Rice','Banku with Tilapia','Riceball','Waakye')
txtmeal.grid(row=0,column=1)


lblmealqty=Label(f1,font=('arial',16,'bold'),text='Qty. Of Meal:',anchor=W)
lblmealqty.grid(row=1,column=0)
txtmealqty=Entry(f1,bg='white',bd=5,
font=('arial',16,'bold'),textvariable=meal1,justify='right')
txtmealqty.grid(row=1,column=1)


########################## Choosing Drink #############################
drink=IntVar()
drinkdicator=StringVar(value='Fresh Drinks')

lbldrink=Label(f1,font=('arial',16,'bold'),text='Choose Drink:',anchor=W)
lbldrink.grid(row=2,column=0)
txtdrink=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=drinkdicator)
txtdrink['values']=('Bottled Water','Coca Cola','Red Wine','Heineken')
txtdrink.grid(row=2,column=1)


lbldrinkqty=Label(f1,font=('arial',16,'bold'),text='Qty. Of Drink:',anchor=W)
lbldrinkqty.grid(row=3,column=0)
txtdrinkqty=Entry(f1,bg='white',bd=5,
font=('arial',16,'bold'),textvariable=drink,justify='right')
txtdrinkqty.grid(row=3,column=1)


####################### order delivery ############################
lbldelivery=Label(f1,font=('arial',16,'bold'),text='Order Delivery',anchor=W)
lbldelivery.grid(row=4,column=0)

chk=IntVar()
chk1=Checkbutton(f1,text='Yes',font=('arial',16,'bold'),variable=chk)
chk1.grid(row=4,column=1)


###################### Booking a room #############################
v=IntVar()
v.set(3)


lblradio=Label(f1,text='Book a room',font=('arial',16,'bold'),anchor=W)
lblradio.grid(row=5,column=0)

myradios=Radiobutton(f1,text='VIP',font=('arial',16,'bold'),variable=v,value=1)
myradios.grid(row=5,column=1,sticky=W)
myradios=Radiobutton(f1,text='Normal',font=('arial',16,'bold'),variable=v,value=2)
myradios.grid(row=5,column=1)
myradios=Radiobutton(f1,text='No',font=('arial',16,'bold'),variable=v,value=3)
myradios.grid(row=5,column=1,sticky=E)



#########################display of cost######################
cost=StringVar()
lblmeal=Label(f1,font=('arial',16,'bold'),text='Cost of meal',anchor=W)
lblmeal.grid(row=0,column=2)
txtmeal1=Entry(f1,bg='blue',bd=5,
font=('arial',16,'bold'),textvariable=cost,justify='right',insertwidth=4,fg='white')
txtmeal1.grid(row=0,column=3)


drink1=StringVar()
lbldrink1=Label(f1,font=('arial',16,'bold'),text='Cost of Drink',anchor=W)
lbldrink1.grid(row=1,column=2)
txtdrink1=Entry(f1,bg='blue',bd=5,
font=('arial',16,'bold'),textvariable=drink1,justify='right',insertwidth=4,fg='white')
txtdrink1.grid(row=1,column=3)



devcost=StringVar()
lbldev=Label(f1,font=('arial',16,'bold'),text='Delivery Cost',anchor=W)
lbldev.grid(row=2,column=2)
txtdev=Entry(f1,bg='blue',bd=5,
font=('arial',16,'bold'),textvariable=devcost,justify='right',insertwidth=4,fg='white')
txtdev.grid(row=2,column=3)



roomcost=StringVar()
lblroom=Label(f1,font=('arial',16,'bold'),text='Cost of Room',anchor=W)
lblroom.grid(row=3,column=2)
txtroom=Entry(f1,bg='blue',bd=5,
font=('arial',16,'bold'),textvariable=roomcost,justify='right',insertwidth=4,fg='white')
txtroom.grid(row=3,column=3)


servicecost=StringVar()
lblservice=Label(f1,font=('arial',16,'bold'),text='Service Fee',anchor=W)
lblservice.grid(row=4,column=2)
txtservice=Entry(f1,bg='blue',bd=5,
font=('arial',16,'bold'),textvariable=servicecost,justify='right',insertwidth=4,fg='white')
txtservice.grid(row=4,column=3)

totalcost=StringVar()
lbltotal=Label(f1,font=('arial',16,'bold'),text='Total Cost',anchor=W)
lbltotal.grid(row=5,column=2)
txttotal=Entry(f1,bg='blue',bd=5,
font=('arial',16,'bold'),textvariable=totalcost,justify='right',insertwidth=4,fg='white')
txttotal.grid(row=5,column=3)

var1=IntVar()
indicator=StringVar(value='choose a country')



lblconcu=Label(f1,font=('arial',16,'bold'),text=('Currency Convertor'.center(50,'-')),anchor=W)#text=('Currency Convertor'.center(20,'-'))'-------------Currency convertor--------------',
lblconcu.grid(row=6,column=0,columnspan=4)

print( ' ')

#CHOOSING THE COUNTRY 
lblcountry=Label(f1,font=('arial',16,'bold'),text='Nationality',anchor=W)#text=('Currency Convertor'.center(20,'-'))'-------------Currency convertor--------------',
lblcountry.grid(row=7,column=0)
#lblcountry=Label(f1,font=('arial',16,'bold'),text='Choose Drink:',anchor=W)
#lblcountry.grid(row=2,column=0)
txtcountry=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=indicator)
txtcountry['values']=('Ghana','France','Nigeria','China')
txtcountry.grid(row=7,column=1)



#TYPING THE AMOUNT OF MONEY YOU WANT TO CONVERT

var1=IntVar(value=0)
lblamount=Label(f1,font=('arial',16,'bold'),text='Amount($)',anchor=W)
lblamount.grid(row=7,column=2)
txtamount=Entry(f1,bg='blue',bd=5,
font=('arial',16,'bold'),textvariable=var1,justify='right',insertwidth=4,fg='white')
txtamount.grid(row=7,column=3)

########################## Adding a photo or logo #########
photo=PhotoImage(file='iicons.png')

myphoto=Label(f1,image=photo)
myphoto.grid(row=9,column=0)



########################## Adding control buttons #############
btnconvert=Button(f1,font=('arial',20,'bold'),padx=10,pady=4,bd=5,text='Convert',fg='white',bg='orange',width=5,command=Convertor)
btnconvert.grid(row=9,column=2)


btntotal=Button(f4,font=('arial',20,'bold'),bd=5,text='Total',fg='white',bg='orange',width=5,command=Totalcost)
btntotal.grid(row=0,column=0)

btnclear=Button(f4,font=('arial',20,'bold'),bd=5,text='Clear',fg='white',bg='blue',width=5,command=clear)
btnclear.grid(row=1,column=0)

btnreset=Button(f4,font=('arial',20,'bold'),bd=5,text='Reset',fg='white',bg='green',width=5,command=reset)
btnreset.grid(row=2,column=0)

btnexit=Button(f4,font=('arial',20,'bold'),bd=5,text='Exit',fg='white',bg='red',width=5,command=exit)
btnexit.grid(row=3,column=0)

#rol_text=StringVar()
#txtscrol=Entry(f1,bg='blue',bd=10,
#font=('arial',16,'bold'),textvariable=scrol_text,justify='right',width=32,fg='white')
#txtscrol.grid(row=0,column=0,columnspan=4)


root.mainloop()