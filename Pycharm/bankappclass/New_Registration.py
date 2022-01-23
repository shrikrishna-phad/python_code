import csv
import logging

import cleanfilename

logging.basicConfig(filename='bankappclass.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(message)s : %(asctime)s',
                    datefmt='%d/%m/%Y %I:%M:%S')

file_name = cleanfilename.file_name(__file__)

logger = logging.getLogger(file_name)


class NewRegistration:
    def __init__(self):
        self.flag = False
        self.name = [input("Enter Your First Name: ").lower().strip(),
                     input("Enter Your Middle Name: ").lower().strip(),
                     input("Enter Your Last Name: ").lower().strip()]
        flag = True
        while flag:
            try:
                self.age = int(input("Enter Your age: "))
                if self.age < 18:
                    print(f"You must be Over 18 years of age to open bank account so wait {18 - self.age} "
                          f"to open bank account, if you want to open child account contact the bank")
                    flag = True
                    break

            except ValueError:
                f = input("Age must be in integer, to try again enter 'y'. "
                          "To exit enter any other key: ").lower().strip()
                if f == 'y':
                    continue
                else:
                    flag = True
                    break
            else:
                flag = False

        if not flag:

            with open('bankappclass.csv', 'r') as fp:
                robj = csv.reader(fp)
                data = list(robj)

            flag = True
            while flag:
                try:
                    self.mobile = int(input("Enter Your Mobile Number (this mobile number will be "
                                            "registered/linked with your bank account): "))
                    if len(str(self.mobile)) != 10:
                        raise RuntimeError
                except ValueError:
                    f = input("Mobile number should be integer."
                              "To try again enter 'y' to Exit enter any other key : ").lower().strip()
                    if f == 'y':
                        continue
                    else:
                        flag = True
                        break
                except RuntimeError:
                    f = input("Mobile number should be 10 digit long."
                              "To try again enter 'y' to Exit enter any other key : ").lower().strip()
                    if f == 'y':
                        continue
                    else:
                        flag = True
                        break
                else:
                    flag = False
                    break

                finally:
                    for lines in data:
                        if str(self.mobile) in lines:
                            print("Entered Mobile Number is already registered with us.\n"
                                  "Try the registration with different number")
                            flag = True
                            break

        if not flag:

            flag = True
            while flag:
                self.username = input("Entered preferred User Name: ").lower().strip()
                z = 'This is Jugad'

                for lines in data:
                    if self.username in lines:
                        z = input("User Name already exists.\nTo enter User Name again "
                                  "enter 'y'; To Exit enter any other kay : ").lower().strip()
                        break
                    else:
                        z = 'xaybzc'

                if z == 'y' or z == 'This is Jugad':
                    flag = True
                    continue
                elif z == 'xaybzc':
                    flag = False
                    break
                elif z not in {'y', 'xyz', 'This is Jugad'}:
                    flag = True
                    break

        if not flag:
            flag = True
            while flag:
                self.password1 = input("Enter the password (case sensitive): ")
                self.password2 = input("Confirm the password: ")
                if self.password1 == self.password2:
                    self.password = self.password2
                    flag = False
                    break
                else:
                    f = input("Entered password does not match to enter again enter 'y'."
                              " To exit enter any other key: ").lower().strip()
                    if f == 'y':
                        continue
                    else:
                        flag = True
                        break

        if not flag:
            import random
            flag = True
            while flag:
                self.account_number = random.randint(10000, 99999)
                for lines in data:
                    if self.account_number in lines:
                        continue
                    else:
                        flag = False
                        break

        if not flag:
            flag = True
            while flag:
                try:
                    self.balance = int(input("Enter the amount you want to deposit in the account: "))
                    if self.balance < 1:
                        f = input("Value must be positive integer.\nTo enter again enter "
                                  "'y', to exit enter any other key: ").lower().strip()
                        if f == 'y':
                            continue
                        else:
                            flag = True
                            break
                except ValueError:
                    f = input("Value must be positive integer.\nTo enter again enter "
                              "'y', to exit enter any other key: ").lower().strip()
                    if f == 'y':
                        continue
                    else:
                        flag = True
                        break
                else:
                    flag = False
                    break

        if not flag:
            print("You have entered following details read them carefully")
            print("First Name = ", self.name[0])
            print("Middle Name = ", self.name[1])
            print("Last Name = ", self.name[2])
            print("Age = ", self.age)
            print("Mobile Number = ", self.mobile)
            print("User Name = ", self.username)
            print("Password = ", self.password)
            print("Initial deposit = ", self.balance)

            flag = True
            while flag:
                f = input("Enter 'y' above information if correct, Enter any other key if not : ").lower().strip()
                if f == 'y':
                    self.flag = True
                    break
                else:
                    f = input(f"Please confirm! Enter 'y' above information if "
                              f"correct, Enter any other key if not : ").lower().strip()
                    if f == 'y':
                        self.flag = False
                        break

    def registration(self):
        if self.flag:
            with open('bankappclass.csv', 'a', newline='') as fp:
                wobj = csv.writer(fp)
                wobj.writerow([self.name[0], self.name[1], self.name[2], self.age, self.mobile,
                               self.username, self.password, self.account_number, self.balance])

            print(f"Your account has been created with account number = "
                  f"{self.account_number} and initial balance = {self.balance}")

            logger.info(f"A customer {self.name} has opened account\n"
                        f" with account number {self.account_number} and balance {self.balance}")

        if not self.flag:
            print("Please try registration process again\nThank You For visiting Bank app with Class")
