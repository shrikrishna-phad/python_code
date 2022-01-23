import logging
import csv
import clear_filename

file_name = clear_filename.filename(__file__)

logging.basicConfig(filename='banklog.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s : %(message)s : %(asctime)s', datefmt='%d/%m/%Y %I:%M:%S')
logger = logging.getLogger('file_name')


def password_change(data, i):
    logger.info(f'customer with account number {data[data.index(i)][7]} '
                f'has requested a password change.')

    password = input("Enter your current password: ")
    if password == data[data.index(i)][6]:
        password1 = input('Enter the new password: ')
        password2 = input('Confirm the new password: ')

        if password1 == password2:
            data[data.index(i)][6] = password2
            p = input("Your password has been changed successfully"
                      "Enter 1 to show your password on the screen: ")
            if p == '1':
                print(password2)
            else:
                pass

            logger.info(f'customer with account number {data[data.index(i)][7]} '
                        f'has has changed his password successfully to {data[data.index(i)][6]}')

            with open('bank_details.csv', 'w', newline='') as fp:
                wobj = csv.writer(fp)
                for obj in data:
                    wobj.writerow(obj)
