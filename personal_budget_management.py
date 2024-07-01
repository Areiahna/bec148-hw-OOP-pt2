# Task 1: Define Budget Category Class - Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.

class BudgetCategory:
    def __init__(self,name,budget = 0):
        self.__name = name
        self.__budget = budget
        self.__current_balance = budget

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).

    # Getters
    def get_budget(self):
        return self.__budget
    
    def get_category(self):
        return self.__name

    def get_current_balance(self):
        return self.__current_balance

    # Setters
    def set_budget(self,new_budget):
        if new_budget  > 0 :
            self.__budget = new_budget
            self.__current_balance = new_budget
        else: 
            print("Budget must be greater than 0")

    def set_category(self,new_category):
        self.__name = new_category


# Task 3: Add Budget Functionality - Implement a method to add expenses to a category and adjust the budget accordingly. - Validate the expense amount before making deductions from the budget.

    def add_expenses(self,amount):
        if 0 < amount and amount <= self.__current_balance :
            self.__current_balance = (self.get_current_balance() - amount)
        elif amount > self.__current_balance :
            print("Sorry boo! That's not in your budget")
        else:
            print("Invalid Entry")

# Task 4: Display Budget Details - Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

    def display_category_summary(self):
        print(f'''
        Category: {self.__name}
        Allocated Budget : {self.__budget}
        Current Budget : {self.__current_balance}
        ''')

if __name__ == "__main__":
    Arei = BudgetCategory("Groceries",400)
    Arei.get_budget() 
    Arei.get_category() 
    Arei.display_category_summary()# Expected Catergory: "Groceries", Initial Budget : 400, Current Budget: 400
    print("-" * 25)
    Arei.set_category("Shopping")
    Arei.set_budget(500)
    Arei.add_expenses(120)
    Arei.add_expenses(565) # Expected "NOT IN BUDGET" msg
    Arei.add_expenses(225)
    Arei.display_category_summary() # Expected --- Category: Shopping, Initial Budget: 500, Current: 155
    
