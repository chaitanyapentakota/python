from datetime import datetime

name= input("enter ur name:")
lists='''
rice Rs 20/kg
sugar Rs 30/kg
salt Rs 20/kg
oil Rs 80/liter
panner Rs 110/kg
maggie Rs 50/each
boost Rs 90/each
colgate Rs 85/each
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
items={'rice':20,'sugar':30,'salt':20,'oil':80,'panner':110,'maggie':50,'boost':90,'colgate':85}
option=int(input("for list of items press 1:"))
if option ==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if u want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items: ")
        quanitity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quanitity*(items[item])
            pricelist.append((item,quanitity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quanitity)
            plist.append(price)
            finalamount= totalprice
        else:
            print("sorry entered item is not avalible")   
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
                print(25*"=","chaitanya generalstore", 25*"=")
                print(28*" ","seethamadara")
                print("name:",name,30*" ","date",datetime.now())
                print(75*"-")
                print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
                for i in range(len(pricelist)):
                    print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*' ',plist[i])
                print(75*"-")    
                print(50*" ", 'totalprice:','Rs',totalprice)
                print(75*"-")
                print(50*" ",'finalamount:','Rs',finalamount)
                print(75*"-")
                print(20*"-","thanks for visiting")
                print(75*"-")