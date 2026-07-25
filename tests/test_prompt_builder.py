from prompt_builder import build_prompt

question = "Explain Retrieval-Augmented Generation."

strategy = "Chain of Thought"

prompt = build_prompt(question, strategy)

print(prompt)

