import time
from threading import Thread, Lock
import sys

lock = Lock() 

def animated_text(text, delay=0.1):
    """Fungsi untuk animasi teks (ketik per karakter)"""
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_song() :
    """Main function untuk menyanyikan lirik"""
    lyrics = [
        ("In my dreams", 0.2),
        ("you're with me", 0.1),
        ("We'll be everything I want us to be", 0.1),
        ("And from there", 0.1),
        ("who knows?", 0.1),
        ("Maybe this will be the night that we kiss", 0.1),
        ("for the first time", 0.1),
        ("Or is that just me and my", 0.1),
        ("imagination?", 0.2)
    ]
    threads = []
    for lyric, speed in lyrics:
        t = Thread(target=animated_text, args=(lyric, speed))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
if __name__ == "__main__":
    print("🎵")
    sing_song()
    print("🎶")