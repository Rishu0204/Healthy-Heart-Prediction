from flask import Flask, render_template,request,send_file
import pickle
import numpy as np
import pandas as pd
import gzip

# Load the pre-trained model from a gzipped pickle file
with gzip.open('model.pkl', 'rb') as f:
    scale,model = pickle.load(f)

#define the flask app
app=Flask(__name__)

#define the home route
@app.route('/')
def index():        #this index() will will called when the user opens the home page
    return render_template('index.html')        #render_template() will render the index.html file i.e return the index.html file

@app.route('/diagnostics')
def dignostics():        #this index() will will called when the user opens the home page
    return render_template('index1.html') 

@app.route('/data')
def data():
    # Load and transform the dataset
    df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

    # Replace 0/1 with Yes/No for relevant columns
    df['DEATH_EVENT'] = df['DEATH_EVENT'].map({0: 'No', 1: 'Yes'})
    df['sex'] = df['sex'].map({0: 'Female', 1: 'Male'})
    df.replace({0: 'No', 1: 'Yes'}, inplace=True)

    # Pagination
    page = int(request.args.get('page', 1))
    per_page = 20
    total_pages = (len(df) - 1) // per_page + 1
    start = (page - 1) * per_page
    end = start + per_page
    paginated_df = df.iloc[start:end]

    # Convert paginated DataFrame to HTML
    data_html = paginated_df.to_html(classes='table table-striped', index=False, escape=False)

    return render_template('data.html', table=data_html, page=page, total_pages=total_pages)

# Download route
@app.route('/download')
def download():
    return send_file('heart_failure_clinical_records_dataset.csv', as_attachment=True)



#define the predict route
@app.route('/predict', methods=['POST'])
def predict_occurance():
    age = float(request.form.get('age'))
    anaemia = int(request.form.get('anaemia'))
    creatinine_phosphokinase = int(request.form.get('creatinine_phosphokinase'))
    diabetes = int(request.form.get('diabetes'))
    ejection_fraction = int(request.form.get('ejection_fraction'))
    high_blood_pressure = int(request.form.get('high_blood_pressure'))
    platelets = float(request.form.get('platelets'))
    serum_creatinine = float(request.form.get('serum_creatinine'))
    serum_sodium = int(request.form.get('serum_sodium'))
    smoking = int(request.form.get('smoking'))
    
    
    input_data = np.array([[age, anaemia, creatinine_phosphokinase, diabetes,
                                ejection_fraction, high_blood_pressure, platelets,
                                serum_creatinine, serum_sodium, smoking]])
    
    scaled_input_data = scale.transform(input_data)
    #predict the outcome
    result= model.predict(scaled_input_data)
   

    if result[0] == 0:
        result = "No Heart Failure"
    else:
        result = "Heart Failure"


    return render_template('index1.html',result=result)  # Render the index.html file with the result

if __name__ == '__main__':
    app.run(debug=True,port=5001)  # Run the Flask app in debug mode