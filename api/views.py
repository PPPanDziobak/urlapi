from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from urltask.models import Url
from .serializers import UrlSerializer


@api_view(['POST'])
def change_url(request):
    serializer = UrlSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def revert_url(request):
    output_url = request.data.get('output_url')
    if output_url:
        try:
            url_instance = Url.objects.get(output_url=output_url)
            return Response({'input_url': url_instance.input_url})
        except Url.DoesNotExist:
            return Response({'message': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'message': 'Missing output_url'}, status=status.HTTP_400_BAD_REQUEST)
