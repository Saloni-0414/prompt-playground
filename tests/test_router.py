from prompt_router import select_prompt_strategy

intents = [
    "Learning",
    "Coding",
    "Writing",
    "Summarization",
    "Information Extraction",
    "Brainstorming"
]

for intent in intents:

    strategy = select_prompt_strategy(intent)

    print("----------------------------")
    print("Intent   :", intent)
    print("Strategy :", strategy)
