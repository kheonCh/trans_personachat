import json

with open('personachat_self_original.json') as json_file:
    json_data = json.load(json_file)

    #print(json_data)
    print(type(json_data))
    #print(json_data['train'][0])
    print(len(json_data['train']))
    print(len(json_data['valid']))
    #print(json_data[train])

    # all
    for key, value in json_data.items():
        print(key)

    # train
    for key, value in json_data['train'][0].items():
        print(key)


    # train
    for key, value in json_data['train'][0]['utterances'][0].items():
        print(key)