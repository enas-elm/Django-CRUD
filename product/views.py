from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ItemForm
from .models import Item


def create(request):
    # on range ce que veut envoyer ici
    context = {}
 
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product:index')
 
    # on récupère envoie à la vue le context 'form
    context['form'] = form
    return render(request, "product/create.html", context)




def index (request):
    context = {}

    context['items'] = Item.objects.all()
    return render(request, 'product/index.html', context)




def show(request, id):
    context = {}

    context['item'] = Item.objects.get(id=id)
    return render(request, 'product/show.html', context)




def update(request, id):
    context = {}

    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('product:show', id=id)

    context['form'] = form
    return render(request, 'product/update.html', context)
    # return render(request, 'product/update.html', context)




def delete(request, id):
    context = {}

    item = Item.objects.get(id=id)
    item.delete()

    return render(request, 'product/delete.html', context)

# show, delete