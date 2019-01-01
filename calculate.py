def calculate_gpa():
    number_of_subjects = int(input('Enter the number of subjects: '))
    
    #Blank Line
    print()

    cumulative_credits = 0
    gpa_by_credits = 0

    subject_names = []
    subjects_grade = []
    subject_credits = []

    for index in range(number_of_subjects):
        print('Enter the name of subject', index + 1, ': ', end="")
        current_subject = str(input())
        subject_names.append(current_subject)
        
        print('Enter the GPA obtained in', subject_names[index], ': ', end="")
        current_grade = float(input())
        subjects_grade.append(current_grade)
        
        print('Enter the number of credits of', subject_names[index], ': ', end="")
        current_credits = float(input())
        subject_credits.append(current_credits)

        cumulative_credits += current_credits
        gpa_by_credits += current_grade*current_credits
        cumulative_gpa = gpa_by_credits/cumulative_credits
        
        undertaken_courses = dict(zip(subject_names, subjects_grade))

        print('\n-- The Current GPA is:', str(current_grade)[:4], '--')
        print('-- The Cumulative GPA is:', str(cumulative_gpa)[:4], '--', end="\n\n")
        
    print('-- The courses undertaken are given below --\n')
    
    for index, grade in enumerate(undertaken_courses):
        print('Subject:', grade, '& Grade:', subjects_grade[index])

    print('\n-- Maximum Grade(s) obtained in the given subject(s) --')

    for checker in range(number_of_subjects):
        if subjects_grade[checker] == max(subjects_grade):
            print('Subject:', subject_names[checker], '& Grade:', max(subjects_grade))


if __name__ == '__main__':
    calculate_gpa()
    print('Thank you for using this program!')
