import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num):
    if num > len(self.contents):
      return self.contents
    else:
      drew_list = []
      for i in range(num):
        ball = self.contents.pop(random.randrange(len(self.contents)))
        drew_list.append(ball)
    return drew_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    flag = True
    hat_copy = copy.deepcopy(hat)
    hat_res = hat_copy.draw(num_balls_drawn)
    for key, value in expected_balls.items():
      if hat_res.count(key) < value:
        flag = False
        break

    if flag == True:
      count += 1

  return count / num_experiments
