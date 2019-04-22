import re


def parseInt(text):
    return re.findall(r'\d+',text)


product_count_text = "381 Products found"
product_count_int = int(parseInt(product_count_text)[0])
print(product_count_int)


