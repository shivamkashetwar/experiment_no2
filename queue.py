queue = []
size = int(input("Enter the size of queue: "))

while True:
    print("\n--- QUEUE OPERATIONS ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Rear")
    print("5. Display")
    print("6. Check Empty")
    print("7. Check Full")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # Enqueue
    if choice == 1:
        if len(queue) == size:
            print("Queue is Full")
        else:
            value = int(input("Enter value: "))
            queue.append(value)
            print("Element inserted:", value)

    # Dequeue
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            value = queue.pop(0)
            print("Element deleted:", value)

    # Front
    elif choice == 3:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Front element:", queue[0])

    # Rear
    elif choice == 4:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Rear element:", queue[-1])

    # Display
    elif choice == 5:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue:", queue)

    # Check Empty
    elif choice == 6:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue is not Empty")

    # Check Full
    elif choice == 7:
        if len(queue) == size:
            print("Queue is Full")
        else:
            print("Queue is not Full")

    # Exit
    elif choice == 8:
        print("Exit")
        break

    else:
        print("Invalid choice")
