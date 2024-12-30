import redis


redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)


def get_current_value():
    """
    Retrieves the current value from Redis. 

    If the 'current_value' key does not exist, initializes it to 0 in Redis 
    and returns 0.

    Returns:
        float: The current value.
    """
    current_value = redis_client.get('current_value')
    if current_value is None:
        redis_client.set('current_value', 0)
        return 0
    return float(current_value)


def set_current_value(value: float):
    """
    Sets the current value in Redis.

    Args:
        value (float): The new value to be set.
    """
    redis_client.set('current_value', value)
