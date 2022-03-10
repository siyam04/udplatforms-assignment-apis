## UDPlatforms Assignment APIs

* Python Version 3.8.10
* Django Version 4.0.3
* Database: SQLite3 (default)
* Developed by Django REST Framework (Version 3.13.1)

> Django follows the Model View Template (MVT) architecture. <br>
> Model = Database, View = Controller, Template = Rendering
---

### Installation and Running
> Commands may differ depending on OS. I'm using Ubuntu 20.04 LTS

* [Python Installation Guide](https://wiki.python.org/moin/BeginnersGuide/Download)

* Clone the repository
``` 
git clone https://github.com/siyam04/udplatforms-assignment-apis.git
```
* Go to the repository directory
``` 
cd udplatforms-assignment-apis
```
* Create virtual environment using python
``` 
python3 -m venv myenv
```
* Activate virtual environment
``` 
source myenv/bin/activate
```
![](../venv.png)

* Install project requirements
``` 
pip3 install -r requirements.txt
```
![](../requirements.png)

* Create the database
``` 
python manage.py makemigrations
```
``` 
python manage.py migrate
```
![](../db-1.png)

* Create the superuser (admin) & provide credentials
``` 
python manage.py createsuperuser
```
* Start the local server
``` 
python manage.py runserver
```
* If everything worked, http://127.0.0.1:8000 will show the root page

![](../root.png)

* You can now access the administrative area at, http://127.0.0.1:8000/admin

![](../admin-01.png)

* Generate fake dummy data
``` 
python fake_data.py
```
![](../faker.png)


