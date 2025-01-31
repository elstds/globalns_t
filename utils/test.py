response = {'uuid': 'a0915be7-1b22-43e7-a6df-0d961de599d5'}
response1 = {'uuid': ''}
response2 = {}
if response['uuid']:
    print(1)
else:
    print(0)
if response1['uuid']:
    print(1)
else:
    print(0)
if response2.get('uuid'):
    print(1)
else:
    print(0)