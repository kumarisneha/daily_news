Link for the README.rst:
https://gist.github.com/kumarisneha/9e23d2115145c0bc9f2e6adf3e986454

Installing Dependencies
***************************
1.Install virtual environment using:
::

    $ sudo pip install virtualenv

2.Create a directory ``virtual`` inside which you will have one virtual environment.

The following commands will create an env called ``assign_env`` :
::

    $ cd virtual
    $ virtualenv assign_env
3.Now activate the ``assign_env`` environment using:
::

    $ source assign_env/bin/activate
    (assign_env)[user@host]$

Setting the project
***************************
1.Run the command in your virtual environment.
::

    $ cd /path/to/janitriproj
    
2. Install the requirements using: 
::

    $ pip install -r requirements.txt

Running the code
***************************
run this command:
::

    $ python manage.py runserver    
You will get something like the following on running the above code −
::

    Performing system checks...

    System check identified no issues (0 silenced).
    May 24, 2017 - 02:46:08
    Django version 1.11, using settings 'janitriproj.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
Now open your browser and enter this address:    
::

   http://127.0.0.1:8000/

Updating news data by celery
******************************
open two new terminal at the project root in your virtual environment and run this command:
::

    $ celery -A janitriproj worker -l info 
    $ celery -A janitriproj beat -l info 
