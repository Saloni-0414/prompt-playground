def select_prompt_strategy(response_style: str) -> str:
    """
    Maps the selected response style
    to the appropriate prompting technique.
    """

    strategy_map = {
        "Quick Answer": "Zero-shot",
        "Learn with Example": "Few-shot",
        "Detailed Explanation": "Chain of Thought"
    }

    return strategy_map.get(
        response_style,
        "Zero-shot"
    )
