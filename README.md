# Building_Safety_System

# Installation instructions 
For beginning you have to install Python3+
In terminal write down following command:
```shell
git clone https://github.com/Lebwa1337/Building_Safety_System.git
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Groups will be added after you run migrations. To set roles, go to admin page: localhost:8000/admin/


Also for testing you can load already prepared data:
```shell
python manage.py loaddata data_fixture.json
```
Fixture only contains 2 buildings, 3 entrance and 2 apartments. Apartments are only in the entrance number 5

To create admin user use this
```shell
python manage.py createsuperuser
```

