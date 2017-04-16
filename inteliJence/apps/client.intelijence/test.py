#test bot for running through api streams
#yup that is it


from requests import put,get

print put('http://localhost:9000/todo1', data={'name': 'Remember the milk'}).json()
print get('http://localhost:9000/hello').json()