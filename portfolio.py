class Portfolio:

  def __init__(self, name, amount = 0, depositPlanOneTimeAmount = 0, depositPlanRecurringAmount = 0):
    self.__name = name
    self.__amount = amount
    self.__depositPlanOneTimeAmount = depositPlanOneTimeAmount
    self.__depositPlanRecurringAmount = depositPlanRecurringAmount

  def getName(self):
    return self.__name

  def getAmount(self) -> str:
    return self.__amount

  def addFund(self, fund: float):
    self.__amount += fund
    return

  def getDepositPlanOneTimeAmount(self) -> float:
    return self.__depositPlanOneTimeAmount

  def setDepositPlanOneTimeAmount(self, amount: float):
    self.__depositPlanOneTimeAmount = amount
    return
    
  def getDepositPlanRecurringAmount(self) -> float:
    return self.__depositPlanRecurringAmount

  def setDepositPlanRecurringAmount(self, amount: float):
    self.__depositPlanRecurringAmount = amount
    return