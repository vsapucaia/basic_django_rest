Django Basic REST boiler plate
=======

Just a template to easily init a Django endpoint with minimal requirements

### Testing Django translate API

- enable django manage.py terminal with CTRL+ALT+R
- runserver
- check URL http://127.0.0.1:8000/translate/
- paste content of app/core/json_examples/test1.json
- post
- check the database again

### Check code with PyLint



```commandline
# generic
pylint ./app
```

```commandline
# django-pylint
pylint --load-plugins pylint_django --load-plugins pylint_django.checkers.db_performance ./app
```
