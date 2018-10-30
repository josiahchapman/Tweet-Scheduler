import time as tm
import re


def days_in_month(mnth, yr):
    def leap_year(mnth):
        leapyr_month_days = {
            "01": "31",
            "02": "29",
            "03": "31",
            "04": "30",
            "05": "31",
            "06": "30",
            "07": "31",
            "08": "31",
            "09": "30",
            "10": "31",
            "11": "30",
            "12": "31"
        }
        return leapyr_month_days.get(mnth)

    def not_leap_year(mnth):
        month_days = {
            "01": "31",
            "02": "28",
            "03": "31",
            "04": "30",
            "05": "31",
            "06": "30",
            "07": "31",
            "08": "31",
            "09": "30",
            "10": "31",
            "11": "30",
            "12": "31"
        }
        return month_days.get(mnth)

    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                leap_year(mnth)
            else:
                not_leap_year(mnth)
        else:
            leap_year(mnth)
    else:
        not_leap_year(mnth)


def month_nums(mnth_num):
    month_num_values = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    return month_num_values.get(mnth_num)


def twenty_four_hour_time(hr):
    twenty_four_to_std = {
        "12 a": "00",
        "01 a": "01",
        "02 a": "02",
        "03 a": "03",
        "04 a": "04",
        "05 a": "05",
        "06 a": "06",
        "07 a": "07",
        "08 a": "08",
        "09 a": "09",
        "10 a": "10",
        "11 a": "11",
        "12 p": "12",
        "01 p": "13",
        "02 p": "14",
        "03 p": "15",
        "04 p": "16",
        "05 p": "17",
        "06 p": "18",
        "07 p": "19",
        "08 p": "20",
        "09 p": "21",
        "10 p": "22",
        "11 p": "23",
    }
    return twenty_four_to_std.get(hr)


text = input("Enter Tweet text: ")

while len(text) > 280:
    print("Tweet is too long")
    text = input("Enter Tweet text: ")

date = input("Enter the date you want your tweet to go out (mm/dd/yyyy): ")
date_format = re.compile(".{2}/.{2}/.{4}")

while len(date) != 10 and not date_format.match(date):
    print("Incorrect format")
    date = input("Enter the date you want your tweet to go out (mm/dd/yyyy): ")

date = date.split("/")

month = date[0]
day = date[1]
year = date[2]
current_year = tm.strftime("%Y")

while int(current_year) > int(year) > (int(current_year) + 2):
    if int(year) > (int(current_year) + 2):
        print("You can only schedule tweets up to 2 years in advance")
        year = input("Reenter year (yyyy): ")
    elif int(year) < int(current_year):
        print("This date is history (it already happened)")
        year = input("Reenter year (yyyy): ")

while len(month) != 2 or (0 >= int(month) > 12):
    print("Month out of bounds")
    month = input("Reenter month (mm): ")

while len(day) != 2 or (0 >= int(day) > int(days_in_month(month, int(year)))):
    print("Day out of bounds")
    day = input("Reenter day (dd) for corresponding month (" + month_nums(month) + "): ")

time = input("Enter the time you want your tweet to go out on " + month_nums(month) + " " + day
             + " ('11:21' OR '05:45'): ")
time_format = re.compile(".{2}:.{2}")

while len(time) != 5 and not time_format.match(time):
    print("Incorrect format")
    time = input("Enter the time you want your tweet to go out on " + month_nums(month) + " " + day
                 + " ('11:21' OR '05:45'): ")

time = time.split(":")

hour = time[0]
minute = time[1]

while 1 > int(hour) > 12:
    print("Hour out of bounds")
    hour = input("Reenter hour (hh): ")

while 0 > int(minute) > 59:
    print("Minute out of bounds")
    minute = input("Reenter minute (mm): ")


am_pm = input("AM or PM? (type 'a' for AM or 'p' for PM): ")

while not (am_pm == 'a' or am_pm == 'p'):
    print("Invalid AM/PM selection")
    am_pm = input("AM or PM? (type 'a' for AM or 'p' for PM): ")

hour = twenty_four_hour_time(hour + " " + am_pm)

tweet_time = month + day + year + hour + minute

print(tweet_time)

# add function that sorts entries in chronological order by date/time
output = open("output.txt", "a")
output.write(tweet_time + "#####" + text + "\n")  # find better way to separate date/time and tweet text than '#####'
output.close()
