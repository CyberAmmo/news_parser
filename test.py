import json

with open("news_dict.json", encoding='utf-8') as f:
    art_dict = json.load(f)

search_id = 'nomer-3066'

if search_id in art_dict:
    print("Новость уже есть")
else:
    print("Свежая новость")