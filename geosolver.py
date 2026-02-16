import tkinter as tk
import math

#rrethi
def open_cc():
    area1 = tk.Toplevel(root)
    area1.title("Circle Calculator")
    area1.geometry("300x350")
    area1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    area1.resizable(False, False)

    header = tk.Label(area1, text="Circle Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)

    tk.Label(area1, text="Radius: ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(area1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)

    result1 = tk.Label(area1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)

    def area():
        result1.configure(text=f"Result: {math.pi * float(n1.get()) ** 2 }m^2")

    def perimieter():
        result1.configure(text=f"Result: {2 * math.pi * float(n1.get())}m")

    calculate = tk.Button(area1, text="Area", command=area, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)

    calculate2 = tk.Button(area1, text="Circumference", command=perimieter, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate2.pack(pady=1)
    
    header1 = tk.Label(area1, text="Area = pi * r^2",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
    header2 = tk.Label(area1, text="Circumference = 2 * pi * r",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header2.pack(fill="x", pady=1)

#katrori/drejtekendeshi
def open_sc():
    square1 = tk.Toplevel(root)
    square1.title("Square & Rectangle Calculator")
    square1.geometry("300x400")
    square1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    square1.resizable(False, False)

    header = tk.Label(square1, text="Square & Rectangle Calculator",  bg="#142038", fg="cyan", font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)

    tk.Label(square1, text="Height: ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(square1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)

    tk.Label(square1, text="Width: ", bg="#1B263B", fg="white").pack()
    n2 = tk.Entry(square1, highlightbackground="cyan", highlightthickness=2)
    n2.pack(pady=10)

    result1 = tk.Label(square1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)

    def area():
        result1.config(text=f"Result: {float(n1.get()) * float(n2.get())}m^2")

    def perimetri():
        result1.config(text=f"Result: { 2 * float(n1.get()) +  2 * float(n2.get())}m")

    calculate = tk.Button(square1, text="Area", command=area, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)

    calculate = tk.Button(square1, text="Circumference", command=perimetri, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    header1 = tk.Label(square1, text="Area(Square) = a^2 - Area(Rectangle):  a * b",  bg="#142038", fg="cyan", font=("Arial", 7, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
    header2 = tk.Label(square1, text="Circimference(Square) = 4a - Circumference(Rectangle): 2a + 2b",  bg="#142038", fg="cyan", font=("Arial", 7, "bold"), highlightbackground="cyan", highlightthickness=2)
    header2.pack(fill="x", pady=1)


#trekendeshi
def open_t():
    triangle1 = tk.Toplevel(root)
    triangle1.title("Triangle Calculator")
    triangle1.geometry("300x480")
    triangle1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    triangle1.resizable(False, False)

    header = tk.Label(triangle1, text="Triangle Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)

    tk.Label(triangle1, text="Height: ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(triangle1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)

    tk.Label(triangle1, text="Width: ", bg="#1B263B", fg="white").pack()
    n2 = tk.Entry(triangle1, highlightbackground="cyan", highlightthickness=2)
    n2.pack(pady=10)

    tk.Label(triangle1, text="Use when calulating Circumference: ", bg="#1B263B", fg="white").pack()
    n3 = tk.Entry(triangle1, highlightbackground="cyan", highlightthickness=2)
    n3.pack(pady=10)

    result1 = tk.Label(triangle1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)

    def area():
        result1.config(text=f"Result: {1/2 * float(n1.get()) * float(n2.get())}m^2")

    def perimetri():
        result1.config(text=f"Result: {float(n1.get()) + float(n2.get()) + float(n3.get())}m")

    calculate = tk.Button(triangle1, text="Area", command=area, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)

    calculate = tk.Button(triangle1, text="Circumference", command=perimetri, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    header1 = tk.Label(triangle1, text="Area = 1/2 * a * b",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
    header2 = tk.Label(triangle1, text="Circumference = a + b + c",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header2.pack(fill="x", pady=1)


#sfera
def open_vs():
    sphere1 = tk.Toplevel(root)
    sphere1.title("Sphere Calculator")
    sphere1.geometry("300x280")
    sphere1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    sphere1.resizable(False, False)

    header = tk.Label(sphere1, text="Sphere Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)

    tk.Label(sphere1, text="Radius: ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(sphere1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)

    result1 = tk.Label(sphere1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)

    def volume():
        result1.config(text=f"Result: {4/3 * math.pi * float(n1.get())** 3}m^3")

    calculate = tk.Button(sphere1, text="Volume", command=volume, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    header1 = tk.Label(sphere1, text="Volume = 4/3 * pi * r^3",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)


#cylinder
def open_c():
    cylinder1 = tk.Toplevel(root)
    cylinder1.title("Cylinder Calculator")
    cylinder1.geometry("300x330")
    cylinder1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    cylinder1.resizable(False, False)

    header = tk.Label(cylinder1, text="Cylinder Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)

    tk.Label(cylinder1, text="Radius: ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(cylinder1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)

    tk.Label(cylinder1, text="Height: ", bg="#1B263B", fg="white").pack()
    n2 = tk.Entry(cylinder1, highlightbackground="cyan", highlightthickness=2)
    n2.pack(pady=10)

    result1 = tk.Label(cylinder1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)

    def volume():
        result1.config(text=f"Result: {math.pi * float(n2.get()) * float(n1.get())**2 }m^3")

    calculate = tk.Button(cylinder1, text="Volume", command=volume, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    header1 = tk.Label(cylinder1, text="Volume = pi * h * r^2",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    

#trapezi
def open_tr():
    trapezi1 = tk.Toplevel(root)
    trapezi1.title("Trapezoid Calculator")
    trapezi1.geometry("500x600")
    trapezi1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    trapezi1.resizable(False, False)
    
    
    header = tk.Label(trapezi1, text="Trapezoid Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)
    
    tk.Label(trapezi1, text="Height(when calculating area): ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(trapezi1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)

    tk.Label(trapezi1, text="Base1: ", bg="#1B263B", fg="white").pack()
    n2 = tk.Entry(trapezi1, highlightbackground="cyan", highlightthickness=2)
    n2.pack(pady=10)
    
    tk.Label(trapezi1, text="Base2: ", bg="#1B263B", fg="white").pack()     
    n3 = tk.Entry(trapezi1, highlightbackground="cyan", highlightthickness=2)
    n3.pack(pady=10)
    
    tk.Label(trapezi1, text="Leg1(Circimference): ", bg="#1B263B", fg="white").pack()
    n4 = tk.Entry(trapezi1, highlightbackground="cyan", highlightthickness=2)
    n4.pack(pady=10)
    
    tk.Label(trapezi1, text="Leg2(Circumference): ", bg="#1B263B", fg="white").pack()
    n5 = tk.Entry(trapezi1, highlightbackground="cyan", highlightthickness=2)
    n5.pack(pady=10)
    
    result1 = tk.Label(trapezi1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)
    
    def perimetri():
            result1.config(text=f"Result: {float(n2.get()) + float(n3.get())+ float(n4.get()) + float(n5.get())}m")
            
    def area():
        result1.config(text=f"{1/2 * (float(n2.get()) + float(n3.get())) * float(n1.get())}m^2")
        
    calculate = tk.Button(trapezi1, text="Circumference", command=perimetri, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1) 
    
    calculate = tk.Button(trapezi1, text="Area", command=area, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1) 
    
    header1 = tk.Label(trapezi1, text="Area = 1/2 * (a * b) + h",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
    header2 = tk.Label(trapezi1, text="Circumference = a + b + c + d",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header2.pack(fill="x", pady=1)
    
    
#parallelogram
def open_p():
    paralleogram1 = tk.Toplevel(root)
    paralleogram1.title("Paralleogram Calculator")
    paralleogram1.geometry("300x480")
    paralleogram1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    paralleogram1.resizable(False, False)
    
    header = tk.Label(paralleogram1, text="Paralleogram Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)
    
    tk.Label(paralleogram1, text="Height(Area): ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(paralleogram1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)
    
    tk.Label(paralleogram1, text="Base: ", bg="#1B263B", fg="white").pack()
    n2 = tk.Entry(paralleogram1, highlightbackground="cyan", highlightthickness=2)
    n2.pack(pady=10)
    
    tk.Label(paralleogram1, text="Leg(Circumference): ", bg="#1B263B", fg="white").pack()
    n3 = tk.Entry(paralleogram1, highlightbackground="cyan", highlightthickness=2)
    n3.pack(pady=10)
    
    result1 = tk.Label(paralleogram1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)
    
    def perimetri():
        result1.config(text=f"Result: { 2 * float(n2.get()) + 2 * float(n3.get())}m")
        
    def area():
        result1.config(text=f"Result: {float(n1.get()) * float(n2.get())}m^2")  
        
        
    calculate = tk.Button(paralleogram1, text="Circumference", command=perimetri, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1) 
    
    calculate = tk.Button(paralleogram1, text="Area", command=area, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    header1 = tk.Label(paralleogram1, text="Area = a * b",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
    header2 = tk.Label(paralleogram1, text="Circumference = 2a * 2b",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header2.pack(fill="x", pady=1)
    
#cone    
def open_cn():
    cone1 = tk.Toplevel(root)
    cone1.title("Cone Calculator")
    cone1.geometry("300x350")
    cone1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    cone1.resizable(False, False)
    
    header = tk.Label(cone1, text="Cone Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)
    
    tk.Label(cone1, text="Radius: ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(cone1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)
    
    tk.Label(cone1, text="Height: ", bg="#1B263B", fg="white").pack()
    n2 = tk.Entry(cone1, highlightbackground="cyan", highlightthickness=2)
    n2.pack(pady=10)
    
    result1 = tk.Label(cone1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)
    
    def volume():
        result1.config(text=f"{1/3 * math.pi * float(n1.get())**2 * float(n2.get())}m^3")
        
    calculate = tk.Button(cone1, text="Volume", command=volume, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    header1 = tk.Label(cone1, text="Volume = 1/3 * pi * r^2 * h",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
 #kite   
def open_k():
    kite1 = tk.Toplevel(root)
    kite1.title("Kite Calculator")
    kite1.geometry("300x550")
    kite1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    kite1.resizable(False, False)
    
    header = tk.Label(kite1, text="Kite Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)
    
    tk.Label(kite1, text="d(1)-Area: ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(kite1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)
    
    tk.Label(kite1, text="d(2)-Area: ", bg="#1B263B", fg="white").pack()
    n2 = tk.Entry(kite1, highlightbackground="cyan", highlightthickness=2)
    n2.pack(pady=10)
    
    tk.Label(kite1, text="a(Circumference): ", bg="#1B263B", fg="white").pack()
    n3 = tk.Entry(kite1, highlightbackground="cyan", highlightthickness=2)
    n3.pack(pady=10)
    
    tk.Label(kite1, text="b(Circumference): ", bg="#1B263B", fg="white").pack()
    n4 = tk.Entry(kite1, highlightbackground="cyan", highlightthickness=2)
    n4.pack(pady=10)
    
    result1 = tk.Label(kite1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)
    
    def area():
        result1.config(text=f"{1/2 * float(n1.get()) * float(n2.get())}m^2")
        
    def perimetri():
        result1.config(text=f"{(2 * float(n3.get())) + 2 * float(n4.get())}m")    
        
    calculate = tk.Button(kite1, text="Area", command=area, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    calculate = tk.Button(kite1, text="Circumference", command=perimetri, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1) 
    
    header1 = tk.Label(kite1, text="Area = 1/2 * d1 * d2",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
    header2 = tk.Label(kite1, text="Circumference = 2a * 2b",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header2.pack(fill="x", pady=1)   
    
#pyramid
def open_pr():
    pyramid1 = tk.Toplevel(root)
    pyramid1.title("Pyramid Calculator")
    pyramid1.geometry("400x720")
    pyramid1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    pyramid1.resizable(False, False)    
    
    header = tk.Label(pyramid1, text="Pyramid Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)
    
    tk.Label(pyramid1, text="How many sides is the base?(Area): ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(pyramid1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)
    
    tk.Label(pyramid1, text="Length of one of the sides(Area): ", bg="#1B263B", fg="white").pack()
    n2 = tk.Entry(pyramid1, highlightbackground="cyan", highlightthickness=2)
    n2.pack(pady=10)
    
    tk.Label(pyramid1, text="Length(Triangle-Area) ", bg="#1B263B", fg="white").pack()
    n3 = tk.Entry(pyramid1, highlightbackground="cyan", highlightthickness=2)
    n3.pack(pady=10)
    
    tk.Label(pyramid1, text="Width(Triangle-Area) ", bg="#1B263B", fg="white").pack()
    n4 = tk.Entry(pyramid1, highlightbackground="cyan", highlightthickness=2)
    n4.pack(pady=10)
    
    tk.Label(pyramid1, text="Length(Pyramid-Volume) ", bg="#1B263B", fg="white").pack()
    n5 = tk.Entry(pyramid1, highlightbackground="cyan", highlightthickness=2)
    n5.pack(pady=10)
    
    tk.Label(pyramid1, text="Width(Pyramid-Volume) ", bg="#1B263B", fg="white").pack()
    n6 = tk.Entry(pyramid1, highlightbackground="cyan", highlightthickness=2)
    n6.pack(pady=10)
    
    tk.Label(pyramid1, text="Height(Pyramid-Volume) ", bg="#1B263B", fg="white").pack()
    n7 = tk.Entry(pyramid1, highlightbackground="cyan", highlightthickness=2)
    n7.pack(pady=10)
    
    result1 = tk.Label(pyramid1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)
    
    def area():
        result1.config(text=f"{float(n2.get())**2 + float(n1.get()) * (1/2 * float(n3.get()) * float(n4.get()))}m^2")
        
    def volume():
        result1.config(text=f"{float(n5.get()) * float(n6.get()) * float(n7.get()) / 3}m^3")
        
    calculate = tk.Button(pyramid1, text="Area", command=area, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    calculate = tk.Button(pyramid1, text="Volume", command=volume, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1) 
    
    header1 = tk.Label(pyramid1, text="Area = B + (n * M)",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
    header2 = tk.Label(pyramid1, text="Volume = 2a * 2b",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header2.pack(fill="x", pady=1) 
        

#cube
def open_cb():
    cube1 = tk.Toplevel(root)
    cube1.title("Cube Calculator")
    cube1.geometry("240x350")
    cube1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    cube1.resizable(False, False)  
    
    header = tk.Label(cube1, text="Cube Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)
    
    tk.Label(cube1, text="Length: ", bg="#1B263B", fg="white").pack()
    n1 = tk.Entry(cube1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)
    
    result1 = tk.Label(cube1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)
    
    def volume():
        result1.config(text=f"{float(n1.get())**3}m^3")
        
    def area():
        result1.config(text=f"{6 * float(n1.get())**2}m^2")
        
    calculate = tk.Button(cube1, text="Area", command=area, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    calculate = tk.Button(cube1, text="Volume", command=volume, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    header1 = tk.Label(cube1, text="Area = 6 * l^2",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
    header2 = tk.Label(cube1, text="Volume = l^3",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header2.pack(fill="x", pady=1) 
    
#cuboid
def open_cu():
    cuboid1 = tk.Toplevel(root)
    cuboid1.title("Cuboid Calculator")
    cuboid1.geometry("290x470")
    cuboid1.configure(bg="#0A0F1F", highlightbackground="cyan", highlightthickness=2)
    cuboid1.resizable(False, False) 
    
    header = tk.Label(cuboid1, text="Cuboid Calculator",  bg="#142038", fg="cyan", font=("Arial", 18, "bold"), highlightbackground="cyan", highlightthickness=2)
    header.pack(fill="x", pady=10)
    
    tk.Label(cuboid1, text="Length: ", bg="#1B263B", fg="white").pack()
    
    
    n1 = tk.Entry(cuboid1, highlightbackground="cyan", highlightthickness=2)
    n1.pack(pady=10)
    
    tk.Label(cuboid1, text="Width: ", bg="#1B263B", fg="white").pack()
    n2 = tk.Entry(cuboid1, highlightbackground="cyan", highlightthickness=2)
    n2.pack(pady=10)
    
    tk.Label(cuboid1, text="Height: ", bg="#1B263B", fg="white").pack()
    n3 = tk.Entry(cuboid1, highlightbackground="cyan", highlightthickness=2)
    n3.pack(pady=10)
    
    result1 = tk.Label(cuboid1, text="Result: ", bg="#1B263B", fg="white",font=("Arial", 14, "bold"), highlightbackground="cyan", highlightthickness=2)
    result1.pack(pady=15)
    
    def volume():
        result1.config(text=f"{float(n1.get()) * float(n2.get()) * float(n3.get())}m^3")
        
    def area():
        result1.config(text=f"{2 * (float(n1.get()) * float(n2.get()) + float(n1.get()) * float(n3.get()) + float(n2.get()) * float(n3.get()))}m^2")
        
    calculate = tk.Button(cuboid1, text="Area", command=area, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    calculate = tk.Button(cuboid1, text="Volume", command=volume, bg="#00BFA6", fg="Black",
                      font="Courier, 10", width=20, height=2,
                      highlightbackground="cyan", highlightthickness=2)
    calculate.pack(pady=1)
    
    header1 = tk.Label(cuboid1, text="Area = 2(lw) + (lh) + (wh)",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header1.pack(fill="x", pady=1)
    
    header2 = tk.Label(cuboid1, text="Volume = l * w * h",  bg="#142038", fg="cyan", font=("Arial", 10, "bold"), highlightbackground="cyan", highlightthickness=2)
    header2.pack(fill="x", pady=1) 
    
         
        
#main
root = tk.Tk()
root.geometry("450x550")
root.resizable(False, False)
root.config(bg="#090B26")
root.title("GeoSolver")


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

welcome = tk.Label(
    root, text="GeoSolver",
    bg="#142038", fg="cyan",
    font=("Arial", 18, "bold"),
    highlightbackground="cyan", highlightthickness=2, padx=300
)
welcome.grid(row=0, column=0, columnspan=2, pady=10)

b1 = tk.Button(root, text="Circle Calculator", command=open_cc,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b1.grid(row=1, column=0, pady=10, padx=5)

b2 = tk.Button(root, text="S & R Calculator", command=open_sc,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b2.grid(row=1, column=1, pady=10, padx=5)

b3 = tk.Button(root, text="Triangle Calculator", command=open_t,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b3.grid(row=2, column=0, pady=10, padx=5)

b4 = tk.Button(root, text="Sphere Calculator", command=open_vs,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b4.grid(row=2, column=1, pady=10, padx=5)

b5 = tk.Button(root, text="Cylinder Calculator", command=open_c,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b5.grid(row=3, column=0, pady=10, padx=5)

b6 = tk.Button(root, text="Trapezoid Calculator", command=open_tr,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b6.grid(row=3, column=1, pady=10, padx=5)

b7 = tk.Button(root, text="Parallelogram Calculator", command=open_p,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b7.grid(row=4, column=0, pady=10, padx=5)

b8 = tk.Button(root, text="Cone Calculator", command=open_cn,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b8.grid(row=4, column=1, pady=10, padx=5)

b9 = tk.Button(root, text="Kite Calculator", command=open_k,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b9.grid(row=5, column=0, pady=10, padx=5)

b10 = tk.Button(root, text="Pyramid Calculator", command=open_pr,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b10.grid(row=5, column=1, pady=10, padx=5)

b11 = tk.Button(root, text="Cube Calculator", command=open_cb,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b11.grid(row=6, column=0, pady=10, padx=5)

b12 = tk.Button(root, text="Cuboid Calculator", command=open_cu,
          bg="#00BFA6", fg="black", font="Courier, 12", width=20, height=2,
          highlightbackground="cyan", highlightthickness=2)
b12.grid(row=6, column=1, pady=10, padx=5)

welcome2 = tk.Label(
    root, text="Created by: Dr.Dielli Misini",
    bg="#090B26", fg="cyan",
    font=("Arial", 14, "bold"),
    padx=300
)
welcome2.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()