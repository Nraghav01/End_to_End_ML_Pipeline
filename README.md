# End_to_End_ML_Pipeline
This repository has an end to end machine learning operation using the MLOps pipelines.
Link to Source Git repositories: https://github.com/entbappy/End-to-End-Machine-Learning-Pipeline

# End-to-End-Machine-Learning-Pipeline


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-End-Machine-Learning-Pipeline
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```
src/{project_name}/__init__.py -> Makes the src/{project_name} directory a proper Python package, allowing its modules to be imported elsewhere in the project.
src/{project_name}/components/__init__.py -> Makes the components directory a package. This directory typically holds individual, reusable building blocks of the MLOps pipeline (e.g., data ingestion, model training, evaluation).
src/{project_name}/utils/__init__.py -> Makes the utils directory a package.
src/{project_name}/utils/common.py -> Contains general utility functions that are used across different parts of the project (e.g., helper functions for reading configuration files, saving data, etc.).
src/{project_name}/config/__init__.py -> Makes the config directory within the source package a package.
src/{project_name}/config/configuration.py -> This is often where you define classes or functions to read and manage the configuration files (config.yaml, params.yaml, etc.) programmatically.
src/{project_name}/pipeline/__init__.py -> Makes the pipeline directory a package. This is where you define the sequential steps of your MLOps workflow (e.g., a data training pipeline, an inference pipeline).
src/{project_name}/entity/__init__.py -> Makes the entity directory a package.
src/{project_name}/entity/config_entity.py -> Defines data classes or entities (often using dataclasses in Python) that structure and validate the configuration parameters used throughout the project. This enforces type safety and clarity.
src/{project_name}/constants/__init__.py -> Stores project-wide constants (e.g., file paths, magic numbers, environment variable names).
config/config.yaml -> The main configuration file, typically storing high-level settings, file paths, and environment-specific parameters.
params.yaml -> Stores hyperparameters or specific parameters for experiments and models, separate from general configuration settings [1].
schema.yaml -> Defines the expected schema or data contract for your data (e.g., column names and data types), ensuring data integrity throughout the pipeline [1].
main.yaml -> An entry point file, likely used to run the main training pipeline or specific application logic (though main.py or app.py is more common in Python projects).
app.yaml -> An entry point file, likely used to run the application/service logic (e.g., a Flask/FastAPI app).
requirements.txt -> Lists all the necessary Python dependencies and their versions needed to run the project.
setup.py -> A script used to package the src/{project_name} directory as an installable Python library (e.g., via pip install .), making the code reusable and manageable.
research/trails.ipynb -> A Jupyter notebook used for initial data analysis, rapid prototyping, and tracking experimental ideas before formalizing them into the main codebase.
templates/index -> This appears to be a directory (templates) with an index file inside. This is typical for web application development (e.g., Flask/Django), where templates/index.html would be an HTML template for the main page.

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
python app.py
```



# AWS-CICD-Deployment-with-Github-Actions
## Make a file named "Docketfile" and add initial docker code there
## MAke a folder named ".github" for github actions - add a folder named "workflows" and under that folder add a file named cicd.yaml
## 1. Login to AWS console. 

## 2. Create IAM user for deployment -  give access to user AmazonEC2ContainerRegistryFullAccess  and  AmazonEC2FullAccess

 -> #with specific access

 -> Create ECR repository on AWS

 -> 1. EC2 access : It is virtual machine

 -> 2. ECR: Elastic Container registry to save your docker image in aws: ECR repository URI: 737247133896.dkr.ecr.ap-south-1.amazonaws.com/wine-ml-cicd-project

 -> #Description: About the deployment

 -> 1. Build docker image of the source code

 -> 2. Push your docker image to ECR

 -> 3. Launch Your EC2 

 -> 4. Pull Your image from ECR in EC2

 -> 5. Lauch your docker image in EC2

 -> #Policy:

 -> 1. AmazonEC2ContainerRegistryFullAccess

 -> 2. AmazonEC2FullAccess

 -> 
## 3. Create ECR repo to store/save docker image
    - Save the URI: 737247133896.dkr.ecr.ap-south-1.amazonaws.com/wine-ml-cicd-project

 -> 
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
 -> 
 -> Connect top the Ubuntu EC2 instance created - Update the ubntu machine - Install the docker in the machine
 -> #optinal

 -> sudo apt-get update -y

 -> sudo apt-get upgrade
 -> 
 -> #required

 -> curl -fsSL https://get.docker.com -o get-docker.sh

 -> sudo sh get-docker.sh

 -> sudo usermod -aG docker ubuntu

 -> newgrp docker
 -> 
# 6. Configure EC2 as self-hosted runner: 
    setting>actions>runner>new self hosted runner> choose os> then run command one by one
    Self hosted runner - connect EC2 with Github, so that when we update any new code pushing to github, it will also automatically get updated tro the EC2 machine
    Run the 4 "Download" commands from the Git repositoru - Actions - Self-hosted runners - Linus machine
    Run the 1st Configure command
    Runner group - just click enter | Na,e of Runner: pick from cicd.yaml[Continuous-Deployment][runs-on] - self-hosted
    Run the 2nd configure command - ./run.sh - this command starts the runner

# 7. Setup github secrets: Go to github repository - secrets and variables - Actions - Create Repositoryt secret
     This is doe to protect sensitive information - we will create a secret in github for the below AWS credentials

    AWS_ACCESS_KEY_ID= ID downloaded from the IAM role

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = ap-south-1

    AWS_ECR_LOGIN_URI = demo>>  737247133896.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = wine-ml-cicd-project

#8. Doing Port mapping for the App - Before doing this when I copy the public IP address of my EC2 instance and run it no application appears
  -> Before port mapping the port mentioned in app.py is port = 8080
  -> To be port mapping do following:
    - Go to EC2 instance - Security - Security group - Edit Inbound rules
    - Inside Edit Inbound Rules - Add rule - Custom TCP - Port range 8080 - Source 0.0.0.0/. - save rule
    - Copy public IP of EC2 instance, in the browser add 8080 in the link after public IP and run the app
    