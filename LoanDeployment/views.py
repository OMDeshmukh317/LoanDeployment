from django.shortcuts import render,HttpResponse
from joblib import load
# Create your views here.

model=load('./savedModels/best_xgc_model1.pkl')

def index(request):
    context={
        'variable':'this is variable'
    }
    return render(request,'index.html',context)
  


def formInfo(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = int(request.POST.get('age', 0))
        gender = int(request.POST.get('gender', 0))
        education = int(request.POST.get('education', 0))
        income = float(request.POST.get('income', 0))
        experience = int(request.POST.get('experience', 0))
        ownership = int(request.POST.get('ownership', 0))
        amount = float(request.POST.get('amount', 0))
        intent = int(request.POST.get('intent', 0))
        interest = float(request.POST.get('interest', 0))
        if income > 0:
            perincome = (amount / income) * 100
        else:
            perincome = 0
        # perincome=amount/income
        # perincome = float(request.POST.get('perincome', 0))
        credithistory = int(request.POST.get('credithistory', 0))
        creditscore = int(request.POST.get('creditscore', 0))
        default = int(request.POST.get('default', 0))

        y_pred = model.predict([[age, gender, education, income, experience, ownership, amount, intent, interest, perincome, credithistory, creditscore, default]])
        if y_pred[0] == 0:
            result = 'Sorry, your loan application was not approved.'
        elif y_pred[0] == 1:
            result = 'success'
        else:
            result = 'Unable to predict your loan status. Please try again.'

        return render(request, 'index.html', {'result': result})
    else:
        return render(request, 'index.html')



def about(request):
    
    
    return render(request,'about.html')



  
# def formInfo(request):
#     name=request.GET['name']
#     age = int(request.GET.get('age', 0))
#     gender = int(request.GET.get('gender', 0))
#     education = int(request.GET.get('education', 0))
#     income = float(request.GET.get('income', 0))
#     experience = int(request.GET.get('experience', 0))
#     ownership = int(request.GET.get('ownership', 0))
#     amount = float(request.GET.get('amount', 0))
#     intent = int(request.GET.get('intent', 0))
#     interest = float(request.GET.get('interest', 0))
#     perincome = float(request.GET.get('perincome', 0))
#     credithistory = int(request.GET.get('credithistory', 0))
#     creditscore = int(request.GET.get('creditscore', 0))
#     default = int(request.GET.get('default', 0))
#     y_pred=model.predict([[age,gender,education,income,experience,ownership,amount,intent,interest,perincome,credithistory,creditscore,default]])
#     if y_pred[0]==0:
#         y_pred='Sorry'
#     elif y_pred[0]==1:
#         y_pred='Congrats'
#     else:
#         y_pred='could not predict'
#     return render(request,'index.html',{'result':y_pred})


def dataanalysis(request):
    return render(request,'dataanalysis.html')
    return HttpResponse("<h1>this is about</h1>")

def services(request):
    return HttpResponse("<h1>this is services</h1>")

def contact(request):
    return HttpResponse("<h1>this is contact</h1>")



  
# def formInfo(request):
#     try:
#         # Retrieve and clean input values
#         name = request.GET.get('name', '').strip()  # Not used in the model, just cleaned
#         age = int(request.GET.get('age', 0))
#         gender = int(request.GET.get('gender', 0))
#         education = int(request.GET.get('education', 0))
#         income = float(request.GET.get('income', 0))
#         experience = int(request.GET.get('experience', 0))
#         ownership = int(request.GET.get('ownership', 0))
#         amount = float(request.GET.get('amount', 0))
#         intent = int(request.GET.get('intent', 0))
#         interest = float(request.GET.get('interest', 0))
#         perincome = float(request.GET.get('perincome', 0))
#         credithistory = int(request.GET.get('credithistory', 0))
#         creditscore = int(request.GET.get('creditscore', 0))
#         default = int(request.GET.get('default', 0))

#         # Create feature vector
#         features = [
#             age, gender, education, income, experience, ownership, amount,
#             intent, interest, perincome, credithistory, creditscore, default
#         ]

#         # Ensure the data is numeric and in the correct format
#         features = [float(value) for value in features]  # Convert all to float
#         features = [features]  # Wrap in a list to match XGBoost's input requirements

#         # Predict
#         y_pred = model.predict(features)

#         # Interpret prediction
#         if y_pred[0] == 0:
#             result = 'Sorry, loan not approved.'
#         elif y_pred[0] == 1:
#             result = 'Congrats, loan approved!'
#         else:
#             result = 'Could not predict the outcome.'
#     except ValueError as ve:
#         return HttpResponse(f"Value Error: {ve}", status=400)
#     except Exception as e:
#         return HttpResponse(f"Error: {e}", status=500)

#     return render(request, 'result.html', {'result': result})
  