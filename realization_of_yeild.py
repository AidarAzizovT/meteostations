import pandas
from data.kuzaikino_nurlat import kuzaikino_nurlat
from meteostations_updated import set_roof, TITLES


def to_dict(data):
    result = dict()
    key = generate_keys_in_children(data)
    while k:=next(key) is not None:
        if k not in ("element_id", "source"):
            result[k] = result.get(k, []) + [element[k]]


def generate_keys_in_children(data):
    for element in data['data']:
        for key in element.keys():
            yield key
    yield None


result = to_dict(kuzaikino_nurlat)
result = set_roof(result)
pandas.DataFrame(result).drop_duplicates().to_excel("kuzaikino_nurlat_final.xlsx", index=False)
