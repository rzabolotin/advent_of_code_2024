from collections import Counter

def check_report(report):
    shifts = [x-y for x,y in zip(report, report[1:])]
    result = (all(x > 0 for x in shifts) or all(x < 0 for x in shifts)) and all(1 <= abs(x) <=3 for x in shifts)
    return result

def check_report2(report):
    if check_report(report):
        return True
    for i in range(len(report)):
        if check_report(report[:i] + report[i+1:]):
            return True

    return False


def main():
    with open("input.txt", "r") as fin:
        data = fin.readlines()

    # Part 1
    reports = [[int(j) for j in x.strip().split()] for x in data]

    results = [check_report(report) for report in reports]
    print("Valid reports: ", sum(results))

    # Part 2
    results = [check_report2(report) for report in reports]
    print("Valid reports 2: ", sum(results))


if __name__ == "__main__":
    main()