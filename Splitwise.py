from enum import Enum
from typing import List
from abc import ABC, abstractmethod

class SplitType(Enum):
    EQUAL = 1
    EXACT = 2
    PERCENT = 3
    SHARE = 4


class Balance:
    def __init__(self):
        self.amountOwed = 0
        self.amountGetBack = 0
    
    def getAmountOwed(self):
        return self.amountOwed

    def getAmountGetBack(self):
        return self.amountGetBack

    def setAmountOwed(self, amount):
        self.amountOwed = amount
    
    def setAmountGetBack(self, amount):
        self.amountGetBack = amount

class User:
    def __init__(self, id: int, name: str, email: str, phone: int):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.userExpenseBalanceSheet: UserExpenseBalanceSheet = UserExpenseBalanceSheet()

    def getUserExpenseBalanceSheet(self):
        return self.userExpenseBalanceSheet
    
    def show(self):
        print(self.id, self.name, self.email, self.phone)

class UserExpenseBalanceSheet:
    def __init__(self):
        self.userBalance: dict[User, Balance] = {}
        self.totalExpense = 0
        self.totalPayment = 0
        self.totalYouOwe = 0
        self.totalYouGetBack = 0

    def getTotalExpense(self):
        return self.totalExpense
    
    def getTotalPayment(self):
        return self.totalPayment
    
    def getTotalYouOwe(self):
        return self.totalYouOwe
    
    def getTotalYouGetBack(self):
        return self.totalYouGetBack
    
    def setTotalExpense(self, amount):
        self.totalExpense = amount
    
    def setTotalPayment(self, amount):
        self.totalPayment = amount
    
    def setTotalYouOwe(self, amount):
        self.totalYouOwe = amount
    
    def setTotalYouGetBack(self, amount):
        self.totalYouGetBack = amount

class Split:
    def __init__(self, user_id: int, amount: float):
        self.user_id = user_id
        self.amount = amount
    
    def getUser(self):
        return self.user_id

    def getAmount(self):
        return self.amount


class BalanceSheetManager:
    def updateUserExpenseBalanceSheet(expensePaidBy: User, splits: List[Split], amount: int):
        paidByUserExpenseBalanceSheet = expensePaidBy.getUserExpenseBalanceSheet()
        paidByUserExpenseBalanceSheet.setTotalPayment(paidByUserExpenseBalanceSheet.getTotalPayment() + amount)

        for split in splits:
            userOwe = split.getUser()
            userOweBalanceSheet = userOwe.getUserExpenseBalanceSheet()
            oweAmount = split.getAmount()
            if expensePaidBy == userOwe:
                paidByUserExpenseBalanceSheet.setTotalExpense(paidByUserExpenseBalanceSheet.getTotalExpense() + oweAmount)
            else:
                paidByUserExpenseBalanceSheet.setTotalYouGetBack(paidByUserExpenseBalanceSheet.getTotalYouGetBack() + oweAmount)
                
                userOweBalance = None
                if userOwe.getUser() in paidByUserExpenseBalanceSheet.userBalance:
                    userOweBalance = paidByUserExpenseBalanceSheet.getUserBalance().get(userOwe.getUser())
                else:
                    userOweBalance = Balance()
                    paidByUserExpenseBalanceSheet.getUserBalance().put(userOwe.getUser(), userOweBalance)
                userOweBalance.setAmountOwed(userOweBalance.getAmountOwed() + oweAmount)

                userOweBalanceSheet.setTotalYouOwe(userOweBalanceSheet.getTotalYouOwe() + oweAmount)
                userOweBalanceSheet.setTotalYourExpense(userOweBalanceSheet.getTotalYourExpense() + oweAmount)

                userPaidByBalance: Balance = None
                if expensePaidBy.getUser() in userOweBalanceSheet.getUserBalance():
                    userPaidByBalance = userOweBalanceSheet.getUserBalance().get(expensePaidBy.getUser())
                else:
                    userPaidByBalance = Balance()
                    userOweBalanceSheet.getUserBalance().put(expensePaidBy.getUser(), userPaidByBalance)
                userPaidByBalance.setAmountGetBack(userPaidByBalance.getAmountGetBack() + oweAmount)

    def showUserExpenseBalanceSheet(user: User):
        print("--------------------------")                
        print("Balance sheet of user: ", user.getId())
        userExpenseBalanecSheet: UserExpenseBalanceSheet = user.getUserExpenseBalanceSheet()

        print("Total Expense: ", userExpenseBalanecSheet.getTotalExpense())
        print("Total Payment: ", userExpenseBalanecSheet.getTotalPayment())
        print("Total You Owe: ", userExpenseBalanecSheet.getTotalYouOwe())
        print("Total You Get Back: ", userExpenseBalanecSheet.getTotalYouGetBack())

        for user, balance in userExpenseBalanecSheet.getUserBalance().items():
            print("User: ", user.getId())
            print("Amount Owed: ", balance.getAmountOwed())
            print("Amount Get Back: ", balance.getAmountGetBack())
            print("--------------------------")
        

class Expense:
    def __init__(self, id: int, description: str, amount: float, paid_by: User, split_type: SplitType, splits: List[Split]):
        self.id = id
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.split_type = split_type
        self.splits = splits

class ExpenseSplit(ABC):
    @abstractmethod
    def validate(self, expense: Expense):
        pass

class SplitFactory:
    def get_split(self, split_type: SplitType):
        if split_type == SplitType.EQUAL:
            return EqualSplit()
        elif split_type == SplitType.EXACT:
            return ExactSplit()
        elif split_type == SplitType.PERCENT:
            return PercentSplit()
        elif split_type == SplitType.SHARE:
            return ShareSplit()


class EqualSplit(ExpenseSplit):
    def validate(self, expense: Expense):
        total_amount = 0
        for split in expense.splits:
            total_amount += split.amount

        if total_amount != expense.amount:
            return False

        return True

class ExactSplit(ExpenseSplit):
    def validate(self, expense: Expense):
        total_amount = 0
        for split in expense.splits:
            total_amount += split.amount

        if total_amount != expense.amount:
            return False

        return True

class PercentSplit(ExpenseSplit):
    def validate(self, expense: Expense):
        total_percent = 0
        for split in expense.splits:
            total_percent += split.amount

        if total_percent != 100:
            return False

        return True

class ShareSplit(ExpenseSplit):
    def validate(self, expense: Expense):
        return True

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, id: int, description: str, amount: float, paid_by: User, split_type: SplitType, splits: List[Split]) -> Expense:
        split_factory = SplitFactory()
        split = split_factory.get_split(split_type)
        if not split.validate(Expense(id, description, amount, paid_by, split_type, splits)):
            print("Invalid expense")
            return None
        expense = Expense(id, description, amount, paid_by, split_type, splits)
        self.expenses.append(expense)
        return expense

    def get_balance_for_user(self, user: User):
        pass

    def show(self):
        pass

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, id: int, name: str, email: str, phone: int):
        user = User(id, name, email, phone, {})
        self.users.append(user)

    def get_user(self, id: int):
        for user in self.users:
            if user.id == id:
                return user

    def show(self):
        for user in self.users:
            print(user.id, user.name, user.email, user.phone)

class Group:
    def __init__(self, id: int, name: str, users: List[User], expenses: List[Expense]):
        self.id = id
        self.name = name
        self.users = users  
        self.expenses = expenses
        self.expense_manager = ExpenseManager()

    def addMember(self, user: User):
        self.users.append(user)
    
    def getGroupId(self):
        return self.id

    def getGroupName(self):
        return self.name

    def setGroupName(self, name):
        self.name = name
    
    def createExpense(self, id: int, description: str, amount: float, paid_by: User, split_type: SplitType, splits: List[Split]) -> Expense:
        expense = self.expense_manager.add_expense(id, description, amount, paid_by, split_type, splits)
        self.expenses.append(expense)
        return expense

    def show(self):
        print("Group Name: ", self.name)
        print("Group Members: ")
        for user in self.users:
            print(user.id, user.name, user.email, user.phone)
        print("Group Expenses: ")
        for expense in self.expenses:
            print(expense.id, expense.description, expense.amount, expense.paid_by.name, expense.split_type)
            for split in expense.splits:
                print(split.user_id.name, split.amount)

class GroupManager:
    def __init__(self):
        self.groups = []

    def createGroup(self, id: int, name: str, users: List[User]):
        group = Group(id, name, users, [])
        self.groups.append(group)
    
    def getGroup(self, id: int):
        for group in self.groups:
            if group.id == id:
                return group

    def show(self):
        for group in self.groups:
            group.show()

class Splitwise:
    def __init__(self):
        self.user_manager = UserManager()
        self.group_manager = GroupManager()

    def show(self):
        self.user_manager.show()
        self.group_manager.show()
    
    def createUser(self, id: int, name: str, email: str, phone: int):
        self.user_manager.add_user(id, name, email, phone)
    
    def createGroup(self, id: int, name: str, users: List[User]):
        self.group_manager.createGroup(id, name, users)

