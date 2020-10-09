# urls.py
from django.urls import path
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    TopDistanceByMonth, \
                    Top5AirportsFrtByDestination, \
                    Top5AirportsFrtByOrigin, \
                    Top5AirportsMailByOrigin, \
                    Top5AirportsMailByDestination, \
                    Top5AirportsDistanceByOrigin,\
                    Top5AirportsDistanceByDestination,\
                    TopPassengersByMonth, \
                    TopFreightByMonth, \
                    TopPassengersByAirline, \
                    TopMailByAirline, \
                    TopDistanceByAirline, \
                    TopPassengersByMonthByAirline, \
                    AveragePassengersByDestination, \
                    AverageFreightByOrigin, \
                    MaxFreightByLongestDistance, \
                    MaxMailByShortestDistance



urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('top5frtorigin/',
        Top5AirportsFrtByOrigin.as_view(
            extra_context={'title': "Top 5 Aiports - Freight by Origin Airport"}
        ),
        name="top5frtorigin"),
    path('top5frtdestination/',
        Top5AirportsFrtByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}
        ),
        name="top5frtdestination"),
    path('top5mailorigin/',
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
        ),
        name="top5mailbyorigin"),
    path('top5maildestination/',
        Top5AirportsMailByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}
        ),
        name="top5mailbydestination"),
    path('top5distbyorigin/',
        Top5AirportsDistanceByOrigin.as_view(
            extra_context={'title': "top 5 Airports - Distance by Origin Airport"}
        ),
        name="top5distbyorigin"),
    path('top5distbydestination/',
        Top5AirportsDistanceByDestination.as_view(
            extra_context={'title': "top 5 Airports - Distance by Destination Airport"}
        ),
        name="top5distbydest"),
    path('toppax_month/',
        TopPassengersByMonth.as_view(
            extra_context={'title': "Top Passengers by Month"}
        ),
        name="toppax_month"),
    path('topfrt_month/',
        TopFreightByMonth.as_view(
            extra_context={'title': "Top Freight by Month"}
        ),
        name="topfrt_month"),    
    path('toppax_total/',
        TopPassengersByAirline.as_view(
            extra_context={'title': "Top Airline by Passengers"}
        ),
        name="toppax_total"),
    path('topmail_total/',
        TopMailByAirline.as_view(
            extra_context={'title': "Top Airline by Mail"}
        ),
        name="topmail_total"),
    path('topdist_total/',
        TopDistanceByAirline.as_view(
            extra_context={'title': "Top Airline by Distance"}
        ),
        name="topdist_total"),
    path('toppax_byairline/',
        TopPassengersByMonthByAirline.as_view(
            extra_context={'title': "Top Passengers by Month By Airline"}
        ),
        name="toppax_byairline"),
    path('avgpax_bydest/',
        AveragePassengersByDestination.as_view(
            extra_context={'title': "Average Passengers by Airline"}
        ),
        name="avgpax_bydest"),
    path('avgfrt_byorig/',
        AverageFreightByOrigin.as_view(
            extra_context={'title': "Average Freight by Airline"}
        ),
        name="avgfrt_byorig"),
    path('maxfrt_dist/',
        MaxFreightByLongestDistance.as_view(
            extra_context={'title': "Max Freight by Longest Distance"}
        ),
        name="maxfrt_dist"),
    path('maxmail_dist/',
        MaxMailByShortestDistance.as_view(
            extra_context={'title': "Max Mail by Shortest Distance"}
        ),
        name="maxmail_dist"
    ),
]