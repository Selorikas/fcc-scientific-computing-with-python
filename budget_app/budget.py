class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category

    def __str__(self):
        title = self.category.center(30, "*") + "\n"
        items = ""
        for item in self.ledger:
            description = f"{item['description'][:23]:23}"
            amount = f"{item['amount']:7.2f}"
            items += description + amount + "\n"
        total = "Total: " + str(self.get_balance())
        return title + items + total
        
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.category)
            category.deposit(amount, "Transfer from " + self.category)
            return True
        return False

    def check_funds(self, amount):
        return False if amount > self.get_balance() else True

def create_spend_chart(categories):
    spent_per_category = []
    for category in categories:
        spent_in_category = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent_in_category += abs(item['amount'])
        spent_per_category.append(spent_in_category)
    spent_total = sum(spent_per_category)
    spent_per_category_in_percent = []
    for category in spent_per_category:
        spent_per_category_in_percent.append(category / spent_total * 100)
    return __print_bar_chart(spent_per_category_in_percent) + __print_category_names(categories)

def __print_bar_chart(spent_per_category_in_percent):
    title = "Percentage spent by category"
    chart = ""
    for percentile in range(100, -1, -10):
        chart += "\n" + str(percentile).rjust(3) + "|"
        for spent_in_category in spent_per_category_in_percent:
            if spent_in_category > percentile:
                chart += " o "
            else:
                chart += "   "
        chart += " "
    separator = "\n    ----------"
    return title + chart + separator

def __print_category_names(categories):
    output = ""
    category_name_lengths = []
    for category in categories:
        category_name_lengths.append(len(category.category))
    max_length = max(category_name_lengths)
    
    for letter_index in range(max_length):
        output += "\n    "
        for category in range(len(categories)):
            if letter_index < category_name_lengths[category]:
                output += " " + categories[category].category[letter_index] + " "
            else:
                output += "   "
        output += " "
    return output