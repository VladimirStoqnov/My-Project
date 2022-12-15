from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from cosplay_project.store.forms import ItemCreateFrom
from cosplay_project.store.models import Items


@login_required()
def store(request):
    items = Items.objects.all()

    context = {
        'items': items,

    }

    return render(request, 'store/store-home.html', context)


def add_item(request):
    if request.method == 'GET':
        form = ItemCreateFrom()
    else:
        form = ItemCreateFrom(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()

            return redirect('store')

    context = {
        'form': form,
    }

    return render(request, 'store/add-store-item.html', context)


class EditStoreItem(views.UpdateView):
    template_name = 'store/edit-store-item.html'
    model = Items
    fields = ('item_name', 'description', 'price', 'image', 'type')

    def get_success_url(self):
        return reverse_lazy('store')


class DeleteStoreItem(views.DeleteView):
    template_name = 'store/store-delete-item.html'
    model = Items
    success_url = reverse_lazy('store')
