import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../')))

import streamlit as st
from utils.llm_client import GeminiClient
from utils.debugging_helper import build_debugging_prompt


def main():
    st.set_page_config(
        page_title='AI Debugging Assistance',
        page_icon='🤖',
        layout='centered'
    )

    st.title("🔎AI Debugging Assistance")
    st.write("Paste Your Code And Error Log And I'll Help You Debug It.")

    user_input=st.text_area(
        "Enter Your Code Or Error Log Below:",
        height=200,
        placeholder="Example:-class Main{.......}"
    )

    if st.button("Debug Code"):
        if not user_input.strip():
            st.warning("Please Enter Some Code Error Log")
            return
        with st.spinner("Analyzing Your Code...."):
            try:
                prompt=build_debugging_prompt(user_input)
                client=GeminiClient()
                response=client.ask(prompt)

                st.markdown("---")
                st.subheader("🎯Debugging Result")
                st.markdown(response)

            except Exception as e:
                st.error(f"An Error Occurred:{str(e)}")


if __name__=='__main__':
    main()