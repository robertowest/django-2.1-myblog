from django import template
from datetime import date, timedelta

register = template.Library()


@register.filter
def fecha_corta(value):
    """ date:"d/m/y" """
    return value.strftime('%d/%m/%y')


@register.filter
def texto_corto(value):
    "devuelve los 150 primeros caracteres"
    """  {{ post.text|slice:"0:150" }}  """
    return value[0:150]


@register.filter
def cuando_se_publico(value):
    delta = value.date() - date.today()

    if delta.days == 0:
        value = "Hoy"

    elif delta.days < 1:
        #value = "Hace %s %s" % (abs(delta.days), ("día" if abs(delta.days) == 1 else "días"))
        if abs(delta.days) == 1:
            value = 'Ayer'
        else:
            value = "Hace %s días" % abs(delta.days)

    elif delta.days == 1:
        value = "Mañana"

    elif delta.days > 1:
        value = "En %s días" % delta.days

    return value


@register.filter
def color_por_fecha(value):
    delta = value.date() - date.today()

    if delta.days == 0:
        value = "#1AA409"    # verde

    elif delta.days < 1:
        value = "#FF0000"   # rojo

    else:
        value = "#B1ADAD"    # gris

    return value
