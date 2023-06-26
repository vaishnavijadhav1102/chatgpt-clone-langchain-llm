import streamlit as st
import os
from dotenv import load_dotenv
from streamlit_chat import message

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.schema import HumanMessage
from langchain.schema import AIMessage


def init():
    load_dotenv()
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY")=="":
        print("not set")
        exit(1)
    else:
        print("is set")
    st.set_page_config(
        page_title="Your own chatgpt",

    )

def main():
    init()
    chat=ChatOpenAI(temperature=0)

    if "messages" not in st.session_state:
        st.session_state.messages = [SystemMessage(content="You are a helpful assistant.")]
    st.header("Your own chatgpt")

    with st.sidebar:
        user_input=st.text_input("Your Message", key="user_input")
        if user_input:
            
            st.session_state.messages.append(HumanMessage(content=user_input))
            response=chat(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
    messages = st.session_state.get('messages',[])
    for i,msg in enumerate(messages[1:]):
        if i%2==0:
            message(msg.content,is_user=True,key=str(i)+'_user')
        else:
            message(msg.content,is_user=False,key=str(i)+'_ai')

if __name__ =='__main__':
    main()