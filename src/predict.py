@app.route('/predict', methods=['POST'])
def predict():
    try:
        import pandas as pd

        age = float(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = float(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']

        data = pd.DataFrame([{
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'region': region
        }])

        prediction = model.predict(data)

        return f"Predicted Expense: ₹ {round(prediction[0], 2)}"

    except Exception as e:
        return f"Error: {str(e)}"