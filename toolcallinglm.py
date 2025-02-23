import os
from dotenv import load_dotenv
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from tools import tools
from langgraph.checkpoint.memory import MemorySaver


load_dotenv()
os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")

class MessageState(TypedDict):
    messages:Annotated[list[AnyMessage],add_messages]
class build_graph():
    def __init__(self):

        t=tools()
        self.model=ChatGroq(model="qwen-2.5-32b")
        self.add=t.add
        self.subtract=t.subtract
        self.multiply=t.multiply
        self.divide=t.divide
        self.memory=MemorySaver()

        self.tools_list=[self.add,self.subtract,self.multiply,self.divide]

        self.llm_with_tool=self.model.bind_tools(self.tools_list)
        self.sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")

        self.builder=StateGraph(MessageState)

        self.builder.add_node("tool_calling_llm",self.tool_calling_llm)
        self.builder.add_node("tools", ToolNode(self.tools_list))

        self.builder.add_edge(START,"tool_calling_llm")
        self.builder.add_conditional_edges("tool_calling_llm",tools_condition,)
        self.builder.add_edge("tools","tool_calling_llm")

        # self.graph=self.builder.compile(checkpointer=self.memory)
        self.graph=self.builder.compile(checkpointer=self.memory)

    def graph_workflow():
        return self.graph

    def tool_calling_llm(self,state=MessageState):
        question = [self.sys_msg]+state["messages"]
        return {"messages" : [self.llm_with_tool.invoke(question)]}

    def response(self,message,name,thread_id):
        config={"configurable":{"thread_id":thread_id}}
        messages=[HumanMessage(content=message,name=name)]
        # response=self.graph.invoke({"messages":messages})
        response=self.graph.stream({"messages":messages},config=config,stream_mode="values")

        last_chat=[]

        for event in response:
            last_chat.append(event["messages"][-1])
        AI_message=[i for i in last_chat if str(type(i))=="<class 'langchain_core.messages.ai.AIMessage'>"]
        Tool_message=[i for i in last_chat if str(type(i))=="<class 'langchain_core.messages.tool.ToolMessage'>"]
        tool_content=""
        for i in Tool_message:
            tool_content=i.content+"\n"
        process=""

        if len(AI_message)>1:
            tools_called=AI_message[-2].additional_kwargs["tool_calls"]
            for i in tools_called:
                process+="\n\n"+str(i["function"]["arguments"] + " \n\n " + str(i["function"]["name"]))

        AI_content=AI_message[-1].content

        final_content=process+"\n\n"+tool_content+"\n\n"+AI_content
        
        return final_content


        # for event in self.graph.stream({"messages":messages},stream_mode="values"):
        #     # print(event)
        #     print(event['messages'])





        # AI_message=[i for i in response["messages"] if str(type(i))=="<class 'langchain_core.messages.ai.AIMessage'>"]
        # Tool_message=[i for i in response["messages"] if str(type(i))=="<class 'langchain_core.messages.tool.ToolMessage'>"]
        # tool_content=""
        # for i in Tool_message:
        #     tool_content=i.content+" \n"
        # AI_content=AI_message[-1].content
        # return tool_content+"\n"+AI_content
        # return "done"