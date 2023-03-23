from prettytable import PrettyTable
MyTable=PrettyTable(['n','misprediction rate'])
for n in range (2,21):
    corr=0
    tot=856017
    a=0
    arr=[]
    while a<(2**n):
        arr.append(0b00)
        a+=1
    f=open("trace.txt","r")
    for i in f:
        add=i.split()
        fadd=int(add[0])
        pred=add[1]
        rem=fadd%(2**n)
        k=arr[rem]
        if (k==0b00 or k==0b01) and pred=='T':
            corr+=1
        elif (k==0b10 or k==0b11) and pred=='N':
            corr+=1    
        if (k!=0b00) and pred=='T':
            arr[rem]-=1
        if (k!=0b11) and pred=='N':
            arr[rem]+=1
    misp=round((tot-corr)*100/tot,2)
    MyTable.add_row([n, misp])
print(MyTable)


    
        
        

