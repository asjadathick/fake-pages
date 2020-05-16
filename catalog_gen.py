from faker import Faker
from string import Template
fake = Faker()

pages_required = 1000000
template = open('catalog.template.html')
src = Template(template.read())

def write_file(filename, data):
    f = open(filename, "w")
    f.write(data)
    f.close()

for i in range(1,pages_required):
    d = {
        'number': i,
        'name': fake.name(),
        'address': fake.address(),
        'description' : fake.text(),
        'prod': 't-shirt',
        'next': "item-" + str(i+1) + ".html"
    }
    write_file('catalog/item-' + str(i) + ".html", src.substitute(d) )
    print(f"Wrote file {i}")

template = open('catalog-index.html')
src = Template(template.read())

list_items = ""

for i in range(1,pages_required):
    list_items += "<li><a href='item-" + str(i) + ".html'>Item " + str(i) + "</a></li>\n"

d = {'list': list_items}

write_file('catalog/index.html', src.substitute(d))
print("Wrote index")