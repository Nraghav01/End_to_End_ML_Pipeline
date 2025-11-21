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

## 1. Login to AWS console.

## 2. Create IAM user for deployment

 -> #with specific access

 -> 1. EC2 access : It is virtual machine

 -> 2. ECR: Elastic Container registry to save your docker image in aws


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
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/winerepo

 -> 
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
 -> 
 -> 
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


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
