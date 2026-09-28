  # using dictionary
Expense={}
while True:
    print("1.Add Expense")
    print("2.View Expense") 
    print("3.Calculate Expense") 
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice ==1:
        new=input("Enter your new expense:")
        value=float(input("Enter amount of expense:"))
        Expense[new]=value
        print("NEW expense added successfully....")

    elif choice==2:
        if len(Expense)==0:
            print("NO EXPENSES...")
        else:
            print("Expenses are:",Expense)

    elif choice==3:
        if len(Expense)>0:
            total=sum(Expense.values())
            print("TOtal expense is:",total)

    elif choice==4:
        print("Thank you for using expense tracker")
        break
    
    else:
        print("INVALID CHOICE")



