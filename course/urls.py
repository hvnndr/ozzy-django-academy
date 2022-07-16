from rest_framework.routers import DefaultRouter
from course import viewsets

router = DefaultRouter()
router.register('course', viewsets.CourseViewSet)
router.register('student', viewsets.StudentViewSet)

urlpatterns = router.urls

