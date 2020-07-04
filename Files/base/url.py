from django.url import path

# Down the road we are going to create many functions
# That's why we import all the functions from views
from . import views  # dot (.) notation means from this folder

urlpatterns = [
    path('', views.home)  # This basically call views home fn when base page loads
]

# Now this is our app url.py file. We've to configure our Files url.py to take us to our app(this one) url.py

