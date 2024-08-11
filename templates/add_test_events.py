import sqlite3
from datetime import datetime, timedelta

def add_test_data():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Assuming you have at least one user in your database
    # If not, you'll need to add a user first
    cursor.execute("SELECT id FROM users LIMIT 1")
    user_id = cursor.fetchone()[0]

    # Test data
    events = [
        ("Team Meeting", datetime.now(), datetime.now() + timedelta(hours=1)),
        ("Project Deadline", datetime.now() + timedelta(days=7), datetime.now() + timedelta(days=7, hours=8)),
        ("Lunch with Client", datetime.now() + timedelta(days=2, hours=12), datetime.now() + timedelta(days=2, hours=13, minutes=30)),
        ("Conference Call", datetime.now() + timedelta(days=3, hours=15), datetime.now() + timedelta(days=3, hours=16)),
        ("Training Session", datetime.now() + timedelta(days=5, hours=10), datetime.now() + timedelta(days=5, hours=16)),
        ("Code Review", datetime.now() + timedelta(days=1, hours=14), datetime.now() + timedelta(days=1, hours=15, minutes=30)),
        ("Team Building Event", datetime.now() + timedelta(days=10), datetime.now() + timedelta(days=10, hours=8)),
        ("Quarterly Review", datetime.now() + timedelta(days=14, hours=9), datetime.now() + timedelta(days=14, hours=11)),
        ("Product Launch", datetime.now() + timedelta(days=30), datetime.now() + timedelta(days=30, hours=4)),
        ("Annual Leave", datetime.now() + timedelta(days=60), datetime.now() + timedelta(days=67))
    ]

    for event in events:
        cursor.execute("""
        INSERT INTO events (user_id, title, start_time, end_time)
        VALUES (?, ?, ?, ?)
        """, (user_id, event[0], event[1], event[2]))

    conn.commit()
    conn.close()

    print("Test data added successfully!")

if __name__ == "__main__":
    add_test_data()