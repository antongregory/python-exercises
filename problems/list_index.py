if __name__ == '__main__':
    N = int(input())
    user_entry = []

    command_dict = {"insert" : lambda x: (user_entry.insert(int(x[0]), int(x[1]))),
                    "print": lambda x: print(user_entry),
                    "remove": lambda x: user_entry.remove(int(x[0])),
                    "append": lambda x: user_entry.append(int(x[0])),
                    "sort" : lambda x: user_entry.sort(),
                    "pop": lambda x: user_entry.pop(),
                    "reverse": lambda x: user_entry.reverse()}


    for i in range(N):
        i, *values  = input().split()
        command_dict[i](values)



