score_dict = {
    'message':'Enter a valid URL',
    'code':'invalid'
}

for key, value in score_dict.items():
    aaa=[]
    for index in value:
        aaa.append(index['message'])
        print(aaa)
