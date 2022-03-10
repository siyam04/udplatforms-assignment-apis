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
![venv](https://user-images.githubusercontent.com/23103980/157701305-be623108-19ae-4882-a657-d3bf35159be2.png)

* Install project requirements
``` 
pip3 install -r requirements.txt
```
![requirements](https://user-images.githubusercontent.com/23103980/157701530-64d5e4b2-007e-4372-9638-0fd73ef41276.png)

* Create the database
``` 
python manage.py makemigrations
```
``` 
python manage.py migrate
```
![db-1](https://user-images.githubusercontent.com/23103980/157701755-c27dac76-c883-4ead-bbb3-52ec154c96ba.png)

* Create the superuser (admin) & provide credentials
``` 
python manage.py createsuperuser
```
* Start the local server
``` 
python manage.py runserver
```
* If everything worked, http://127.0.0.1:8000 will show the root page

![root](https://user-images.githubusercontent.com/23103980/157701935-919020b4-f748-429a-86cf-3476b8f9c914.png)

* You can now access the administrative area at, http://127.0.0.1:8000/admin

![admin-01](https://user-images.githubusercontent.com/23103980/157702075-0aa4de0e-8efd-40a7-a5fb-0e021850b6cf.png)

* Generate fake dummy data
``` 
python fake_data.py
```
![faker](https://user-images.githubusercontent.com/23103980/157702177-fe27c2bb-2e22-43bc-85a3-734127f9e05e.png)

* Run test cases (Unit Testing)
``` 
python manage.py test
```
>> Success

![test-case](https://user-images.githubusercontent.com/23103980/157743875-344eb440-fb0a-4205-88df-f8e3d4369008.png)

>> Failed

![test-case-F](https://user-images.githubusercontent.com/23103980/157744032-f5f27796-1924-49ea-bf7d-8c30bac3b734.png)


