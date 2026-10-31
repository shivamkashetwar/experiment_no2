size = 10
table = [None] * size

# Insert key
def insert(key):
    index = key % size

    while table[index] != None:
        index = (index + 1) % size

    table[index] = key
    print("Key inserted")


# Search key
def search(key):
    index = key % size

    for i in range(size):
        if table[index] == key:
            print("Key found")
            return

        if table[index] == None:
            break

        index = (index + 1) % size

    print("Key not found")


# Delete key
def delete(key):
    index = key % size

    for i in range(size):
        if table[index] == key:
            table[index] = "DELETED"
            print("Key deleted")
            return

        if table[index] == None:
            break

        index = (index + 1) % size

    print("Key not found")


# Main program
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        insert(key)

    elif ch == 2:
        key = int(input("Enter key: "))
        search(key)

    elif ch == 3:
        key = int(input("Enter key: "))
        delete(key)

    elif ch == 4:
        print(table)

    elif ch == 5:
        break

    else:
        print("Invalid choice")