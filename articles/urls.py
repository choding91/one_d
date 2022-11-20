from django.urls import path
from articles import views


urlpatterns = [
    path("", views.ArticleView.as_view(), name="article_view"),
    path("<int:article_id>/", views.ArticleDetailView.as_view(), name="article_detail_view"),
    path("like/", views.LikeView.as_view(), name="like_view"),
    path("<int:article_id>/like/", views.ArticleLikeView.as_view(), name="article_like_view"),
    path("<int:article_id>/comment/", views.ArticleCommentView.as_view(), name="article_comment_view"),
    path("<int:article_id>/comment/<comment_id>/", views.ArticleCommentDetialView.as_view(), name="article_comment_detail_view"),
]
