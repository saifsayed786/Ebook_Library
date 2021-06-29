from django.urls import path
from .views import HomePageView,NewSearchResultView,BrowseSearchView,BrowseSearchResultView,ListingSearchView,ListingSearchResultView
urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path("NewsearchResult/", NewSearchResultView.as_view(), name="newsearchresult"),
    path('browseSearch/',BrowseSearchView.as_view(),name='browse'),

    path("browsesearchresult/",BrowseSearchResultView.as_view(),name="browse_result"),
    path("A-Z_Search/", ListingSearchView.as_view(), name="A-Z_Search"),
    path("A-Z_SearchResult/",ListingSearchResultView.as_view(),name="listingsearchresult"),


]