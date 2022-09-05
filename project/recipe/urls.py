from django.urls import path
from .views import *


urlpatterns = [
    path('', RecipeList.as_view(), name='index'),           # path orqali url yo'nalish berilyapdi va views dagi index (indexni ArticleList ga o'zgartirdik) classini olyapdi va nomi index bosin
    path('category/<int:pk>/', RecipeListByCategory.as_view(), name='category_list'),
    path('recipe/<int:pk>', RecipeDetails.as_view(), name='recipe_detail'),
    path('new/', NewArticle.as_view(), name='add_article'),           # views dagi add_article(NewArticle ga o'zgartirdik) classini olyapdi
    path('search/', SearchResults.as_view(), name='search_results'),
    path('article/<int:pk>/update', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
    path('profile/', profile, name='profile'),            # views dagi profile def ni olyapdi va nomi profile bosin
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', registration, name='register'),
    path('programmer/', programmer, name='programmer')
]


