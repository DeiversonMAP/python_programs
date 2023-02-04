import random

from faker import Faker

# https://hackernoon.com/how-to-create-dummy-data-in-python-lpn37x1

# Passar como argumento localização de onde deve vir o dado falso
# https://faker.readthedocs.io/en/master/locales.html
fake = Faker('pt_BR')
for i in range(200):
    profile= fake.profile()
    name=profile['name'].split(' ')
    print(f"""('{name[0]}','{' '.join(name[1:])}','99999999999','{profile['mail']}','{fake.date_time()}','{fake.text()}',{random.randint(1,3)})""", end=',\n')
    print()
