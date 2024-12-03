import re

def main():
    with open("input.txt", "r") as fin:
        data = fin.read()

    # Part 1
    results = re.findall(r'mul\((\d+),(\d+)\)', data)
    total_sum = sum(int(x) * int(y) for x, y in results)
    print(f"Total sum: {total_sum}")

    # Part 2
    results = re.findall(r'(d)on\'t\(\)|(d)o\(\)|mul\((\d+),(\d+)\)', data)
    state = "do"
    total_sum = 0
    for dont, do, x, y in results:
        if dont:
            state = "dont"
        elif do:
            state = "do"
        elif state == "do":
            total_sum += int(x) * int(y)

    print(f"Total sum 2 : {total_sum}")


if __name__ == "__main__":
    main()