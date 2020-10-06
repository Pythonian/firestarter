import datetime

from django.shortcuts import render
from django.db.models import Sum
from django.conf import settings

from .models import Order, Reward

def intWithCommas(x):
	if x < 0:
		return '-' + intWithCommas(-x)
	result = ''
	while x >= 1000:
		x, r = divmod(x, 1000)
		result = ",%03d%s" % (r, result)
	return "%d%s" % (x, result)

def get_context():
	total = Order.objects.all().aggregate(Sum('amount'))['amount__sum']
	pct = ((100 * float(total) / float(settings.GOAL)) if total else 0)
	c = {
		'activepage': 'home',
		'goal': intWithCommas(settings.GOAL),
		'backers': Order.objects.count(),
		'pct': pct,
		'pct_disp': (int(pct) if total else 0),
		'total': (intWithCommas(int(total)) if total else '0'),
		'nopay': (True if settings.STOP and (settings.DATE - datetime.datetime.now()).days < 0 else False),
		'days': (settings.DATE - datetime.datetime.now()).days,
		'rewards': sorted(Reward.objects.all(), key=lambda i: i.min_amount),
		'proj_name': settings.PROJECT_NAME,
		'proj_addr': settings.PROJECT_ADDR
		}
	return c

def home(request):
	return render(request, 'home.html', get_context())

def choose(request):
	proj_name = settings.PROJECT_NAME
	pay_types = settings.PAY_TYPES
	if settings.STOP and (settings.DATE - datetime.datetime.now()).days < 0:
		msg = 'The funding campaign is complete and is no longer accepting new contributions.'
		return render(request, 'error.html', locals())
	else:
		return render(request, 'payment/choose.html', locals())
