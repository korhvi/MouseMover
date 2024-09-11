from flask import Flask, render_template, jsonify
import pyautogui as pag
import threading
import time
from pynput import keyboard

app = Flask(__name__)

bot_running = False
stop_key = keyboard.KeyCode(char='q')

def on_press(key):
    global bot_running
    if key == stop_key:
        bot_running = False

def move_mouse():
    global bot_running
    x, y = pag.position()
    while bot_running:
        x += 200
        y += 200
        pag.moveTo(x, y)
        if x > 1900:
            x = 0
        if y > 1000:
            y = 0
        time.sleep(2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_bot', methods=['POST'])
def start_bot():
    global bot_running
    if not bot_running:
        bot_running = True
        threading.Thread(target=move_mouse).start()
    return jsonify({'status': 'started'})

@app.route('/stop_bot', methods=['POST'])
def stop_bot():
    global bot_running
    bot_running = False
    return jsonify({'status': 'stopped'})

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    try:
        app.run(debug=True)
    finally:
        listener.stop()
