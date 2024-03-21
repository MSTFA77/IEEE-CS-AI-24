if __name__ == '__main__':
    n = int(input())
    students = []
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: (x[1], x[0]))  
    second_lowest_grade = students[0][1]
    for student in students:
        if student[1] > second_lowest_grade:
            second_lowest_grade = student[1]
            break
    for student in students:
        if student[1] == second_lowest_grade:
            print(student[0])
