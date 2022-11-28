# Я дико извиняюсь, но нет.
# Яндекс практически каждый проект даёт мне новую репу с дефолтными файлами,
# и каждый раз шариться по стандартным файлам Джанго
# выискивая и удалая дефолтные комменты и докстринги для прохождения ревью
# это не совсем то, чем мне хочется (и вообще нужно) сейчас заниматься
# Замечание принял к сведению, по поводу поддержания чистоты к коде в курсе.

"""
WSGI config for yatube_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatube_api.settings')

application = get_wsgi_application()
