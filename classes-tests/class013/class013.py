# Test for learning how to use hashlib.sha256
from hashlib import sha256
from rich import print


password = 'Heart@'
cod = password.encode('utf-8')
password_hash = sha256(cod).hexdigest()
print(password_hash)
print()

user = str(input('Enter password: '))

if sha256(user.strip().encode('utf-8')).hexdigest() == password_hash:
    print('[green]Valid Password![/]')
else:
    print('[red]Invalid Password![/]')
