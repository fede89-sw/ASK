from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'questions', views.QuestionAPIModelView)


urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/answer/', views.AnswerCreateAPIView.as_view(), name="create-answer"),
    path('questions/<slug:slug>/answers/', views.AnswersListAPIView.as_view(), name="answers-list"),
    path('answers/<int:pk>/', views.AnswerRUDApiView.as_view(), name="answer-detail"),
    path('answers/<int:pk>/like/', views.AnswerLikeAPIView.as_view(), name="answer-like")
]