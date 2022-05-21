
from django.contrib import admin
from django.urls import path
from core import views as core_views
from Odontologo import views as odonto_views
from Especialidad import views as espe_views
from Contacto import views as contacto_views
#from portfolio import views as portfolio_views
#from contact import views as contact_views
#from blog import views as blog_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about-us/', odonto_views.nosotros, name="about"),
    path('Servicios/', espe_views.especialidad, name="espcialidad"),
    #path('blog/', blog_views.blog, name="blog"),
    #path('blog/<int:id>', blog_views.blog_detail, name="blog_detail"),
    path('contacto/', contacto_views.contacto, name="contacto"), 
    path('admin/', admin.site.urls, name="admin"),
    path('admin/logout', admin.site.logout)
]

admin.site.site_header = "Administrador de Servioral"
admin.site.site_title = "ServiSIS portal Administrador"
admin.site.index_title = "Bienvenido al gestor de citas ServiSIS  "

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
