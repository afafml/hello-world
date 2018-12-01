from flask import Flask
app = Flask(__name__)

@app.route("/")
print('The sum is %.1f' %(float(input('Enter first number: '))+float(input('Enter second number: '))))
