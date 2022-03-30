from rest_framework.decorators import api_view
# where we define what request time the function can handle
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def cars_list(request):

    return Response('ok')
