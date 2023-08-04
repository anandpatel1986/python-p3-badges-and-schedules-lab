def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [badge_maker(name) for name in names]


def assign_rooms(names):
    list_messages = []
    i = 1
    for name in names:
        list_messages.append(f"Hello, {name}! You'll be assigned to room {i}!")
        i = i + 1
    return list_messages


def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for message in assign_rooms(names):
        print(message)
