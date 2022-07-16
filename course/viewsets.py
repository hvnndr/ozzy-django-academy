from rest_framework import viewsets
from course import serializers, models

class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all() # SELECT * FROM course;
    serializer_class = serializers.CourseSerializer
