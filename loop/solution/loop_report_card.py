ALLOWED_GRADES = [float(x) for x in (2, 3, 3.5, 4, 4.5, 5)]
report_card = []


while True:
    grade = input('Grade: ')

    if not grade:
        break

    grade = float(grade)
    if grade in ALLOWED_GRADES:
        print(f'Adding {grade}')
        report_card.append(grade)
    else:
        print('Grade is not allowed')


average = sum(report_card) / len(report_card)
print(f'Average: {average}')
