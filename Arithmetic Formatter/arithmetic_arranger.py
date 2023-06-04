def arithmetic_arranger(problems, solve = False):
  line1, line2, line3, line4 = "", "","",""
  if len(problems) > 5:
    return "Error: Too many problems."

  for cal in problems:
    list = cal.split()
    if list[1] != '+' and list[1] != '-':
      return "Error: Operator must be \'+\' or \'-\'."
    elif not list[0].isdigit() or not list[2].isdigit():
      return "Error: Numbers must only contain digits."
    elif len(list[0]) > 4 or len(list[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    else:
      len_max = max(len(list[0]), len(list[2]))
      if line1 != "":
        line1 += "    "
        line2 += "    "
        line3 += "    "
        line4 += "    "

      line1 += " " * (len_max + 2 - len(list[0]))
      line1 += list[0]

      line2 += list[1]
      line2 += " "
      line2 += " " * (len_max - len(list[2]))
      line2 += list[2]

      line3 += "-" * (len_max + 2)

      if solve:
        if list[1] == "+":
          res = str(int(list[0]) + int(list[2]))
          line4 += " " * (len_max + 2 - len(res))
          line4 += res
        else:
          res = str(int(list[0])  - int(list[2]))
          line4 += " " * (len_max + 2 - len(res))
          line4 += res
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
      else:
        arranged_problems = line1 + "\n" + line2 + "\n" + line3 
        
  return arranged_problems
