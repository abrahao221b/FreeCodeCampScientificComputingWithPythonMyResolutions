# Constant
DAYS = {
    1: "MONDAY",
    2: "TUESDAY",
    3: "WEDNESDAY",
    4: "THURSDAY",
    5: "FRIDAY",
    6: "SATURDAY",
    7: "SUNDAY"
}


# Function add_time
def add_time(start, duration, day="TODAY"):

  # Correcting the start time
  start_correct = start_time_reviser(start_time=start)
  duration_correct = duration_time_reviser(duration_time=duration)

  # Summing the total quantity of minutes of the input
  result = start_correct + duration_correct

  # Converting the minutes to hour
  total_time = convert_minute_to_hour(result)

  # Treating the day input
  day_correct = day.upper()

  # Calculating the day and the quantity of days passed by
  final_day, n_day = day_calculator(minutes=result, day=day_correct)

  # Correcting the print out time period
  time_printout = day_print_out(total_time=total_time)

  # Print out
  new_time = day_output(time_printout=time_printout,
                        final_day=final_day,
                        quantity_of_days=n_day)

  # Return
  return new_time


# Function that corrects the start time
def start_time_reviser(start_time):
  # Correcting the start time
  temp_time_period = start_time.split(" ")

  # Converting hours to minutes
  temp_time = convert_hour_to_minute(temp_time_period[0].split(":"),
                                     temp_time_period[1])

  return temp_time


# Function that corrects the duration time
def duration_time_reviser(duration_time):
  # Converting hours to minutes, the duration time
  temp_duration_time = convert_hour_to_minute(duration_time.split(":"))
  return temp_duration_time


# Function that converts hours to minutes
def convert_hour_to_minute(time, period="none"):
  # Variables
  hour = int(time[0])
  minutes = int(time[1])

  # Setting the time format to 24h for a better calculation
  if period == "PM":
    hour += 12

  # Converting hours to minutes
  hour_to_minute = hour * 60

  return hour_to_minute + minutes


# Function that converts minutes to hours
def convert_minute_to_hour(minutes):
  # Period variable
  period = ""
  # Getting the hours
  hour = int((minutes / 60) % 24)
  # Getting the minutes
  day_minute = minutes % 60

  # Converting the hours to the format 12h
  if hour >= 12:
    if hour != 12:
      hour -= 12
    period = "PM"
  else:
    period = "AM"
    if hour == 0:
      hour += 12

  return hour, day_minute, period


# Function that calculates the current day
def day_calculator(minutes, day="TODAY"):
  # Converting the day to a number
  number_day = day_convert(day=day)
  # Number of days passed by
  number_of_day = 0
  if day != "TODAY":
    if number_day in DAYS:
      number_of_day = int(int(minutes / 60) / 24)
      day_number = ((number_of_day + day_convert(day=day)) % 7)
      # Verifying if it is need to return to number of days
      if day_number == 0:
        return DAYS.get(7), number_of_day
      else:
        return DAYS.get(day_number), number_of_day
  else:
    # If doesn't have the input of the "day"
    number_of_day = int(int(minutes / 60) / 24)
  return "TODAY", number_of_day


# Function that convert the day to a number in the dictionary
def day_convert(day="TODAY"):
  for index in DAYS:
    if day == DAYS.get(index):
      return index
  return 0


# Function that corrects the print out
def day_print_out(total_time):
  hour, minutes, period = total_time
  time = ""

  time += f"{hour}"

  time += ":"

  if minutes < 10:
    time += f"0{minutes}"
  else:
    time += f"{minutes}"

  time += " " + period

  return time


# Function that selects the print out related to the input
def day_output(time_printout, final_day, quantity_of_days):
  if final_day != "TODAY":
    if quantity_of_days > 1:
      return f"{time_printout}, {final_day.capitalize()} ({quantity_of_days} days later)"
    elif quantity_of_days == 1:
      return f"{time_printout}, {final_day.capitalize()} (next day)"
    elif quantity_of_days == 0:
      return f"{time_printout}, {final_day.capitalize()}"
  else:
    if quantity_of_days > 1:
      return f"{time_printout} ({quantity_of_days} days later)"
    elif quantity_of_days == 1:
      return f"{time_printout} (next day)"
    elif quantity_of_days == 0:
      return f"{time_printout}"
