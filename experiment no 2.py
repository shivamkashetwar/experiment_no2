n=int(input("enter the no of accounr"))
my_list=[]

for i in range(n):
         id=int(input("enter the  account no "))
         my_list.append(id)


print(my_list)
a=my_list
n1=int(input("which no to you search the no"))



for i in range(len(a)):
    if n1 == a[i]:
           print(f"found the no {a[i] } on the index {i}")

    else:
          i=i+1



