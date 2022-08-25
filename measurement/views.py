from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(sefl, request, pk=0):

        if pk == 0:
            response = super().get(request=request)
            return response
        
        sens = Sensor.objects.filter(id=pk).first()
        if sens is not None:
            
            content = {
                'id': sens.id,
                'name': sens.name,
                'desription': sens.description,
                "measurements": []
            }
            
            measurements = Measurement.objects.filter(sensor=sens).all()

            for m in measurements:
                lst = {"temperature": m.temperature,
                       "created_at": m.created_at}
                content.get('measurements').append(lst)
            stat = status.HTTP_200_OK
        else:
            content = {
                'server_message': 'Sensor ID is out of range',
                'id': pk,
            }
            stat = status.HTTP_400_BAD_REQUEST

        return Response(content, status=stat)
    #end get()

    def post(self, request):

        obj, created = Sensor.objects.get_or_create(
            name=request.data.get('name'), 
            description=request.data.get('description')
            )
        
        if created:
            stat = status.HTTP_201_CREATED
            msg = 'Data saved'
        else:
            stat = status.HTTP_500_INTERNAL_SERVER_ERROR
            msg = 'Record already exist'
        
        content = {
            'server_message': msg,
            'id': obj.id,
            'name': obj.name,
            'desription': obj.description,
        }

        return Response(content, status=stat)
    # end post()
    
    def patch(self, request, pk):

        record_updated = Sensor.objects.filter(id=pk).update(description=request.data.get('description'))

        msg = 'Updated records ' + str(record_updated)
        if record_updated > 0:
            stat = status.HTTP_200_OK
        else:
            stat = status.HTTP_400_BAD_REQUEST

        content = {
            'server_message': msg,
        }

        return Response(content, status=stat)
    #end patch()

#end class SensorView

class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):

        sens = Sensor.objects.filter(id=request.data.get('sensor')).first()

        if sens is not None:
            m = Measurement(sensor=sens, temperature=request.data.get('temperature'))
            m.save()
        
            stat = status.HTTP_201_CREATED
            msg = 'Data saved'
        else:
            stat = status.HTTP_500_INTERNAL_SERVER_ERROR
            msg = 'Sensor ID is out of range'
        
        content = {
            'server_message': msg,
            'sensor_id': request.data.get('sensor'), 
            'temperature': request.data.get('temperature'),
        }

        return Response(content, status=stat)
    # end post()

#end class MeasurementView
