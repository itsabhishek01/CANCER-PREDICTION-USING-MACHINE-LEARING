def result():
    new=pd.DataFrame({"radius_mean":[float(a1.get())],"texture_mean":[float(a2.get())],"perimeter_mean":[float(a3.get())],"area_mean":[float(a4.get())],"smoothness_mean":[float(a5.get())],"compactness_mean":[float(a6.get())],"concave points_mean":[float(a7.get())],"symmetry_mean":[float(a8.get())],"fractal_dimension_mean":[float(a9.get())],"radius_se":[float(a10.get())],"texture_se":[float(a11.get())],"perimeter_se":[float(a12.get())],"area_se":[float(a13.get())],"smoothness_se":[float(a14.get())],"compactness_se":[float(a15.get())],"concave points_se":[float(a16.get())],"symmetry_se":[float(a17.get())],"fractal_dimension_se":[float(a18.get())],"radius_worst":[float(a19.get())],"texture_worst":[float(a20.get())],"perimeter_worst":[float(a21.get())],"area_worst":[float(a22.get())],"smoothness_worst":[float(a23.get())],"compactness_worst":[float(a24.get())],"concave points_worst":[float(a25.get())],"symmetry_worst":[float(a26.get())],"fractal_dimension_worst":[float(a22.get())]})
    print(new)
   # new=sc.transform(new)
   # o=lr.predict(new)
  #  if o==0:
    #    print("Person Has Breast Cancer")
  #  else:
  #      print("Person is Healthy")
###########################################################################################################################################
#-------------------------------------------------------
from tkinter import *
root=Tk()
root.geometry("1920x1080")
root.title("Breast Cancer Prediction")

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
#######################################################################################################################

r1=Label(root,text="Enter the radius mean").place(x=10,y=50)
r1e=Entry(root,textvariable=a1)
r1e.place(x=200,y=50)

t1=Label(root,text="Enter the texture mean").place(x=10,y=80)
t1e=Entry(root,textvariable=a2)
t1e.place(x=200,y=80)

p1=Label(root,text="Enter the Perimeter mean").place(x=10,y=110)
p1e=Entry(root,textvariable=a3)
p1e.place(x=200,y=110)

a1=Label(root,text="Enter the Area Mean").place(x=10,y=140)
a1e=Entry(root,textvariable=a4)
a1e.place(x=200,y=140)

s1=Label(root,text="Enter the Smoothness Mean").place(x=10,y=170)
s1e=Entry(root,textvariable=a5)
s1e.place(x=200,y=170)

c1=Label(root,text="Enter the compactness mean").place(x=10,y=200)
c1e=Entry(root,textvariable=a6)
c1e.place(x=200,y=200)

cp1=Label(root,text="Enter the concave points mean").place(x=10,y=230)
cp1e=Entry(root,textvariable=a7)
cp1e.place(x=200,y=230)

sy1=Label(root,text="Enter the Symmetry mean").place(x=10,y=260)
sy1e=Entry(root,textvariable=a8)
sy1e.place(x=200,y=260)

fd1=Label(root,text="Enter the fractal dimension mean").place(x=10,y=290)
fd1e=Entry(root,textvariable=a9)
fd1e.place(x=200,y=290)
########################################################################################
r2=Label(root,text="Enter the radius size").place(x=300,y=50)
r2e=Entry(root,textvariable=a10)
r2e.place(x=480,y=50)

t2=Label(root,text="Enter the texture size").place(x=300,y=80)
t2e=Entry(root,textvariable=a11)
t2e.place(x=480,y=80)

p2=Label(root,text="Enter the perimeter size").place(x=300,y=110)
p2e=Entry(root,textvariable=a12)
p2e.place(x=480,y=110)

a2=Label(root,text="Enter the area size").place(x=300,y=140)
a2e=Entry(root,textvariable=a13)
a2e.place(x=480,y=140)

s2=Label(root,text="Enter the smoothness size").place(x=300,y=170)
s2e=Entry(root,textvariable=a14)
s2e.place(x=480,y=170)

c2=Label(root,text="Enter the compactness size").place(x=300,y=200)
c2e=Entry(root,textvariable=a15)
c2e.place(x=480,y=200)

cp2=Label(root,text="Enter the concave points size").place(x=300,y=230)
cp2e=Entry(root,textvariable=a16)
cp2e.place(x=480,y=230)

sy2=Label(root,text="Enter the Symmetry size").place(x=300,y=260)
sy2e=Entry(root,textvariable=a17)
sy2e.place(x=480,y=260)

fd2=Label(root,text="Enter the fractal dimension size").place(x=300,y=290)
fd2e=Entry(root,textvariable=a18)
fd2e.place(x=480,y=290)
##################################################################################
r3=Label(root,text="Enter the radius worst").place(x=580,y=50)
r3e=Entry(root,textvariable=a19)
r3e.place(x=780,y=50)

t3=Label(root,text="Enter the texture worst").place(x=580,y=80)
t3e=Entry(root,textvariable=a20)
t3e.place(x=780,y=80)

p3=Label(root,text="Enter the perimeter wsorst").place(x=580,y=110)
p3e=Entry(root,textvariable=a21)
p3e.place(x=780,y=110)

a3=Label(root,text="Enter the area worst").place(x=580,y=140)
a3e=Entry(root,textvariable=a22)
a3e.place(x=780,y=140)

s3=Label(root,text="Enter the smoothness worst").place(x=580,y=170)
s3e=Entry(root,textvariable=a23)
s3e.place(x=780,y=170)

c3=Label(root,text="Enter the compactness worst").place(x=580,y=200)
c3e=Entry(root,textvariable=a24)
c3e.place(x=780,y=200)

cp3=Label(root,text="Enter the concave points worst").place(x=580,y=230)
cp3e=Entry(root,textvariable=a25)
cp3e.place(x=780,y=230)

sy3=Label(root,text="Enter the Symmetry worst").place(x=580,y=260)
sy3e=Entry(root,textvariable=a26)
sy3e.place(x=780,y=260)

fd3=Label(root,text="Enter the fractal dimension worst").place(x=580,y=290)
fd3e=Entry(root,textvariable=a27)
fd3e.place(x=780,y=290)

submit=Button(root,text="Submit",bg="green",font=("Arial",20),command=display)
submit.place(x=500,y=350)
##################################################################################################################
root.mainloop()