from django.shortcuts import render,redirect
from myapp.models import HeartPrediction
from myapp.forms import HeartPredictionForm
import joblib
import pandas as pd
import mysql.connector
# Create your views here.

#To show data using table
def index(request):
    predictions = HeartPrediction.objects.all()
    return render(request, "show.html", {'predictions' : predictions} )

#Create prediction 
#Load the model and scaler from jupyter
model = joblib.load('C:\\Users\\welun\\Documents\\Heart Failure Prediction\\hearpredictionmodel.pkl')
scaler = joblib.load('C:\\Users\\welun\\Documents\\Heart Failure Prediction\\hearpredictionscaler.pkl')


def predict(request):
    if request.method == "POST":
        try:
            # Extract data from POST
                # age - variable to store the extracted value
                # 'age'-  retrieves the value from the form input with the name age
                # variable_name = data_type(request.POST.get('attribute_name'))
                
            age = int(request.POST.get('age'))
            anemia = int(request.POST.get('anemia'))
            creatinine_phosphokinase = int(request.POST.get('creatinine_phosphokinase'))
            diabetes = int(request.POST.get('diabetes'))
            ejection_fraction = int(request.POST.get('ejection_fraction'))
            high_blood_pressure = int(request.POST.get('high_blood_pressure'))
            platelets = float(request.POST.get('platelets'))  # Should be float
            serum_creatinin = float(request.POST.get('serum_creatinin'))  # Should be float
            serum_sodium = float(request.POST.get('serum_sodium'))
            sex = int(request.POST.get('sex'))
            smoking = int(request.POST.get('smoking'))
            time = int(request.POST.get('time'))

            # Create input data for prediction
            input_data = pd.DataFrame({
                'Age': [age],
                'Anemia': [anemia],
                'Creatinine Phopokinase': [creatinine_phosphokinase],
                'Diabetes': [diabetes],
                'Ejection Fraction': [ejection_fraction],
                'High Blood Pressure': [high_blood_pressure],
                'Platelets': [platelets],
                'Creatinine': [serum_creatinin],
                'Sodium': [serum_sodium],
                'Sex': [sex],
                'Smoking': [smoking],
                'Time': [time]
            })

            # Make the prediction
            prediction = model.predict(input_data)
            rounded_prediction = round(prediction[0])

            # Save the input data and prediction result to the database
                # age - is the name of the attribute (or field) in the HeartPrediction model.
                # The 'age' field in the model is set to the value of the 'age' variable above (not in the input data)

            HeartPrediction.objects.create(
                age=age,
                anemia=anemia,
                creatinine_phosphokinase=creatinine_phosphokinase,
                diabetes=diabetes,
                ejection_fraction=ejection_fraction,
                high_blood_pressure=high_blood_pressure,
                platelets=platelets,
                serum_creatinin=serum_creatinin,
                serum_sodium=serum_sodium,
                sex=sex,
                smoking=smoking,
                time=time,
                predicted_death_event=rounded_prediction  # Now this variable is defined
            )

            # Render the result on the index page
            return render(request, 'index.html', {'prediction': rounded_prediction})

        except Exception as e:
            print(f"Error during prediction: {e}")
            return render(request, 'index.html', {'prediction': None})  # Handle error case

    else:
        form = HeartPredictionForm()  # Create a blank form for GET requests
    return render(request, 'index.html', {'form': form})



