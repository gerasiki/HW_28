import csv
import json

DATA_ADS = 'data/ads.csv'
JSON_ADS = 'ads.json'

DATA_CAT = 'data/categories.csv'
JSON_CAT = 'categories.json'


def convert_file_ads(csv_file, model_name, json_file):
    res = []
    with open(csv_file, encoding='utf-8') as csvf:
        for row in csv.DictReader(csvf):
            to_add = {"model": model_name, "pk": int(row['Id']), "fields": row}
            del row['Id']
            if row['is_published'] == 'TRUE':
                row['is_published'] = True
            else:
                row['is_published'] = False
            row['price'] = int(row['price'])
            to_add['fields'] = row
            res.append(to_add)

    with open(json_file, "w", encoding='utf-8') as jsf:
        jsf.write(json.dumps(res, ensure_ascii=False))


def convert_file_categories(csv_file, model_name, json_file):
    res = []
    with open(csv_file, encoding='utf-8') as csvf:
        for row in csv.DictReader(csvf):
            to_add = {"model": model_name, "pk": int(row['id']), "fields": row}
            del row['id']
            to_add['fields'] = row
            res.append(to_add)

    with open(json_file, "w", encoding='utf-8') as jsf:
        jsf.write(json.dumps(res, ensure_ascii=False))


# convert_file_ads(DATA_ADS, "ads.ad", JSON_ADS)
convert_file_categories(DATA_CAT, "ads.categories", JSON_CAT)
