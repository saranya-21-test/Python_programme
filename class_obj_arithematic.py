class arithmetic_op:
    def sum(self):
        x=20
        y=30
        return x+y
    def mul(self):
        a=20
        b=5
        return a*b
    def sub(self):
        p=100
        q=50
        return p-q

    def div(self):
        s=100
        t=20
        return s//t

    def mod(self):
        e=12
        f=6
        return e%f

    def even_odd(self):
        c=12
        d=5
        if c%2==0:
            print("given number is even")
        else:
            print("given number is odd")


    def pos_negative(self):
        t=12

        if t>0:
            print("given number is positive")
        else:
            print("given number is negitive")

    def fact(self):
        no=5
        i = 1
        fact = 1
        while (i <= no):
            fact = fact * i
            i = i + 1
        return fact

    def prime_no(self):
        count=0
        n=8
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count==2:
            print("given number is prime")
        else:
            print("given number is not a prime")





    def mobile_no_validation(self):
        z="9440688613"

        if len(z)==10:
            print("given number is valid")
        else:
            print("given number is invalid")