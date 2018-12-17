# SnackBar
This is a web app for a digital coffee list hosted on an IPad.

It is based on CoffeeList from "duscheln": https://github.com/duscheln/CoffeeList
and based on SnackBar from "clemenstyp": https://github.com/clemenstyp/SnackBar
# Installation
## Manual
1. Install the pip requirements as denoted in requirements.txt and the missing python-packages.
```
apt-get install python-psycopg2 python-flask python-flask-sqlalchemy python-tablib python-numpy python-schedule python-requests python-werkzeug python-jinja2 python-click python-itsdangerous python-sqlalchemy
pip install --user -r requirements.txt
```
2. You can change the userList.csv as shown in the template. These users will be imported, when a database is created. You can add or remove useres at a later time
3. Standard items will be created at start. You can change the price and names in the admin panel later.
4. To start the SnackBar with the folowing command:
```
python SnackBar.py
```
5. you can add --port and --host to change port and host.
```
python SnackBar.py --host 0.0.0.0 --port 8000
```
6. The initial username and password for the admin interface are:
```
username: admin
password: admin
```
7. you can change the password in the "Admins" section.
## Automatic
1. Install the Debian-Package
```
dpkg -i amd64-snackbar_0.8-0.deb
```
2. Start the software
```
service snackbar start
```
# Screenshots
![alt tag](https://github.com/blubbfish/SnackBar/raw/master/screenshots/overview.png)
![alt tag](https://github.com/blubbfish/SnackBar/raw/master/screenshots/buy.png)
![alt tag](https://github.com/blubbfish/SnackBar/raw/master/screenshots/user.png)
![alt tag](https://github.com/blubbfish/SnackBar/raw/master/screenshots/bill.png)