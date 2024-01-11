from datetime import datetime

generate_timestamp = None

def generate_global_timestamp():
    global generate_timestamp
    if generate_timestamp is None:
        generate_timestamp=datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

    return generate_timestamp

