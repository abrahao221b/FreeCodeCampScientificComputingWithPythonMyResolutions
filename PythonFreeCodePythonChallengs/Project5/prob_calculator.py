import copy
import random

# Consider using the modules imported above.


# Class Hat
class Hat:

  def __init__(self, **balls):
    if len(balls) != 0:
      self.balls = balls
      self.contents_list = [(key + ",") * balls[key] for key in balls]
      temp_contents_list = []
      contents = []
      for collors in self.contents_list:
        temp_contents_list = collors.split(",")
        for rep_collors in temp_contents_list:
          if rep_collors != "":
            contents.append(rep_collors)
      self.contents = contents

  # Function that returns the correct distribution of balls as an array
  def correct_contents(self):
    temp_contents_list = []
    contents = []
    for collors in self.contents_list:
      temp_contents_list = collors.split(",")
      for rep_collors in temp_contents_list:
        if rep_collors != "":
          contents.append(rep_collors)
    return contents

  # Function that returns the string array of a random pick number of balls
  def draw(self, number_of_balls):
    if number_of_balls <= len(self.contents):
      draws_balls = []
      last_index_contents = len(self.contents) - 1
      for _ in range(number_of_balls):
        draws_balls.append(
            self.contents.pop(random.randint(0, last_index_contents)))
        last_index_contents -= 1
      return draws_balls
    else:
      return self.contents

  # Gets

  def get_balls(self):
    return self.balls

  def get_contents(self):
    return self.contents

  # Resetting the hat
  def reset_hat(self):
    self.contents = self.correct_contents()


# Probability experiment
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  estimated_probability = 0.0
  if num_balls_drawn < len(hat.get_contents()):
    favorable_cases = 0
    for _ in range(num_experiments):
      # Case variables
      valid_case = [False for _ in range(len(expected_balls))]
      draw_balls = hat.draw(num_balls_drawn)
      hat.reset_hat()
      case_dict = {}
      for ball in draw_balls:
        if ball not in case_dict:
          case_dict[ball] = 1
        else:
          case_dict[ball] += 1

      # Comparing cases
      a = 0
      for key in expected_balls:
        if key in case_dict:
          if expected_balls[key] <= case_dict[key]:
            valid_case[a] = True
          else:
            valid_case[a] = False
        a += 1

      number_of_trues = 0
      for case in valid_case:
        if case:
          number_of_trues += 1

      if number_of_trues == len(valid_case):
        favorable_cases += 1

    estimated_probability = favorable_cases / num_experiments
  else:
    estimated_probability = 1.0

  return estimated_probability
