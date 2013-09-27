{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}


LICENSE: BSD

Deployment
------------

    heroku create
    heroku addons:add heroku-postgresql:dev
    heroku addons:add pgbackups
    heroku addons:add sendgrid:starter
    heroku addons:add memcachier:dev
    heroku pg:promote HEROKU_POSTGRESQL_<COLOR>_URL

    heroku config:add CACHE_URL=locmem://
    heroku config:add DJANGO_AWS_ACCESS_KEY_ID=...
    heroku config:add DJANGO_AWS_SECRET_ACCESS_KEY=...
    heroku config:add DJANGO_AWS_STORAGE_BUCKET_NAME=...
    heroku config:add DJANGO_CONFIGURATION=Production
    heroku config:add DJANGO_CSRF_COOKIE_SECURE=False
    heroku config:add DJANGO_DEBUG=False
    heroku config:add DJANGO_SECRET_KEY=...
    heroku config:add DJANGO_SECURE_SSL_REDIRECT=False
    heroku config:add DJANGO_SESSION_COOKIE_SECURE=False

    git push heroku master

    heroku run python {{cookiecutter.repo_name}}/manage.py syncdb --noinput --settings=config.settings
    heroku run python {{cookiecutter.repo_name}}/manage.py migrate --settings=config.settings
    heroku run python {{cookiecutter.repo_name}}/manage.py collectstatic --settings=config.settings

_Note:_

* I had issues dealing with memcache on heroku so I gave up due to time contraints and decided to just use locMem caching.
* Also, wanted to use dj-static for serving assets but could not get that working either [see issues]()
* Just stuck with AWS since I already had it. Unless you are using SSL, keep the SECURE-type settings set to false.


### Run this script: (TODO - automate this)

    heroku run python <app>/manage.py shello --settings=config.settings

    from django.contrib.sites.models import Site
    site = Site.objects.get()
    site.domain = "{{cookiecutter.domain_name}}"
    site.name = "{{cookiecutter.project_name}}"
    site.save()
