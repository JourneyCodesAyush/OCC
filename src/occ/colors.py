class Color:
    RESET = "\033[0m"
    WHITE = "\033[37m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"


def get_color(label: str) -> str:
    if "[ERROR]" == label:
        return Color.RED
    elif "[WARN]" == label:
        return Color.YELLOW
    elif "[NOTICE]" == label:
        return Color.CYAN
    else:
        return Color.WHITE
