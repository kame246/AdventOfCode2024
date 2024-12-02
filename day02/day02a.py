def is_report_safe(report):
    previous = report[0]
    increasing = report[1] > report[0]

    for level in report[1:]:
        if increasing:
            if level <= previous:
                return False
        else:
            if level >= previous:
                return False
        diff = abs(level - previous)
        if not (1 <= diff <= 3):
            return False
        previous = level
    return True


with open('real.txt') as fin:
    reports = [[int(x) for x in line.split()] for line in fin]

print(sum([is_report_safe(report) for report in reports]))
