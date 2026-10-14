simple_dict = {"user":"john doe","id": 101}

# INDEXING DOES NOT WORK ON DICTS
#print(simple_dict["user"])

complex_dict_1 = {"name":"john","permissions":["read","write","execute"]}
#print(complex_dict_1['permissions'][1])

complex_dict_2 = {"name": "jane","data": {"location": "USA","job": "developer"}}
print(complex_dict_2['data']['job'])