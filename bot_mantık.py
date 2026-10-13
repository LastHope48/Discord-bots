import random

emojiler = [
    # Yüzler ve İfadeler (25)
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇",
    "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😋", "😛", "😜",
    "🤪", "🤨", "🧐", "🤓", "😎",

    # Jestler ve Kalpler (15)
    "👍", "👎", "👌", "✌️", "🤞", "🤟", "🤘", "🤙", "👏", "🙌",
    "❤️", "🧡", "💛", "💚", "💙",

    # Doğa, Hava ve Bitkiler (15)
    "🌞", "🌝", "⭐", "🌟", "✨", "⚡", "🔥", "🌈", "🌊", "🌸",
    "🌺", "🌻", "🌲", "🍀", "🍁",

    # Hayvanlar (15)
    "🐶", "🐱", "🐭", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁",
    "🐸", "🐵", "🐔", "🐧", "🐍",

    # Yiyecek ve İçecekler (15)
    "🍎", "🍌", "🍉", "🍇", "🍓", "🍒", "🥑", "🍕", "🍔", "🍟",
    "🍣", "🍦", "🍩", "☕", "🍺",

    # Nesneler, Araçlar ve Semboller (15)
    "🚀", "✈️", "🚗", "🚲", "💡", "🎉", "🏆", "🎯", "🎮", "📱",
    "💻", "📚", "🔔", "🔑", "💎"
]

def emoji(repeat):
    emojis_choiced = []

    for i in range(repeat):
        choiced = random.choice(emojiler)

        emojis_choiced.append(choiced)

    return (str(_emoji) for _emoji in emojis_choiced)

def secret_function(times):
    selects = []

    for _ in times:
        selected = random.choice(
            [
                "yazı", "tura"
            ]
        )

        selects.append(selected)

    return ", ".join(selects)
