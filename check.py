def sel_pack(v):

    if(v==1):
        tmp = Image.open("tamil nadu package.jpg")
        tmp = tmp.resize((775,550))
        tmp1 = ImageTk.PhotoImage(tmp)
        l1 = Label(image=tmp1)
        l1.place(x=380,y=185)    
    elif(v==2):
        tmp = Image.open("kerala package.jpg")
        tmp = tmp.resize((775,550))
        tmp1 = ImageTk.PhotoImage(tmp)
        l1 = Label(image=tmp1)
        l1.place(x=380,y=185)             
    elif(v==3):
        tmp = Image.open("karnataka package.jpg")
        tmp = tmp.resize((775,550))
        tmp1 = ImageTk.PhotoImage(tmp)
        l1 = Label(image=tmp1)
        l1.place(x=380,y=185) 
    elif(v==4):
        tmp = Image.open("south inida package.jpg")
        tmp = tmp.resize((775,550))
        tmp1 = ImageTk.PhotoImage(tmp)
        l1 = Label(image=tmp1)
        l1.place(x=380,y=185) 
    elif(v==5):
        tmp = Image.open("north india package.jpg")
        tmp = tmp.resize((775,550))
        tmp1 = ImageTk.PhotoImage(tmp)
        l1 = Label(image=tmp1)
        l1.place(x=380,y=185) 
    elif(v==6): 
        tmp = Image.open("all over india package.jpg")
        tmp = tmp.resize((775,550))
        tmp1 = ImageTk.PhotoImage(tmp)
        l1 = Label(image=tmp1)
        l1.place(x=380,y=185) 