if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range (n):
        name,*lines = input().split()
        lines = list(map(float,lines))
        student_marks[name] = lines


    marks = student_marks.get(input())
    total = sum(marks)
    num_subjects = len(marks)
    print("{:.2f}".format(total/num_subjects))