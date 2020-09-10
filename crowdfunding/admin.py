from django.contrib import admin

from .models import Order, Reward, Update, Question, Value
from .forms import AdminOrderForm, AdminRewardForm, AdminUpdateForm
from .forms import AdminQuestionForm, AdminValueForm

admin.site.register(Order, AdminOrderForm)
admin.site.register(Reward, AdminRewardForm)
admin.site.register(Update, AdminUpdateForm)
admin.site.register(Question, AdminQuestionForm)
admin.site.register(Value, AdminValueForm)
