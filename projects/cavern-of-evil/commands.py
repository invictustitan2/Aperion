from verbs import VERBS


def parse_command(command):
    command = command.strip().lower()
    words = command.split()
    if not words:
        return ("", "")

    verb = words[0]
    obj = " ".join(words[1:]) if len(words) > 1 else ""

    # Synonym mapping
    synonyms = {
        "grab": "take",
        "pick": "take",
        "walk": "go",
        "move": "go",
        "inspect": "examine",
    }
    verb = synonyms.get(verb, verb)

    if verb not in VERBS:
        return ("unknown", obj)

    return verb, obj
