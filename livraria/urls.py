from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autor/', include('autor.urls')),
    path('livros/', include('livro.urls')),
    path('', include('index.urls'))
]
