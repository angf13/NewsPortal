from django import template


register = template.Library()


censor_filter = ['бля', 'идиот', 'придурок', 'дрянь']


@register.filter()
def censor(word):
    if isinstance(word, str):
        for a in word.split():
            if a.capitalize() in censor_filter:
                word = word.replace(a, a[0] + '*' * len(a))
    return word