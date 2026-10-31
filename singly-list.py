head=None

while True:
    print("\n 1.add the student")
    print("show the student")
    print("exist")

    ch=int(input("enter the you choice"))

    if ch==1:
        name=input("enter the student name")
        new_node=[name,None]

        if head==None:
            head=new_node
        else:
            temp=head

            while temp[1]!=None:
                temp=temp[1]

            temp[1]=new_node

        print("student add succesfully")

    elif ch==2:
        temp=head

        if temp==None:
            print("list is empty")
        else:
            print("student list")
            while temp!=None:
                print(temp[0])
                temp=temp[1]

    elif ch==3:
        print("program exist")
        break

    else:
        print("invalid choice")


        





    