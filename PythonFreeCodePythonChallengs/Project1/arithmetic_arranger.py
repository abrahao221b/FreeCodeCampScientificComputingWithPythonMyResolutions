def arithmetic_arranger(problems, show_result=False):
  # Organizing the problem variables
  print(problems)
  arranged_problems_array = problems
  print(problems)
  arranged_problems = ""
  # Verification dictionary
  verification = {
      "good_size_number": True,
      "good_format_number": True,
      "good_operator": True
  }
  # All maths terms array
  all_terms = []

  # Verifying the quantity of maths terms
  if size_verifier(arranged_problems_array):
    # Verifying if all features have been satisfied
    if verification["good_size_number"] and verification[
        "good_format_number"] and verification["good_operator"]:
      # All terms array index
      all_terms_index = 0
      # Looping through problems array
      for term in problems:
        # Verifying if the math term has the operator '+' or '-'
        if operator_verification(term):
          # Organizing the maths terms
          all_terms.append(term.split(" "))
          # First and second number size verification
          if number_size_verification(all_terms[all_terms_index][0],
                                      all_terms[all_terms_index][2]):
            # First and second number format verification
            if number_format_verification(all_terms[all_terms_index][0],
                                          all_terms[all_terms_index][2]):
              pass
            else:
              verification["good_format_number"] = False
              return error_call(verification=verification)
          else:
            verification["good_size_number"] = False
            return error_call(verification=verification)
        else:
          verification["good_operator"] = False
          return error_call(verification)
        all_terms_index += 1
    else:
      return error_call(verification)
  else:
    return "Error: Too many problems."

  arranged_problems = term_format(all_terms, show_result)

  return arranged_problems


# Function that verifies quantity of math terms
def size_verifier(arranged_problems_array):
  if len(arranged_problems_array) < 6:
    return True
  return False


# Function that verifies if the math term has the operator '+' or '-'
def operator_verification(term):
  if '+' in term or '-' in term:
    return True
  return False


# Error function
def error_call(verification):
  if not verification["good_operator"]:
    return "Error: Operator must be '+' or '-'."
  elif not verification["good_format_number"]:
    return "Error: Numbers must only contain digits."
  elif not verification["good_size_number"]:
    return "Error: Numbers cannot be more than four digits."


# Function that verifies the number size
def number_size_verification(first_number, second_number):
  if len(first_number) - 1 < 4 and len(second_number) - 1 < 4:
    return True
  return False


# Function that verifies the number format
def number_format_verification(first_number, second_number):
  if first_number.isdigit() and second_number.isdigit():
    return True
  return False


# Function that formats the output for the required
def term_format(term, show_result):
  format_term = ""
  first_numbers = []
  operator = []
  second_numbers = []
  lines = []
  result = []
  # Getting the respective math term array's elements in order
  for operation in range(len(term)):
    first_numbers.append(term[operation][0])
    operator.append(term[operation][1])
    second_numbers.append(term[operation][2])
  ''' Calculating the results, and verifying, how many "-" 
   are needed to the line that separates the sum and the result.'''
  for index in range(len(first_numbers)):
    # Sum
    if operator[index] == '+':
      result.append(int(first_numbers[index]) + int(second_numbers[index]))
    # Subtraction
    elif operator[index] == '-':
      result.append(int(first_numbers[index]) - int(second_numbers[index]))
    # Verifying how many '-' are required
    if len(first_numbers[index]) > len(second_numbers[index]):
      if len(first_numbers[index]) == 4:
        lines.append(6)
      elif len(first_numbers[index]) == 3:
        lines.append(5)
      elif len(first_numbers[index]) == 2:
        lines.append(4)
      elif len(first_numbers[index]) == 1:
        lines.append(3)
    else:
      if len(second_numbers[index]) == 4:
        lines.append(6)
      elif len(second_numbers[index]) == 3:
        lines.append(5)
      elif len(second_numbers[index]) == 2:
        lines.append(4)
      elif len(second_numbers[index]) == 1:
        lines.append(3)

  # Getting the loop's max upper bound limit
  first_line = second_line = result_line = len(first_numbers)
  third_line = len(lines)

  # Placing, in order, the first numbers of each math term
  for element in range(first_line):
    space = lines[element] - len(first_numbers[element])
    for times in range(space):
      format_term += " "
    format_term += first_numbers[element]
    if len(term) == 1:
      if element == 0 or element == 1:
        format_term += "    "
    elif len(term) == 2:
      if element == 0 or element == 2:
        format_term += "    "
    elif len(term) == 3:
      if element == 0 or element != 3:
        format_term += "    "
    elif len(term) == 4:
      if element != 3:
        format_term += "    "
    else:
      if element != 4:
        format_term += "    "

  # Jumping a line
  format_term += "\n"

  # Placing, in order, the second numbers of each math term
  for element in range(second_line):
    format_term += operator[element]
    space = lines[element] - len(second_numbers[element]) - 1
    for times in range(space):
      format_term += " "
    format_term += second_numbers[element]
    if len(term) == 1:
      if element == 0 or element == 1:
        format_term += "    "
    elif len(term) == 2:
      if element == 0 or element == 2:
        format_term += "    "
    elif len(term) == 3:
      if element == 0 or element != 3:
        format_term += "    "
    elif len(term) == 4:
      if element != 3:
        format_term += "    "
    else:
      if element != 4:
        format_term += "    "

  # Jumping a line again
  format_term += "\n"

  # Placing the line that separates the sum and the result
  for element in range(third_line):
    for index in range(lines[element]):
      format_term += '-'
    if len(term) == 1:
      if element == 0 or element == 1:
        format_term += "    "
    elif len(term) == 2:
      if element == 0 or element == 2:
        format_term += "    "
    elif len(term) == 3:
      if element == 0 or element != 3:
        format_term += "    "
    elif len(term) == 4:
      if element != 3:
        format_term += "    "
    else:
      if element != 4:
        format_term += "    "

  # Verifying if has to show the result
  if show_result:
    format_term += "\n"
    # Placing the result to it respective local
    for element in range(result_line):
      space = lines[element] - len(str(result[element]))
      for times in range(space):
        format_term += " "
      format_term += str(result[element])
      if len(term) == 1:
        if element == 0:
          format_term += "    "
      elif len(term) == 2:
        if element == 0:
          format_term += "    "
      elif len(term) == 3:
        if element == 0 or element != 3:
          format_term += "    "
      elif len(term) == 4:
        if element != 3:
          format_term += "    "
      else:
        if element != 4:
          format_term += "    "

  # Returning the format term
  return format_term
