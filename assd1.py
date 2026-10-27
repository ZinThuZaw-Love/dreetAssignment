students = [
{"name": "Aung Aung","age":20,"studyhour":5, "score": 70},
{"name": "Mya Mya","age":20,"studyhour":5, "score": 85},
{"name": "Kyaw Kyaw","age":20,"studyhour":5, "score": 65},
{"name": "Aye Aye","age":20,"studyhour":5, "score": 45},
{"name": "Zaw Zaw","age":20,"studyhour":5, "score": 30}
]

scores=[student["score"]for student in students]

def classify_grade(scores):
    if scores < 0 or scores > 100:
        return "Invalid"
    elif scores >=80:
        return "EXCELLENT"
    elif scores >=60:
        return "GOOD"
    elif scores >= 40:
        return "PASS"
    elif scores>0: return "FAIL"

print("=====STUDENT PERFORMANCE REPORT=====")
for student in students:
    print("Name: ",student["name"])
    print("Age: ",student["age"])
    print("Study Hour: ",student["studyhour"])
    print("Score",student["score"])
    print("Grade: ",classify_grade(student["score"]))

print("=====SUMMARY=====")
print ("Total Student: ",len(students))

def calculate_average(scores):
    return sum(scores)/len(scores)
print("Average Scores: ",calculate_average(scores))

print ("Highest Score: ",max(scores))
print("Lowest Score: ",min(scores))

def count_passed(students):
    count=0
    for student in students:
        if student["score"]>=40:
            count += 1
    return count
passed=count_passed(students)
print ("Passed Students: ",passed)

def count_failed(students):
    count=0
    for student in students:
        if student["score"]<40:
            count += 1
    return count
failed=count_failed(students)
print ("Failed Students: ",failed)

def top_student(students):
    t=max(scores)
    for student in students:
        if student["score"]==t:
            return student["name"],student["age"],student["studyhour"],student["score"]
s=top_student(students)
print ("Top Student: ",s)