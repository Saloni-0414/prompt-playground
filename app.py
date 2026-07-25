import streamlit as st

from llm import generate_response
from prompt_router import select_prompt_strategy
from prompt_builder import build_prompt


st.set_page_config(
    page_title="Prompt Playground",
    layout="wide"
)

st.title("Prompt Playground")
st.caption("Compare different Prompt Engineering techniques")

with st.form("prompt_form"):

    question = st.text_area(
        "Enter your question",
        placeholder="Ask me Anything."
    )

    selected_style = st.selectbox(
        "Choose Response Style",
        [
            "Quick Answer",
            "Learn with Example",
            "Detailed Explanation"
        ]
    )

    generate = st.form_submit_button(
        "Generate Response",
        use_container_width=True
    )


if generate:

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    strategy = select_prompt_strategy(selected_style)

    optimized_prompt = build_prompt(
        question,
        strategy
    )

    with st.spinner("Generating response..."):
        answer = generate_response(optimized_prompt)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Selected Response Style")
        st.info(selected_style)

    with col2:
        st.subheader("Prompting Technique")
        st.info(strategy)

    with st.expander("View Optimized Prompt"):
        st.code(optimized_prompt, language="text")

    st.subheader("Generated Response")
    st.write(answer)
