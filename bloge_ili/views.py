from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
data_naprimer = [{"id":1,"title":"moi ded","content":"plotniy bumchik ya lutal","is_published":False},
                 {"id":2,"title":"geroicheski geroi","content":"vot blin","is_published":True},
                 {"id":3,"title":"hairabezol","content":"ti ne tuda voyuesh","is_published":True}]
def opachki(request):
    return HttpResponse("<h1>Error 404</h1>")
def way_of_nothing(reuest):
    return HttpResponse("посто текст")
def shef_uzbek(request):
    return HttpResponse("Кавабагна")
def login(request):
    return HttpResponse("<h1>layla v tanka novaya meta</h1><p>")
def katya_sluk(request,indexsl):
    return HttpResponse(f"<h1>ya lesli v reiting vozmu na 1-st pik</h1><p>{indexsl}</p>")
def page_not_found(request,exception):
    return HttpResponseNotFound("<h1>oshipka prirodi </h1>")
def houm_paij(request):
    menu = [
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
    ]
    dapa = {"meta":"мeтой декабря считается: Хаябуса, Суе, Ванван, Джусинь, Чип, Джой, Фанни","pytle":"мейнер Хуфры","menu":menu,
            "posts":data_naprimer}
    return render(request,"bloge_ili/index.html",context = dapa)
def shpaga_praga(request):
    data = {"posts":data_naprimer}
    return render(request,"bloge_ili/sun_templata.html",context = data)
def sho_post(request,postid):
    return HttpResponse(f"otobrazit postich numbir ili s aydi takim-to {postid}")
