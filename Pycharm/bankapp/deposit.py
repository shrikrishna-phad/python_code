import logging
import csv
import clear_filename

file_name = clear_filename.filename(__file__)

logging.basicConfig(filename='banklog.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s : %(message)s : %(asctime)s', datefmt='%d/%m/%Y %I:%M:%S')
logger = logging.getLogger('file_name')


def deposit(data, i):
    logger.info(f'customer with account number {data[data.index(i)][7]} '
                f'has requested a deposit')

    print(f'Your account number is {data[data.index(i)][7]}')
    check = input('''Enter 'y' if account number is correct else enter 'n': ''')

    if check == 'y' or 'yes':
        print(f'Your account balance is {data[data.index(i)][8]}')
        amount = float(input('Enter The amount to deposit in Indian rupees: '))

        data[data.index(i)][8] = (float(data[data.index(i)][8]) + amount)
        print(f'Your new account balance is Rs.{data[data.index(i)][8]}')

        logger.info(f'customer with account number {data[data.index(i)][7]} '
                    f'has successfully deposited Rs.{amount}')

        with open('bank_details.csv', 'w', newline='') as fp:
            wobj = csv.writer(fp)
            for obj in data:
                wobj.writerow(obj)
