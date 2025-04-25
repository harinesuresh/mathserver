
from django.shortcuts import render
def power(request):  
    if request.method == 'POST':
        intensity = int(request.POST.get('intensity-input'))
        resistance = int(request.POST.get('resistance-input'))
        output = (intensity ** 2) * resistance  
        return render(request, 'math.html', {'output': output})
    return render(request,'math.html')
