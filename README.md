# Setting up the python environment

Before running any python specific commands, we need to be sure
we're using the right (sandboxed) python

    $ C:\r3
    $ Scripts\activate
    $ cd r3
    $ python manage.py <command>

Usual commands of interest are:

* runserver - start the webserver at http://127.0.0.1:8000
* shell - open up a python shell with access to your django project (via `import models ...`)
