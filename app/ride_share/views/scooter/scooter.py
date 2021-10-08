from rest_framework.views import APIView
from rest_framework.response import Response

from ride_share.utility.utility import find_nearest_vehicle

class ScooterView(APIView):
    """
    View to order a scooter
    """
    def order_scooter(self, search_radius):
        find_nearest_vehicle(search_radius, "scooter")

    def get(self, request, format=None):
        """
        Order a scooter within a certain radius.
        """
        self.order_scooter()
        return Response(["Scooter view"])
