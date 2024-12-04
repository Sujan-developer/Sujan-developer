import time

class Bank:

    balance = []
    
    while True:
        create_acc = input("Do you want to create account? 'Yes' | 'No': ").lower()
        if create_acc == "yes":
            print("Going to next step, wait...")
            break
            #time.sleep(3)
        elif create_acc == "no":
            break
        
        else:
            continue
    
    #Creating account
    if create_acc == "yes":
        name = input("Enter your name: ")
        while not any(char.isalpha() for char in name):
            name = input("Only alphabetical can be acceptance: ")
            if len(name) <= 2:
                print("3 or more")
                pass
                print("Next step wait...")
                #time.sleep(2)
        while True:
            age = input("Enter your age: ")
            if age.isdigit():
                print("Waiting for ans")
                #time.sleep(2)
                age = int(age)
                break
            else:
                continue

            if age >= 18:
                print("Account sucessfully created!")
            else:
                print("Sorry, we can't accept you.")
        

        
    while True:
        dep_withdraw = input("what do you want to do ?: 'Deposit' | 'Withdraw', | 'Exit': ").lower()
        if dep_withdraw == "deposit":
            max_dep = 10000
            while True:
                dep = input("How much do you want to deposit: ")
                if dep.isdigit():
                    dep = int(dep)
                    if dep > max_dep:
                        print("You can only print upto $10000.")
                        dep = input("How much do you want to deposit: ")
                        break
                balance.append(dep)
                break
            break

        elif dep_withdraw == "withdraw":
            max_wit = 10000
            while True:
                wit = input("How much do you want to withdraw: ")
                if wit.isdigit():
                    wit = int(wit)
                    if wit > balance:
                        print(f"You only have{balance}")
                    if wit > max_wit:
                        print("You can only withdraw upto $10000.")
                elif dep_withdraw == "exit":
                    break


    
    with open("store.txt", "a") as f:
        f.write(f"{name}, {age}, {balance}\n")
        print(f"Your name is {name}, your age is {age}, your balance is ${balance}")












b = Bank()

