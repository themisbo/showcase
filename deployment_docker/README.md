# Deployment with docker (in Windows 10 with cmd)

This is part of the showcase.

## Install the virtualenv package
  
   ```sh
   python -m pip install virtualenv
   ```

## Create a folder for the project

   ```sh
   mkdir deployment_docker
   cd deployment_docker
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

## Build and run the docker image


   ```sh
   docker build -t palmer-docker .
   docker run -p 8000:8000 palmer-docker
   ```

Copy the following URL and paste it into a browser:

   ```sh
   http://localhost:8000/
   ```
Once done, we should also deactivate the virtual environment

   ```sh
   deactivate
   ```
