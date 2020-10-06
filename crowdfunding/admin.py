from django.contrib import admin

from .models import Order, Reward


class AdminOrderForm(admin.ModelAdmin):
	list_display = ('name', 'amount', 'created_at')

	# def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
	# 	field = super(AdminOrderForm, self).formfield_for_foreignkey(
	# 		db_field, request, **kwargs)
	# 	if db_field.rel.to == Reward:
	# 		field.label_from_instance = self.get_reward_name
	# 	return field

	def get_reward_name(self, reward):
		return reward.name

admin.site.register(Order, AdminOrderForm)

class AdminReward(admin.ModelAdmin):
	list_display = ('name', 'min_amount')

admin.site.register(Reward, AdminReward)