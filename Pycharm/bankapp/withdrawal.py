import logging
import csv
import clear_filename

file_name = clear_filename.filename(__file__)

logging.basicConfig(filename='banklog.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s : %(message)s : %(asctime)s', datefmt='%d/%m/%Y %I:%M:%S')
logger = logging.getLogger(file_name)


def withdrawal(data, i):
    logger.info(f'customer with account number {data[data.index(i)][7]} '
                f'has requested a withdrawal')

    print(f'Your account number is {data[data.index(i)][7]}')
    check = input('''Enter 'y' if account number is correct else enter 'n': ''')
    if check == 'y' or 'yes':
        print(f'Your account balance is {data[data.index(i)][8]}')

        flag1 = True
        while flag1:
            try:
                amount = float(input('Enter The amount to withdraw in Indian rupees: '))
            except ValueError:
                f = input("please enter the correct amount.\n"
                          "to try again Enter 'y' else press any other key: ")
                if f == 'y':
                    flag1 = True
                    continue
                else:
                    flag1 = False
                    break
            else:
                flag1 = False
                break

        if not flag1:

            if amount > float(data[data.index(i)][8]):
                print('Insufficient balance')

                logger.info(f'customer with account number {data[data.index(i)][7]} '
                            f'Was unable to withdraw due to insufficient balance')
            else:
                data[data.index(i)][8] = (float(data[data.index(i)][8]) - amount)
                print(f'Your new account balance is Rs.{data[data.index(i)][8]}')

                logger.info(f'customer with account number {data[data.index(i)][7]} '
                            f'has withdrew Rs.{amount} successfully')

                with open('bank_details.csv', 'w', newline='') as fp:
                    wobj = csv.writer(fp)
                    for obj in data:
                        wobj.writerow(obj)

    else:
        print("Please Contact the bank")
        r = input("If you want To raise a complaint about this issue Enter 'y': ")
        if r == 'y':
            print("For our reference we need some information")
            mob = input("Mobile number: ")
            name = [input("First Name: "), input("Middle Name"), input("Last Name")]
            an = input("Enter Your Account number: ")
            comp = input("Enter your complaint: ")

            with open("bank_complaints.csv", 'a', newline='') as f:
                wb = csv.writer(f)
                wb.writerow([name[0], name[1], name[2], mob, an, comp])

            print("Your complaint has been registered successfully\n"
                  "Please note down your complaint number for future reference\n"
                  "Your complaint number is ")
