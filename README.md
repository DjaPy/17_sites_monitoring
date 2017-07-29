# Sites Monitoring Utility

The script checks the "health" 

The script returns:
1. The status of the website.
2. How many subscription expires.

The program uses the library [python-whois](https://bitbucket.org/richardpenman/pywhois).

# HowTo

To run the script you need python 3.5(and later), Linux.

Use Venv or virtualenv for insulation project.
Virtualenv example:

```
$python virtualevn myenv
$source myenv/bin/activate
```
Install requirements:

```
pip install -r requirements.txt
```
if you have error, you need enter `sudo` before command.

An example of running

```
Website:  http://juniorpythonblog.com
Status:  200
Until the date of expiry of: 9 months
==================================================
Website:  http://yandex.ru
Status:  200
Until the date of expiry of: 2 months
==================================================
Website:  http://google.com
Status:  200
Until the date of expiry of: 38 months
==================================================
Website:  http://vk.com
Status:  200
Until the date of expiry of: 10 months
==================================================
Website:  http://stackoverflow.com
Status:  200
Until the date of expiry of: 6 months
==================================================

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
