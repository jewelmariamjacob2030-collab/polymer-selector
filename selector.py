"""Decision logic for the Polyverse polymer requirement selector."""

# The fifth scenario is the printer-guide peer-testing challenge.
REQUIREMENTS = {
    "1": {
        "title": "Lightweight, strong reinforcement for a laptop bag",
        "polymer": "Kevlar",
        "reason": "Kevlar has a high strength-to-weight ratio, making it suitable for lightweight reinforcement.",
        "icon": "🎒",
        "tag": "Strength + low weight",
    },
    "2": {
        "title": "A conducting coating for a sensor",
        "polymer": "Polyaniline (PANI)",
        "reason": "In a suitable doped form, polyaniline can conduct electricity and is useful in sensor coatings.",
        "icon": "📟",
        "tag": "Electrical conductivity",
    },
    "3": {
        "title": "Disposable packaging intended for industrial composting",
        "polymer": "Polylactic Acid (PLA)",
        "reason": "Suitable PLA grades can biodegrade under controlled industrial composting conditions.",
        "icon": "🥡",
        "tag": "Industrial composting",
    },
    "4": {
        "title": "A low-friction surface for a sliding component",
        "polymer": "PTFE",
        "reason": "PTFE has a very low coefficient of friction, helping surfaces slide smoothly.",
        "icon": "⚙️",
        "tag": "Low friction",
    },
    "5": {
        "title": "A small guide inside a printer must let a moving part slide smoothly",
        "polymer": "PTFE",
        "reason": "PTFE's low coefficient of friction makes it a suitable candidate for a smooth-sliding printer guide.",
        "icon": "🖨️",
        "tag": "Peer-testing challenge",
    },
}


def get_recommendation(choice):
    """Return a recommendation for a valid numbered choice, else None.

    The input is converted to text and whitespace is removed so values such as
    1, "1" and " 1 " all behave consistently.
    """
    return REQUIREMENTS.get(str(choice).strip())
