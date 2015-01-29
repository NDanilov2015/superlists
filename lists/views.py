from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.

# View (i.e. controller) for home page
# Не понимаю, зачем при запросе домашней страницы POST писать? Или он один раз запросится когда первичо вызываешь, и еще раз после нажатия Enter при отправке формы7 (И тогда в БД будет создан элемент)
def home_page(request):
	return render(request, 'home.html')

# View (i.e. controller!) for individual list
def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	return render(request, 'list.html', {'list':list_})

# View (i.e.controller!) for a new list
def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
	
def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))