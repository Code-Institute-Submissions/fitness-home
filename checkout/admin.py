from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',
                       'order_total')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total',)

    list_display = ('order_number', 'date', 'full_name', 'order_total')

    ordering = ('-date',)

