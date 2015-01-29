from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.

# View (i.e. controller) for home page
# Не понимаю, зачем при запросе домашней страницы POST писать? Или он один раз запросится когда первичо вызываешь, и еще раз после нажатия Enter при отправке формы7 (И тогда в БД будет создан элемент)
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	
	return render(request, 'home.html')

# View (i.e. controller!) for individual list
def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items':items})