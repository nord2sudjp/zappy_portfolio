from django.urls import path
from . import views

# Blog Pathの計画
# urls.pyへパスのパターンを追加
# viewsへ関数追加
# renderするhtmlを追加
# renderへモデルを渡す
# htmlでモデルを展開

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail')
    ]
