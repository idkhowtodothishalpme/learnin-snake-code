import pyautogui
import time
import random

phrases = [
    "hey", "hi", "hello", "bitch", "shit",
    "fuck", "ass", "bye", "cya", "no", "yes"
]

print("=" * 40)
print("  Discord Auto Typer")
print("=" * 40)
print()
print("Click into your Discord chat box NOW.")
print("Starting in 5 seconds...")
print()

for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("GO!")

while True:
    phrase = random.choice(phrases)
    pyautogui.typewrite(phrase, interval=0.05)
    pyautogui.press('enter')
    print(f"Sent: {phrase}")
    time.sleep(12)