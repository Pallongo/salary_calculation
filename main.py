#How to obtain the amount paid to an employee, where the amount of money depends on the day and in the hour interval.


# --------------------------- DATA -----------------------------#

#Dictionary or hash that has the salary paid at the corresponding hours on the week
salary_by_hours_week = {"00:00-09:00": 25,
                        "09:01-18:00": 15,
                        "18:01-00:00": 20}

#Dictionary or hash that has the salary paid at the corresponding hours on the weekend
salary_by_hours_weekend = { "00:00-09:00": 30,
                            "09:01-18:00": 20,
                            "18:01-00:00": 25}



#---------------------------- FUNCTIONS -------------------------#



#Returns TRUE if the day is from monday to friday and FALSE if it is saturday or sunday
#string_code parameter recieves the string of the day
def betweenMondayToFriday(string_code):
    week = ["MO", "TU", "WE", "TH", "FR"]
    if (string_code in week):
        return True
    else:
        return False

#Calculates the salary of one hour interval depending on the day and hour
def calculateHourSalary(monday_to_friday, hour):
    if (monday_to_friday):
        return salary_by_hours_week[getHourRange(hour)]
    else:
        return salary_by_hours_weekend[getHourRange(hour)]

#Returns the string of the time interval that contains the worked hour
def getHourRange(start_hour):
    dictionary_strings = {
        0: "00:00-09:00",
        1: "00:00-09:00",
        2: "00:00-09:00",
        3: "00:00-09:00",
        4: "00:00-09:00",
        5: "00:00-09:00",
        6: "00:00-09:00",
        7: "00:00-09:00",
        8: "00:00-09:00",
        9: "09:01-18:00",
        10: "09:01-18:00",
        11: "09:01-18:00",
        12: "09:01-18:00",
        13: "09:01-18:00",
        14: "09:01-18:00",
        15: "09:01-18:00",
        16: "09:01-18:00",
        17: "09:01-18:00",
        18: "18:01-00:00",
        19: "18:01-00:00",
        20: "18:01-00:00",
        21: "18:01-00:00",
        22: "18:01-00:00",
        23: "18:01-00:00",
    }

    return dictionary_strings[start_hour]

#Calculates de Salary of one day
def calculateDailySalary(day, start_hour, end_hour):
    #Initialize salary variable
    daily_salary = 0

    #Iterate hour by hour
    for hour in range(start_hour, end_hour):
        #Add the hour salary obtained using the "salary_by_hours" data.
        hour_salary = calculateHourSalary(betweenMondayToFriday(day), hour)
        daily_salary += hour_salary

    return daily_salary


#Calculates the weekly salary from the data string
#The data string is the part of the string that does not contain the name:
#For example: MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
def calculateWeeklySalary(string_data):
    daily_data = string_data.split(",")
    week_salary = 0
    for day in daily_data:
        day_code = day[:2]
        day_data = day[2:]

        #Splits the data into two different hours
        hour_interval_data = day_data.split("-")

        #Gets the hour ignoring the minutes
        start_hour = hour_interval_data[0][:2]
        end_hour = hour_interval_data[1][:2]

        #Adds the daily salary to the weekly salary
        daily_salary = calculateDailySalary(day_code, int(start_hour),int(end_hour))
        week_salary += daily_salary

    return week_salary

#Prints the weekly salary
#text_string parameter corresponds to any line of data used for calculating the salary
def outputSalary(text_string):
    splitted_data = text_string.split('=')
    employee_name = splitted_data[0]

    salary = calculateWeeklySalary(splitted_data[1])

    print("The employee " + employee_name + " has a weekly salary of " + str(salary) + " USD.")


def fileToSalary(file_name):
    # Open text file in read-only mode
    data_file = open(file_name, "r")

    for line in data_file:
        # Output the resultant salary
        outputSalary(line)

    # Close the file
    data_file.close()

#-------------------------------- MAIN PROGRAM -------------------------#

fileToSalary("data.txt")