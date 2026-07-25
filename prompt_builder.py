from pathlib import Path


TEMPLATE_DIR = Path(__file__).parent / "templates"


def load_template(template_name: str) -> str:
    """
    Load a prompt template from the templates directory.
    """
    template_path = TEMPLATE_DIR / template_name

    with open(template_path, "r", encoding="utf-8") as file:
        return file.read()


def build_prompt(question: str, strategy: str) -> str:
    """
    Build the final prompt based on the selected prompting strategy.
    """

    template_map = {
        "Zero-shot": "zero_shot.txt",
        "Few-shot": "few_shot.txt",
        "Chain of Thought": "chain_of_thought.txt"
    }

    template_file = template_map.get(strategy, "zero_shot.txt")

    template = load_template(template_file)

    prompt = template.format(
        question=question
    )

    return prompt
