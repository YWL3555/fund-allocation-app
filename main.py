from customer import Customer

deposits = [11500, 200]

A = Customer("Jack")
A.addPortfolio('High risk')
A.addPortfolio('Retirement')
A.setDepositPlanOneTime([10000,500])
A.setDepositPlanRecurring([50,100])
A.handleDeposits(deposits)
A.printCustomerDetails()

B = Customer("Mark")
B.addPortfolio('High risk')
B.addPortfolio('Retirement')
B.setDepositPlanOneTime([10000,500])
B.setDepositPlanRecurring([0,100])
B.handleDeposits(deposits)
B.printCustomerDetails()

C = Customer("Sally")
C.addPortfolio('High risk')
C.addPortfolio('Retirement')
C.addPortfolio('Casual')
C.setDepositPlanOneTime([10000,500,500])
C.setDepositPlanRecurring([50,100,100])
C.handleDeposits(deposits)
C.printCustomerDetails()