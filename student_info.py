import csv

def info_into_csv(info_list):
    with open('Student_info.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["NAME","AGE","EMAIL_ID"])
        writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    while condition:
        student_info=input("Enter the student info in the give format[NAME AGE EMAIL_ID]: ")
        student_info_list=student_info.split(' ')
        print("\nThis is your enterd info:\nNAME:{}\nAGE:{}\nEMAIL_ID:{}"
              .format(student_info_list[0],student_info_list[1],student_info_list[2]))
        info_check=input("Is your enterd info correct(yes/no): ")
        if info_check=="yes":
            info_into_csv(student_info_list)
            conditon_check=input("Do you want to enter information for another student(yes/no): ")
            if conditon_check=="yes":
                condition=True
            elif conditon_check=="no":
                condition=False

        elif info_check=="no":
            print("\nPlease re-enter the info ")
