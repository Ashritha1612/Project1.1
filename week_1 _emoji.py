user_mood = input("How are you feeling today").lower()
mood_responses = {
        "happy": {"emoji": "😊", "message": "Keep smiling!"},
        "sad": {"emoji": "😔", "message": "Brighter days are ahead."},
        "angry": {"emoji": "😠", "message": "Take a deep breath"},
        "excited": {"emoji": "🤩", "message": "Awesome! Embrace that energy!"},
        "tired": {"emoji": "😴", "message": "Take rest "}
        }
if user_mood in mood_responses:
        response = mood_responses[user_mood]
        print(f"\nYou're feeling {user_mood}? {response['emoji']} {response['message']}")
else:
    print(f"\I don't recognize '{user_mood}'.😊 Hope you have a good day!")