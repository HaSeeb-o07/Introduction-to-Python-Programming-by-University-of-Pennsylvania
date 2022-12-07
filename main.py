import nose.tools as tools
import re


def import_and_create_bank(filename):
    bank = {}
    f = open(filename, 'r')
    lines = f.readlines()

    for line in lines:
        lst = line.strip().split(':')

        if len(lst) <= 1:
            continue

        key = lst[0].strip()
        value = lst[1].strip()
        try:
            value = float(value)
            bank[key] = bank.get(key, 0) + value
        except:
            continue

    f.close()
    return bank


def signup(user_accounts, log_in, username, password):
    def valid(password):
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        p = re.compile(regex)
        if re.search(p, password):
            return True
        else:
            return False

    if username == password:
        return False
    else:
        if username in user_accounts.keys():
            return True
        else:
            if valid(password) == True:
                user_accounts[username] = password
                log_in[username] = False
                return user_accounts, log_in
            else:
                return False


def import_and_create_accounts(filename):
    user_accounts = {}
    log_in = {}
    with open(filename, "r") as data:
        lines = data.readlines()
        for i in lines:
            new = i.strip().split("-")
            if len(new) <= 1:
                continue
            key = new[0].strip()
            value = new[1].strip()
            try:
                user_accounts, log_in = signup(user_accounts, log_in, key, value)
            except:
                pass
    return user_accounts, log_in


def login(user_accounts, log_in, username, password):
    if username not in user_accounts.keys():
        return False
    elif user_accounts[username] != password:
        return False

    log_in[username] = True
    return True


def update(bank, log_in, username, amount):
    # your code here
    if username in bank:
        if log_in[username] == True:
            if amount + bank[username] >= 0:
                bank[username] = bank[username] + amount
                return True
            else:
                return False
        else:
            return False
    else:
        bank[username] = amount
        return True


def transfer(bank, log_in, userA, userB, amount):
    # your code here
    if (userA in bank.keys()):
        if (userB in log_in.keys()):
            if log_in[userA] == True:
                if bank[userA] - amount >= 0:
                    bank[userA] = bank[userA] - amount
                    try:
                        bank[userB] = bank[userB] + amount
                    except:
                        bank[userB] = amount
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False


def change_password(user_accounts, log_in, username, old_password, new_password):
    def valid(password):
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        p = re.compile(regex)
        if re.search(p, password):
            return True
        else:
            return False

    if username in user_accounts.keys():
        if log_in[username] == True:
            if old_password == user_accounts[username]:
                if new_password != old_password:
                    if valid(new_password):
                        user_accounts[username] = new_password
                        return True
        else:
            return False


def delete_account(user_accounts, log_in, bank, username, password):

    # your code here
    if username in user_accounts.keys():
        if log_in[username] == True:
            if user_accounts[username] == password:
                del log_in[username]
                del bank[username]
                del user_accounts[username]
                return True
            else:
                return False
        else:
            return False
    else:
        return False



def main():
    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
                       "1. login\n"
                       "2. signup\n"
                       "3. change password\n"
                       "4. delete account\n"
                       "5. update amount\n"
                       "6. make a transfer\n"
                       "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")


if __name__ == '__main__':
    main()

