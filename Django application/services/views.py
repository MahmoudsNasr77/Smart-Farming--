from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from joblib import load
from services.models import croppredictions,waterpredictions
classifer = load('./Classifer/RandomForest.pkl')
MLpredictor = load('./Predictor/RandomForestPredict.pkl')
#Dlpredictor = load('./Predictor/model.pickle')


@login_required
def crop_Suggestions(request):
    if request.method == 'POST':
        N = request.POST['N']
        P = request.POST['P']
        K = request.POST['K']
        temperature = request.POST['temperature']
        humidity = request.POST['humidity']
        ph = request.POST['ph']
        rainfall = request.POST['rainfall']
        y_predict = classifer.predict(
            [[N, P, K, temperature, humidity, ph, rainfall]])
        predict = croppredictions(N=N, P=P, K=K, temperature=temperature, humidity=humidity,
                              ph=ph, rainfall=rainfall, perviouspredictions=y_predict[0],
                              user=request.user)
        predict.save()
        context = {"y_predict": y_predict[0], "predict": predict}
        return render(request, 'suggest/suggest.html', context)
    return render(request, 'suggest/suggest.html')
@login_required
def water_predictions(request):
    if request.method == 'POST':
        Water_Loss = request.POST['Water_Loss']
        soil_moisture = request.POST['soil_moisture']
        Water_Level = request.POST['Water_Level']
        temperature = request.POST['temperature']
        humidity = request.POST['humidity']
        Lighting = request.POST['Lighting']
        myoption = request.POST.get('plant')
        Pepper=0
        Strawberry=0
        if myoption =='Pepper':
            Pepper=1         
        elif myoption =='Strawberry':
            Strawberry=1
        y_predict = MLpredictor.predict(
            [[soil_moisture, Water_Level, temperature,
               humidity,Lighting,Water_Loss,Pepper,Strawberry]])
        
        predict = waterpredictions(temperature=temperature, humidity=humidity, soilMoisture=soil_moisture
                                   , waterLevel=Water_Level, lighting=Lighting,
                              crop_type=myoption, water_loss=Water_Loss, actual=y_predict[0],
                              user=request.user)
        predict.save()
        context = {"y_predict": round(y_predict[0],2), "predict": predict,'plant':myoption}
        return render(request, 'predict/predict.html', context)
    return (render(request, 'predict/predict.html'))
