from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Weibostatus
# Create your views here.

def _paginate(request, paginator):
    page = request.GET.get('page', 1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return page, items



def index(request):
    return render(request, 'index.html')


def search(request):
    q = request.GET.get('q', '')
    title = ''
    if q:
        title = 'search: "%s"' % q
    return render(request, 'search.html', {
        'title': title,
        'q': q,
    })


def weibos(request):
    qs_weibos = Weibostatus.objects.order_by('-date_published')
    paginator = Paginator(qs_weibos, 50)
    page, weibos = _paginate(request, paginator)
    return render(request, 'weibos.html', {
        'title': 'Weibo Data Statistic',
        'weibos': weibos,
        'paginator': paginator,
        'page': page,
    })


