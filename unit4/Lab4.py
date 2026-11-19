import json

logs = [
    {"timestamp": "10:00", "level": "INFO", "message": "Application started"},
    {"timestamp": "10:05", "level": "WARNING", "message": "Low memory"},
    {"timestamp": "10:10", "level": "ERROR", "message": "File not found"},
    {"timestamp": "10:15", "level": "INFO", "message": "User logged in"}
]

with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

with open("logs.json", "r") as file:
    data = json.load(file)

print("JSON LOG ANALYZER")
print("-------------------")

info = 0
warning = 0
error = 0

for log in data:
    print("\nTimestamp:", log["timestamp"])
    print("Level:", log["level"])
    print("Message:", log["message"])

    if log["level"] == "INFO":
        info += 1
    elif log["level"] == "WARNING":
        warning += 1
    elif log["level"] == "ERROR":
        error += 1

print("\n--- LOG SUMMARY ---")
print("INFO:", info)
print("WARNING:", warning)
print("ERROR:", error)
print("Total Logs:", len(data))
