import csv
import logging
import cleanfilename

logging.basicConfig(filename='bankappclass.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(message)s : %(asctime)s',
                    datefmt='%d/%m/%Y %I:%M:%S')

file_name = cleanfilename.file_name(__file__)

logger = logging.getLogger(file_name)


class Login:
    def __init__(self):
        with open('bankappclass.csv', 'r') as fp:
            robj = csv.reader(fp)
            self.data = list(robj)

    def login(self):
        flag = True
        flag1 = True

        self.mobile = input("Enter Your Registered mobile number : ").lower().strip()

        for lines in self.data:

            if self.mobile in lines:
                ind = lines
                flag = False

                # 5-username
                # 6-password
                # 7-account
                # 8-balance
                break

            elif self.mobile not in lines:
                flag = 'xaybzc'
        if not flag:
            self.account = input("Enter Your Account number : ").lower().strip()

            if self.account == self.data[self.data.index(ind)][7]:
                # print(self.data.index(ind))

                self.user_name = input("Enter Your User name : ").lower().strip()
                self.password = input("Enter your Password : ").strip()

                if self.user_name == self.data[self.data.index(ind)][5] and \
                    self.password == self.data[self.data.index(ind)][6]:

                    flag1 = False
                    a = (False, self.data, ind)

                    logger.info(f"Customer with account number {self.account} has logged in successfully")

                else:
                    print("Incorrect Username or password")
            else:
                print("Incorrect Account number")

        elif flag == 'xaybzc':
            print("This mobile number is no registered with us, please try again. "
                  "If not customer please Go to New Registration")

        if not flag1:
            return a

        elif flag1:
            return flag1
