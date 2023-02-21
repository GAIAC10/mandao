
import requests,json,re
# url = 'http://www.zaguopei.com/api/Exam/GetPaperQuestion?CourseId=47349&PaperId=0&IsContinue=false'
url = 'http://www.zaguopei.com/api/Exam/GetPaperQuestion?CourseId=47349&PaperId=0&IsContinue=false'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    # 'Cookie': 'etlbdyssession=e7a98cc5-e013-40b3-a490-9a596e01e464',
    'Cookie': 'etlbdyssession=5bfaf497-d0ec-49fb-9e1e-541fb423af1e',

}

res = requests.get(url,headers=headers)
json_data = json.loads(res.text)

datas = json_data['data'][0]['QuestionList']
data1 = json_data['data'][1]['QuestionList']
data2 = json_data['data'][2]['QuestionList']
data3 = json_data['data'][3]['QuestionList']
answer = {}
answer1 = {}
answer2 = {}
answer3 = {}
for i in datas:
    # print(i)
    # print(i['Option'])
    # print(i['QuestionContentFormat'])
    question = re.search('<span style=\'font-weight:bold\'>(.*)</span>',i['QuestionContentFormat']).group(1)
    # print(question)
    #
    for j in i['Option']:
        if j["IsTrue"] == True:
            answer[question] = j['ValueFormat']
for i in data1:
    # print(i)
    # print(i['Option'])
    # print(i['QuestionContentFormat'])
    question = re.search('<span style=\'font-weight:bold\'>(.*)</span>',i['QuestionContentFormat']).group(1)
    # print(question)
    #
    for j in i['Option']:
        if j["IsTrue"] == True:
            answer1[question] = j['ValueFormat']
for i in data2:
    # print(i)
    # print(i['Option'])
    # print(i['QuestionContentFormat'])
    question = re.search('<span style=\'font-weight:bold\'>(.*)</span>',i['QuestionContentFormat']).group(1)
    # print(question)
    #
    for j in i['Option']:
        if j["IsTrue"] == True:
            answer2[question] = j['ValueFormat']
for i in data3:
    # print(i)
    # print(i['Option'])
    # print(i['QuestionContentFormat'])
    question_anli = re.search('<span style=\'font-weight:bold\'>(.*)</span>',i['QuestionContentFormat']).group(1)
    # print(question)
    #
    # print(i)
    # print('*'*30)
    for j in i['ChildQuestions']:
        # print(j)
        question = re.search('<span style=\'font-weight:bold\'>(.*)</span>',j['QuestionContentFormat']).group(1)
        for k in j['Option']:
            # print(k)
            if k["IsTrue"] == True:
                answer3[question] = k['ValueFormat']
# print(answer)
# print(answer1)
# print(answer2)
# print(answer3)

res2 = {**answer, **answer1,**answer2,**answer3}
print(res2)
with open("tiku2.txt",'w') as fp:
    fp.write(str(res2))
