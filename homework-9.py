#clock app

def jam(d1,d2):
    result={}
    result["h"]=d1["h"]+d2["h"]
    result["mi"]=d1["mi"]+d2["mi"]
    result["se"]=d1["se"]+d2["se"]
    if  result["se"]>=60:
        result["se"]-=60
        result["mi"]+=1
        
    if  result["mi"]>=60:
        result["h"]+=1
        result["mi"]-=60
        
    if  result["h"]>=24:
        print("wrong!")
        result={"h":0 , "mi":0 , "se":0}
    return result    


def tafrigh(d1,d2):
    result={}
    result['h']=d2['h']-d1['h']
    result['mi']=d2['mi']-d1['mi']
    result['se']=d2['se']-d1['se']
    if result["se"]<0:
       result["mi"]-=1
       result["se"]+=60
        
    if result["mi"]<0:
       result["h"]-=1
       result["se"]+=60
        
    if result["h"]<0:
        print("wrong!")
        
        
    return result


def show(result):
    print(f'{result["h"]}: {result["mi"]} : {result["se"]}')


d1={"h":int(input("saate aval:")) , "mi":int(input("daqiqe aval:")) , "se":int(input(" sanie aval:"))}
d2={"h":int(input("saate dovom:")) , "mi":int(input("daqiqe dovom:")) , "se":int(input("sanie dovom:"))}

result_s= jam(d1,d2)
show(result_s)

result_m= tafrigh(d1,d2)
show(result_m)
