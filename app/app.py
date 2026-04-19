from flask import Flask, render_template, request
import pickle
import os
import pandas as pd

app = Flask(__name__)

# Load model safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'model', 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = float(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']

        import pandas as pd

        data = pd.DataFrame([{
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'region': region
        }])

        prediction = model.predict(data)

        inr = prediction[0] * 83

        return render_template(
            'index.html',
            prediction_text=f"Estimated Medical Cost: ₹ {round(inr, 2)}"
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"Error: {str(e)}"
        )

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)