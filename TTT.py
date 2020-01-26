import random
import time

def printbox(a):
    k=0
    for i in range(3): 
       print(' '*40,a[k],a[k+1],a[k+2],end='\n')
       k+=3

def find(a,s1,s2):
    w=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    x,y=[],[]
    for i in w:
        for j in i:
            if a[j]==s1:
                x.append(i)
                break
    #print(x,end='\n')
    for i in x:
        cont=0
        cont2=0
        for j in i:
            if a[j]==s1:
                cont+=1
            if a[j]!='.':
                cont2+=1
        if cont2!=3:
            y.append(cont)
        elif cont2==3:
            y.append(0)
    #print(y,end="\n")
    #print(cont2,end=" ")
    #print(y.index(max(y)))
    ind=y.index(max(y))
    if max(y)==2:
           #print("hi")
           return random.choice(x[ind])
    else:
           return random.randint(2,9)-1
        


def check(a,s):
    if a[0]==a[1]==a[2]==s or a[3]==a[4]==a[5]==s or a[6]==a[7]==a[8]==s or a[0]==a[3]==a[6]==s or a[1]==a[4]==a[7]==s or a[2]==a[5]==a[8]==s or a[2]==a[4]==a[6]==s or a[0]==a[4]==a[8]==s:
        return 1
    else:
        return 0
    

print(' '*25,"<Welcome to Tic Tac Toe game>")

choice="no"
user,pc=0,0
win="user"

while(True):
    
    a=['.','.','.','.','.','.','.','.','.']
    b=[0,0,0,0,0,0,0,0,0]
    
    print()
    print(" "*15,"Your score:",user," "*15,"PC score:",pc)
    print()
    
    while(True):
        s1=str(input("\nChoose icon(o/x):"))
        if(s1=='o' or s1=='x'):
            if s1=='o':
                s2='x'
            elif s1=='x':
                s2='o'
            break
        else:
            print("Please choose a valid icon!!")
        print(end='\n')   
    while(True):
        d=0
        while(True):
            print(" "*25)
            c=int(input("Choose a number(1-9):"))-1
            if b[c]!=1:
                    a[c]=s1
                    b[c]=1
                    printbox(a)
                    break
            else:
                    continue
     
            
        time.sleep(0.5)

        if(check(a,s1)):
            print("You have won")
            user+=1
            win="user"
            break
       
        if(sum(b)==9):
            print("Game over\n")
        else:
            print("\n")

        while(True):
            t=find(a,s1,s2)
            if b[t]!=1:
                    a[t]=s2
                    b[t]=1
                    printbox(a)
                    break
            elif(sum(b)==9):
                    break
            else:
                    continue
        if(check(a,s2)):
             print("PC has won")
             pc+=1
             win="pc"
             break
        if(sum(b)==9):
             print("Draw\n")
             user+=1
             pc+=1
             break
        else:
             print("\n")
    choice=str(input("Do you wanna continue(yes):"))
    if choice != "yes":
        break
