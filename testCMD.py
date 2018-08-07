import os

cmd1 = 'd:&&cd mysite/mysite&&python manage.py runserver 8080'
info = os.system(cmd1)
print(info)

