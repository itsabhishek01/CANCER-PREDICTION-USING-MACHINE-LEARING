import pandas as pd
from joblib import load
from tkinter import *
##########################################################################################################################################
sc=load("scaling.joblib")
rfc=load("regressor.joblib")

def outcome():
    new=pd.DataFrame({"radius_mean":[float(a1.get())],"texture_mean":[float(a2.get())],"perimeter_mean":[float(a3.get())],"area_mean":[float(a4.get())],"smoothness_mean":[float(a5.get())],"compactness_mean":[float(a6.get())],"concavity_mean":[float(a7.get())],"concave points_mean":[float(a8.get())],"symmetry_mean":[float(a9.get())],"fractal_dimension_mean":[float(a10.get())],"radius_se":[float(a11.get())],"texture_se":[float(a12.get())],"perimeter_se":[float(a13.get())],"area_se":[float(a14.get())],"smoothness_se":[float(a15.get())],"compactness_se":[float(a16.get())],"concavity_se":[float(a17.get())],"concave points_se":[float(a18.get())],"symmetry_se":[float(a19.get())],"fractal_dimension_se":[float(a20.get())],"radius_worst":[float(a21.get())],"texture_worst":[float(a22.get())],"perimeter_worst":[float(a23.get())],"area_worst":[float(a24.get())],"smoothness_worst":[float(a25.get())],"compactness_worst":[float(a26.get())],"concavity_worst":[float(a27.get())],"concave points_worst":[float(a28.get())],"symmetry_worst":[float(a29.get())],"fractal_dimension_worst":[float(a30.get())]})
    new=sc.transform(new)
    res=rfc.predict(new)
    print(res)
    if res==0:
        result1=Label(root,text="Person is healthy",fg="WHITE",bg="green",font=("arial",45))
        result1.place(x=10,y=450)
        
    else:
      result2=Label(root,text="Person has cancer",fg="WHITE",bg="red",font=("arial",45))
      result2.place(x=10,y=450)
###########################################################################################################################################
#-------------------------------------------------------
root=Tk()
root.geometry("1000x600")
root.resizable(0,0)
root.title("Breast Cancer Prediction")
#############################################
logo = PhotoImage(file = "logo.png")
root.iconphoto(False, logo)

############################################
a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=StringVar()
a6=StringVar()
a7=StringVar()
a8=StringVar()
a9=StringVar()
a10=StringVar()
a11=StringVar()
a12=StringVar()
a13=StringVar()
a14=StringVar()
a15=StringVar()
a16=StringVar()
a17=StringVar()
a18=StringVar()
a19=StringVar()
a20=StringVar()
a21=StringVar()
a22=StringVar()
a23=StringVar()
a24=StringVar()
a25=StringVar()
a26=StringVar()
a27=StringVar()
a28=StringVar()
a29=StringVar()
a30=StringVar()
#######################################################################################################################

heading=Label(root,text="ENTER THE VALUES TO PREDICT BREAST CANCER",font=("Arial",20),fg="PURPLE")
heading.place(x=10,y=5)

r1=Label(root,text="Enter the radius mean")
r1.place(x=10,y=50)
r1e=Entry(root,textvariable=a1)
r1e.place(x=200,y=50)

t1=Label(root,text="Enter the texture mean")
t1.place(x=10,y=80)
t1e=Entry(root,textvariable=a2)
t1e.place(x=200,y=80)

p1=Label(root,text="Enter the Perimeter mean")
p1.place(x=10,y=110)
p1e=Entry(root,textvariable=a3)
p1e.place(x=200,y=110)

a1l=Label(root,text="Enter the Area Mean")
a1l.place(x=10,y=140)
a1e=Entry(root,textvariable=a4)
a1e.place(x=200,y=140)

s1=Label(root,text="Enter the Smoothness Mean")
s1.place(x=10,y=170)
s1e=Entry(root,textvariable=a5)
s1e.place(x=200,y=170)

c1=Label(root,text="Enter the compactness mean")
c1.place(x=10,y=200)
c1e=Entry(root,textvariable=a6)
c1e.place(x=200,y=200)

co1=Label(root,text="Enter the concavity mean")
co1.place(x=10,y=230)
co1e=Entry(root,textvariable=a7)
co1e.place(x=200,y=230)

cp1=Label(root,text="Enter the concave points mean")
cp1.place(x=10,y=260)
cp1e=Entry(root,textvariable=a8)
cp1e.place(x=200,y=260)

sy1=Label(root,text="Enter the Symmetry mean")
sy1.place(x=10,y=290)
sy1e=Entry(root,textvariable=a9)
sy1e.place(x=200,y=290)

fd1=Label(root,text="Enter the fractal dimension mean")
fd1.place(x=10,y=320)
fd1e=Entry(root,textvariable=a10)
fd1e.place(x=200,y=320)
########################################################################################
r2=Label(root,text="Enter the radius size")
r2.place(x=300,y=50)
r2e=Entry(root,textvariable=a11)
r2e.place(x=480,y=50)

t2=Label(root,text="Enter the texture size")
t2.place(x=300,y=80)
t2e=Entry(root,textvariable=a12)
t2e.place(x=480,y=80)

p2=Label(root,text="Enter the perimeter size")
p2.place(x=300,y=110)
p2e=Entry(root,textvariable=a13)
p2e.place(x=480,y=110)

a2l=Label(root,text="Enter the area size")
a2l.place(x=300,y=140)
a2e=Entry(root,textvariable=a14)
a2e.place(x=480,y=140)

s2=Label(root,text="Enter the smoothness size")
s2.place(x=300,y=170)
s2e=Entry(root,textvariable=a15)
s2e.place(x=480,y=170)

c2=Label(root,text="Enter the compactness size")
c2.place(x=300,y=200)
c2e=Entry(root,textvariable=a16)
c2e.place(x=480,y=200)

co2=Label(root,text="Enter the concavity size")
co2.place(x=300,y=230)
co2e=Entry(root,textvariable=a17)
co2e.place(x=480,y=230)

cp2=Label(root,text="Enter the concave points size")
cp2.place(x=300,y=260)
cp2e=Entry(root,textvariable=a18)
cp2e.place(x=480,y=260)

sy2=Label(root,text="Enter the Symmetry size")
sy2.place(x=300,y=290)
sy2e=Entry(root,textvariable=a19)
sy2e.place(x=480,y=290)

fd2=Label(root,text="Enter the fractal dimension size")
fd2.place(x=300,y=320)
fd2e=Entry(root,textvariable=a20)
fd2e.place(x=480,y=320)
##################################################################################
r3=Label(root,text="Enter the radius worst")
r3.place(x=580,y=50)
r3e=Entry(root,textvariable=a21)
r3e.place(x=780,y=50)

t3=Label(root,text="Enter the texture worst")
t3.place(x=580,y=80)
t3e=Entry(root,textvariable=a22)
t3e.place(x=780,y=80)

p3=Label(root,text="Enter the perimeter wsorst")
p3.place(x=580,y=110)
p3e=Entry(root,textvariable=a23)
p3e.place(x=780,y=110)

a3l=Label(root,text="Enter the area worst")
a3l.place(x=580,y=140)
a3e=Entry(root,textvariable=a24)
a3e.place(x=780,y=140)

s3=Label(root,text="Enter the smoothness worst")
s3.place(x=580,y=170)
s3e=Entry(root,textvariable=a25)
s3e.place(x=780,y=170)

c3=Label(root,text="Enter the compactness worst")
c3.place(x=580,y=200)
c3e=Entry(root,textvariable=a26)
c3e.place(x=780,y=200)

co3=Label(root,text="Enter the concavity worst")
co3.place(x=580,y=230)
co3e=Entry(root,textvariable=a27)
co3e.place(x=780,y=230)

cp3=Label(root,text="Enter the concave points worst")
cp3.place(x=580,y=260)
cp3e=Entry(root,textvariable=a28)
cp3e.place(x=780,y=260)

sy3=Label(root,text="Enter the Symmetry worst")
sy3.place(x=580,y=290)
sy3e=Entry(root,textvariable=a29)
sy3e.place(x=780,y=290)

fd3=Label(root,text="Enter the fractal dimension worst")
fd3.place(x=580,y=320)
fd3e=Entry(root,textvariable=a30)
fd3e.place(x=780,y=320)
#-----------------------------------####----------------------######---------------##
def ent(e):
    submit.config(bg='RED',fg='yellow')

def lev(e):
    submit.config(bg='lightgrey',fg='black')

submit=Button(root,text="Predict",bg="lightgrey",font=("Arial",30),command=outcome,width=10,fg='black')
submit.place(x=10,y=350)
submit.bind('<Enter>',ent)
submit.bind('<Leave>',lev)
####******************------------------------------------*****************#######################################
def clearform():
    r1e.delete(0, END)
    t1e.delete(0, END)
    p1e.delete(0, END)
    a1e.delete(0, END)
    s1e.delete(0, END)
    c1e.delete(0, END)
    co1e.delete(0, END)
    cp1e.delete(0, END)
    sy1e.delete(0, END)
    fd1e.delete(0, END)
    r2e.delete(0, END)
    t2e.delete(0, END)
    p2e.delete(0, END)
    a2e.delete(0, END)
    s2e.delete(0, END)
    c2e.delete(0, END)
    co2e.delete(0, END)
    cp2e.delete(0, END)
    sy2e.delete(0, END)
    fd2e.delete(0, END)
    r3e.delete(0, END)
    t3e.delete(0, END)
    p3e.delete(0, END)
    a3e.delete(0, END)
    s3e.delete(0, END)
    c3e.delete(0, END)
    co3e.delete(0, END)
    cp3e.delete(0, END)
    sy3e.delete(0, END)
    fd3e.delete(0, END)
##################################################################################################################
def entc(e):
    clear.config(bg='RED',fg='yellow')

def levc(e):
    clear.config(bg='lightgrey',fg='black')

clear=Button(root,text="Clear",bg="lightgrey",font=("Arial",30),command=clearform,width=10)
clear.place(x=280,y=350)
clear.bind('<Enter>',entc)
clear.bind('<Leave>',levc)
##################################################################################################################
def ente(e):
    exit_button.config(bg='RED',fg='yellow')

def leve(e):
    exit_button.config(bg='lightgrey',fg='black')
exit_button = Button(root, text="Exit",bg="lightgrey",font=("Arial",30),command=root.destroy,width=10)
exit_button.place(x=550,y=350)
exit_button.bind('<Enter>',ente)
exit_button.bind('<Leave>',leve)
##################################################################################################################
dev=Label(root,text="MADE BY ABHISHEK",font=("Helvetica",25),fg='blue')
dev.place(x=10,y=550)
root.mainloop()
