import  tkinter as tik
from math import *
root=tik.Tk()
root.title("BMI Calculator")
def calculate_BMI ():
    kg= float(entery_kg.get())
    t=float(entery_height.get())
    height=t/100
    b= int((kg/height**2))
    round(b)
    label_result ['text']=f" {b}"
    if 19>b:
        label_level2 ['text']=f" Underweight"
        label_level2['foreground'] = "blue"
    elif 19<=b<25:
        label_level2['text'] = f" Normal"
        label_level2['foreground'] = "green3"
    elif 25<=b<30:
        label_level2['text'] = f" Over weight"
        label_level2['foreground'] = "darkgoldenrod2"
    elif 30<b :
        label_level2['text'] = f" Obesity"
        label_level2['foreground']="red"
    if 24.9<b:
        x1= (24.9*height**2)
        x=kg-x1
        n=round(x1)
        m=round(x)
        label_perfect2 ['text'] = f" {n}"
        label_suggetion2['text'] = f" You should loss your \n weight {m}Kg only."
        print("Perfect \nWeight : ",round(x1),"Kg")
        print ("Suggetion : You should loss your weight [",round(x),"Kg] only.")
    elif 19>b:
        x1= (20*height**2)
        x=x1-kg
        m=round(x)
        n=round(x1)
        label_suggetion2['text'] = f" You should gain your weight {m}Kg only."
        label_perfect2 ['text'] = f" {n}"
        print("Perfect \nWeight : ",round(x1))
        print ("Suggetion : You should gain your weight [",round(x),'Kg] only.')
    elif 19<=b<25:
        kg= int(entery_kg.get())
        label_suggetion2['text'] = f"   *   ~\n   -.__.-"
        label_suggetion2['foreground']="orangered"
        label_perfect2 ['text'] = f" {kg}"
        
label_kg= tik.Label(root,font=("Agency FB",36),text="WEIGHT : ",foreground='dodgerblue2' )
label_kg.grid(column=0,row=0)
entery_kg = tik.Entry(root,font=("Agency FB",36),foreground="orangered2",width=20)
entery_kg.grid(column=1,row=0)

label_height= tik.Label(root,font=("Agency FB",36),text="HEIGHT : ",foreground='dodgerblue2' )
label_height.grid(column=0,row=1)
entery_height= tik.Entry(root,font=("Agency FB",36),foreground="orangered2",width=20)
entery_height.grid(column=1,row=1)

button_calculat=tik.Button(root,text="BMI :",command=calculate_BMI,font=("DS-Digital",36),foreground="maroon2")
button_calculat.grid(column=0,row=2)

label_result=tik.Label(root,text=" ",font=("Agency FB",36),foreground="deepskyblue")
label_result.grid(column=1,row=2)

label_level = tik.Label(root, text="LEVEL : ", font=("Agency FB", 36))
label_level.grid(column=0,row=3)

label_level2 = tik.Label(root, text=" ", font=("Agency FB", 36))
label_level2.grid(column=1,row=3)
    

label_perfect  = tik.Label(root, text="PERFECT \nWEIGHT : ", font=("Agency FB", 36),foreground="brown1")
label_perfect.grid(column=0,row=4)

label_perfect2  = tik.Label(root, text=" ", font=("Agency FB", 36),foreground="brown1")
label_perfect2.grid(column=1,row=4)

label_suggetion  = tik.Label(root, text="SUGGETION : ", font=("Agency FB", 30),foreground="DeepPink2")
label_suggetion.grid(column=0,row=5)

label_suggetion2  = tik.Label(root, text="   ", font=("Agency FB", 30),foreground="DeepPink2")
label_suggetion2.grid(column=1,row=5)

root.mainloop()
