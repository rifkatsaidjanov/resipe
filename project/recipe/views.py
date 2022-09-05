from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Recipe, Categorie
from .forms import ArticleForm, LoginForm, RegistrationForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages                     # alert chiqishi uchun


# def index(request):
#     recipes = Recipe.objects.all()                  # bu malumotlar omboridagi Recipe calssini xamma obektlarini olyapdi
#
#     content = {
#         'recipes': recipes
#     }
#     return render(request, 'recipe/recipe_list.html', content)        #  render-> HTML stranitsa chizib berish uchun
#                                                                       # yani HTML orqali contentni chiqaramiz
#                                                                       # content esa malumotlar omboridagi malumotlar
# Funcsiyada qilinganlarni endi kalassda qib chiqamiz
class RecipeList(ListView):  # bosh saxifaniki
    model = Recipe
    context_object_name = 'recipes'
    # template_name = 'recipe/all_recipes'                  # --> html faylni nomini o'zgartirishni xoxlamasak (qaysi html ni ishlatamiz)

    paginate_by = 6             # saxifada nechta maqola ko'rinishi

    def get_queryset(self):
        return Recipe.objects.filter(is_published=True).select_related('category')  # select_related saytni ishlashini tezlashtirdi


# def category_list(request, pk):
#     recipes = Recipe.objects.filter(category_id=pk)                  # bu malumotlar omboridan recipe ni xamma obektlarini olyapdi
#
#     content = {
#         'recipes': recipes
#     }
#     return render(request, 'recipe/recipe_list.html', content)        #  render-> HTML stranitsa chizib berish uchun
#                                                                 # yani HTML orqali contentni chiqaramiz
#                                                                 # content esa malumotlar omboridagi malumotlar
# Funcsiyada qilinganlarni endi kalassda qib chiqamiz
class RecipeListByCategory(RecipeList):                          # tepadagi RecipeList classidan meros olamiz
    def get_queryset(self):
        return Recipe.objects.filter(                                # Recipe jadvalidan categoriyalarni id si bo'yicha filter qilib ber
            category_id=self.kwargs['pk'], is_published=True
        ).select_related('category')                                # Recipe dagi categoriya bilan maqolalarni ulab ket

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()                         # tepa qatordagi get_context_data dan meros olamiz
        category = Categorie.objects.get(pk=self.kwargs['pk'])       # modelsdagi Categorie classini obektlari olinyapdi (id bo'yicha)
        context['title'] = category.title                            # context title kaliti bo'yicha tenglashadi categoryni title liga
        return context


# def recipe_detail(request, pk):
#     recipe = Recipe.objects.get(pk=pk)          # bu malumotlar omboridagi (yani modelsdan) Recipe classdan idsi orqali element olyapdi
#     context = {
#         'title': recipe.title,
#         'recipe': recipe
#     }
#     return render(request, 'recipe/recipe_detail.html', context)

# Funcsiyada qilinganlarni endi kalassda qib chiqamiz
class RecipeDetails(DetailView):
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(pk=self.kwargs['pk'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        context['title'] = f"Maqola {recipe.title}"
        return context


# def add_article(request):                                              # form yatatish uchun def
#     if request.method == 'POST':
#         form = ArticleForm(data=request.POST)                          # requestdan kegan POST malumotni formga tengladik
#         if form.is_valid():                                            # is_valid--> formamiz tog'ri to'ldirilgan bo'lsa
#             article = Recipe.objects.create(**form.cleaned_data)       # modelsdagi Recipe jadvalidagi create ni ishga tushuryapdi. Yani form bo'yicha yaratib beryapdi
#             article.save()                                             # article ni saxranit qildik
#             return redirect('index')                                   # redirect--> form to'g'ri to'ldirilganda bosh saxifaga jo'natib yuboradi
#     else:
#         form = ArticleForm
#
#     context = {
#         'form': form,
#         'title': "Maqola qo'shish"
#     }
#     return render(request, 'recipe/add_article.html', context)

# Funcsiyada qilinganlarni endi kalassda qib chiqamiz
# Maqola qo'shish
class NewArticle(CreateView):
    form_class = ArticleForm  # forms.py dagi ArticleForm kelyapdi
    template_name = 'recipe/add_article.html'  # qaysi html ni ishlatamiz
    extra_context = {
        'title': "Maqola qo'shish"
    }
    success_url = reverse_lazy('index')  # form to'ldirilgandan keyin qaysi saxifadan chiqishi

# xar bir odam o'z maqolasini o'chira olishi uchun
    def form_valid(self, form):
        form.instance.author = self.request.user        # formani kiritgan avtor teng bo'sin so'rov jo'natgan foydalanuvchiga
        return super().form_valid(form)                 # form_valid ga tepa qatordagi form ni dobavit qildik


# Qidirish
class SearchResults(RecipeList):  # tepadagi RecipeList classidan meros olamiz
    def get_queryset(self):
        word = self.request.GET.get('q')  # foydalanuvchi inputga yozgan so'zni olamiz. (navbardagi inputni name mi 'q')
        article = Recipe.objects.filter(  # Recipe dan filter qil foydalanuvchi yozgan so'zni
            Q(title__icontains=word) | Q(content__icontains=word), is_published=True  # texti va title bo'yicha qiridari
        )
        return article


# O'zgartirish
class ArticleUpdate(UpdateView):
    model = Recipe
    form_class = ArticleForm  # froms.py dagi ArticleForm kelyapdi
    template_name = 'recipe/add_article.html'  # qaysi html ni ishlatamiz

# O'chirish
class ArticleDelete(DeleteView):
    model = Recipe
    context_object_name = 'recipe'  # tepa qatordagi modelni nomini recipe deb qo'ydik
    success_url = reverse_lazy('index')

# profil saxifasi uchun
@login_required
def profile(request):
    return render(request, 'recipe/profile.html', {'title': 'Sizning profil'})


# kirish saxifasi uchun
def user_login(request):
    if request.method == 'POST':                                             # agar zapros POST bo'lsa
        form = LoginForm(data=request.POST)                                  # so'rov jo'natgan foydalanuvchini post zaprosiga tenglashadi
        if form.is_valid():                                                  # agar form to'g'ri yozilgan bo'sa
            user = form.get_user()                                           # foydalanuvchini formi = bo'sin user ga
            if user:                                                             # agar user bo'lsa
                login(request, user)                                             # login qil so'rov va foydalanuvchini
                messages.success(request, "Siz muvaffaqiyatli o'tdingiz")        # alertda yozuv chiqsin
                return redirect('index')                                         # o'xshasa bosh saxifaga qaytsin
            else:
                messages.error(request, "Xatolik")                                  # alertda xatolik chiqsin
                return redirect('login')                                            # O'xshasa login saxifaga qaytsin
        else:
            messages.error(request, "Xatolik")
            return redirect('login')
    else:
        form = LoginForm()                                                    # forms.py dagi LoginForm ni olyapdi
        context = {
            'title': 'Foydalanuvchi avtorizatsiyasi',
            'form': form
        }
        return render(request, 'recipe/user_login.html', context)


# chiqish saxifa uchun
def user_logout(request):
    logout(request)
    messages.warning(request, "Sizning akkauntingiz o'chirildi")
    return redirect('index')


# registrationsaxifa uchun
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)       # so'rov jo'natgan foydalanuvchini post zaprosiga tenglashadi
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Akkaunt muvaffaqiyatli yaratildi')
            return redirect('index')
    else:
        form = RegistrationForm()

    context = {
        'title': 'Foydalanuvchi registratsiyasi',
        'form': form
    }
    return render(request, 'recipe/register.html', context)


def programmer(request):
    context = {

    }
    return render(request, 'recipe/programmer.html', context)



