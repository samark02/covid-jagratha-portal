from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import random

mydb = mysql.connector.connect(host="localhost",user="root",password="samar",database="cp")
mycursor = mydb.cursor()


def main():
    def add():
        def submit():
                a,b,c,d,e=ename.get(),evehicle.get(),efrom.get(),eto.get(),eno.get()
                a,b,c,d,e=a.upper(),b.upper(),c.upper(),d.upper(),e.upper()
                
                qry="INSERT INTO vehicle (name,vehicle,start,end,number) VALUES(%s,%s,%s,%s,%s)"
                abcde=(a,b,c,d,e)
                mycursor.execute(qry,abcde)
                mydb.commit()
                window2.destroy()
                
                #window3
                window3 =Tk()
                window3.title("Covid 19")
                window3.iconbitmap('covid.ico')
                window3.resizable(0,0)
                window3.configure(bg='#c1e4ea')
                added=Label(window3,text="Pass Issued\nHave A Safe Journey\n\nStay Safe Stay Healthy",fg='#000000',bg='#c1e4ea',font='italic')
                added.grid(row=0,column=0)
                
        #formbox
                
        #entry box
        search.grid_forget()
        add.grid_forget()
        delete.grid_forget()
        ename=Entry(window2,width=30,borderwidth=3)
        evehicle=Entry(window2,width=30,borderwidth=3)
        efrom=Entry(window2,width=30,borderwidth=3)
        eto=Entry(window2,width=30,borderwidth=3)
        eno=Entry(window2,width=30,borderwidth=3)

        ename.grid(row=1,column=1,padx=10,pady=5)
        evehicle.grid(row=2,column=1,padx=10,pady=5)
        efrom.grid(row=3,column=1,padx=10,pady=5)
        eto.grid(row=4,column=1,padx=10,pady=5)
        eno.grid(row=5,column=1,padx=10,pady=5)
        #box name
        lname=Label(window2,text="NAME",anchor=W,fg='#000000',bg='#c1e4ea')
        lvehicle=Label(window2,text="VEHICLE NUMBER",anchor=W,fg='#000000',bg='#c1e4ea')
        lfrom=Label(window2,text="START FROM",anchor=W,fg='#000000',bg='#c1e4ea')
        lto=Label(window2,text="DESTINATION",anchor=W,fg='#000000',bg='#c1e4ea')
        lno=Label(window2,text="NO OF PEOPLE",anchor=W,fg='#000000',bg='#c1e4ea')


        lname.grid(row=1,column=0)
        lvehicle.grid(row=2,column=0)
        lfrom.grid(row=3,column=0)
        lto.grid(row=4,column=0)
        lno.grid(row=5,column=0)

        submit=Button(window2,text="Submit",command=submit,width=25,fg='#000000',bg='#ffffff',borderwidth=3)
        submit.grid(row=9,column=1,padx=10,pady=5)
    
    def search():
        def searching():
            #window3
            window3 =Tk()
            window3.title("Covid 19")
            window3.iconbitmap('covid.ico')
            window3.resizable(0,0)
            window3.configure(bg='#c1e4ea')
            nameno=name.get()
            plateno=plate.get()
            qry="select * from vehicle where name='{}' and vehicle='{}'".format(nameno,plateno)
            mycursor.execute(qry)
            result = mycursor.fetchone()
            if result != None:
                result1=Label(window3,text="NAME",bg='#c1e4ea',fg='#000000')
                result1.grid(row=0,column=0,sticky=W)
                divider=Label(window3,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=1,padx=10,sticky=W)
                
                result1=Label(window3,text="VEHICLE NUMBER",bg='#c1e4ea',fg='#000000')
                result1.grid(row=0,column=2,sticky=W)
                divider=Label(window3,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=3,padx=10,sticky=W)
                
                result1=Label(window3,text="STARTING DISTRICT",bg='#c1e4ea',fg='#000000')
                result1.grid(row=0,column=4,sticky=W)
                divider=Label(window3,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=5,padx=10,sticky=W)
                
                result1=Label(window3,text="DESTINATION DISTRICT",bg='#c1e4ea',fg='#000000')
                result1.grid(row=0,column=6,sticky=W)
                divider=Label(window3,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=7,padx=10,sticky=W)
                
                result1=Label(window3,text="NO OF PEOPLE",bg='#c1e4ea',fg='#000000')
                result1.grid(row=0,column=8,sticky=W)
                
                #records               
                result2=Label(window3,text=result[0],bg='#c1e4ea',fg='#000000')
                result2.grid(row=1,column=0)
                divider=Label(window3,text="|",bg='#c1e4ea',fg='#000000').grid(row=1,column=1,padx=10,sticky=W)                
                
                result2=Label(window3,text=result[1],bg='#c1e4ea',fg='#000000')
                result2.grid(row=1,column=2)
                divider=Label(window3,text="|",bg='#c1e4ea',fg='#000000').grid(row=1,column=3,padx=10,sticky=W)
                
                result2=Label(window3,text=result[2],bg='#c1e4ea',fg='#000000')
                result2.grid(row=1,column=4)
                divider=Label(window3,text="|",bg='#c1e4ea',fg='#000000').grid(row=1,column=5,padx=10,sticky=W)
                
                result2=Label(window3,text=result[3],bg='#c1e4ea',fg='#000000')
                result2.grid(row=1,column=6)
                divider=Label(window3,text="|",bg='#c1e4ea',fg='#000000').grid(row=1,column=7,padx=10,sticky=W)
                
                result2=Label(window3,text=result[4],bg='#c1e4ea',fg='#000000')
                result2.grid(row=1,column=8,sticky=W)
            else:
                result1=Label(window3,text="Pass not issued\nPlease register again",bg='#c1e4ea',fg='#000000')
                result1.grid(row=0,column=0)
        
        search.grid_forget()
        add.grid_forget()
        delete.grid_forget()

        headingl=Label(window2,text="ENTER DETAILS TO SERACH",fg='#000000',bg='#c1e4ea')
        headingl.grid(row=0,column=0,columnspan=2)

        namen=Label(window2,text="NAME : ",anchor=W,fg='#000000',bg='#c1e4ea')
        namen.grid(row=1,column=0)

        name=Entry(window2,width=30,borderwidth=3)
        name.grid(row=1,column=1,padx=5,pady=5)
        
        platen=Label(window2,text=" VEHICLE NUMBER : ",anchor=W,fg='#000000',bg='#c1e4ea')
        platen.grid(row=2,column=0)
        
        plate=Entry(window2,width=30,borderwidth=3)
        plate.grid(row=2,column=1,padx=5)
        
        searchb=Button(window2,text="Search",command=searching,width=25,bg='#ffffff',fg='#000000',borderwidth=3)
        searchb.grid(row=3,column=1,padx=5,pady=5)

    def delete():
        def deleting():
            #window3
            window3 =Tk()
            window3.title("Covid 19")
            window3.iconbitmap('covid.ico')
            window3.resizable(0,0)
            window3.configure(bg='#c1e4ea')
            nameno=name.get()
            plateno=plate.get()
            name.delete(0,END)
            plate.delete(0,END)
            qry="select * from vehicle where name='{}' and vehicle='{}'".format(nameno,plateno)
            mycursor.execute(qry)
            result = mycursor.fetchone()
            if result != None:
                qry="delete from vehicle where name='{}' and vehicle='{}'".format(nameno,plateno)
                mycursor.execute(qry)
                result = mycursor.fetchone()
                mydb.commit()
            
                if result == None:
                    result1=Label(window3,text="Your Pass is deleted",bg='#c1e4ea',fg='#000000')
                    result1.grid(row=1,column=0)
            else:
                result1=Label(window3,text="Pass not issued\n Please enter correct details.",fg='#000000',bg='#c1e4ea')
                result1.grid(row=0,column=0)
        
        search.grid_forget()
        add.grid_forget()
        delete.grid_forget()

        headingl=Label(window2,text="ENTER DETAILS TO DELETE",fg='#000000',bg='#c1e4ea')
        headingl.grid(row=0,column=0,columnspan=2)

        namen=Label(window2,text="Name : ",anchor=W,fg='#000000',bg='#c1e4ea')
        namen.grid(row=1,column=0)

        name=Entry(window2,width=30,borderwidth=3)
        name.grid(row=1,column=1,padx=5,pady=5)
        
        platen=Label(window2,text="Vehicle Number : ",anchor=W,fg='#000000',bg='#c1e4ea')
        platen.grid(row=2,column=0)
        
        plate=Entry(window2,width=30,borderwidth=3)
        plate.grid(row=2,column=1,padx=5)
        
        deleteb=Button(window2,text="Delete",command=deleting,width=25,fg='#000000',bg='#ffffff',borderwidth=3)
        deleteb.grid(row=3,column=1,padx=5,pady=5)
        
        
    #Enter window2
    window2=Tk()
    window2.title("Covid 19")
    window2.iconbitmap('covid.ico')
    window2.configure(bg='#c1e4ea')
    window2.resizable(0,0)

    search=Button(window2,text="Search A Pass",width=25,height=2,command=search,bg='#ffffff',fg='#000000')
    search.grid(row=0,column=0,padx=5,pady=2)
    add=Button(window2,text="Add A Pass",width=25,height=2,command=add,bg='#ffffff',fg='#000000')
    add.grid(row=1,column=0,padx=5,pady=2)
    delete=Button(window2,text="Delete A Pass",width=25,height=2,command=delete,bg='#ffffff',fg='#000000')
    delete.grid(row=2,column=0,padx=5,pady=2)


def facts():
    #Facts window2
    window2=Tk()
    window2.title("Covid 19")
    window2.iconbitmap('covid.ico')
    window2.resizable(0,0)
    window2.configure(bg='#c1e4ea')
    facts=["The time between exposure to covid 19 and the moment when symptoms\nstart is commonly around 5 to 6 days but can range from 1- 14 days.",
           "If you are experiencing stress, you are not alone. Right now,there\nare many other people in your community and all around the\nworld who are also struggling with stress.",
           "8 out of every 10 people with Covid-19 will have mild symptoms",
           "Only 1 in 6 people will become severely ill & need hospital care",
           "Water or swimming does not transmit the COVID-19 virus",
           "Studies show hydroxychloroquine does not have clinical benefits\nin treating COVID-19.",
           "Being able to hold your breath for 10 seconds or more without\ncoughing or feeling discomfort DOES NOT mean you are free from\nCOVID-19 or any other lung disease.",
           "Drinking methanol, ethanol or bleach DOES NOT prevent or cure\nCOVID-19 and can be extremely dangerous",
           "There is NO evidence that companion animals/pets such as dogs\nor cats can transmit the coronavirus.",
           "Vaccines against pneumonia, such as pneumococcal vaccine and\nHaemophilus influenzae type b (Hib) vaccine, DO NOT provide\nprotection against the coronavirus.",
           "Antibiotics DO NOT work against viruses, antibiotics\nonly work against bacteria.",
           "You can recover from COVID-19. Catching COVID-19 DOES NOT mean\nyou will have it for life",
           "COVID-19 can survive temperatures higher than 25C.\nYou can catch it no matter how sunny and warm it is."]
    i=random.choice(facts)
    fact1=Label(window2,text=i,anchor=W,fg='#000000',bg='#c1e4ea')
    fact1.grid(row=0,column=0,columnspan=3)

    close=Button(window2,text="Close",width=15,command=window2.destroy,bg='#ffffff',fg='#000000')
    close.grid(row=5,column=1,pady=8)

def insert():
    window3= Tk()
    window3.title("Covid 19")
    window3.configure(bg='#c1e4ea')
    window3.iconbitmap('covid.ico')
    p="Important Numbers :"
    z="Covid Call Center : 1075 / 0471-2552056"
    y="Ambulance : 112\n\n"
    s ="To register for Covid-19 Vaccination:"
    c="\tLog on to cowin.gov.in"
    a="\nImportant things to note:"
    d="\t> Always double mask yourself while going out"
    e="\t> Keep atleast 6 ft distance with people"
    f="\t> Sanitize or wash your hand regularly\n"
    l="TAKE CARE"
    K="THANK YOU"
    Label (window3,text=p,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=2,column=0,sticky=W)
    Label (window3,text=z,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=3,column=0,sticky=W)
    Label (window3,text=y,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=4,column=0,sticky=W)
    Label (window3,text=s,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=5,column=0,sticky=W)
    Label (window3,text=c,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=6,column=0,sticky=W)
    Label (window3,text=a,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=7,column=0,sticky=W)
    Label (window3,text=d,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=8,column=0,sticky=W)
    Label (window3,text=e,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=9,column=0,sticky=W)
    Label (window3,text=f,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=10,column=0,sticky=W)
    Label (window3,text=l,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=11,column=0,sticky=W)
    Label (window3,text=K,fg='#000000',bg='#c1e4ea',font="none 12").grid(row=12,column=0,sticky=W)
def insa():
    def show():
        window1.destroy()
        window2=Tk()
        window2.title("Covid 19")
        window2.iconbitmap('covid.ico')
        window2.resizable(0,0)
        window2.configure(bg='#c1e4ea')
        xds=clicked.get()
        if xds=="Kannur":
            mycursor.execute("SELECT * FROM kannur")
            p=mycursor.fetchall()
            mycursor.execute("select * from kannur")
            c=2
            for x in range (0,len(p)):
                result = mycursor.fetchone()
                label=Label(window2,text=result[0],bg='#c1e4ea',fg='#000000').grid(row=c,column=0,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=1,padx=10,sticky=W)
                label=Label(window2,text=result[1],bg='#c1e4ea',fg='#000000').grid(row=c,column=2,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=3,padx=10,sticky=W)
                label=Label(window2,text=result[2],bg='#c1e4ea',fg='#000000').grid(row=c,column=4,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=5,padx=10,sticky=W)
                label=Label(window2,text=result[3],bg='#c1e4ea',fg='#000000').grid(row=c,column=6,padx=10,sticky=W)
                c+=1
            result1=Label(window2,text="Hospital Name",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=0)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=1,padx=10,sticky=W)
            
            result1=Label(window2,text="Phone",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=2)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=3,padx=10,sticky=W)
            
            result1=Label(window2,text="Address",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=4)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=5,padx=10,sticky=W)
            
            result1=Label(window2,text="Private/Govt",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=6)

            result1=Label(window2,text="",bg='#c1e4ea',fg='#000000')
            result1.grid(row=1,column=3)
        if xds=="Ernakulam":
            mycursor.execute("SELECT * FROM ernakulam")
            p=mycursor.fetchall()
            mycursor.execute("select * from ernakulam")
            c=2
            for x in range (0,len(p)):
                result = mycursor.fetchone()
                label=Label(window2,text=result[0],bg='#c1e4ea',fg='#000000').grid(row=c,column=0,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=1,padx=10,sticky=W)
                label=Label(window2,text=result[1],bg='#c1e4ea',fg='#000000').grid(row=c,column=2,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=3,padx=10,sticky=W)
                label=Label(window2,text=result[2],bg='#c1e4ea',fg='#000000').grid(row=c,column=4,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=5,padx=10,sticky=W)
                label=Label(window2,text=result[3],bg='#c1e4ea',fg='#000000').grid(row=c,column=6,padx=10,sticky=W)
                c+=1
            result1=Label(window2,text="Hospital Name",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=0)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=1,padx=10,sticky=W)
            
            result1=Label(window2,text="Phone",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=2)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=3,padx=10,sticky=W)
            
            result1=Label(window2,text="Address",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=4)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=5,padx=10,sticky=W)
            
            result1=Label(window2,text="Private/Govt",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=6)

            result1=Label(window2,text="",bg='#c1e4ea',fg='#000000')
            result1.grid(row=1,column=3)
        if xds=="Trivandrum":
            mycursor.execute("SELECT * FROM trivandrum")
            p=mycursor.fetchall()
            mycursor.execute("select * from trivandrum")
            c=2
            for x in range (0,len(p)):
                result = mycursor.fetchone()
                label=Label(window2,text=result[0],bg='#c1e4ea',fg='#000000').grid(row=c,column=0,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=1,padx=10,sticky=W)
                label=Label(window2,text=result[1],bg='#c1e4ea',fg='#000000').grid(row=c,column=2,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=3,padx=10,sticky=W)
                label=Label(window2,text=result[2],bg='#c1e4ea',fg='#000000').grid(row=c,column=4,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=5,padx=10,sticky=W)
                label=Label(window2,text=result[3],bg='#c1e4ea',fg='#000000').grid(row=c,column=6,padx=10,sticky=W)
                c+=1
            result1=Label(window2,text="Hospital Name",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=0)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=1,padx=10,sticky=W)
            
            result1=Label(window2,text="Phone",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=2)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=3,padx=10,sticky=W)
            
            result1=Label(window2,text="Address",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=4)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=5,padx=10,sticky=W)
            
            result1=Label(window2,text="Private/Govt",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=6)

            result1=Label(window2,text="",bg='#c1e4ea',fg='#000000')
            result1.grid(row=1,column=3)
        if xds=="Kozhikode":
            mycursor.execute("SELECT * FROM kozhikode")
            p=mycursor.fetchall()
            mycursor.execute("select * from kozhikode")
            c=2
            for x in range (0,len(p)):
                result = mycursor.fetchone()
                label=Label(window2,text=result[0],bg='#c1e4ea',fg='#000000').grid(row=c,column=0,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=1,padx=10,sticky=W)
                label=Label(window2,text=result[1],bg='#c1e4ea',fg='#000000').grid(row=c,column=2,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=3,padx=10,sticky=W)
                label=Label(window2,text=result[2],bg='#c1e4ea',fg='#000000').grid(row=c,column=4,padx=10,sticky=W)
                label=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=c,column=5,padx=10,sticky=W)
                label=Label(window2,text=result[3],bg='#c1e4ea',fg='#000000').grid(row=c,column=6,padx=10,sticky=W)
                c+=1
            result1=Label(window2,text="Hospital Name",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=0)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=1,padx=10,sticky=W)
            
            result1=Label(window2,text="Phone",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=2)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=3,padx=10,sticky=W)
            
            result1=Label(window2,text="Address",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=4)
            divider=Label(window2,text="|",bg='#c1e4ea',fg='#000000').grid(row=0,column=5,padx=10,sticky=W)
            
            result1=Label(window2,text="Private/Govt",bg='#c1e4ea',fg='#000000')
            result1.grid(row=0,column=6)

            result1=Label(window2,text="",bg='#c1e4ea',fg='#000000')
            result1.grid(row=1,column=3)
    window1=Tk()
    window1.title("Covid 19")
    window1.iconbitmap('covid.ico')
    window1.resizable(0,0)
    window1.configure(bg='#57D6B4')
    num1=['Ernakulam',
          'Kannur',
          'Trivandrum',
          'Kozhikode',
           ]
    clicked=StringVar(window1)
    clicked.set(num1[0])
    drop12=OptionMenu(window1,clicked,*num1)
    drop12.grid(row=1,column=0,sticky=W,padx=10,pady=10)
    drop12.configure(bg='#ffffff')
    drop12["menu"].config(bg="#ffffff")
    showScores = Button(window1, text="Show", width=15, command=show,bg='#ffffff',fg='#000000',padx=10,pady=10).grid(row=4, column=0)
#main window
window=Tk()
window.title("Covid 19")
window.iconbitmap('covid.ico')
window.resizable(0,0)

img1 = Image.open("home.jpg")
resized1= img1.resize((310,310),Image.ANTIALIAS)
photo= ImageTk.PhotoImage(resized1)
pic=Label (window,image=photo)
pic.grid(row=0,column=0,columnspan=2)

#enter button
img1 = Image.open("vehicle.png")
resized1= img1.resize((150,85),Image.ANTIALIAS)
new_img1= ImageTk.PhotoImage(resized1)

enter=Button(window,command=main,image=new_img1)
enter.grid(row=1,column=0)

#fact button
img4 = Image.open("facts.png")
resized4= img4.resize((150,85),Image.ANTIALIAS)
new_img4= ImageTk.PhotoImage(resized4)

fact=Button(window,image=new_img4,command=facts)
fact.grid(row=1,column=1)

#help button
img3 = Image.open("help.png")
resized3= img3.resize((150,85),Image.ANTIALIAS)
new_img3= ImageTk.PhotoImage(resized3)
Button(window,command=insert,image=new_img3).grid(row=4,column=0)

#hospital button
img2 = Image.open("hospital.png")
resized2= img2.resize((150,85),Image.ANTIALIAS)
new_img2= ImageTk.PhotoImage(resized2)
Button(window,image=new_img2,command=insa).grid(row=4,column=1)


window.mainloop()
