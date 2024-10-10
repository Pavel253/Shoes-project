#!/bin/bash

# Путь к вашей папке с Django-проектом
cd ../
source venv/bin/activate
cd django
# Запускаем Django сервер
python manage.py runserver 

# Возвращаемся в папку с React-приложением
cd ../react

# Запускаем React приложение
npm start
