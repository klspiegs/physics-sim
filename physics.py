from Tkinter import *
master = Tk()


class Bucket:
    def __init__(self, tensionForce, gravitationalForce, mass, radius, speed):
        self.tensionForce = tensionForce
        self.gravitationalForce = gravitationalForce
        self.mass = mass
        self.radius = radius
        self.speed = speed

        # a = v^2/R
        global acceleration
        acceleration = (speed ** 2)/radius

        global netForce
        netForce = mass * acceleration


def getvalues():
    tensionForce = w1.get()
    gravitationalForce = w2.get()
    mass = w3.get()
    radius = w4.get()
    speed = w5.get()
    bottom = Bucket(tensionForce, gravitationalForce, mass, radius, speed)
    print1 = "This is the acceleration: ", acceleration
    print2 = "This is the net force: ", netForce
    label = Label(master, text=print1).grid(row=3, column=3)
    label1 = Label(master, text=print2).grid(row=4, column=3)

# print("Put 'x' when inputting what you want to solve for.")
# acceleration = raw_input("What is the acceleration?")
# netForce = raw_input("What is the net force?")


# tensionForce
label1 = Label(master, text="Tension Force").grid(row=0, column=1)
w1 = Scale(master, from_=0, to=100)
w1.grid(row=1, column=1)

# gravitationalForce
label2 = Label(master, text="Gravitational Force").grid(row=0, column=2)
w2 = Scale(master, from_=0, to=100)
w2.grid(row=1, column=2)

# mass
label3 = Label(master, text="Mass").grid(row=0, column=3)
w3 = Scale(master, from_=0, to=100)
w3.grid(row=1, column=3)

# radius
label4 = Label(master, text="Radius").grid(row=0, column=4)
w4 = Scale(master, from_=0, to=100)
w4.grid(row=1, column=4)

# speed
label5 = Label(master, text="Speed").grid(row=0, column=5)
w5 = Scale(master, from_=0, to=100)
w5.grid(row=1, column=5)

b = Button(master, text="done", command=getvalues).grid(row=2, column=3)


mainloop()
