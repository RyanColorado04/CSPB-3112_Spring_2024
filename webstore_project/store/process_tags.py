# Import the Category model from the models module in the same directory
from .models import Category

# Define a context processor function called links
def links(request):
    # Retrieve all objects from the Category model using the .all() method
    links = Category.objects.all()
    # Return a dictionary with the 'links' key holding all Category objects
    # This dictionary will be added to the context of every template
    return dict(links=links)