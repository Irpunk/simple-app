# from flask import Flask
# app = Flask(__name__) 

# @app.route('/') 
# def hello(): 
#     return "Halo dari Flask + Docker + Jenkins!"

# if __name__ == '__main__':
#     app.run( host='0.0.0.0', port=5000 )

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ganti dengan API key kamu dari https://openweathermap.org/api
API_KEY = "5cfe07214f76f167a41ce12b6af1936f"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city = None

    if request.method == 'POST':
        city = request.form['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=id'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather_data = {'error': 'Kota tidak ditemukan. Coba lagi.'}

    return render_template('index.html', weather=weather_data, city=city)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
