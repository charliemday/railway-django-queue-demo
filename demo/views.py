from rest_framework.views import APIView
from rest_framework.response import Response
from django_q.tasks import async_task


from .tasks import run_task

class DemoView(APIView):

    def post(self, request):
        
        async_task(run_task)

        return Response({
            "message": "API Success"
        })
