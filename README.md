This is bugfix-flask-client for flask project's.
VERSION 0.0.1

Installation:

1) pip install git+https://github.com/6JluH4uk/bugfix-flask-client.git

2) Add to admin Flask-admin:

class BugFixModelView(ModelView):
    form_overrides = dict(status=SelectField)
    form_args = dict(
        status=dict(
            choices = [(u'0', u'Поставлена'),
                       (u'1', u'Проверка'),
                       (u'2', u'Отменена'),
                       (u'3', u'Выполнена'),
                       (u'4', u'Удалена'), ]
        ))

...

admin.add_view(BugFixModelView(BugFix, db.session))

3) Add in config.py:

BUGFIX_URL =" http://your-bugfix-server-url/load/"
BUGFIX_PROJECT = "your_project_name"
