__author__ = 'Sharayah Reyes'

class GradedActivity:
    score = 0.0

    def set_score(self, s):
        self.score = s

    def get_score(self):
        return self.score

    def get_grade(self):
        grade = ""

        if self.score >= 90:
            grade = "A"
        elif self.score >= 80:
            grade = "B"
        elif self.score >= 70:
            grade = "C"
        elif self.score >= 60:
            grade = "D"
        else:
            grade = "F"

        return grade

class FinalExam(GradedActivity):
    num_questions = 0
    points_each = 0.0
    num_missed = 0

    def __init__(self, questions, missed):
        self.numeric_score = 0

        self.num_questions = questions
        self.num_missed = missed

        self.points_each = 100.0 / questions
        self.numeric_score = 100.0 - (missed * self.points_each)
        self.set_score(self.numeric_score)

    def get_points_each(self):
        return self.points_each

    def get_num_missed(self):
        return self.num_missed

def main():
    questions = 0
    missed = 0

    questions = int(input("Enter the number of questions on exam: "))
    missed = int(input("Enter the number of questions missed on exam: "))
    exam = FinalExam(questions, missed)

    print("Each question on the exam counts as", exam.get_points_each(), "points.")
    print("The exam score is:", exam.get_score())
    print("The exam grade is:", exam.get_grade())
main()