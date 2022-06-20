class rectangle:
    height=int(input("Enter the height of rectangle:"))
    width=int(input("Enter the height of rectangle:"))
    corner_X1=int(input("Enter corner X1 of rectangle:"))
    corner_X2=int(input("Enter corner X2 of rectangle:"))
    corner_Y1=int(input("Enter corner Y1 of rectangle:"))
    corner_Y2=int(input("Enter corner Y2 of rectangle:"))
    def centre(self):
        x1=self.corner_X1
        x2=self.corner_X2
        y1=self.corner_Y1
        y2=self.corner_Y2
        x=(x1+x2)//2
        y=(y1+y2)//2
        print("center=",x,y)
    def area(self):
        a=self.height*self.width
        print("area=",a)
    def peri(self):
        p=2*(self.height+self.width)
        print("perimeter= ",p)

rec=rectangle()
rec.centre()
rec.area()
rec.peri()