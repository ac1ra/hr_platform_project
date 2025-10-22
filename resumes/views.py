# from rest_framework import viewsets
from rest_framework import viewsets,permissions
from .custom_permissions import IsOwnerOrAdmin
from .models import Resume
from .serializers import ResumeSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action != "create":
            return [IsOwnerOrAdmin()]
        return super().get_permissions()
    
    def get_queryset(self):
        try:
            if not self.request.user.is_staff or not self.request.user.is_superuser:
                return Resume.objects.filter(user_id=self.request.user)
        except Exception:
            return Resume.objects.none()
        return super().get_queryset()