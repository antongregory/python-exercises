if __name__ == '__main__':
    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        new = [name, score]
        students.append(new)
    print(students)
    alphabetical_order = sorted(students)
    second_highest = sorted(list(set([marks for name, marks in students])))[1]
    print('\n'.join([a for a,b in sorted(students) if b == second_highest]))
