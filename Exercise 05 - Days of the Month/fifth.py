## Exercise 5: Days of the Month   
def main():
    #dictionary with month number and days
 Days_in_month = {
    1: 31,  #January
    2: 28,  #february
    3: 31,  #March
    4: 30,  #April
    5: 31,  #May
    6: 30,  #june
    7: 31,  #July
    8: 31,  #August
    9: 30,  #September
    10: 31, #October
    11: 30, #November
    12: 31, #december
}
#Ask the user for a month number
month = int(input("Enter the month number (1-12): "))

#check if the month is valid
if month in days_in_month:
  #special case: february (month 2)
  if month == 2:
    leap = input("is it a leap year? (yes/no): ").strip().lower()
    if leap == "yes":
      days_in_month[2] = 29

      #  Print the number of days
      print(f"Month {month} has {days_in_month[month]} days.")
    else:
        print("Invalid month number! Please enter a number between 1 and 12.")


#Run the program
if __name__ == "__main__":
        main()
