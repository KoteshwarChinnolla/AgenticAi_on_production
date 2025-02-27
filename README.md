# AgenticAi_on_production

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

I implimented every functionality in a supperate file then imported it as libreryes so that there will be a ease of debugging and clear understading of code. i found out this this technique is known as modular coding. This method made my task esy to just import every functionality into one app.py(FastAPI file) then exicute the functions.

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
uvicorn main:app --host 0.0.0.0 --port 80
```

There are other alternatives [more information click here](https://fastapi.tiangolo.com/deployment/manually/#install-the-server-program)

[UVICORN](https://www.uvicorn.org/)
(FASTAPI Doccumentation for better detail)[https://fastapi.tiangolo.com/tutorial/first-steps/)





 
 
