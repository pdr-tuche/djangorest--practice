import requests

response = requests.get('http://localhost:8000/api/{}'.format('livrarias/'))

data = response.json()
print(type(data))
print (response.status_code, data)


for elem in data:
    livro_jhen_id = []
    if elem['nome'] == 'Jhennyfer':
        jhen_id = elem['id']
        for items in elem['livro']:
            livro_jhen_id.append(items)

for item in livro_jhen_id:
    response2 = requests.get('http://localhost:8000/api/livros/{}'.format(item))
    response_data = response2.json()
    print(response_data)
    print(f'livro de id {response_data["id"]} : {response_data["titulo"]}')

print(f"id da jhen = {jhen_id}, ids do livro = {livro_jhen_id}")
