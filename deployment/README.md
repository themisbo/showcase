# Deployment with Flask (in Windows 10 with cmd)

## Install the virtualenv package
  
   ```sh
   python -m pip install virtualenv
   ```

## Create a folder for the project

   ```sh
   mkdir deployment
   cd deployment
   ```

## Create a virtual environment

   ```sh
   python -m virtualenv env
   ```

## Activate the virtual environment

   ```sh
   env\Scripts\activate.bat
   ```

## Install python packages


   ```sh
   pip install -r requirements.txt
   ```

## Set-up Flask environmental variables and run the app

   ```sh
   set FLASK_APP=server.py
   set FLASK_ENV=development
   flask run
   ```

Copy the URL and paste it into a browser, typically:

   ```sh
   http://127.0.0.1:5000/
   ```
Once done, we should also deactivate the virtual environment

   ```sh
   deactivate
   ```
