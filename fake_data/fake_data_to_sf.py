import random

from faker import Faker

# https://hackernoon.com/how-to-create-dummy-data-in-python-lpn37x1

# Passar como argumento localização de onde deve vir o dado falso
# https://faker.readthedocs.io/en/master/locales.html
fake = Faker('pt_BR')
with open('teste.csv', 'w') as arquivo:
    arquivo.write("Name,External_Id__c") 
    arquivo.write('\n')
    for i,u in enumerate(range(20898)):  
        profile= fake.profile()
        name=profile['name']
        # print(f"""('{name[0]}','{' '.join(name[1:])}','99999999999','{profile['mail']}','{fake.date_time()}','{fake.text()}',{random.randint(1,3)}, {u+1})""", end=',\n')
        # print()
        data=f"{name},{u+1}" 
        arquivo.write(data)
        arquivo.write('\n')
