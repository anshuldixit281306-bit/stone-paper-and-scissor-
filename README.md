# time up counter 

```import time

seconds = int(input("Enter the number of seconds: "))

# Countdown loop
while seconds > 0:
    print(seconds)
    time.sleep(1)   # Wait for 1 second
    seconds -= 1    # Reduce the seconds by 1

print("Time's up!")
```

# ATM Machine Simulation

```
balance = 10000

while True:
    print("===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print("Your current balance is: ₹", balance)

    elif choice == 2:
        deposit = float(input("Enter amount to deposit: ₹"))
        if deposit > 0:
            balance = balance + deposit
            print("₹", deposit, "deposited successfully.")
            print("Updated Balance: ₹", balance)
        else:
            print("Invalid deposit amount.")

    elif choice == 3:
        withdraw = float(input("Enter amount to withdraw: ₹"))
        if withdraw > balance:
            print("Insufficient Balance")
        elif withdraw <= 0:
            print("Invalid withdrawal amount.")
        else:
            balance = balance - withdraw
            print("Please collect your cash.")
            print("Remaining Balance: ₹", balance)

    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid Choice")
```
