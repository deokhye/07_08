import json

students_file_path = './students_json'

def read_students_json():
    with open(students_file_path, "r") as json_file:
        students_json_data = json.load(json_file)

    return students_json_data


def write_students_json(students_json_data):
    with open(students_file_path, 'w') as outfile:
        json.dump(students_json_data, outfile, ensure_ascii=False, indent=4)

#모든 학생 출력
def all_name(students_json_data):
    for i in range(len(students_json_data["students"])):
    print(students_json_data["students"][i]["name"])
    
        
#20세 미만 확인, 출력
def under_(students_json_data):
    for i in range(len(students_json_data["students"])):
        if int(students_json_data["students"][i]["age"]) < 20:
            print(json_data["students"][i]["name"], ", 나이:",json_data["students"][i]["age"])
            

#새로운 학생 넣기//잘 모르겠다    
new_student = {'name':'kim', 'age':'11', 'job':'elem_stu', 'id':'dokdo', 'pw':'1004'}

students['students'] += [new_student]

with open(students_file_path, 'w') as new_make:
    json.dump(students_json_data, new_make, ensure_ascii=False, indent=4)


# 조건문으로 아이디를 안넣으면 쓰기 안되게 막기
if id == False:
  print(None)
