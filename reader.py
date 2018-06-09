import json

with open('train-v1.1.json') as data_file:
        file = json.load(data_file)
        # data = file
        dataArray = file["data"]
        version = file["version"]
        # print("00000000000000000000000000000000000")
        # print(file)
        # print("00000000000000000000000000000000000")
        # print(version)
        print(len(dataArray))
        # for element in dataArray:
        #         print(element["title"])

        # dataArray = dataArray.splice(0, 300);
        del dataArray[0:441]
        print("1111111111111111111111111111111")
        # print(file)
        print("1111111111111111111111111111111")
        print(len(dataArray))
        for element in dataArray:
                print(element["title"])

        obj1 = {}
        obj1['title'] = "Java"
        paragraphArray = []

        contextObj = {}
        contextObj['context'] = "Java is programmmm"
        qasArray = []
        ansObj={}
        ansArray=[]
        answerObj1 = {}
        answerObj1['answer_start']=10
        answerObj1['text']="Java is a programming language"
        ansArray.append(answerObj1)
        ansObj["answers"] = ansArray
        ansArray = []
        qasArray
        contextObj['qas'] = "Java is programmmm"
        contextObj['question'] = "What is Java?"
        contextObj['id'] = "57359bbcdc94161900571ee9"


        paragraphArray.append(contextObj)
        obj1['paragraphs'] = paragraphArray
        dataArray.append(obj1)
        print(dataArray)

        dataArray = dataArray[0]
        title = dataArray["title"]
        # print(title)
        paragraphs = dataArray["paragraphs"]

        # print(paragraphs)

        # for element in data:
        #         print()
                # del element['hours']
        # for element in data:
        #         element.pop('hours', None)
        #










        with open('data.json', 'w') as data_file:
                data = json.dump(file, data_file)