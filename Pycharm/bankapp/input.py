print("Welcome to the BankApp")

flag1 = True
while flag1:
    try:
        choice = int(input("Enter 1 for login\nEnter 2 for new registration: "))

    except ValueError:
        f = input("Please Enter the correct value.\nTo try again Enter 'y' To get To exit enter any other key: ").strip()
        if f == 'y':
            flag1 = True
            continue
        else:
            flag1 = True
            break
    else:
        flag1 = False
        break

if not flag1:
    if choice == 1:
        from login import login

        a = login()
        if not a:
            flag = a
        else:
            flag, data, i = a

        if flag:
            choice1 = input('Enter 1 for Withdrawal\n'
                            'Enter 2 for Deposit\n'
                            'Enter 3 for Password change: ')

            if choice1 == '1':
                import withdrawal
                withdrawal.withdrawal(data, i)

            elif choice1 == '2':
                import deposit
                deposit.deposit(data, i)

            elif choice1 == '3':
                import password_change
                password_change.password_change(data, i)

        print("Thank you for banking with us")

    elif choice == 2:
        import new_registration
        new_registration.newreg()

        print("Thank you for banking with us")

else:
    pass
