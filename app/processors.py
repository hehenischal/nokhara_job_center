

def category_processor(request):
    from .models import Category
    categories = Category.objects.all()
    return {'categories': categories}