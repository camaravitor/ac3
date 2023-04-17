from flask import Flask, render_template
import os

app = Flask(__name__)

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

@app.route('/')
def index():
    count = 0
    num = 2
    primos = []
    while count < 100:
        if primo(num):
            primos.append(num)
            count += 1
        num += 1
    return render_template('index.html', primos=primos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
