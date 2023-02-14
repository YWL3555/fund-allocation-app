# Deposit distribution app

This is an application to allocate and distribute deposits into different portfolios created by customers, according to the deposit plans.

A *screenshot* is included in the project named *"screenshot.png"* as a reference.

## Instruction
*All codes should be written in the main.py*

1. Create a customer
``` 
customer = Customer("Jack")
```
2. Create portfolios
``` 
customer.addPortfolio('High risk')
customer.addPortfolio('Retirement')
```
3. Setup deposit plans (One time/recurring)
``` 
customer.setDepositPlanOneTime([10000,500])
customer.setDepositPlanRecurring([50,100])
```
4. Create an array consists of deposits, and execute the **handleDeposits** function
``` 
deposits = [10000, 500]
customer.handleDeposits(deposits)
```
5. Display the fund details by executing the **printCustomerDetails** function
``` 
customer.printCustomerDetails()
```

## High Level Explanation

In this small application, user can create multiple customers and portfolios.

A flowchart *"flowchart for fund allocation.png"* is attached in this project to explain how will the deposit be allocated and distributed.

## Low level Explanation

A diagram *"class-diagram.png"* is attached in this project to explain the relationships of classes in this project.

There are four .py files in this project, to implement the OOP concept and SOLID principle.

* main.py: Main file of this project.
* customer.py: File for storing the **Customer** class
* portfolio.py: File for storing the **Portfolio** class
* util.py: File for storing the **Util** class, consisting all the **logics** of fund allocation and distribution

In the util class, the process of adding funding into portfolios is **seperated out** from *allocation* function, means that only amount will be distributed into portfolios **after** the calculation of the allocation is done. This is to ensure that there will be **NO** multiple process of adding funds into portfolios.# fund-allocation-app
