from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from joblib import load
from services.models import croppredictions
model = load('./Classifer/RandomForest.pkl')


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
        y_predict = model.predict(
            [[N, P, K, temperature, humidity, ph, rainfall]])
        predict = croppredictions(N=N, P=P, K=K, temperature=temperature, humidity=humidity,
                              ph=ph, rainfall=rainfall, perviouspredictions=y_predict[0],
                              user=request.user)
        predict.save()
        context = {"y_predict": y_predict[0], "predict": predict}
        return render(request, 'suggest/suggest.html', context)
    return render(request, 'suggest/suggest.html')
@login_required
def crop_predictions(request):
    return (render(request, 'predict/predict.html'))
