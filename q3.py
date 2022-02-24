from turtle import *

class Disk(object):
    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

        self.t = Turtle()
        # self.t.speed(0)
        self.t.fillcolor("#808080")

    def showdisk(self):
        self.t.pu()
        self.t.setpos(self.dxpos, self.dypos)
        self.t.pd()
        self.t.begin_fill()
        for i in range(2):
            self.t.fd(self.dwidth / 2)
            self.t.lt(90)
            self.t.fd(self.dheight)
            self.t.lt(90)
            self.t.fd(self.dwidth / 2)
        self.t.end_fill()
        self.t.pu()

    def newpos(self,xpos,ypos):
        self.dxpos, self.dypos = xpos, ypos

    def cleardisk(self):
        self.t.clear()


class Pole(object):
    def __init__(self,name="",xpos=0,ypos=0,thick=10,length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

        self.t = Turtle()
        # self.t.speed(0)
        self.t.fillcolor("#808080")

    def showpole(self):
        self.t.pu()
        self.t.setpos(self.pxpos, self.pypos)
        self.t.pd()
        self.t.begin_fill()
        for i in range(2):
            self.t.fd(self.pthick / 2)
            self.t.lt(90)
            self.t.fd(self.plength)
            self.t.lt(90)
            self.t.fd(self.pthick / 2)
        self.t.end_fill()
        self.t.pu()

    def pushdisk(self,disk):
        disk.newpos(self.pxpos, self.toppos)
        disk.showdisk()
        self.toppos += disk.dheight
        self.stack.append(disk)

    def popdisk(self):
        disk = self.stack.pop()
        disk.cleardisk()
        self.toppos -= disk.dheight
        return disk


class Hanoi(object):
    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i),0,i*20,20,(n-i)*30))

    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)
        
h = Hanoi()
h.solve()
