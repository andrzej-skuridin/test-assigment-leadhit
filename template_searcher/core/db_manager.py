from tinydb import TinyDB, Query

db_templates = TinyDB('db_templates.json')

# db_templates.insert({
#     'name': 'T Email',
#     'fields': [{'contact_email': 'email'}],
# })
# db_templates.insert({
#     'name': 'T Email + Telephone',
#     'fields': [{'contact_email': 'email'}, {'contact_number': 'telephone'}],
# })
# db_templates.truncate()
# db_templates.insert_multiple([
#     Document({'name': 'John', 'age': 22}, doc_id=12),
#     Document({'name': 'Jane', 'age': 24}, doc_id=14),])
#print(db_templates.all().sort())
# db_templates.truncate()
# q = Query()
# result = db_templates.search(Query().fragment({'bio': 'text'}))
# print(result)
