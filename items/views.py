from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Items
from .forms import NewItemsForms

@login_required
def Detail(request, pk):
   item = get_object_or_404(Items, pk=pk )
   related_items = Items.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
   return render(request, 'item/detail.html', {
    "item":item,
    'related_items':related_items
   })

@login_required
def NewItems(request):
   if request.method == 'POST':
     form = NewItemsForms(request.POST, request.FILES)

     if form.is_valid():
       item = form.save(commit=False)
       item = created_by = request.user
       item.save()
       return redirect('/', pk=item.id)
   else:
     form = NewItemsForms()

   return render(request, 'item/form.html', {
      'form':form
   })