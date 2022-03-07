### Calculating the weekly salary

We must calculate the salary of any number of employees given a text file with its data. 

In order to solve this problem, I implemented a function oriented architecture.
This is because I want to simplify the code as much as possible, for an easy re-use of the functions.

The resultant function **_fileToSalary(file_name)_**, just needs the name of the file.
It will work with any file that satisfies the conditions given in the problem statement.

The main workflow of this solution is the following:
1) Reads the file and separate its lines.
2) Split the data of each line and process their data on functions.
3) Output the results

The algorithm to calculate the salary works in the following way:
1) Each hour is considerated individually. For example, from 03:00 to 07:00, we have the hour 3, the hour 4, the hour 5 and the hour 6. The ending hour is not considered.
2) To calculate the hour salary we consider the start time and also if it is from monday to friday or weekend. There is a function **_betweenMondayToFriday(string_code)_** that returns this data.
3) The function to calculate the hour salary uses the previous inputs and query the hourly value from two dictionaries: the first one contains the hourly salary from the week, and the second one from weekend.
4) To calculate the daily salary, we iterate every hour and calculate its corresponding value depeding on the time interval.
5) Finally, we iterate day by day to calculate the weekly salary.

The original data is saved on dictionaries for ordering purposes.

The program uses no external libraries so it can be easilly executed on command line:

`python main.py`