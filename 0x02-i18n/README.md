# 0x02-i18n
Creating a language and time responsive backend on a simple flask App

## 0-app.py, templates/0-index.html
Set up a simple webpage to be delivered vai th flask app

## 1-app.py
Add babel from flasbable to the app with a Config

## 2-app.py
Create a get_locale func to determine best match with suppported languages

## 3-app.py
Create dictionaries for the supported languages and add a translation

## 4-app.py
Force the desired locale using a URI key(locale) value

## 5-app.py
Mock a database(JSON) of users to display webpage in diff languages based on user prefferred locale as stored in the DB

## 6-app.py
Change get_locale function to use a user’s preferred local if it is supported

## 7-app.py
Define a get_timezone function and use the babel.timezoneselector decorator