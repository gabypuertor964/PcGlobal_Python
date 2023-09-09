from django import template

register = template.Library()

@register.filter
def price_format(value):
    # Formatear el valor con punto como separador de miles y coma como separador decimal
    formatted_value = '{:,.2f}'.format(value).replace(',', ';').replace('.', ',').replace(';', '.')
    
    # Agregar el símbolo de moneda (por ejemplo, $) al principio
    formatted_value = f'$ {formatted_value} COP'
    
    return formatted_value