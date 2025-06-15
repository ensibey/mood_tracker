import json
import datetime
import os
from collections import Counter
import matplotlib.pyplot as plt

DATA_FILE = "mood_data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_entry():
    date = str(datetime.date.today())
    print(f"\nToday's date: {date}")
    print("Choose your mood: Happy, Sad, Stressed, Tired")
    mood = input(">> ").capitalize().strip()
    note = input("Write your journal note: ").strip()

    data = load_data()
    data.append({"date": date, "mood": mood, "note": note})
    save_data(data)
    print("Entry saved.")

def show_stats():
    data = load_data()
    if not data:
        print("No data available.")
        return

    moods = [entry["mood"] for entry in data]
    counter = Counter(moods)

    print("\nMood stats:")
    for mood, count in counter.items():
        print(f"{mood}: {count} days")

    plt.bar(counter.keys(), counter.values(), color=['green', 'red', 'orange', 'blue'])
    plt.title("Mood Distribution")
    plt.ylabel("Days")
    plt.xlabel("Mood")
    plt.tight_layout()
    plt.show()

def main():
    print("Mood Tracker")
    while True:
        print("\n1. Add today's mood")
        print("2. Show stats")
        print("3. Exit")
        choice = input(">> ").strip()
        if choice == "1":
            add_entry()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
