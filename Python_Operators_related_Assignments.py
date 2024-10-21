#write a python program to compute area and perimeter for given rectangle
#area=l*w
#p=2*(l+w)
'''length=int(input("enter the length:"))
width=int(input("enter the width:"))
area=length*width
p=2*(length+width)
print("the area is:",area)
print("the parameter is:",p)'''

def cal_rect(l,w):
    a=l*w
    p=2*(l+w)
    print(a)
    print(p)


#to calculate the interest
'''p=int(input("enter the principle amount:"))
t=int(input("enter the time period:"))
r=int(input("enter the rate of interest:"))
print("the total interest is:",p*t*r/100)'''

def cal_interest(p,t,r):
    i=p*t*r/100
    print(i)



#write a python program to convert celsius to farenheit
#formula:f=(9/5)*c+32
'''c=int(input("enter the celsius:"))
f=(9/5)*c+32
print("the farenheit is:",f)'''

def cal_far(c):
    f=(9/5)*c+32
    print(f)


#write a python to compute spead using s=ut+1/2at2 using functions
def cal_speed(u,t,a):
    s=u*t+1/2*(a*t*t)
    print(s)