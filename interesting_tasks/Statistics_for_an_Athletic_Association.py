#Задача Codewars: 6 kyu.
# You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete. Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5 runners:
# "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"
# Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits. Substrings in the input string are separated by , or ,.
# To compare the results of the teams you are asked for giving three statistics; range, average and median.
# Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.
# Mean or Average : To calculate mean, add together all of the numbers in a set and then divide the sum by the total count of numbers.
# Median : In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).
# Your task is to return a string giving these 3 values. For the example given above, the string result will be
# "Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"
# of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`
# where hh, mm, ss are integers (represented by strings) with each 2 digits.

import statistics


def ranges(result):
    x = max(result) - min(result)
    return f"{int(x // 3600):02}|{int((x // 60) % 60):02}|{int(x % 60):02}"


def average(result):
    x = sum(result)/len(result)
    return f"{int(x // 3600):02}|{int((x // 60) % 60):02}|{int(x % 60):02}"


def mediana(result):
    x = statistics.median(result)
    return f"{int(x // 3600):02}|{int((x // 60) % 60):02}|{int(x % 60):02}"


def stat(strg):
    if strg == "":
        return ""
    else:
        runners = [[int(j) for j in i.split('|')] for i in strg.split(', ')]
        result = [(i[0] * 3600 + i[1] * 60 + i[2]) for i in runners]
        return f"Range: {ranges(result)} Average: {average(result)} Median: {mediana(result)}"


strg = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"

strg_2 = "11|15|59, 10|16|16, 12|17|20, 9|22|34, 13|19|34, 11|15|17, 11|22|00, 10|26|37, 12|17|48, 9|16|30, 12|20|14, 11|25|11"

print(stat(strg))

print(stat(strg_2))