class Util:

  @staticmethod
  def __followOneTime(portfolios, scheme):
    for portfolio in portfolios:
      scheme[portfolio.getName()] += portfolio.getDepositPlanOneTimeAmount()
    return

  @staticmethod
  def __followRecurring(portfolios, scheme):
    for portfolio in portfolios:
      scheme[portfolio.getName()] += portfolio.getDepositPlanRecurringAmount()
    return

  @staticmethod
  def __followRecurringRatio(portfolios, totalRecurring, remainingFund, scheme):
    for portfolio in portfolios:
      scheme[portfolio.getName()] += (portfolio.getDepositPlanRecurringAmount() / totalRecurring) * remainingFund
    return

  @staticmethod
  def distribution(portfolios, scheme):
    for portfolio in portfolios:
      portfolio.addFund(scheme[portfolio.getName()])
    return

  @staticmethod
  def allocation(portfolios, deposits):
    totalAmountOneTime = sum([p.getDepositPlanOneTimeAmount() for p in portfolios])
    totalAmountRecurring = sum([p.getDepositPlanRecurringAmount() for p in portfolios])
    scheme = {p.getName(): 0 for p in portfolios}
    for deposit in deposits:
      if deposit == totalAmountOneTime:
        Util.__followOneTime(portfolios, scheme)
      elif deposit > totalAmountOneTime:
        remainingFund = deposit - totalAmountOneTime
        Util.__followOneTime(portfolios, scheme)
        if remainingFund == totalAmountRecurring:
          Util.__followRecurring(portfolios, scheme)
        else:
          Util.__followRecurringRatio(portfolios, totalAmountRecurring, remainingFund, scheme)
      elif deposit == totalAmountRecurring:
        Util.__followRecurring(portfolios, scheme)
      else:
        Util.__followRecurringRatio(portfolios, totalAmountRecurring, deposit, scheme)
    scheme = {k: round(v, 2) for k, v in scheme.items()}
    #Only amount will be distributed into portfolios after the calculation of the allocation is done
    Util.distribution(portfolios, scheme)
    return
