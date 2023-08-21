
#barname kasr ha

def jam(f1,f2):
    result={}
    result['s']=(f1['s']*f2['m']+ f2['s']*f1['m'])
    result['m']=f1['m']*f2['m']
    return result
def zarb(f1,f2):
    result={}
    result['s']=f1["s"]*f2["s"]
    result['m']=f1["m"]*f2["m"]
    return result
def taghsim(f1,f2):
    result={}
    result['s']=(f1['s']* f2['m'])
    result['m']=(f1['m']* f2['s'])
    return result
def tafrigh(f1,f2):
    result={}
    result['s']=(((f1['m']*f2['m']/f1['m'])*f1['s'])- (f1['m']*f2['m']/ f2['m'])*f2['s'])
    result['m']=(f1['m']*f2['m'])
    return result
def show(r):
    print(f'{r["s"]} / {r["m"]}')

def options():
    while 1:
        num1=float(input("enter top num: "))
        num2=float(input("enter down num: "))
        if num2==0:
            print("wrong")
            while 1:
                num2=float(input("try again : "))
                if num2!=0:
                    break
        num3=float(input("enter top num : "))
        num4=float(input("enter down num: "))
        if num4==0:
            print("wrong!!!")
            while 1:
                num4=float(input("try again: "))
                if num4!=0:
                    break
                
        print(f"kasr aval :\n  {num1}/{num2} va kasr dovom: {num3}/{num4} ")
        break
        
    f1={"s":num1 ,  "m":num2}
    f2={"s":num3 ,  "m":num4} 

    print("dastoore khod ra entekhab konid: \t 1: jam  \t 2:zarb \t 3:tafrigh  \t 4:taghsim")
    option=int(input())
    if option==1:
        show(jam(f1,f2))
    elif option==2:
        show(zarb(f1,f2))
    elif option==3:
        show(tafrigh(f1,f2))
    elif option==4:
        show(taghsim(f1,f2))
    else:
        print("wrong!!!")


options()       
        

