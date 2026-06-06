import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

students = {
    "Ali": {"math": 18, "science": 15, "english": 17},
    "Sara": {"math": 14, "science": 16, "english": 19},
    "Reza": {"math": 12, "science": 13, "english": 11}
}

while True:
    print("===مدیریت نمرات===")
    print("1.نمایش همه دانش اموزان و نمرات")
    print("2.اضافه کردن دانش اموز جدید")
    print("3.محاسبه معدل یک دانش اموز")
    print("4.بهترین دانش اموز(بالاترین معدل)")
    print("5.تغییر نمره یک درس خاص")
    print("خروج.6")


    choise=int(input("your choice: "))
    match choise:
        case 1:
            for name_stu,scores in students.items():
                print(f"{name_stu}--->{scores}")

        case 2:
            new_name=input("Enter your name")
            new_math=int(input("Enter your math score."))
            new_science=int(input("Enter your scinece score."))
            new_english=int(input("Enter your english score."))

            repeated_name=False
            for name_stu,scores in students.items():
                if new_name==name_stu:
                    print("The name is repeated!!")
                    repeated_name=True
                    break
            if repeated_name==False:
                students[new_name]={"math": new_math, "science": new_science, "english": new_english}
        
        case 3:
            existence_name=False
            name_for_avg=input("Enter the name you want to see the grade for.")
            for name_stu,scores in students.items():
                if name_for_avg==name_stu:
                    existence_name=True
                    average=(scores["math"]+scores["science"]+scores["english"])/len(scores)
                    print(f"{name_stu}==>{average:.2f}")
                    break
            if existence_name==False:
                print("This name does not exist")
        
        case 4:
            best_name=""
            best_avg=0
            avg={}

            for name,scores in students.items():
                average=(scores["math"]+scores["science"]+scores["english"])/len(scores)
                avg[name]=average

            for name,average in avg.items():
                if average>best_avg:
                    best_avg=average
                    best_name=name

            print(f"بهترین دانش‌آموز: {best_name} با معدل {best_avg:.2f}")
        
        case 5:
            edit_name=input("enter the name you want to change the scores: ")
            edit_lesson=input("enter the lesson you want to change the scores: ")
            edit_scores=int(input(f"enter the new score {edit_lesson}: "))
            
            if edit_name in students:
                if edit_lesson in students[edit_name]:
                    students[edit_name][edit_lesson] = edit_scores
                    print(f"{edit_name}'s {edit_lesson} changed to {edit_scores}")
                else:
                    print("There is no such lesson!")
            else:
                print("There is no such user!")
            
        case 6:
            print("Goodbye!")
            break
        
        case _:
            print("Invalid choice!")
            
