import csv
import json

task_list = []

with open("C:\\Users\\pc11\\Desktop\\03.04数据.csv")as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        print(row['business_id'], row['extra'], row['create_time'])
        ids = json.loads(row['extra'])
        task_list.append(
            {
                'business': row['business_id'],
                'id': {
                    'uid': ids['uid'],
                    'secUid': ids['secUid'],
                },
                'create_time': row['create_time']
            }
        )


with open("C:\\Users\\pc11\\Desktop\\03.04数据.json", 'w', encoding='utf-8')as f:

    json.dump(task_list, f)