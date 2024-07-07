import random


def flip_lines(file):
    files = open(file, 'r')
    filelines = files.readlines()
    lcount = 0

    for line in filelines:
        lcount += 1

    if (lcount % 2 == 0):
        for i in range(0, lcount-1, 2):
            print(filelines[i+1].upper(), end="")
            print(filelines[i].lower(), end="")

    else:
        for i in range(0, lcount, 2):
            if (i == lcount-1):
                print(filelines[i].upper())

            else:
                print(filelines[i+1].upper(), end="")
                print(filelines[i].lower(), end="")


def factor_count(num):
    list = []
    for number in range(1, num+1):
        if (num % number == 0):
            list.append(number)
    return len(list)


def count_unique(one, two, three):
    clock = 0
    if (one != two):
        clock += 1
    if (one != three):
        clock += 1
    if (three != two):
        clock += 1
    if ((one == two) and (two == three)):
        clock += 1

    return clock


def switch_pairs(string):
    listed = list(string)
    for i in range(0, len(listed) - 1, 2):

        listed[i], listed[i + 1] = listed[i + 1], listed[i]

    switched = ''.join(listed)

    return switched


def compute_average(a):
    result = 0
    for number in range(len(a)):
        result += a[number]

    resultTwo = result / len(a)
    return resultTwo


def contains(a1, a2):
    for i in range(len(a1)):
        if a1[i] == a2[0]:
            if a1[i:i+len(a2)] == a2:
                return True
    return False


def count_duplicates(a1):
    tmp = []
    clock = 0
    for i in range(len(a1)-1):
        if (a1[i] not in tmp):
            for j in range(1, len(a1)):
                if (a1[i] == a1[j] and i != j):
                    tmp.append(a1[j])
                    clock += 1
            else:
                continue

    return clock


def find_median(nums):
    nums.sort()
    result = int((len(nums)-1)/2)
    return nums[result]


def find_range(a):
    min = a[0]
    max = a[0]
    for i in range(len(a)):
        if (a[i] < min):
            min = a[i]
        if (a[i] > max):
            max = a[i]
    result = max-min+1
    return result


def has_mirror_twice(a1, a2):
    count = 0
    a2_reversed = a2[::-1]
    for i in range(len(a1) - len(a2_reversed) + 1):
        if a1[i:i+len(a2_reversed)] == a2_reversed:
            count += 1

    return count >= 2


def max_value(nums):
    result = 0
    if (len(nums) > 0):
        result = nums[0]
        for number in nums:
            if (number > result):
                result = number
        return result

    else:
        unexcepted = "The list must contain at least one item."
        return unexcepted


def even_avarage():
    result = True
    sum = 0
    clock = 0

    while (result == True):
        sayi = int(input("Integer? "))

        if (sayi == 0):
            break
        elif (sayi % 2 == 0):
            clock += 1
            sum += sayi
            resultTwo = float(sum/clock)

    print("Average:", resultTwo)


def even_sum():
    count = int(input("how many integers? "))
    sum = 0
    max_number = float('-inf')

    for i in range(count):
        num = int(input("next integer? "))

        if num % 2 == 0:
            sum += num
            max_number = max(max_number, num)

    print("even sum =", sum)
    print("even max =", max_number)


def class_presidents(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().split()
    except FileNotFoundError:
        print(f"Unable to open input file \"{filename}\"!")
        return

    sophomores = {}
    juniors = {}

    i = 0
    while i < len(data):
        name = data[i]
        year = data[i + 1]
        votes = int(data[i + 2])

        if year == 's':
            sophomores[name] = votes
        elif year == 'j':
            juniors[name] = votes

        i += 3

    sophomore_winner = max(sophomores, key=sophomores.get)
    junior_winner = max(juniors, key=juniors.get)

    print(f"Sophomore Class President: {
          sophomore_winner} ({sophomores[sophomore_winner]} votes)")
    print(f"Junior Class President: {
          junior_winner} ({juniors[junior_winner]} votes)")


def hours():
    filename = input("Input file? ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Unable to open input file \"{filename}\"!")
        return

    for line in lines:
        data = line.split()
        empID = data[0]
        empName = data[1]
        hoursWork = [float(hours) for hours in data[2:]]
        totHours = sum(hoursWork)
        average = totHours / len(hoursWork)

        print(f"{empName} (ID#{empID}) worked {
              format(totHours, '.1f')} hours ({format(average, '.1f')}/day)")


def input_stats(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            totChar = 0
            longestLine = 0

            for i, line in enumerate(lines, 1):
                line_length = len(line.rstrip('\n'))
                totChar += line_length
                longestLine = max(longestLine, line_length)
                print(f"Line {i} has {line_length} chars")

            numLine = len(lines)
            average = totChar / numLine

            print(f"{numLine} lines; longest = {
                  longestLine}, average = {average:.1f}")

    except FileNotFoundError:
        print(f"Unable to open input file \"{filename}\"!")


def negative_sum(filename):
    try:
        with open(filename, 'r') as file:
            number = [int(num) for num in file.read().split()]

            cumulativeSum = 0
            step = 0

            for i, num in enumerate(number, 1):
                cumulativeSum += num
                step += 1

                if cumulativeSum < 0:
                    print(f"{cumulativeSum} after {step} steps")
                    return True

            print("no negative sum")
            return False

    except FileNotFoundError:
        print(f"Unable to open input file \"{filename}\"!")


def print_box(file_name, width):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    def format_line(line):
        truncated_line = line[:width - 2].strip()
        return f"#{truncated_line.capitalize().ljust(width - 2)}#"

    print("#" * width)

    for line in lines:
        print(format_line(line))

    print("#" * width)


def W_temperature_change(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    temperatures = []
    for line in lines:
        for token in line.split():
            try:
                temperature = float(token)
                temperatures.append(temperature)
            except ValueError:
                pass

    for i in range(1, len(temperatures)):
        change = temperatures[i] - temperatures[i - 1]
        print(f"{temperatures[i - 1]} to {temperatures[i]
                                          }, change = {change:.1f}")


file_name = input("Input file? ")
W_temperature_change(file_name)


def word_stats(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().split()

            total_words = len(words)
            total_chars = sum(len(word) for word in words)
            unique_letters = len(
                set(char.lower() for word in words for char in word if char.isalpha()))

            average_length = total_chars / total_words

            print(f"Total words    = {total_words}")
            print(f"Average length = {average_length:.1f}")
            print(f"Unique letters = {unique_letters}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{file_name}'.")


word_stats("tobe.txt")


def flip_coin_three_heads():
    clock = 0
    while (clock != 3):
        if (int((random.random()*10)/5) == 0):
            print("H", end=" ")
            clock += 1
        else:
            print("T", end=" ")
            clock = 0

    if (clock == 3):
        print(" ")
        print("Three heads in a row!")


flip_coin_three_heads()


def play_roulette(starting_money, bet_amount):
    current_m = starting_money
    max_money = starting_money

    print(f"start with $ {starting_money} and bet up to $ {bet_amount} ")

    print("bet\tspin\tmoney")

    while current_m > 0:

        spin = random.randint(0, 36)
        actual_bet = min(bet_amount, current_m)

        if spin % 2 == 0 and spin != 0:
            current_m += actual_bet
        else:
            current_m -= actual_bet

        max_money = max(max_money, current_m)

        print(f"{actual_bet}\t{spin}\t{current_m}")

    print(f"max money: $ {max_money}")


def random_walk(firstStep):
    if firstStep <= 0:
        return

    position = 0
    max_position = 0
    steps = 0

    while abs(position) < abs(firstStep):
        print(f"Position = {position}")
        move = random.choice([-1, 1])

        position += move
        steps += 1

        if position > max_position:
            max_position = position

    print(f"Position = {position}")
    print(f"Finished after {steps} step(s)")
    print(f"Max position = {max_position}")


def three_consecutive(num1, num2, num3):
    nums = [num1, num2, num3]
    nums.sort()
    if nums[1] == nums[0] + 1 and nums[2] == nums[1] + 1:
        return True
    else:
        return False


def contains_twice(a, b):
    clock = 0
    for i in range(len(a)):
        if (a[i] == b):
            clock += 1
    if (clock >= 2):
        return True
    else:
        return False


def is_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return string.lower() in vowels


def name_diamond(a):
    for i in range(len(a)):
        print(a[:i+1])
        j = 1
    while (j < len(a)):
        print(" " * j+a[j:])
        j += 1


def remove_all(s, char):
    result = ""
    for j in s:
        if j != char:
            result += j
    return result


def remove_duplicates(a):
    result = ""
    result_char = None
    for char in a:
        if char != result_char:
            result += char
            result_char = char
    return result


def reverse_chunks(s, k):
    result = ""
    i = 0
    while i < len(s):
        chunk = s[i: i + k]
        if len(chunk) == k:
            result += chunk[::-1]
        else:
            result += chunk
        i += k
    return result


def find_range_2d(liste):
    if not liste:
        return 0

    min_value = liste[0][0]
    max_value = liste[0][0]

    for sublist in liste:
        for num in sublist:
            min_value = min(min_value, num)
            max_value = max(max_value, num)

    return max_value - min_value + 1


def game():
    def name_game(name):
        firstName, lastName = name.split(" ")
        firstName = firstName.capitalize()
        lastName = lastName.capitalize()

        name_game = f"{firstName}, {firstName}, bo-B{firstName[1:]}\n"
        name_game += f"Banana-fana fo-F{firstName[1:]}\n"
        name_game += f"Fee-fi-mo-M{firstName[1:]}\n"
        name_game += f"{firstName.upper()}!\n"
        name_game += f"\n"
        name_game += f"{lastName}, {lastName}, bo-B{lastName[1:]}\n"
        name_game += f"Banana-fana fo-F{lastName[1:]}\n"
        name_game += f"Fee-fi-mo-M{lastName[1:]}\n"
        name_game += f"{lastName.upper()}!"

        return name_game

    name = input("What is your name? ")
    name_gamee = name_game(name)
    print(name_gamee)


def matrix_add(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result


def word_wrap(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            if len(line) <= 60:
                print(line)
            else:
                while len(line) > 60:
                    print(line[:60])
                    line = line[60:]
                print(line)


def word_wrap2(input_file, output_file):
    MAX_LINE_LENGTH = 60

    with open(input_file, 'r') as file:
        content = file.read()

    wrapped_lines = []
    words = content.split()
    current_line = words[0]
    for word in words[1:]:
        if len(current_line) + len(word) + 1 <= MAX_LINE_LENGTH:
            current_line += ' ' + word
        else:
            wrapped_lines.append(current_line)
            current_line = word

    wrapped_lines.append(current_line)

    with open(output_file, 'w') as file:
        file.write('\n'.join(wrapped_lines))


def dice_sum():
    result = int(input("Desired dice sum: "))
    temp = 0
    temp1 = 0

    while (temp+temp1 != result):
        temp = random.randint(1, 7)
        temp1 = random.randint(1, 7)
        print(temp, "and", temp1, "=", temp+temp1)


def digit_sum(a):
    tmp = str(a)
    result = 0
    clock = 0
    num1 = abs(a)

    while (len(tmp) != clock):
        result += num1 % 10
        num1 = int(num1/10)
        clock += 1
    return result


def print_average():
    sayi = 0
    result = 0
    clock = 0
    tmp = 0
    while (sayi >= 0):
        sayi = int(input("Type a number: "))
        if (sayi < 0):
            break
        else:
            result += sayi
            clock += 1

            tmp = result/clock
    if (tmp > 0):
        print("Average was", tmp)


def print_factors(num):
    factor_list = []
    for number in range(1, num+1):
        if num % number == 0:
            factor_list.append(number)
    result = ' and '.join(str(factor) for factor in factor_list)
    print(result)


print_factors(45)
