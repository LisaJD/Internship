observation = {'client': [{150: 0, 39:0}],
                'exchange':[] } #dict inside dict
expectation = {'client': [{150: 0}],
                'exchange':[] }

def check(expectation, observation):
    if expectation['client'] != []:
        x = expectation['client'][0]
        y = observation['client'][0]
        for key, value in x.items():
            if key in y and value == y[key]:
                continue
            else:
                return 0
    if expectation['exchange'] != []:
        a = expectation['exchange'][0]
        b = observation['exchange'][0]
        for key, value in a.items():
            if key in b and value == b[key]:
                continue
            else:
                return 0
    return 1



