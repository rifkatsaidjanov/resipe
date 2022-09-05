from django import template
from recipe.models import Categorie                  # models dan Categorie class ni chaqirdik
from django.db.models import Count                   # Sanash metodini chaqirdik
register = template.Library()                        # Yangi kutubxona yaratdik


@register.simple_tag()                                                # recipes_tags.py ni Djangoga registratsiya qildik.
def get_all_categories():                                            # Xamma categoryalarni ob beruvchi funcsiya
    categories = Categorie.objects.annotate(Count('recipe'))        # Categoriyalarni sanab berdi
    return categories