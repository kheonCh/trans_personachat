import json

with open('personachat_self_original.json') as json_file:
    json_all_data = json.load(json_file)
    for index, json_train_data in enumerate(json_all_data['train']):
        if index == 3:
            break
        file_name = '%d_train_personachat.json' % index
        f = open(file_name, 'w')
        json.dump(json_train_data, f)
