user_message_cache = {}

def is_duplicate(user_id: str, message: str):
    messages = user_message_cache.get(user_id, [])

    if message in messages:
        return True
    return False


def update_cache(user_id: str, message: str):
    if user_id not in user_message_cache:
        user_message_cache[user_id] = []

    user_message_cache[user_id].append(message)