def add_time(start, duration,weekday= None):
  weekdays = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]
  duration = duration.split(':')
  hr_add = int(duration[0])
  min_add = int(duration[1])
  start = start.split()
  startlist = start[0].split(':')
  start_hr = int(startlist[0])
  start_min = int(startlist[1])
  start_ap = start[1]
  #print("gg:",start_hr)

  #convert to 24hr
  if start_ap == "PM":
    start_hr +=  12
  else:
    start_ap = "PM"

  #add the duration
  after_hr = start_hr + hr_add
  
  after_min = start_min + min_add
  if after_min > 60:
    after_hr += after_min // 60
    after_min = after_min % 60
  if after_min < 10:
    after_min = "0" + str(after_min)

  day_add = 0
  if after_hr > 24:
    day_add = after_hr // 24
    after_hr_new = after_hr % 24
    #print("gg:",after_hr_new)
  else:
    after_hr_new = after_hr
    
  if after_hr_new > 12:
    start_ap = "PM"
    after_hr_new -= 12
  elif after_hr_new == 12:
    start_ap = "PM"
  elif after_hr_new == 0:
    after_hr_new = 12
    start_ap = "AM"
  else:
    start_ap = "AM"

  new_time = str(after_hr_new) + ":" + str(after_min) + " " + start_ap

  if weekday is None:
    if day_add == 1:
      new_time += " (next day)"
    elif day_add > 1:
      new_time += " (" + str(day_add) + " days later)"
  else:
    if day_add == 0:
      new_time += ", " + weekday.lower().capitalize()
    else:
      day_index = weekdays.index(weekday.lower().capitalize()) + day_add
      if day_index >= 7:
        day_index %= 7

      if day_add == 1:
        new_time += ", " + weekdays[day_index] + " (next day)"
      else:
        new_time += ", " + weekdays[day_index] + " (" + str(day_add) + " days later)"
  
  
  return new_time
