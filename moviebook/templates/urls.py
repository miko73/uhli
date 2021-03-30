from django.urls import path, include
from moviebook import views
from moviebook import url_handlers

urlpatterns = [	
    path("film_index/", views.FilmIndex.as_view(), name="filmovy_index"),
    path("zanr_index/", views.ZanrIndex.as_view(), name="zanrovy_index"),
    path("platba_index/", views.PlatbaIndex, name="platba_index"),
    path("<int:pk>/platba_detail/", views.CurrentPlatbaView.as_view(), name="platba_detail"),
    path("<int:pk>/edit_platba/", views.EditPlatba.as_view(), name="edit_platba"),
    path("<int:pk>/film_detail/", views.CurrentFilmView.as_view(), name="filmovy_detail"),
    path("<int:pk>/zanr_detail/", views.CurrentZanrView.as_view(), name="zanrovy_detail"),
    path("create_film/", views.CreateFilm.as_view(), name="novy_film"),	
    path("create_zanr/", views.CreateZanr.as_view(), name="novy_zanr"),	
    path("<int:pk>/edit_film/", views.EditFilm.as_view(), name="edit_film"),
    path("<int:pk>/edit_zanr/", views.EditZanr.as_view(), name="edit_zanr"),
# sada formulářů pro člena
    # path("clen_index/", views.ClenIndex.as_view(), name="clenove_index"),
    path('clen_index/', views.ClenIndex, name='clenove_index'),
    path("<int:pk>/clen_detail/", views.CurrentClenView.as_view(), name="clen_detail"),
    path("create_clen/", views.CreateClen.as_view(), name="novy_clen"),
    path("<int:pk>/edit_clen/", views.EditClen.as_view(), name="edit_clen"),
    path("<int:pk>/db_tests/", views.DbTestClen.as_view(), name="db_tests"),
    
# standardni formsy pro spravu uzivatelu
    path("register/", views.UzivatelViewRegister.as_view(), name = "registrace"),
    path("login/", views.UzivatelViewLogin.as_view(), name = "login"),
    path("logout/", views.logout_user, name = "logout"),
    path("", url_handlers.index_handler),
]