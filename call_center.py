print("===== CALL CENTER =====")

name = input("Enter your name: ")
phone = input("Enter your phone number: ")

print("\nSelect your problem:")
print("1. Internet Problem")
print("2. Billing Problem")
print("3. Account Problem")
print("4. Other")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("\nYour complaint is registered for an Internet Problem.")
    print("Our technical team will contact you soon.")

elif choice == 2:
    print("\nYour complaint is registered for a Billing Problem.")
    print("Our billing team will contact you soon.")

elif choice == 3:
    print("\nYour complaint is registered for an Account Problem.")
    print("Our account team will contact you soon.")

elif choice == 4:
    print("\nYour complaint is registered.")
    print("Our customer support team will contact you soon.")

else:
    print("\nInvalid choice.")

print("\nThank you for contacting our Call Center.")
