import requests

year = 2015
day = 1

with open('sessioncookie.txt') as f : 
    session_cookie = f.read()

print(session_cookie)
response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input',cookies={'session':f'{session_cookie}'})
print(type(response))
print(response)
print(response.content)
