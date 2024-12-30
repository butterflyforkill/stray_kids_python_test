import os
import time

LAST_UPDATE_FILE = 'last_update.txt'

def check_last_update():
    """
    Checks when the data was last updated. Returns the time in seconds since the last update.

    Returns:
        float: Time of last update in seconds, or None if no update file exists.
    """
    if os.path.exists(LAST_UPDATE_FILE):
        with open(LAST_UPDATE_FILE, 'r') as f:
            return float(f.read().strip())
    return None


def is_data_outdated():
    """
    Checks if the data is outdated. If it is more than 24 hours old, it will need to be updated.
    
    Returns:
        bool: True if the data is outdated, False otherwise.
    """
    last_update = check_last_update()
    if not last_update:
        return True

    current_time = time.time()
    if current_time - last_update > 24 * 60 * 60:  # 24 hours in seconds
        return True

    return False