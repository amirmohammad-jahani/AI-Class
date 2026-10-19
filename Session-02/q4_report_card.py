scores = {"Ali": 18, "Sara": 20, "Reza": 9, "Mina": 14, "Omid": 11.5}

passed_students = []   
total_score = 0           
top_student = ""      
highest_score = 0  

print("--- بخش الف: کارنامه ---")

for name in scores:
    score = scores[name]
    
    if score >= 17:
        rank = "عالی"
    elif score >= 14:
        rank = "خوب"
    elif score >= 10:
        rank = "قبول"
    else:
        rank = "مردود"
        
    print(name, "با نمره", score, ":", rank)
    
    if score >= 10:
        passed_students.append(name)
        
    total_score = total_score + score
    
    if score > highest_score:
        highest_score = score
        top_student = name


print("\n--- بخش ب: لیست قبولی‌ها ---")
print(passed_students)

print("\n--- بخش ج: میانگین کلاس ---")
average = total_score / len(scores)
print(average)

print("\n--- بخش د: شاگرد اول ---")
print(top_student, "با نمره", highest_score)