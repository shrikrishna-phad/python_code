import logging
import csv
import clear_filename

file_name = clear_filename.filename(__file__)

logging.basicConfig(filename='banklog.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(message)s : %(asctime)s', datefmt='%d/%m/%Y %I:%M:%S')

logger = logging.getLogger(file_name)


def login():
    flag = False
    with open('bank_details.csv', 'r') as fp:
        robj = csv.reader(fp)
        data = list(robj)
        # print(data)

        mob_no = input('To login please enter your registered mobile number: ').lower().strip()

        logger.info(f"customer with mobile number {mob_no} has requested a login.")

        for i in data:

            if mob_no in i:
                # print(data.index(i))
                # print(i.index(mob_no))

                user_name = input("Enter your user name: ").lower().strip()
                password = input("Enter your password (password is case sensitive ): ").strip()

                if user_name == data[data.index(i)][5] and password == data[data.index(i)][6]:

                    logger.info(f'customer with mobile number {mob_no} user name {user_name} '
                                f'has logged in successfully.')
                    flag = True
                    a = (True, data, i)

                else:
                    print("incorrect password or user name")
    if flag:
        return a
    else:
        return flag
