
from django.shortcuts import  get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from .choices import prices_choices, bedroooms_choices, state_choices

from .models import Listings

def index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_publish= True)
    paginator = Paginator(listings, 6 )
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings\listings.html', context)

def listing(request, listing_id):
    listings = get_object_or_404(Listings, pk=listing_id)
    context = {
        'listings': listings
    }
    return render(request, 'listings\listing.html', context)

def search(request):
    queryset_list = Listings.objects.order_by('-list_date')
    #keywords
    #prices
    if 'price' in request.GET:
        price= request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price) 

    if 'anywords' in request.GET:
        anywords= request.GET['anywords']
        if anywords:
            queryset_list = queryset_list.filter(description__icontains=anywords) 
      #City
    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
     #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms= request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

     #state
    if 'state' in request.GET:
        state= request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

  

   
    context ={
    'state_choices': state_choices,
    'prices_choices': prices_choices,
    'bedrooms_choices': bedroooms_choices,
    'listings': queryset_list,
    'values': request.GET

    }  
    return render(request, 'listings\search.html', context)


    