import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)



@app.route("/")
def loadPage():
    return render_template('njareb.html', query="")

@app.route("/", methods=['POST'])
def predict():
    '''
    gender
    Contract
    InternationalPlan
    VoiceMailPlan
    InternetService
    OnlineSecurity
    OnlineBackup
    DeviceProtection
    TechSupport
    StreamingTV
    StreamingMovies
    TotalNightMinutes
    TotalDayMinutes
    TotalIntlMinutes
    TotalEveMinutes
    TotalRevenue
    TotalNightCalls
    NumbervMailMessages
    CustomerServiceCalls
    '''
    
    
            
                
    input1=request.form['gender']
    input2=request.form['Contract']
    input3=request.form['InternationalPlan']
    input4=request.form['VoiceMailPlan']
    input5=request.form['InternetService']
    input6=request.form['OnlineSecurity']
    input7=request.form['OnlineBackup']
    input8=request.form['DeviceProtection']
    input9=request.form['TechSupport']
    input10=request.form['StreamingTV']
    input11=request.form['StreamingMovies']
    input12=request.form['TotalNightMinutes']
    input13=request.form['TotalDayMinutes']
    input14=request.form['TotalIntlMinutes']
    input15=request.form['TotalEveMinutes']
    input16=request.form['TotalRevenue']
    input17=request.form['TotalNightCalls']
    input18=request.form['NumbervMailMessages']
    input19=request.form['CustomerServiceCalls']
        
        
    model=pickle.load(open('model.sav','rb'))
    data=[[input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12,input13,input14,input15,input16,input17,input18,input19]]
    new_df=pd.DataFrame(data,columns = [ 'gender','Contract','InternationalPlan','VoiceMailPlan','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','TotalNightMinutes','TotalDayMinutes','TotalIntlMinutes','TotalEveMinutes','TotalRevenue','TotalNightCalls','NumbervMailMessages','CustomerServiceCalls'])
    single=model.predict(new_df.tail(1))  
    probability=model.predict_proba(new_df.tail(1))[:,1]
    if single==1:
        o1 = "This Customer is likely to be Churned !"
        o2 =  "Confidence {}".format(probability*100)
    else:
        o1 = "This Customer is likely to Continue"
        o2 = "Confidence{}".format(probability*100)
    return render_template('njareb.html', output1=o1, output2= o2,
                               input1=request.form['gender'],
                               input2=request.form['Contract'],
                               input3=request.form['InternationalPlan'],
                               input4=request.form['VoiceMailPlan'],
                               input5=request.form['InternetService'],
                               input6=request.form['OnlineSecurity'],
                               input7=request.form['OnlineBackup'],
                               input8=request.form['DeviceProtection'],
                               input9=request.form['TechSupport'],
                               input10=request.form['StreamingTV'],
                               input11=request.form['StreamingMovies'],
                               input12=request.form['TotalNightMinutes'],
                               input13=request.form['TotalDayMinutes'],
                               input14=request.form['TotalIntlMinutes'],
                               input15=request.form['TotalEveMinutes'],
                               input16=request.form['TotalRevenue'],
                               input17=request.form['TotalNightCalls'],
                               input18=request.form['NumbervMailMessages'], 
                               input19=request.form['CustomerServiceCalls'])
    app.run()


