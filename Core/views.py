from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "Public endpoint working."})

@api_view(['GET'])
def protected_api(request):
    return Response({"message": f"Hello, {request.user.username}"})
