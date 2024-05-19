from flask import Flask,request,render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form

        city_name = request.form['user_data']
        API_key = "cb8370abd156d9dde5127695c59647fd"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

        response = requests.get(url)
        data = response.json()
        if data['cod'] == '404':
           return '<center><h3>City Not Found</h3></center>'
        else:
            return render_template('index.html', user_data=data)

        # Pass the data back to the template to display it

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)