def write(settings, file='settings.json'):
    import json
    
    myJSON = json.dumps(settings)

    with open(file, "w") as f:
        f.write(myJSON)


def update(key, newfig, file='settings.json'):
    import json

    with open(file, "r") as f:
        data = json.load(f)
        f.close()

    data[key] = newfig
    with open(file, "w") as f:
        myjson = json.dump(data, f)

        f.close()

def read(key='all', file='settings.json'):
    import json
    if key == 'all':

        with open(file, "r") as f:
            data = json.load(f)

        f.close()
        return data
    else:
        with open(file, "r") as f:
            data = json.load(f)

        f.close()
        return data[key]
