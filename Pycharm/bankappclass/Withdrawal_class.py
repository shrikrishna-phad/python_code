import csv
import logging
import cleanfilename

logging.basicConfig(filename='bankappclass.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(message)s : %(asctime)s',
                    datefmt='%d/%m/%Y %I:%M:%S')

file_name = cleanfilename.file_name(__file__)

logger = logging.getLogger(file_name)


class Withdrawal:
    def __init__(self, data, ind):
        self.data = data
        self.ind = ind
        # 5-username
        # 6-password
        # 7-account
        # 8-balance

    def withdrawal(self):
        flag = True
        while flag:
            try:
                self.amount = int(input("Enter the amount you want to withdraw(in indian rupees) : "))
            except ValueError:
                f = input("please enter the correct amount\n"
                          "To try again enter 'y'; To exit enter any other key : ")
                if f == 'y':
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break

        if not flag:
            if self.amount > int(self.data[self.data.index(self.ind)][8]):
                print("Insufficient Balance")

            else:
                self.bal = int(self.data[self.data.index(self.ind)][8]) - self.amount

                self.data[self.data.index(self.ind)][8] = self.bal

                logger.info(f"Customer with account number {self.data[self.data.index(self.ind)][7]} "
                            f"has withdrew Rs.{self.bal} from account")

                with open("bankappclass.csv", 'w', newline='') as fp:
                    wobj = csv.writer(fp)
                    for lines in self.data:
                        wobj.writerow(lines)

                        flag = True
                        a = (True, self.data, self.ind)

        print(f"Your new account balance is Rs.{self.bal}")
