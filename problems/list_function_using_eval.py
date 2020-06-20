if __name__ == '__main__':
    N= int(input("Enter the number of operations to perform on a list"))




    user_list=[]
    for _ in range(N):
        s=input().split()
        cmd = s[0]
        args = s[1:]

        args = "("+ ",".join(args)+")"

        if cmd != 'print':
            eval("user_list."+cmd+args)

        else:
            print(user_list)


