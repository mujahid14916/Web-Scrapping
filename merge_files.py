import glob
import json


files = glob.glob('coursera data/*.json')
coursera_doc = []
for file in files:
    with open(file, 'r') as f:
        data = json.loads(f.read())
        for d in data:
            d['subject'] = [file.split('\\')[-1][:-5]]
        coursera_doc += data


processed_doc = []
titles = []
i = 0
for d in coursera_doc:
    if d['title'] in titles:
        for i in range(len(processed_doc)):
            if processed_doc[i]['title'] == d['title']:
                if type(d['category']) == type([]):
                    for category in d['category']:
                        if category not in processed_doc[i]['category']:
                            processed_doc[i]['category'].append(category)
                else:
                    processed_doc[i]['category'].append(d['category'])
                if processed_doc[i]['subject'] != d['subject']:
                    processed_doc[i]['subject'] += d['subject']
                break
        i += 1
        continue
    processed_doc.append(d)
    titles.append(d['title'])
print("Duplicates found: {}".format(i))

with open('data.json', 'w') as f:
    f.write(json.dumps(processed_doc, indent=4))
