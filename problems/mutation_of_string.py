def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    print (string)

if __name__ == '__main__':
    first_input= input("Enter a string: ")
    second_input = input("Enter position and character to modify").split(' ')

    if len(second_input) < 2:
        raise ValueError

    mutate_string(first_input, int(second_input[0]), second_input[1])