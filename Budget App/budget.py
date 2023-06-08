class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount * -1, "description": description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, another_cat):
    if self.withdraw(amount, "Transfer to " + another_cat.category):
      another_cat.deposit(amount, "Transfer from " + self.category)
      return True
    return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True

  def __str__(self):
    s = self.category.center(30, "*") + "\n"
    for item in self.ledger:
      s += f"{item['description'][:23]:<23}{item['amount']:>7.2f}" + '\n'
    s += "Total: " + str(self.get_balance())
    return s


def create_spend_chart(categories):
  spent = []
  for cat in categories:
    tmp = 0
    for item in cat.ledger:
      if item['amount'] < 0:
        tmp -= item['amount']
    spent.append(tmp)

  total = 0
  for cat in spent:
    total += cat

  percentage = []
  for cat in spent:
    tmp = cat / total * 100
    percentage.append(tmp)

  output = "Percentage spent by category\n"
  for i in range(100, -1, -10):
    # if i == 0:
    #   output += " "
    # if i != 100:
    #   output+= " "
    # output += str(i) + "|"
    output += str(i).rjust(3) + "| "

    flag = 0
    count = 0
    for num in percentage:
      count+=1
      if num >= i:
        output += "o  " 
        # if flag != 0:
        #   if count ==1:
        #     output += " " 
        #     output += " " * (flag -1)
        #   else:
        #     output += "  " * flag
        #     output += "  o"
        #     flag = 0
        # else:
        #   if count == 1:
        #     output += " o"
        #   else:
        #     output += "  o"
      else:
        output += "   " 
        #flag += 1

    output += '\n'

  #print(len(percentage))
  output += "    " + "-" + "-" * len(percentage)*3 

  cat_len = []
  maxlen = 0
  for cat in categories:
    cat_len.append(len(cat.category))
    maxlen = max(maxlen, len(cat.category))

  for i in range(0, maxlen):
    output += '\n'
    output += "     "
    for j in range(len(categories)):
      if i < cat_len[j]:
        output +=  categories[j].category[i] + "  "
      else:
        output += "   "
    #if i < maxlen -1:

  return output
