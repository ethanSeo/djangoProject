from django.db.models import Q #Filter에서 OR 조건 쓸 때 --> querySet.filter( Q(field1__icontains=~ | Q(field2__icontains=~)
from django.shortcuts import render, get_object_or_404
from .models import Category


def post_list(request):
    qs = Category.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(Q(kr_name_category__icontains=q) | Q(name_category__icontains=q))

    return render(request, 'blog/post_list.html',
        {
            'category_list': qs,
            'q': q
        }
    )

def post_detail(request, id):

    #category = Category.objects.get(id=id)

    category = get_object_or_404(Category, id=id)
    return render(request, 'blog/post_detail.html',
        {'category': category }
    )
# Create your views here.
