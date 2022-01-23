import csv
import logging
import cleanfilename

logging.basicConfig(filename='bankappclass.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(message)s : %(asctime)s',
                    datefmt='%d/%m/%Y %I:%M:%S')

file_name = cleanfilename.file_name(__file__)

logger = logging.getLogger(file_name)


class Password_Change:
    def __init__(self, data, ind):
        self.data = data
        self.ind = ind
        # 5-username
        # 6-password
        # 7-account
        # 8-balance

    def password_change(self):
        flag = True
        n = 4
        while n > 0 and flag:

            self.passw = input(f"Enter the current Password: ")

            if self.passw == self.data[self.data.index(self.ind)][6]:
                flag = False
                break

            else:

                f = input(f"Incorrect password; If you want to enter it again enter 'y' ({n-1} tries left); "
                          "To exit enter any other key: ")
                n -= 1
                if f == 'y':
                    flag = True
                    continue
                else:
                    flag = True
                    break

        if not flag:
            self.passw1 = input("Enter the new Password: ")

            self.passw2 = input("Please Confirm the Password: ")

            if self.passw1 == self.passw2:

                self.data[self.data.index(self.ind)][6] = self.passw2

                logger.info(f"Customer with account number {self.data[self.data.index(self.ind)][7]} "
                            f"has changed password.")

                with open("bankappclass.csv", 'w', newline='') as fp:
                    wobj = csv.writer(fp)
                    for lines in self.data:
                        wobj.writerow(lines)

                print("Your password has been changed successfully")
