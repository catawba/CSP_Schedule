# This us used to tweak the database when changes are needed
from tinydb import TinyDB,Query
db = TinyDB('conflict.json')



myClass = Query()


db.update({'conflict': 'Larsen_C_Plan_AD1'}, myClass.conflict == 'Larsen_C_Plan_AD')
for item in db.search(myClass.name == 'Larsen_C_Plan_AD'):
    print(item)

#db.search(User.name.matches('[aZ]*'))

for item in db.search(myClass.conflict == 'Larsen_C_Plan_AD'):
    print(item['name'],item['conflict'])