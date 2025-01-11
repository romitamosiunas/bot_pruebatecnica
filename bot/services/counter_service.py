import json
import os
COUNTER_FILE = "counters.json"


#Función para contador
def load_counters():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as file:
            return json.load(file)
    return {}

def save_counters(counters):
    with open(COUNTER_FILE, "w") as file:
        json.dump(counters, file)

def get_counter(user_id):
    counters = load_counters()
    return counters.get(str(user_id), 0)

def update_counter(user_id, count):
    counters = load_counters()
    counters[str(user_id)] = count
    save_counters(counters)




