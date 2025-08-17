import time
import sys


lyrics = [
    ("\nCuma kamu tiada yang lain", 0.09),
    ("Kubilang aku gak main main", 0.09),
    ("Apa yang kau mau kuturutin", 0.09),
    ("Sekarang kamu sama yang lain", 0.09),
    ("Awalnya kucuma cobain", 0.09),
    ("Tapi ku ketagihan", 0.09),
    ("Kubilang amin", 0.09),
    ("Sampai kepelaminan", 0.09),
    ("Jangan disamain, sama mantanmu bajingan", 0.09),
    ("Ulang lagi kucari yang lain", 0.09),
]

delays = [3.8,
        3.6,
        3.3,
        3.3,
        3.1,
        2,
        2,
        2,
        2,
        2,
        2]

def animate_text(text, char_delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    for i, (text, char_delay) in enumerate(lyrics):
        animate_text(text, char_delay)
        if i < len(lyrics) - 1:
            # Calculate the time until the next line should start
            next_line_delay = max(0, delays[i] - len(text) * char_delay)
            time.sleep(next_line_delay)

if __name__ == "__main__":
    main()