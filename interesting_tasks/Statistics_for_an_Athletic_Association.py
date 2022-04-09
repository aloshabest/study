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