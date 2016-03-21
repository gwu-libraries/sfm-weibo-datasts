from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Weibostatus
from datetime import datetime
from django.db import connection

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
    return render(request, 'index.html', {
        'title': 'Rainbow Colors Life',
        })


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        start_date = request.GET['start_date']
        end_date = request.GET['end_date']
        start_date_object = None
        end_date_object = None

        qs_weibos=[]
        if start_date:
            start_date_object = datetime.strptime(start_date, '%m-%d-%Y')
        if end_date:
            end_date_object = datetime.strptime(end_date, '%m-%d-%Y')

        if start_date_object and not end_date_object:
            qs_weibos = Weibostatus.objects.filter(screen_name=q, date_published__gte=start_date_object).order_by('-date_published')
        elif end_date_object and not start_date_object:
            qs_weibos = Weibostatus.objects.filter(screen_name=q, date_published__lte=end_date_object).order_by('-date_published')
        elif not end_date_object and not start_date_object:
            qs_weibos = Weibostatus.objects.filter(screen_name=q).order_by('-date_published')
        elif end_date_object and start_date_object:
            qs_weibos = Weibostatus.objects.filter(screen_name=q,
                                                   date_published__range=(start_date_object, end_date_object)).order_by('-date_published')

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT DATE_TRUNC('day', date_published) AS day, COUNT(*) AS item_count "
                           "FROM datasts_weibostatus WHERE screen_name = %s GROUP BY 1 ORDER BY day ", [q])
            daily_counts = [[row[0].strftime('%Y-%m-%d'), int(row[1])]
                            for row in cursor.fetchall()]
        except:
            daily_counts=[]

        title = q
        weibo_count= qs_weibos.count()
        paginator = Paginator(qs_weibos, 30)
        page, weibos = _paginate(request, paginator)
        search_url = "q="+request.GET['q']+"&start_date="+request.GET['start_date']+"&end_date="+request.GET['end_date']

        """
        daily_counts=[['03-02-2016',120],['03-01-2016',200],['03-05-2016',600],['03-07-2016',110],
                      ['02-02-2016',100],['02-01-2016',222],['02-05-2016',900],['02-07-2016',110],
                       ['02-02-2016',100],['02-01-2016',222],['02-05-2016',900],['02-07-2016',110],
                       ['02-02-2016',100],['02-01-2016',222],['02-05-2016',900],['02-07-2016',110]]
        """
        return render(request, 'search.html', {
            'weibos': weibos,
            'weibo_count':weibo_count,
            'title': title,
            'daily_counts': daily_counts,
            'paginator': paginator,
            'page': page,
            'search_url': search_url,
        })
    else:
        return render(request, 'search.html', {
        'title': 'Weibo Data Statistic',
        'error': True,
        })


def weibos(request):
    qs_weibos = Weibostatus.objects.order_by('-date_published')
    weibo_count= qs_weibos.count()
    screen_name_set = Weibostatus.objects.order_by().values('screen_name').distinct()
    paginator = Paginator(qs_weibos, 30)
    page, weibos = _paginate(request, paginator)
    return render(request, 'weibos.html', {
        'title': 'Weibo Data Statistic',
        'screen_name_set': screen_name_set,
        'weibos': weibos,
        'weibo_count':weibo_count,
        'paginator': paginator,
        'page': page,
    })
