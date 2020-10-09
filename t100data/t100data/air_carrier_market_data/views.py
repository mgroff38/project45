# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum, Avg, Min, Q

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"
# What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsFrtByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_frt=Sum('freight')) \
                        .order_by('-total_frt')[0:5]
    template_name="rankorder_list_origin_frt.html"
# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFrtByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_frt=Sum('freight')) \
                        .order_by('-total_frt')[0:5]
    template_name="rankorder_list_destination_frt.html"
# What are the top 5 airports in the terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_origin_mail.html"
# What airline carred the most mail
class TopMailByAirline(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:1]
    template_name="rankorder_list_mail_total.html"
# What airline traveled the furthest distance
class TopDistanceByAirline(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name') \
                        .annotate(total_dist=Sum('distance')) \
                        .order_by('-total_dist')[0:1]
    template_name="rankorder_list_distance_total.html"                    
# What airline carried the most passengers
class TopPassengersByAirline(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name')\
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:1]
    template_name="rankorder_list_passengers_total.html"    
# What are the top 5 airports in terms of: total mail by destination
class Top5AirportsMailByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_destination_mail.html"
#Top 5 airports distance by origin
class Top5AirportsDistanceByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_dist=Sum('distance')) \
                        .order_by('-total_dist')[0:5]
    template_name="rankorder_list_origin_distance.html"
#Top 5 airports by distance and destination
class Top5AirportsDistanceByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .annotate(total_dist=Sum('distance')) \
                        .order_by('-total_dist')[0:5]
    template_name="rankorder_list_destination_distance.html"
# Which airport reported the most passengers by month?
class TopPassengersByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_passengers_month.html"

    def get_queryset(self):

        month_list = []

        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Max('passengers')) \
                .order_by('-total_passengers')[0:1]

            month_list.append(queryset)
        return month_list
#Total Passengers by month
class TopPassengersByMonthByAirline(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_passengers_month.html"
    def get_queryset(self):
        month_list = []
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name','month') \
                .filter(carrier_name__in=['American Airlines Inc.','Southwest Airlines Co.','United Air Lines Inc.','Delta Air Lines Inc.','Alaska Airlines Inc.']) \
                .filter(month__exact=month) \
                .annotate(total_pax=Sum('passengers')) \
                .order_by('-total_pax')[0:5]
            month_list.append(queryset)
        return month_list
# Which airport reported the most freight by month?
class TopFreightByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_freight_month.html"
    def get_queryset(self):
        month_list = []
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_freight=Max('freight')) \
                .order_by('-total_freight')[0:1]
            month_list.append(queryset) 
        return month_list   
#Average Freight by origin
class AverageFreightByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .filter(orig_iata_code__in=['MIA','MEM','JFK','ANC','SDF']) \
                        .annotate(average_frt=Avg('freight')) \
                        .order_by('-average_frt')
    template_name="average_freight_origin.html"
#Most Mail by shortest distance
class MaxMailByShortestDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_city_name','dest_city_name','distance') \
                        .annotate(total_mail=Max('mail')) \
                        .filter(~Q(distance=0)) \
                        .order_by('distance','-total_mail')[0:1] 
    template_name="max_mail_by_distance.html"
#Max Freight by longest distance
class MaxFreightByLongestDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_city_name','dest_city_name','freight') \
                        .annotate(total_dist=Max('distance')) \
                        .order_by('-total_dist','-freight')[0:1]
    template_name="max_freight_by_distance.html"
#Average Passengers by destination
class AveragePassengersByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('dest_iata_code','dest_city_name') \
                        .filter(dest_iata_code__in=['LAX','ATL','SFO','DFW','ORD']) \
                        .annotate(average_pax=Avg('passengers')) \
                        .order_by('-average_pax')
    template_name="average_passengers_destination.html"
# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

