from util import Util
from portfolio import Portfolio

class Customer:

  def __init__(self, name):
    self.__name = name
    self.__portfolios = []

  def addPortfolio(self,
                   name,
                   amount=0,
                   depositPlanOneTimeAmount=0,
                   depositPlanRecurringAmount=0):
    portfolio = Portfolio(name, amount, depositPlanOneTimeAmount,
                          depositPlanRecurringAmount)
    self.__portfolios.append(portfolio)
    return

  def handleDeposits(self, deposits):
    Util.allocation(self.__portfolios, deposits)
    return self.__portfolios

  def setDepositPlanOneTime(self, depositPlanOneTime):
    if len(depositPlanOneTime) == len(self.__portfolios):
      for i in range(len(self.__portfolios)):
        self.__portfolios[i].setDepositPlanOneTimeAmount(depositPlanOneTime[i])
    else:
      print(
        "ERROR: the length of params is not equal to the number of portfolios"
      )

  def setDepositPlanRecurring(self, depositPlanRecurring):
    if len(depositPlanRecurring) == len(self.__portfolios):
        for i in range(len(self.__portfolios)):
          self.__portfolios[i].setDepositPlanRecurringAmount(depositPlanRecurring[i])
    else:
      print(
        "ERROR: the length of params is not equal to the number of portfolios"
      )

  def printCustomerDetails(self):
    print("Customer name: {}".format(self.__name))
    print("+--------------------+--------------------+")
    print("| {:<18} | {:<18} |".format("Portfolio", "Amount"))
    print("+--------------------+--------------------+")
    for portfolio in self.__portfolios:
        print("| {:<18} | ${:<17} |".format(portfolio.getName(), portfolio.getAmount()))
    print("+--------------------+--------------------+\n")
