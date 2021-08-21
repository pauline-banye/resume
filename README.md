> # Resume

> ## Table of contents
* [Project Overview](#project-overview)
* [Project Features](#project-features)
* [Technologies for Backend](#technologies-for-backend)
* [Setting up the project](#setup)
* [Setting up the PostgreSql Database](#setting-up-the-postgresql-database)
* [Contact](#contact)
#
>## Project Overview
<p align="justify">
Resume app is an interactive personal resume. It outlines my work experience, education, skills and a few more sections.
</p> 

<p align="justify">
The site also provide an option where you can contact me for enquiries.  
</p>

Link to deployed site - https://paulineresume.herokuapp.com/

![site image](https://drive.google.com/uc?export=view&id=1sIjWflNn7nQI1laEEaxzFMJRec9dmBSD)

#
> ## Project Features
- Interactive Resume

- Functional contact page to send emails using gmail server.

- Links to portfolios and samples provided

- Links to internship institutions

</p>

#
> ## Technologies

<p align="justify">
*Note: This project was setup and developed on a system running Windows 10. The stacks used for the project backend include:
</p>


| <b><u>Stack</u></b> | <b><u>Usage</u></b> |
| :---         | :---         |
| **`Python 3.9`** | Programming language. |
| **`Django`** | General backend |
| **`HTML`** | Templates. |
| **`CSS`** | Templates. |
| **`Javascript`** | Templates. |


> ## Setting up the project
<p align="justify">
The first step requires the download and installation of Python 3.9 and a check to confirm that pip and the necessary dependencies are properly installed.
</p>

<p align="justify">
After the installation of the Python program, setup the project environment with pip and virtualenv in the command prompt, powershell or gitbash terminal. Virtualenv helps to create an isolated Python environment containing all the packages necessary for the project.
</p>

*Note: 
- This project was setup using the gitbash terminal. Some of the commands used do not work with command prompt or powershell.
- If a "pip command not found error" is encountered, download get-pip.py and run `phython get-pip.py` to install it. 

```bash
# pip install virtualenv
```

Navigate to the resume-project folder and run `virtualenv folder-name` to create a virtual environment folder.

Activate the environment by running the following command in the gitbash terminal.


```bash
# source folder-name/scripts/activate
```

<p align="justify">
Once the virtual environment is active, the next step is the Django installation. Django is an open source Python web application framework thats helps with the rapid development of secure websites.
</p>

```bash
# (venv) pip install django
```
<p align="justify">
After installing Django, install all the necessary dependencies for the project. A few of them are listed below.
</p>
 


| <b><u>Modules</u></b> | <b><u>Usage</u></b> |
| :---         | :---         |
| **`gunicorn`** | WSGI HTTP server |
| **`psycopg2`** | PostgreSQL database adapter |
| **`whitenoise`** | Static files |
| **`django-environ`** | Environment configuration |

An exhaustive list can be found in the requirements.txt file included in this project. The modules can be 'batch installed' using the following command.

```bash
# (venv) pip install -r requirements.txt
```


#
> ## Setting up the PostgreSQL Database

<p align="justify">
Django's default database is Sqlite3 and it was used in the local development stage of this project. PostgreSQL is an object relational database with features for the safe storage and scaling of complicated data workloads hence decision to utilize it for the deployment of this project.
</p>


The method used for this project involved the download and installation of the **dj-database-url module** using the command *`pip install dj-database-url`* and the configuration of the settings.py file located in the resume_project folder.


<p align="justify">
This module provides a Django database connection dictionary, populated with all the data specified in your URLs. This is especially useful for deployment on sites like Heroku
</p>

To setup, simply import the module using `import dj_database_url` at the top of the document and configure your database as shown below.

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3")),
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
```

> ## Status
This project is in progress. 

#
> ## Contributing to the project

If you find something worth contributing, please fork the repo, make a pull request and add valid and well-reasoned explanations about your changes or comments.

Please note:

- `It should be inviting and clear.`

- `Any additions should be relevant.`

- `It should be easy to contribute to.`

Urls marked **\*** are temporarily unavailable. Don't delete it without confirming that it has permanently expired.

Before adding a pull request, please remember:

```bash
This repository is not meant to contain everything. Only good quality verified information.
```

All **`suggestions`** are welcome!


#
> ## Contact me

Pauline Banye
- Email - paulinebanye@gmail.com
- GitHub - https://github.com/pauline-banye

#
> Readme created by Pauline Banye

