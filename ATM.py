from enum import Enum

class TransactionType(Enum):
    WITHDRAWAL = 1
    BALANCE_CHECK = 2

    @staticmethod
    def show_transaction_types():
        for transaction_type in TransactionType:
            print(transaction_type)

class Card:
    def __init__(self, card_number, pin, account):
        self.__card_number = card_number
        self.__pin = pin
        self.__account = account
    
    def is_pin_correct(self, pin):
        return self.__pin == pin

    def get_bank_balance(self):
        return self.__account.get_balance()

    def withdraw(self, amount):
        return self.__account.withdraw(amount)
    
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance -= amount
        return "Withdrawal successful"

class User:
    def __init__(self, name, card, account):
        self.__name = name
        self.__card = card
        self.__account = account
    
    def get_card(self):
        return self.__card
    
    def set_card(self, card):
        self.__card = card

    def get_account(self):
        return self.__account

class ATMState:
    
    def insert_card(self, card):
        print("OOPs! Invalid operation")
    
    def authenticate_pin(self, card, pin):
        print("OOPs! Invalid operation")

    def select_operation(self, card, transaction_type):
        print("OOPs! Invalid operation")
    
    def withdraw(self, card, amount):
        print("OOPs! Invalid operation")
    
    def check_balance(self, card):
        print("OOPs! Invalid operation")
    
    def return_card(self):
        print("OOPs! Invalid operation")
    
    def exit(atm):
        print("OOPs! Invalid operation")

class IdleState(ATMState):
    def insert_card(self, atm, card):
        print("Card inserted")
        atm.set_curr_atm_state(HasCardState())

class HasCardState(ATMState):
    def authenticate_pin(self, atm, card, pin):
        if card.is_pin_correct(pin):
            print("Pin authenticated")
            atm.set_curr_atm_state(SelectOperationState())
        else:
            print("Invalid pin")
            self.exit(atm)
    
    def return_card(self):
        print("Card returned")
    
    def exit(self, atm):
        self.return_card()
        atm.set_curr_atm_state(IdleState())
        print("Exiting")
        
class SelectOperationState(ATMState):
    def __init__(self):
        self.show_operations()
    
    def show_operations(self):
        print("Select operation")
        TransactionType.show_transaction_types()


    def select_operation(self, atm, card, transaction_type):
        if transaction_type == TransactionType.WITHDRAWAL:
            atm.set_curr_atm_state(WithdrawalState())
        elif transaction_type == TransactionType.BALANCE_CHECK:
            atm.set_curr_atm_state(CheckBalanceState())
        else:
            print("Invalid operation")
            self.exit(atm)
    
    def return_card(self):
        print("Card returned")
    
    def exit(self, atm):
        self.return_card()
        atm.set_curr_atm_state(IdleState())
        print("Exiting")

class CheckBalanceState(ATMState):
    def check_balance(self, atm, card):
        print("Balance: ", card.get_bank_balance())
        self.exit(atm)
    
    def return_card(self):
        print("Card returned")
    
    def exit(self, atm):
        self.return_card()
        atm.set_curr_atm_state(IdleState())
        print("Exiting")

class WithdrawalState(ATMState):
    def __init__(self):
        print("Enter amount to withdraw")

    def withdraw(self, atm, card, amount):
        if atm.get_balance() < amount:
            print("Insufficient balance in the ATM")
            self.exit(atm)
        elif card.get_bank_balance() < amount:
            print("Insufficient balance in the account")
            self.exit(atm)
        else:
            card.withdraw(amount)
            atm.withdraw(amount)
            
            # chain of responsibility
            cash_withdraw_processor = HundredCashWithdrawProcessor(TwentyCashWithdrawProcessor(FiveCashWithdrawProcessor(OneCashWithdrawProcessor(None))))

            cash_withdraw_processor.withdraw(atm, amount)
            self.exit(atm)

    def return_card(self):
        print("Card returned")
    
    def exit(self, atm):
        self.return_card()
        atm.set_curr_atm_state(IdleState())
        print("Exiting")

class CashWithdrawProcessor:
    def __init__(self, successor):
        self.__successor = successor

    def withdraw(self, atm, rem_amount):
        if self.__successor is not None:
            self.__successor.withdraw(atm, rem_amount)

class HundredCashWithdrawProcessor(CashWithdrawProcessor):
    def __init__(self, successor):
        super().__init__(successor)
    
    def withdraw(self, atm, rem_amount):
        print("HundredCashWithdrawProcessor", rem_amount)
        required = rem_amount // 100
        remaining = rem_amount % 100

        if required <= atm.get_hundred_count():
            atm.withdraw_hundred(required)
        else:
            atm.withdraw_hundred(atm.get_hundred_count())
            remaining += (required - atm.get_hundred_count()) * 100
        
        if remaining != 0:
            super().withdraw(atm, remaining)

class TwentyCashWithdrawProcessor(CashWithdrawProcessor):
    def __init__(self, successor):
        super().__init__(successor)
    
    def withdraw(self, atm, rem_amount):
        required = rem_amount // 20
        remaining = rem_amount % 20

        if required <= atm.get_twenty_count():
            atm.withdraw_twenty(required)
        else:
            atm.withdraw_twenty(atm.get_twenty_count())
            remaining += (required - atm.get_twenty_count()) * 20
        
        if remaining != 0:
            super().withdraw(atm, remaining)

class FiveCashWithdrawProcessor(CashWithdrawProcessor):
    def __init__(self, successor):
        super().__init__(successor)
    
    def withdraw(self, atm, rem_amount):
        required = rem_amount // 5
        remaining = rem_amount % 5

        if required <= atm.get_five_count():
            atm.withdraw_five(required)
        else:
            atm.withdraw_five(atm.get_five_count())
            remaining += (required - atm.get_five_count()) * 5
        
        if remaining != 0:
            super().withdraw(atm, remaining)

class OneCashWithdrawProcessor(CashWithdrawProcessor):
    def __init__(self, successor):
        super().__init__(successor)
    
    def withdraw(self, atm, rem_amount):
        required = rem_amount // 1
        remaining = rem_amount % 1

        if required <= atm.get_one_count():
            atm.withdraw_one(required)
        else:
            atm.withdraw_one(atm.get_one_count())
            remaining += (required - atm.get_one_count()) * 1
        
        if remaining != 0:
            super().withdraw(atm, remaining)
    
class __ATM(type):
    __instance = None

    def __new__(cls, name, bases, dct):
        if cls.__instance is None:
            cls.__instance = type.__new__(cls, name, bases, dct)
        return cls.__instance

class ATM(metaclass=__ATM):
    def __init__(self):
        self.__hundred_count = 0
        self.__twenty_count = 0
        self.__five_count = 0
        self.__one_count = 0
        self.__curr_atm_state = IdleState()
        self.__balance = 100 * self.__hundred_count + 20 * self.__twenty_count + 5 * self.__five_count + self.__one_count
    
    def get_atm_instance(self):
        return self.__instance

    def get_curr_atm_state(self):
        return self.__curr_atm_state

    def set_curr_atm_state(self, curr_atm_state):
        self.__curr_atm_state = curr_atm_state
    
    def get_atm_object(self):
        return self.get_atm_instance()

    def get_balance(self):
        return self.__balance
    
    def set_atm_balance(self, hundred_count, twenty_count, five_count, one_count):
        self.__hundred_count = hundred_count
        self.__twenty_count = twenty_count
        self.__five_count = five_count
        self.__one_count = one_count
        self.__balance = 100 * self.__hundred_count + 20 * self.__twenty_count + 5 * self.__five_count + self.__one_count
    
    def get_hundred_count(self):
        return self.__hundred_count

    def get_twenty_count(self):
        return self.__twenty_count

    def get_five_count(self):
        return self.__five_count

    def get_one_count(self):
        return self.__one_count
    
    def withdraw(self, amount):
        self.__balance -= amount

    def withdraw_hundred(self, count):
        self.__hundred_count -= count
    
    def withdraw_twenty(self, count):
        self.__twenty_count -= count
    
    def withdraw_five(self, count):
        self.__five_count -= count
    
    def withdraw_one(self, count):
        self.__one_count -= count
    
    def print_atm_state(self):
        print("ATM State")
        print("Curr State: ", self.__curr_atm_state.__class__.__name__)
        print("Hundreds: ", self.__hundred_count)
        print("Twenties: ", self.__twenty_count)
        print("Fives: ", self.__five_count)
        print("Ones: ", self.__one_count)
        print("Balance: ", self.__balance)


if __name__ == "__main__":
    atm = ATM()
    atm.print_atm_state()
    atm.set_atm_balance(10, 10, 10, 10)
    atm.print_atm_state()
    account =  BankAccount(1000)
    card = Card("1234", "1234", account)
    user = User("John", card, account)

    atm.get_curr_atm_state().insert_card(atm, card)
    atm.get_curr_atm_state().authenticate_pin(atm, card, "1234")
    atm.get_curr_atm_state().select_operation(atm, card, TransactionType.WITHDRAWAL)
    atm.get_curr_atm_state().withdraw(atm, card, 500)
    atm.print_atm_state()
    print("=====================================")


    atm.get_curr_atm_state().insert_card(atm, card)
    atm.get_curr_atm_state().authenticate_pin(atm, card, "12345")
    print("=====================================")

    atm.get_curr_atm_state().insert_card(atm, card)
    atm.get_curr_atm_state().authenticate_pin(atm, card, "1234")
    atm.get_curr_atm_state().select_operation(atm, card, TransactionType.BALANCE_CHECK)
    atm.get_curr_atm_state().check_balance(atm, card)
    atm.print_atm_state()
    print("=====================================")

    atm.get_curr_atm_state().insert_card(atm, card)
    atm.get_curr_atm_state().authenticate_pin(atm, card, "1234")
    atm.get_curr_atm_state().select_operation(atm, card, TransactionType.WITHDRAWAL)
    atm.get_curr_atm_state().withdraw(atm, card, 800)
    atm.print_atm_state()
    print("=====================================")

    atm.get_curr_atm_state().insert_card(atm, card)
    atm.get_curr_atm_state().authenticate_pin(atm, card, "1234")
    atm.get_curr_atm_state().select_operation(atm, card, TransactionType.WITHDRAWAL)
    atm.get_curr_atm_state().withdraw(atm, card, 700)
    atm.print_atm_state()
    print("=====================================")

    atm.get_curr_atm_state().insert_card(atm, card)
    atm.get_curr_atm_state().authenticate_pin(atm, card, "1234")
    atm.get_curr_atm_state().select_operation(atm, card, TransactionType.WITHDRAWAL)
    atm.get_curr_atm_state().withdraw(atm, card, 400)
    atm.print_atm_state()