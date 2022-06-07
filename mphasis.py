input_1 = {
    "devices": {
        "1": {
            "name": "lenovoZ570",
            "ip": "1.1.1.1"
            },
        "2": {
            "name": "iphone12",
            "ip": "1.1.1.2"
            },
        "3": {
            "name": "iphone10",
            "ip": "10.11.1.20"
            }
        }
}
#print(input_1["devices"]["1"]["name"])


new_dict=dict(list(input_1.values())[0])
print(new_dict)
#my_dict=dict(new_dict[0])
#print(type(my_dict))
#lst=list(my_dict.values())
#print(lst[0])



  


# {'1': {'name': 'lenovoZ570', 'ip': '1.1.1.1'}, '2': {'name': 'iphone12', 'ip': '1.1.1.2'}, '3': {'name': 'iphone10', 'ip': '10.11.1.20'}}

