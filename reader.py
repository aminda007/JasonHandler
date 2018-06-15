import json

with open('train-v1.1.json') as data_file:
        file = json.load(data_file)
        # data = file
        dataArray = file["data"]
        version = file["version"]
        print(len(dataArray))
        # for element in dataArray:
        #         print(element["title"])

        # dataArray = dataArray.splice(0, 300);
        del dataArray[441:442]
        print("1111111111111111111111111111111")
        # print(file)
        print("1111111111111111111111111111111")
        print(len(dataArray))
        for element in dataArray:
                print(element["title"])

        obj1 = {}
        obj1['title'] = "Java"
        paragraphArray = []


        # start first context object
        contextObj = {}
        contextObj['context'] = "Java is programmmm"
        # start qas array
        qasArray = []
        # first answer object
        ansObj={}
        ansArray=[]
        answerObj1 = {}
        answerObj1['answer_start'] = 10
        answerObj1['text'] = "Java is a programming language"
        ansArray.append(answerObj1)
        ansObj["answers"] = ansArray
        ansObj['question'] = "What is Java?"
        ansObj['id'] = "57359bbcdc94161900571ee9"
        qasArray.append(ansObj)
        # second answer object
        ansObj = {}
        ansArray = []
        answerObj1 = {}
        answerObj1['answer_start'] = 10
        answerObj1['text'] = "Java is a programming language"
        ansArray.append(answerObj1)
        ansObj["answers"] = ansArray
        ansObj['question'] = "What is Java?"
        ansObj['id'] = "57359bbcdc94161900571ee9"
        qasArray.append(ansObj)
        # third answer object
        ansObj = {}
        ansArray = []
        answerObj1 = {}
        answerObj1['answer_start'] = 10
        answerObj1['text'] = "Java is a programming language"
        ansArray.append(answerObj1)
        ansObj["answers"] = ansArray
        ansObj['question'] = "What is Java?"
        ansObj['id'] = "57359bbcdc94161900571ee9"
        qasArray.append(ansObj)
        # add qas array
        contextObj['qas'] = qasArray
        # add firat context
        paragraphArray.append(contextObj)




        # start second context object
        contextObj = {}
        contextObj['context'] = "Java is programmmm"
        # start qas array
        qasArray = []
        # first answer object
        ansObj = {}
        ansArray = []
        answerObj1 = {}
        answerObj1['answer_start'] = 10
        answerObj1['text'] = "Java is a programming language"
        ansArray.append(answerObj1)
        ansObj["answers"] = ansArray
        ansObj['question'] = "What is Java?"
        ansObj['id'] = "57359bbcdc94161900571ee9"
        qasArray.append(ansObj)
        # second answer object
        ansObj = {}
        ansArray = []
        answerObj1 = {}
        answerObj1['answer_start'] = 10
        answerObj1['text'] = "Java is a programming language"
        ansArray.append(answerObj1)
        ansObj["answers"] = ansArray
        ansObj['question'] = "What is Java?"
        ansObj['id'] = "57359bbcdc94161900571ee9"
        qasArray.append(ansObj)
        # third answer object
        ansObj = {}
        ansArray = []
        answerObj1 = {}
        answerObj1['answer_start'] = 10
        answerObj1['text'] = "Java is a programming language"
        ansArray.append(answerObj1)
        ansObj["answers"] = ansArray
        ansObj['question'] = "What is Java?"
        ansObj['id'] = "57359bbcdc94161900571ee9"
        qasArray.append(ansObj)
        # add qas array
        contextObj['qas'] = qasArray
        # add second context
        paragraphArray.append(contextObj)

        # add paragraph to object
        obj1['paragraphs'] = paragraphArray
        # append object to data array
        dataArray.append(obj1)

        print(file)


        with open('data.json', 'w') as data_file:
                data = json.dump(file, data_file)