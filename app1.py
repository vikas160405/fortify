from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    """Generate a secure password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def home():
    password = None
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        password = generate_password(length)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
