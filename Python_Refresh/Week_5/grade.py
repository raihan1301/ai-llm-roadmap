def round_scores(scores):
    # map(round, scores) applies round() to every item instantly
    return list(map(round, scores))

def count_failed_students(student_scores):
    count = 0

    for score in student_scores:
        if score <= 40:
            count += 1
    return count

def above_threshold(student_scores, threshold):
    best_Scores = []

    for score in student_scores:
        if score >= threshold:
            best_Scores.append(score)

    return best_Scores

def letter_grades(highest):
    failing_grade = 40

    difference = 100 - highest
    if difference == 0:
        difference = 15

    letter_grade = []
    grade = failing_grade

    while grade < highest:
        letter_grade.append(grade + 1)
        grade = grade + difference

    return letter_grade

def student_ranking(student_scores, student_names):

    ranking = []

    for i in range(len(student_scores)):
        rank_list = str(i+1) + '. ' + student_names[i] + ': ' + str(student_scores[i])
        ranking.append(rank_list)

    return ranking

def perfect_score(student_info):

    hero = []
    for student in student_info:
        if student[1] == 100:
            hero.append(student)

    return hero


def main():
    result1 = round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])
    print(result1)

    result2 = count_failed_students([90,40,55,70,30,25,80,95,38,40])
    print(result2)

    result3 = above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75)
    print(result3)

    result4 = letter_grades(highest=88)
    print(result4)

    result5 = letter_grades(highest=100)
    print(result5)

    result6 = student_ranking([100, 99, 90, 84, 66, 53, 47], ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred'])
    print(result6)

    result7 = perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]])
    print(result7)

main()