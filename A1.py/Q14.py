def read_lines():
    lines = []
    print("Enter your lines of text")

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    return lines


def print_lines(lines):
    print("\nYou entered:")
    for line in lines:
        print(line)


user_lines = read_lines()

print_lines(user_lines)