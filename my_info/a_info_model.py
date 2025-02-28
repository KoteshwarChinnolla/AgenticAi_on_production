from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END

from model_calling import model_calling
md=model_calling()

class MessageState(TypedDict):
    messages:Annotated[list[AnyMessage],add_messages]

class gen_info:

    def __init__(self):
        self.memory=MemorySaver()
        self.model=md.model
        self.sys_msg = SystemMessage(content="You are a helpful assistant named koteshwar respond from this inforamtion  => Your information: your Name: Chinnolla Koteshwar ,your birth dayBirthday: 21st March 2004,Phone: +91 6300727875,City: Hyderabad, India,Email: chinnollakoteshwar@gmail.com,Age: 20,Degree: B-Tech (Bachelo of Technology),Father name: Santhosh,Mother name:Godhavari, Sister : Srinija college name=Gokarajub Rangaraju Institute of Engineering and Technology,Branch: Electronics and Communication Engineering,Year of study: 4th year, goals: to become a AI/ML backend dev, skills= Machine Learning, Deep Learning, python, AWS, Docker, Java projects : A* algorithm based autonomus navigation system, A finetuned chatbot with rag , Poduct demand prediction etc..")
        self.builder=StateGraph(MessageState)
        self.builder.add_node("model_calling",self.model_response)
        self.builder.add_edge(START,"model_calling")
        self.graph=self.builder.compile(checkpointer=self.memory)
    
    def graph_workflow(self):
        return self.graph

    def model_response(self,state=MessageState):
        question = [self.sys_msg]+state["messages"]
        return {"messages" : [self.model.invoke(question)]}

    def response(self,message,name,thread_id):
        config={"configurable":{"thread_id":thread_id}}
        messages=[HumanMessage(content=message,name=name)]
        # response=self.graph.invoke({"messages":messages})
        response=self.graph.stream({"messages":messages},config=config,stream_mode="values")

        last_chat=[]

        for event in response:
            last_chat.append(event["messages"][-1])
        AI_message=[i for i in last_chat if str(type(i))=="<class 'langchain_core.messages.ai.AIMessage'>"]

        return AI_message[0].content
