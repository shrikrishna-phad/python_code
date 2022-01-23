import logging
import clear_filename

file_name = clear_filename.filename(__file__)

logging.basicConfig(filename='banklog.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s : %(name)s : %(message)s : %(asctime)s', datefmt='%d/%m/%Y %I:%M:%S')
logger = logging.getLogger(file_name)


def newreg():
    import csv
    import random

    fn = input('Enter your first name: ').lower().strip()
    mn = input('Enter your middle name: ').lower().strip()
    ls = input('Enter your last name: ').lower().strip()

    flag1 = True
    while flag1:
        try:
            age = int(input('Enter your age: '))
            if age < 18:
                raise Exception(f'To open a bank account you must be 18 years old please wait for {18-age} '
                                f'years to open an account')
        except Exception as msg:
            print(msg)
            flag1 = True
            break
        except ValueError:
            f = input("Please Enter the correct value (ony integer value is allowed)."
                      "\nTo try again Enter 'y' To get To exit enter any other key: ").strip()
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

        flag2 = True
        while flag2:
            try:
                mob = int(input('Enter your 10 digit mobile number: '))
                if len(str(mob)) != 10:
                    raise Exception('Mobile Number should be exactly 10 digit')

            except (ValueError , Exception):
                f = input("Please Enter the correct value (ony integer value is allowed)."
                          "\nTo try again Enter 'y' To get To exit enter any other key: ").strip()
                if f == 'y':
                    flag2 = True
                    continue
                else:
                    flag2 = True
                    break
            else:
                flag2 = False
                break

        if not flag2:
            un = input('Enter your preferred username (space not allowed at starting and end): ').lower().strip()
            passw = input('Enter your password(space not allowed at starting and end): ').strip()
            an = random.randint(10000, 99999)

            flag3 = True
            while flag3:
                try:
                    bl = int(input('Enter initial amount you want to deposit: '))
                except (ValueError, Exception):
                    f = input("Please Enter the correct value (ony integer value is allowed)."
                              "Note If you did not deposit valid amount your account would not be created\n"
                              "\nTo try again Enter 'y' To get To exit enter any other key: ").strip()
                    if f == 'y':
                        flag3 = True
                        continue
                    else:
                        flag3 = True
                        break
                else:
                    flag3 = False
                    break

            if not flag3:

                logger.info(f'customer with name {fn, mn, ls} has successfully created new account with number {an}')

                print(f'Your account has been created successfully\n'
                      f'your account number is {an}\n'
                      f'your account balance is {bl}')

                with open('bank_details.csv', 'a', newline='') as fp:
                    wobj = csv.writer(fp)
                    wobj.writerow([fn, mn, ls, age, mob, un, passw, an, bl])
