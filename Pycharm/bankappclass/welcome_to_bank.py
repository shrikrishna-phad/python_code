print("Wel-Come to Bankapp with class")

choice = input("Enter 1 for New Registration\nEnter 2 for login : ")

if choice == '1':
    import New_Registration

    obj_Reg = New_Registration.NewRegistration()
    obj_Reg.registration()

if choice == '2':
    import Login_class

    obj = Login_class.Login()
    a = obj.login()
    # a = obj.login()
    if a == True:
        flag = True
    else:
        flag, data, ind = a

    if not flag:
        choice2 = input("You have logged in successfully\n"
                        "Enter 1 for Withdrawal\n"
                        "Enter 2 for Deposit\n"
                        "Enter 3 for Password Change\n"
                        "Enter 4 to raise a Complaint: ")

        if choice2 == '1':
            import Withdrawal_class
            obj_With = Withdrawal_class.Withdrawal(data, ind)
            obj_With.withdrawal()

        elif choice2 == '2':
            import Deposite_class
            obj_Dep = Deposite_class.Deposit(data, ind)
            obj_Dep.deposit()

        elif choice2 == '3':
            import PasswordChange_class
            obj_Passw = PasswordChange_class.Password_Change(data, ind)
            obj_Passw.password_change()
