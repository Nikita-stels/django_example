from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Category


def category_list(request):
    if request.method == 'GET':
        root_cats = Category.objects.filter(parent_id=None).all()
        all_cats = Category.objects.all()
        data = {'root_cats': root_cats, 'all_cats': all_cats}
        return render(request, 'test_work/category_list.html', data)
    elif request.method == 'POST':
        par_id = request.POST.get('parent')
        if par_id:
            Category.objects.create(name=request.POST.get('name'), parent_id=par_id)
        else:
            Category.objects.create(name=request.POST.get('name'))
        return redirect('./')


def category_page(request):
    if request.method == 'GET':
        obj = Category.objects.filter(id=request.GET.get('id')).first()
        root_cats = Category.objects.filter(parent_id=None).all()
        data = {'root_cats': root_cats, 'category': obj}
        return render(request, 'test_work/category_page.html', data)
    elif request.method == 'POST':
        obj = Category.objects.filter(id=request.POST.get('id')).first()
        obj.name = request.POST.get('name')
        obj.save()
        return HttpResponseRedirect(f'category?id={obj.id}')


def del_category(request):
    Category.objects.filter(id=request.GET.get('id')).delete()
    return JsonResponse({'status': True})
