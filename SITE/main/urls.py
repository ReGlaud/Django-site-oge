from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.math),
    path('math/', views.math),
    path('physics/', views.physics),
    path('informatics/', views.informatics),
    path('task/math/<int:pk>/', views.TaskMath.as_view(), name='task_m'),
    path('task/physics/<int:pk>/', views.TaskPhysics.as_view(), name='task_p'),
    path('task/informatics/<int:pk>/', views.TaskInformatics.as_view(), name='task_i'),
    path('end/math/<int:pk>/', views.End_m.as_view(), name='end_m'),
    path('end/physics/<int:pk>/', views.End_p.as_view(), name='end_p'),
    path('end/informatics/<int:pk>/', views.End_i.as_view(), name='end_i'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)