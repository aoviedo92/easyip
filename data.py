data_json = 'data'


def save_file():
    # json_ = json.dumps(dict_, sort_keys=True, indent=4 * ' ')
    f = open(data_json, 'w')
    f.write(str(dict_))
    f.close()


def del_data(id_):
    load_data()
    config = dict_['config']
    ctrl = False
    for list_ in config:
        if id_ in list_:
            dict_['config'].remove(list_)
            ctrl = True
            break
    save_file()
    return ctrl


def load_data():
    try:
        f = open(data_json, 'r')
        dict__ = dict(eval(f.read()))
        f.close()
        dict_['config'] = dict__['config']
        dict_['options'] = dict__['options']
        # return json.loads(json_)
    except IOError:
        # dict_ = {'config': [], 'opt': [False, '255.255.255.0', False, '10.0.0.3']}
        save_file()
    return dict_


def save_data(id_, ad, nm, ip, ms, gw='', dns=''):
    load_data()
    dict_["config"].append([id_, ad, nm, ip, ms, gw, dns])
    save_file()


def save_options(options):
    load_data()
    dict_['options'] = options
    save_file()

dict_ = dict()
dict_['config'] = []
dict_['options'] = [False, '255.255.255.0', False, '10.0.0.3', 6]

# save_data(45, 'adapter name', 'ip', 'mask')
# del_data(45)