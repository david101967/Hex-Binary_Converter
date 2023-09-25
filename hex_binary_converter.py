def main():

    #operation and checking to make sure it is the right operation
    operator_input = input("Enter Operation ^ & | or q to quit: ")
    while operator_input != "q":
        operators = ["^","&","|"]


        while operator_input not in operators:
            operator_input = input("Please enter | & ^  or q.  ")
        integers = int(input("Enter the number of integers: "))
        numbers = []
        for i in range(0, integers):
            num = input(("Enter Integer %i: " % (i + 1)))
            while not check_hex(num):
                num = input("Enter integer %i: " % (i + 1))
            numbers.append(num)

        new_numbers = fix_hex_length(numbers)
        for i in range(len(new_numbers)):
            if i ==0:
                print("Hexadecimal operation:")
                print("  ",new_numbers[i])
            else:
                print(operator_input,new_numbers[i])
        if operator_input == "|":
            ans = or_func(new_numbers)
            print("=", ans )
        elif operator_input == "^":
            ans = orx_func(new_numbers)
            print("=", ans)
        elif operator_input == "&":
            ans = and_func(new_numbers)
            print("=", ans)
        print("Binary operations:")
        hex_binary(new_numbers, operator_input)

        operator_input = input("Enter Operation: ")





#Checking to make sure the hex enter is under 8 digits

def check_hex(num):
    for ch in num:
        if ch not in "0123456789abcdefABCDEF" or len(num) >8:
            return False
        return True
#make the length proper
def fix_hex_length(numbers):
    new_numbers = []
    for i in numbers:
        if len(i)<8:
            ck = 8-len(i)
            str1='0'*ck
            i = str1+i
            new_numbers.append(i)
        else:
            new_numbers.append(i)
    return new_numbers
# result for | operator
def or_func(new_numbers):
    result = int(new_numbers[0],16)
    i=1
    for i in range(len(new_numbers)):
        result|= int(new_numbers[i],16)

    return "%08X"%result

def orx_func(new_numbers):
    result = int(new_numbers[0], 16)
    i = 1
    for i in range(len(new_numbers)):
        result^= int(new_numbers[i], 16)
    return "%08X" % result

def and_func(new_numbers):
    result = int(new_numbers[0], 16)
    i = 1
    for i in range(len(new_numbers)):
        result&= int(new_numbers[i], 16)
    return "%08X" % result

def bin_conversion(new_numbers):
    the_list = []
    for k in new_numbers:
        n_pairs = 1
        str_binary = ""
        for j in k:
            str_binary += format(int(j,16), '0>4b')
            if n_pairs % 2 == 0 and n_pairs <7:
                str_binary += " "
                n_pairs += 1
            else:
                n_pairs += 1
        the_list.append(str_binary)
    return the_list

def hex_binary(numbers, operator_input):
    new_numbers = bin_conversion(numbers)
    final_result = int(new_numbers[0].replace(" ", ""), 2)
    if operator_input == "|":
        print(" ", new_numbers[0])
        print("|", new_numbers[1])
        i=1
        for i in range(len(new_numbers)):
            final_result |= int(new_numbers[i].replace(" ", ""), 2)
        hex_result = ['%08X'%final_result]
        bin_result = bin_conversion(hex_result)[0]
        print("=", bin_result)
    elif operator_input == "&":
        print(" ", new_numbers[0])
        print("&", new_numbers[1])
        i=1
        for i in range(len(new_numbers)):
            final_result &= int(new_numbers[i].replace(" ", ""), 2)
        hex_result = ['%08X'%final_result]
        bin_result = bin_conversion(hex_result)[0]
        print("=", bin_result)
    elif operator_input == "^":
        print(" ", new_numbers[0])
        print("^", new_numbers[1])
        i=1
        for i in range(len(new_numbers)):
            final_result ^= int(new_numbers[i].replace(" ", ""), 2)
        hex_result = ['%08X'%final_result]
        bin_result = bin_conversion(hex_result)[0]
        print("=", bin_result)


main()
