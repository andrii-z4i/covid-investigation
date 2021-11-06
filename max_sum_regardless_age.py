import csv

data_male_female = {
    'male': {},
    'female': {}
}

with open('data/all.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    counter = 0
    for row in csv_reader:
        if counter == 0:
            counter += 1
            continue

        if not row[0] in data_male_female['female' if row[2] == 'Z' else 'male']:
            data_male_female['female' if row[2] == 'Z' else 'male'][row[0]] = 0
        data_male_female['female' if row[2] == 'Z' else 'male'][row[0]] = data_male_female['female' if row[2] == 'Z' else 'male'][row[0]] + 1

# male
max_male = max(data_male_female['male'].values())
print ('Max males at one day', '\t\t',max_male)
sum_males = sum(data_male_female['male'].values())
print('Sum males over the time', '\t', sum_males)

max_female = max(data_male_female['female'].values())
print ('Max females at one day', '\t\t', max_female)
sum_females = sum(data_male_female['female'].values())
print('Sum females over the time', '\t', sum_females)