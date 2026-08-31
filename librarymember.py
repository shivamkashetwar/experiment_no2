                
n=int(input("book member"))
book_name=[]
book_count=[]
for i in range(n):
    name=input("Enter book name: ")
    count=input("Enter book taken: ")
    book_name.append(name)
    book_count.append(count)
total=sum(book_count)
avg=total/n
print("Average of book: ",avg)