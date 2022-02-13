def accountAction(account):
    action = 0
    while action != 4:
        print("Please choose what to do.")
        print("(1) See Balance (2) Deposit (3) Withdraw (4) Quit")

        action = int(input())
        if action == 1:
            account.balance()
        elif action == 2:
            print("Please enter the amount to deposit.")
            dep = int(input())
            account.deposit(dep)
        elif action == 3:
            print("Please enter the amount to withdraw.")
            wit = int(input())
            account.withdraw(wit)


def selectAccount(card):
    print("Please choose the account you want to use.")
    account_list = card.get_account()
    for acc in account_list:
        print(
            "({idx}) {acc}".format(
                idx=account_list.index(acc) + 1, acc=acc.get_number()
            )
        )

    n = int(input())
    accountAction(card.account[n - 1])


def pinCheck(card):
    print("Please enter your PIN number.")
    pin = int(input())
    if pin == card.pin:
        print("Verified")
        selectAccount(card)
    else:
        print("Wrong PIN number.")


class accountInformation:
    def __init__(self, account_number, money):
        self.account_number = account_number
        self.money = money

    def balance(self):
        print("Balance is {money} dollar.".format(money=self.money))

    def get_number(self):
        return self.account_number

    def deposit(self, dep_money):
        self.money += dep_money
        print(
            "{dep} dollar deposited. Now balance is {bal} dollar.".format(
                dep=dep_money, bal=self.money
            )
        )

    def withdraw(self, with_money):
        if self.money - with_money < 0:
            print("The balance is insufficient.")
        else:
            self.money -= with_money
            print(
                "{wit} dollar withdrawed. Now balance is {bal} dollar.".format(
                    wit=with_money, bal=self.money
                )
            )


class cardInformation:
    account = []

    def __init__(self, pin, account):
        self.pin = pin
        self.account.append(account)

    def add_account(self, account):
        self.account.append(account)

    def get_account(self):
        return self.account

    def modify_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            print("Seccess to modify PIN number")
        else:
            print("Wrong PIN number")


def intro_atm():
    print("Welcome to BearBank ATM\n Please insert your card.")
    print("(1) Make a card (2) Insert card(use test card) ")
    n = int(input())
    if n == 1:
        print("How many accounts do you have to connect to your card?")
        acc_num = int(input())
        account = []
        for i in range(acc_num):
            print("Enter your account number.")
            acc = int(input())
            print("Enter your account balance.")
            bal = int(input())
            account.append(accountInformation(acc, bal))
        print("Enter your card PIN number.")
        pin = int(input())

        if acc_num > 1:
            card = cardInformation(pin, account[0])
            for i in range(1, acc_num):
                card.add_account(account[i])
        else:
            card = cardInformation(pin, account[0])

        pinCheck(card)

    elif n == 2:
        # test account
        ex_account_1 = accountInformation(1131423, 10)
        ex_account_2 = accountInformation(4463587, 35)
        ex_card = cardInformation(1234, ex_account_1)
        ex_card.add_account(ex_account_2)

        pinCheck(ex_card)

    else:
        print("Please choose 1 or 2.")


if __name__ == "__main__":
    intro_atm()
