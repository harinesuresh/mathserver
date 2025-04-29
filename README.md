# Ex.05 Design a Website for Server Side Processing
# Date: 25.04.2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
math.html


<html>
    <head>
        <title>Calculate Power of a lamp</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color:rgb(216, 81, 162);
                margin: 0;
                padding: 0;
            }
    
            h1 {
                text-align: center;
                color: #0a0909;
                margin-top: 40px;
            }
    
            form {
                background-color: rgb(221, 155, 219);
                max-width: 400px;
                margin: 30px auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
    
            label {
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
            }
    
            input[type="number"] {
                width: 100%;
                padding: 8px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }
    
            button {
                background-color: #d915a1;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 16px;
                width: 100;
            }
    
            button:hover {
                background-color:rgb(53, 51, 57);
            }
    
            p {
                margin-top: 20px;
                text-align: center;
                font-size: 18px;
                color: #222;
            }
        </style>
    </head>
    <body>
        <h1 align="center">Calculate Power of a Lamp</h1>
    <form action="{% url 'home' %}" method="POST">
         {% csrf_token %}
    Intensity:
    <input type="text" name="intensity-input"> in m<br><br>
    Resistance:
    <input type="text" name="resistance-input">in ohms <br><br>
    <button type="submit">Calculate</button>
    <p align="center">The power of the lamp is:{{output}} watt </p>
    </form>
    </body>
</html>

urls.py


from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.power,name='home'),

]

views.py


from django.shortcuts import render
def power(request):  
    if request.method == 'POST':
        intensity = int(request.POST.get('intensity-input'))
        resistance = int(request.POST.get('resistance-input'))
        output = (intensity ** 2) * resistance  
        return render(request, 'math.html', {'output': output})
    return render(request,'math.html')

```
# SERVER SIDE PROCESSING:

![image](https://github.com/user-attachments/assets/b31ce50c-5099-440f-9af4-0c9af36c4c01)

# HOMEPAGE:

![image](https://github.com/user-attachments/assets/b80b0d1a-84cb-4e7e-99af-992d1faf29a0)


# RESULT:
The program for performing server side processing is completed successfully.
