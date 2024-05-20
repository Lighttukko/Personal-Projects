#the variable "principal" will store an integer numeric data type of 40000.
principal = 40000
#the variable "payment_month" will store an integer numeric data type of 300.
payment_month = 300
#the variable "monthly_interest" will store an integer numeric data type of 0.00005.
monthly_interest = 0.00005 #the percentage of 0.005% has been taken, therefore to covert it to decimal you have to add 2 zeros.
#the variable "months" will store an integer numeric data type of 0. It is the intital month.
months = 0
#the variable "money" will store an integer numeric data type of 0. initial 
money= 0
#the variable "interest_list" will be assigned a list with 0 as the first item. The initial interest is 0.
interest_list = [0]
#the variable "total_paid_list" will be assigned a list with 0 as the first item. The initial total paid money is 0.
total_paid_list = [0]
#the variable "principal_list" will be assigned a list with 40000 as the first item. The initial debt is 40000.
principal_list = [40000]
#the variable "monthly_paid_list" will be assigned a list with 0 as the first item.
monthly_paid_list = [0]

#while loop, while the variable "principle" is bigger or equal to 300.
while principal >= 300:
    #the variable "interest_payment" will store the multiplication between variable "principal" and 0.00005
    interest_payment = principal * 0.00005
    #the variable "money" will be added (300 + variable "interest_payment").
    money += (300 + interest_payment)
    #the variable "principal" will be subtracted by 300.
    principal -= 300
    #the variable "months" will be added 1.
    months += 1
    #the list "principal_list" will be appended a new item variable "principal".
    principal_list.append(principal)
    #the list "total_paid_list" will be appended a new item variable "money".
    total_paid_list.append(money)
    #the list "interest_list" will be appended a new item variable "interest_payment".
    interest_list.append(interest_payment)
    #the list "monthly_paid_list" will be appended a new item "-300".
    monthly_paid_list.append(-300)

#if statement, if the variable "principal" is less than 300.
if  principal < 300:
    #this line of code will append subtracted variable "principal" in the list "monthly_paid_list"
    monthly_paid_list.append(f"-{principal}")
    #the  variable "interest_payment" will store the multiplaication between variable "principal" and 0.00005
    interest_payment = principal * 0.00005
    #the variable "money" will be added variables "principal" and "interest_payment".
    money += (principal + interest_payment)
    #the variable "principal" will be subtracted by the variable "principal".
    principal -= principal
    #the variable "months" will be added 1.
    months += 1
    #the list "principal_list" will be appended a new item variable "principal".
    principal_list.append(principal)
    #the list "total_paid_list" will be appended a new item variable "money".
    total_paid_list.append(money)
    #the list "interest_list" will be appended a new item variable "interest_payment".
    interest_list.append(interest_payment)

#print() function, this line of code will print out the title of each colon in defined place.
print('{:^4}'.format("Months"), '{:^20}'.format("Monthly paid"), '{:^20}'.format("Monthly interest charge"),
      '{:^20}'.format("Remaining debt"), '{:^26}'.format("Total paid"))
#for loop, for x in range of variable "months" added by 1.
for x in range(months+1):
    #print() function, this line of code will print out the item of the list of each colon in defined place.
    print('{:^4}'.format(x), '{:^20}'.format(f"{monthly_paid_list[x]}$"), '{:^20}'.format(f"{round(interest_list[x], 3)}$"), '{:^24}'.format(f"{principal_list[x]}$"), '{:^28}'.format(f"{round(total_paid_list[x], 2)}$"))


