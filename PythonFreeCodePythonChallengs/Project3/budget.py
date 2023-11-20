# Category class
class Category:
  # Constracture 
  def __init__(self, category_name):
    self.category_name = category_name
    self.historic = []
    self.ledger = []

  # Desposit function
  def deposit(self, amount=0.0, description=""):
    # If already has a deposit in the Category
    if len(self.ledger) != 0:
      self.ledger[0]["amount"] += amount
      self.ledger[0]["description"] = description
    # If hasn't any deposit in the Category
    else:
      self.ledger.append({"amount": amount, "description": description})
    # Updating the historic category register
    if "deposit" not in description:
      self.historic.append({f"{description} deposit": float(amount)})
    else:
      self.historic.append({description: float(amount)})

  # Withdraw function
  def withdraw(self, amount=0.0, invest_name=""):
    if self.check_funds(amount):
      value = float(amount)
      self.ledger[0]["amount"] -= value
      self.ledger.append({"amount": -1 * amount, "description": invest_name})
      self.historic.append({invest_name: -1 * value})
      return True
    else:
      return False

  # Get balance function
  def get_balance(self):
    if len(self.ledger) == 0:
      self.deposit(0, "")
    return self.ledger[0]["amount"]

  # To string function
  def __str__(self):
    ledger_print = ""
    # Restricting the number of characters 
    number_characters = 31 - len(self.category_name)
    # Where the category name will be print
    number_middle = number_characters // 2
    # Printing the character "*" and the category name
    for element in range(int(number_characters)):
      if element != number_middle:
        ledger_print += "*"
      else:
        for character in self.category_name:
          ledger_print += character
        element += int(len(self.category_name))
    ledger_print += "\n"

    # Printing the budget historic 
    for element in self.historic:
      for term in element:
        if term != "description":
          if len(str(term) + str(element[term])) < 30:
            last_part = 30 - len(str(element[term])) - len(term)
            ledger_print += term
            temp = element[term]
            if element[term] % 10 == 0:
              temp = f"{float(element[term]):.2f}".format()
              for _ in range(last_part - 1):
                ledger_print += " "
            else:
              for _ in range(last_part):
                ledger_print += " "
            ledger_print += str(temp)
          else:
            if element[term] < 0 and element[term] % 10 == 0:
              last_part = 30 - len(str({element[term]}))
            elif element[term] < 0 and element[term] % 10 != 0:
              last_part = 31 - len(str({element[term]}))
            else:
              last_part = 30 - len(str({element[term]}))
            ledger_print += term[:last_part]
            ledger_print += " "
            temp = element[term]
            if isinstance(element[term], float):
              temp = f"{float(element[term]):.2f}".format()
            ledger_print += str(temp)
        else:
          break
      ledger_print += "\n"

    ledger_print += "Total: "
    ledger_print += str(self.ledger[0]["amount"])
    return ledger_print

  # Transference function
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount=amount,
                    invest_name=f"Transfer to {category.category_name}")
      category.deposit(amount=amount,
                       description=f"Transfer from {self.category_name}")
      return True
    else:
      return False

  # Check funds functions
  def check_funds(self, amount=0.0):
    return any(self.ledger[i]["amount"] >= amount
               for i in range(len(self.ledger)))


# Spend chart function
def create_spend_chart(categories):
  output = "Percentage spent by category\n"
  total_spent = 0
  porcentage = {}

  # Getting the category expenses
  for i in range(len(categories)):
    for element in categories[i].historic:
      for term in element:
        if "deposit" not in term:
          value = abs(element[term])
          total_spent += value
          if term not in porcentage:
            porcentage[categories[i].category_name] = value
          else:
            porcentage[term] += value
            
  # Getting the category expenses porcentage
  for term in porcentage:
    value = porcentage[term]
    porcentage[term] = round((abs(value) * (1 / total_spent)) * 100.0)

  # Verifying how many "-" characters  
  dash_figures = len(porcentage)
  dash_figures *= dash_figures
  dash_figures += 1

  # Printing the porcentage label 
  for element in range(10, -1, -1):
    treat_element = element * 10
    if element != 10 and element != 0:
      output += f" {treat_element}|"
    elif element == 0:
      output += f"  {treat_element}|"
    else:
      output += f"{treat_element}|"
    # Marking the "o" on the related percentage
    output = marck_out(porcentage, treat_element, output, dash_figures)

  output += "    "
  
  for _ in range(dash_figures):
    output += "-"
  
  output += "\n"
  # Printing the categories names 
  output += categories_names_record(categories=categories)

  return output


# Function that prints the "o" characters
def marck_out(porcentage, element, output, dash_figures):
  i = 0
  space = 0
  phrase = ""

  # Printing the "o" character 
  for term in porcentage:
    if porcentage[term] >= element:
      if "o" not in phrase:
        if i != 0:
          space = 1 + 3 * i
          for _ in range(space):
            phrase += " "
          phrase += "o"
        else:
          phrase += " o"
      else:
        phrase += "  o"
    i += 1
  if "o" in phrase:
    size_jump = dash_figures - len(phrase)
    for _ in range(size_jump):
      phrase += " "
  else:
    for _ in range(dash_figures):
      phrase += " "
  phrase += "\n"
  output += phrase

  return output


# Function that returns the average value of the percentage dictionary
def average_value(porcentage):
  total = 0
  for element in porcentage:
    total += porcentage[element]
  return total / len(porcentage)


# Function that prints out the categories names
def categories_names_record(categories):
  names = ""
  names_list = []
  bigest_size = -99999

  names += "    "

  # Getting the biggest name in the categories objects array
  for element in categories:
    names_list.append(element.category_name)
    if bigest_size < len(element.category_name):
      bigest_size = len(element.category_name)

  names_size = len(names_list)

  # Printing the names 
  for i in range(bigest_size):
    for a in range(names_size):
      if i < len(names_list[a]):
        names += " "
        names += f"{names_list[a][i]}"
        names += " "
        if i < bigest_size - 1 and a == names_size - 1:
          names += " \n"
          names += "    "
      else:
        names += "   "
        if a == names_size - 1:
          names += " \n"
          names += "    "
  names += " "
  return names
