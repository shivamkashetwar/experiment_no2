n=int(input("enter the nio of salary"))

list=[]

for i in range(n):
    id=int(input(f"enter the salary {i+1}  "))
    list.append(id)

print("unsorted list is",list)

for i in range(n-1):
    min=i;

    for j in range(i+1,n):
        if(list[j]<list[min]):
            min=j


    list[i],list[min]=list[min],list[i]


print("sorrted salary is",list)


