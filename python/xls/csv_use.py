import csv
import json

good_list = []
follow_list = []
count = 0

with open("C:\\Users\\pc11\\Desktop\\check_system_test_data\\03.18data.csv")as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        print(row['type'], row['business_user_id'], row['create_time'])
        if row['type'].strip() == "good":
            good_list.append(
                {
                    'business': row['business_id'],
                    'uid': row['business_user_id'],
                    'create_time': row['create_time'],
                }
            )

        elif row['type'].strip() == "follow":
            follow_list.append(
                {
                    'business': row['business_id'],
                    'uid': row['business_user_id'],
                    'create_time': row['create_time'],
                }
            )

with open("C:\\Users\\pc11\\Desktop\\check_system_test_data\\03.18.good.json", 'w', encoding='utf-8')as f:
    json.dump(good_list, f)


with open("C:\\Users\\pc11\\Desktop\\check_system_test_data\\03.18.follow.json", 'w', encoding='utf-8')as f:
    json.dump(follow_list, f)
