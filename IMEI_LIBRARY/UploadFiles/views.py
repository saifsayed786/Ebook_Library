from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Document
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


class HomePageView(TemplateView):
    template_name = 'UploadFiles/home.html'


class NewSearchResultView(ListView):
    model = Document
    template_name = 'UploadFiles/newsearchresult.html'
    context_object_name = 'all_posts'

    def get_context_data(self, *args, **kwargs):
        context = super(NewSearchResultView, self).get_context_data()
        context['query'] = self.request.GET.get('query')
        context['all'] = Document.objects.all().count()
        return context

    def get_queryset(self):
        query = self.request.GET.get('query')
        if len(query)>60:
            object_list = Document.objects.none()
        else:
            object_list = Document.objects.filter(
                Q(eBookData__icontains=query)|Q(eBookName__icontains=query)|Q(category__icontains=query)|Q(author__icontains=query)
                ).order_by('id')
            
        paginator = Paginator(object_list, 3) # Show 3 books per page
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            object_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 999), deliver last page of results.
            object_list = paginator.page(paginator.num_pages)

        return object_list
class BrowseSearchView(TemplateView):
    template_name = 'UploadFiles/browseSearch.html'

class BrowseSearchResultView(ListView):
    model = Document
    template_name = 'UploadFiles/browsesearchresult.html'
    context_object_name = 'all_posts'


    def get_context_data(self, *args, **kwargs):
        context = super(BrowseSearchResultView, self).get_context_data()
        context['query'] = self.request.GET.get('query')
        context['all'] = Document.objects.all().count()
        return context


    def get_queryset(self):
        query = self.request.GET.get('query')
        if len(query)>60:
            object_list = Document.objects.none()
        else:
            object_list = Document.objects.filter(
                Q(eBookName__icontains=query)|Q(category__icontains=query)|Q(author__icontains=query)
                ).order_by('id')

            
        paginator = Paginator(object_list, 3) # Show 3 books per page
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            object_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 999), deliver last page of results.
            object_list = paginator.page(paginator.num_pages)
        return object_list
    

class ListingSearchView(TemplateView):
    template_name = 'UploadFiles/listingsearch.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ListingSearchView, self).get_context_data()
        context['query'] = self.request.GET.get('query')
        context['glossary_filters'] = ['All','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        return context

class ListingSearchResultView(ListView):
    model =Document
    template_name = 'UploadFiles/listingsearchresult.html'
    context_object_name = 'all_posts'

    def get_context_data(self,*args,**kwargs):
        context = super(ListingSearchResultView, self).get_context_data()
        context['query'] = self.request.GET.get('query')
        context['glossary_filters'] = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        context['all'] = Document.objects.all().count()
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('query')
        if len(query)>60:
            object_list = Document.objects.none()
        else:
            object_list = Document.objects.filter(
                Q(eBookName__istartswith=query)
                ).order_by('id')

            
        paginator = Paginator(object_list, 3) # Show 3 books per page
        page = self.request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            object_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 999), deliver last page of results.
            object_list = paginator.page(paginator.num_pages)
        return object_list

