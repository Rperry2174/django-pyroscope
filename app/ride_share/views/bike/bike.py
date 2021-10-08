from rest_framework.views import APIView
from rest_framework.response import Response


class BikeView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        print("testview is happening")
        return Response(["Bike view"])
