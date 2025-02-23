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
        self.model=ChatGroq(model="DeepSeek-R1-Distill-Llama-70B")
        self.add=t.add
        self.Subtract=t.Subtract
        self.multiply=t.multiply
        self.divide=t.divide
        self.memory=MemorySaver()

        self.llm_with_tool=self.model.bind_tools([self.add,self.Subtract,self.multiply,self.divide],parallel_tool_calls=False)
        self.sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")

        self.builder=StateGraph(MessageState)

        self.builder.add_node("tool_calling_llm",self.tool_calling_llm)
        self.builder.add_node("tools", ToolNode([self.add,self.Subtract,self.multiply,self.divide]))

        self.builder.add_edge(START,"tool_calling_llm")
        self.builder.add_conditional_edges("tool_calling_llm",tools_condition,)
        self.builder.add_edge("tools","tool_calling_llm")

        # self.graph=self.builder.compile(checkpointer=self.memory)
        self.graph=self.builder.compile()

    def graph_workflow():
        return self.graph

    def tool_calling_llm(self,state=MessageState):
        question = [self.sys_msg]+state["messages"]
        return {"messages" : [self.llm_with_tool.invoke(question)]}

    def response(self,message,name,thread_id):
        config={"configurable":{"thread_id":thread_id}}
        messages=[HumanMessage(content=message,name=name)]
        response=self.graph.invoke({"messages":messages})
        AI_message=[i for i in response["messages"] if str(type(i))=="<class 'langchain_core.messages.ai.AIMessage'>"]
        Tool_message=[i for i in response["messages"] if str(type(i))=="<class 'langchain_core.messages.tool.ToolMessage'>"]
        tool_content=""
        for i in Tool_message:
            tool_content=i.content+" \n"
        AI_content=AI_message[-1].content
        return tool_content+"\n"+AI_content