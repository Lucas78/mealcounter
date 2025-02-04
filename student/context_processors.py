from .models import Student
from meal.models import ItemMeal, Plate


def student(request):
    context = {}
    try:
        student = Student.objects.get(user_ptr=request.user)
        dangerous_items = ItemMeal.objects.filter(
            allergy__in=student.allergy.values_list('pk'))
        dangerous_plates = []
        if dangerous_items:
            dangerous_plates = Plate.objects.filter(
                item_meal__in=dangerous_items.values_list('pk'))

        context['student'] = student
        context['dangerous_items'] = dangerous_items
        context['dangerous_plates'] = dangerous_plates
    except:
        context['student'] = False
        context['dangerous_items'] = False
        context['dangerous_plates'] = False
    return context
