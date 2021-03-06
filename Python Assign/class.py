import time,os
def abc():
    print('This Func^n ABC')

    class My_class():
        def __init__(self,tn,counter,Delay):
            print('This is constructor')
            self.tn=tn
            self.counter=counter
            self.Delay=Delay
        def run(self):
            print('This is run method',self.tn, self.counter,self.Delay)
    s1 = My_class('T1',3,2)
    s1.run()
abc() 		