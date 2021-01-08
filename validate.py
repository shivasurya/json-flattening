def flatten_json(y):
    output = {}

    def flatten(jsonObject, name=''):
        if type(jsonObject) is dict:
            for a in jsonObject:
                if type(jsonObject[a]) is dict:
                    flatten(jsonObject[a], name + a + '.')
                elif type(jsonObject[a]) is list:
                    flatten(jsonObject[a], name + a)
                else:
                    flatten(jsonObject[a], name + a + '.')
        elif type(jsonObject) is list:
            output[name] = []
            for a in jsonObject:
                if type(a) is dict:
                    result = flatten_json(a)
                    output[name].append(result)
                else:
                    output[name] = jsonObject
        else:
            output[name[:-1]] = jsonObject

    flatten(y)
    return output

sample_object = {'Name':'John', 'Location':{'City':'Los Angeles','State':'CA'}, 'hobbies':['Music', 'Running']}
sample_object2 = {
    "App": {
        "Name": "Words with Friends",
        "BundleID": "com.zynga.words",
        "Categories": [1, 3, 15]
    },
    "Device": {
        "OS": "Android",
        "OSVersion": "Jellybean"
    },
    "AdSlots": [
        {
            "Type": "Banner",
            "Size": "320x50",
            "Position": "0",
            "PrivateDeal": {
                "PriceCPM": 2.2,
                "AuctionType": 1,
                "ID": "abc"
            }
        },
        {
            "Type": "video",
            "Size": "320jsonObject50",
            "Position": "1",
            "Duration": 15
        }
    ]
}

flat = flatten_json(sample_object2)
print(flat)