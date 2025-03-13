# Implementation Detail's 

 I feel like it would be interesting if I just Deploy what I learnt through the process of learning Agentic AI. Here is a complete detailed approach if someone wants to deploy Agentic ai applications on to cloud in my case (AWS). I have documented it so that it will be lot helpful for me in the future as well as for someone who wants to research on this.

  So I used modular coding techniques( Making every function as a supporter Python file and importing when required) to integrate all functions in the case of Agentic AI Tools, Agent's, Building graphs etc.. made individual Python files and imported it according to the requirements. It made a lot of tasks easy in terms of debugging and Clarity of code.
  

> ## **Steps I followed**
> 1. Building and Testing a Fast API Application
>  2. Writing the Docker File
>  3. Building a Docker image and Docker Container Testing it on Local System
>  4. CI pipeLine code
>       > 1. Log in to Docker Hub
>       > 2. Automating Building Docker image for every commit
>       > 3. Pushing to Docker Hub
>  5. CD pipeline
>       > 1. Pull the Docker Image
>       > 2. Delete Old Container
>       > 3. Run the Container
>  6. Setting up Docker Hub
>  7. Creating EC2 Instance
>  8. Setting up Linux VM for docker
>  9. Understanding GIT and VM connection -- **Self Hosted Runners**
>  10. Running Jobs 

## **Building and Testing FastAPI**

We are using FastAPI to create our API. I have included various functionalities into one API, such as a companion bot, a Calculator bot, etc The fast api made it easy to integrate all together and create different operations with different routes. 

I implemented every functionality in a suppurate file then imported it as libraries so that there will be a ease of debugging and clear understating of code. i found out this this technique is known as modular coding. This method made my task easy to just import every functionality into one app.py(FastAPI file) then execute the functions.

First thing is that while we are giving a input to any function it checks whether it is in the required format or data type. outputs are inaccurate if not. So the input needs to be in a format that is accepted by the functions we are using. for validation of inputs we use  **PYDANTIC**

#### **PYDANTIC** :
Pydantic is a data validation and settings management library that leverages Python's type annotations to provide powerful and easy-to-use tools for ensuring our data is in the correct format.
[pydantic](https://docs.pydantic.dev/2.10/)

```python
from pydantic import BaseModel
class ChatRequest(BaseModel):
    message: str
    name: str
    thread_id: str
```

In some cases, there might be multiple requests at the same time. For handling this case, FastAPI has a unique functionality of processing it asynchronously. It is most important when we are dealing with a production-level application.
**async Def for asynchronous request processing**
```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Also, multiple connections need to be handled independently; there must not be any concurrency in between requests. This is where **UVICORN** comes into the picture. We can handle running our server with the general method, but running the  application with **UVICORN** brings a lot of advantages.

**UVICORN**:  Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server implementation for Python. It is designed to handle multiple connections and events concurrently, making it an excellent choice for serving FastAPI applications. 

**Normal run**
```
fastapi run main.py
```
**Unicorn run**
```
uvicorn main:app --host 127.0.0.1 --port 5000
```

```python
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000) 
```
Understand we are running it on ``127.0.0.1`` wich means local host port 5000

There are other alternatives [For more information, click here](https://fastapi.tiangolo.com/deployment/manually/#install-the-server-program)

[UVICORN](https://www.uvicorn.org/)

[FASTAPI Doccumentation for better detail](https://fastapi.tiangolo.com/tutorial/first-steps/)

[My fast API application](https://github.com/KoteshwarChinnolla/AgenticAi_on_production/blob/main/app.py)

## **Writing Docker File**

Till now, we just tested our code on local host port 5000, which is just tested on our system. What if we want to make the application public? What if our friend has to access it without installing any dependencies? Yes, it is possible; just use docker.

**Docker** : Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

**How can we Build ?** You can imagine creating files or installing dependencies by using commands (of ciratin format) on a fresh computer. where there is no files no Python nothing. What steps do you follow to run your code over there?

**Steps involved**
> 1. you install python
> 2. Create a working directory where your ll code will be present
> 3. Copy all your code into that directory.
> 4. Install what all the dependencies you need to run your code
> 5. then run your script.

This is what we are following to create a docker Image
**Docker Image** ? 

Everything we specified will be stored in this image. Imagine it as a mobile application on the Play Store that contains all the dependencies needed to run that app on your device. Similarly, a Docker image contains everything necessary to run a Docker container.

**Docker Container**? 

It is a runtime instance of a Docker image, providing an isolated environment for running applications. Running the application means making the requests to the fast api application. Now, imagine you're done installing the Play Store application(Creating a Docker image in our case). We can only use their functionalities when we open and make requests( Containers provide you with this environment where you can make your to the internal python codes). It is like running the API's.



I followed the doccumentation for writing the dockerfile`

(Basic format) https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/)

### ***Steps***

> 1. Create a file named Dockerfile ( it is a standard name)
> 2. First, we install Python - for that, we import a base image. Instead of installing the entire image which is huge, we use SLAM version it is docker-optimised.
 ```python
FROM python:3.12-slim
```
> 3. A folder to store your fies and run code - Working Directory
```python
WORKDIR /code
```
> 4. COPY all your required files into the Working directory
```python
COPY temp_venv.txt requirements.txt
COPY app.py app.py
COPY toolcallinglm.py toolcallinglm.py
...
```
> 5. Install all the dependencies; before that, make sure you specify your dependencies in the requirements.txt file.
```python
RUN pip install --no-cache-dir -r requirements.txt
```
> 4. Specify where you want to run and what you want to run. in our case, we just need to run app.py so that we can get our host link.
```python
EXPOSE 5000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
```
**Done. we specified what all you required to run our application**

Before building the image, install the [Docker engine](https://www.docker.com/products/docker-desktop/), which helps us to create docker images and run docker containers.

Now, we just build an image with those files and requirements. This image will further be used to run our containers.

For building image
```python
docker build -t <__name__> .
```
<__name__> Fill in the blank with the name you want.
It will take some minutes to install all the dependencies. The image we built will contain all files and dependencies, and we also mentioned what file to run. Who will run these files for this? We need containers to help us to run the docker image continuously. to run the containers.

```python
docker container run \
--name "test_container_1" -d -p 5000:5000 \
-e GROQ_API_KEY="<API_key>" -e LANG_CHAIN_API_KEY="<API_KEY>" agenticai_model
```
`-e` represents setting ENVIRONMENT variables. I pass it while the container is running as we have Secrate keys.

         
**Test the working**-- by running your container.

 Now, navigate to Docker Desktop. You will be able to see a container is in running state. Click on `5000:5000`. If it is in underlined, then the container is running. If you click on that, we navigate to a local host ```http://localhost:5000``` Just add `/docs` at the end to see the swagger UI. we are now at ```http://localhost:5000/docs``` to test our API's.

## **CLOUD DEPLOYMENTS** 

So now that we have the working container, every time we run the container, we can execute our functionalities. But understand that if you want to make others access the same link, you can't do that. Why? So it is because the container is running on the local host( that means it only running on the local computer). 

But you don't build the container only for you. You want to make it available for everyone so that they can also use your application. To make this, we need to understand the concept of the cloud. Using cloud deployment, we can actually make it available on the internet ( so that everyone can access it ). 

So How?
So we are using EC2.

EC2 is famously known for building, Deploying and Managing applications. AWS provide you with a dedicated virtual machine to run our Application. EC2 provides all the resources that are used by the virtual machine for running our application. as local machene is a computer owned by us. But the virtual machine is a computer that is owned by someone ( Cloud provider) but runs our application. as EC2 is a platform where we can choose the kind of resource we need to run Application. The cloud provider creates a server using those resources so that our container runs on that and provides you with a link that can be accessible by everyone on the internet. so whatever the local host link we got by running our continer on local devise. In the cloud, the concept is same but we just run it continuously. As it is on the internet, we can control who can access it using the public IP address.

our task is to extract that public IP address so that everyone on the inter net can able to access it.

> Steps to be followed to do that.
> 1. Pushing Docker Image onto Docker HUB ( or any container registry)
