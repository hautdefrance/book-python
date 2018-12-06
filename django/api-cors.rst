********
API CORS
********

.. code-block:: python

    import datetime
    import json
    from http import HTTPStatus

    from django.db import IntegrityError
    from django.http import HttpResponse, JsonResponse
    from django.views.generic import View


    class APIv3(View):
        http_method_names = ['get', 'post', 'options']

        def options(self, request, *args, **kwargs):
            response = HttpResponse(status=200)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = ', '.join(self.http_method_names).upper()
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            return response

        def get(self, request, *args, **kwargs):
            response = JsonResponse(data={})
            response['Access-Control-Allow-Origin'] = '*'
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'

            try:
                start_datetime = datetime.datetime.strptime(request.GET['start_datetime'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
                result = Result.objects.filter(start_datetime=start_datetime)[0]
                return JsonResponse(status=200, data=result.get_data())

            except (Result.DoesNotExist, IndexError):
                response['status'] = 404
                response['data'] = {'code': 404, 'status': 'Not Found', 'message': 'Result Does Not Exists'}

            return response

        def post(self, request, *args, **kwargs):
            response = JsonResponse(data={})
            response['Access-Control-Allow-Origin'] = '*'
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'

            try:
                data = json.loads(str(request.body, encoding='utf-8'), object_hook=json_datetime_decoder)
                response['status'] = HTTPStatus.CREATED
                response['data'] = {'message': 'Result added to the database.'}
                return response

            except IntegrityError:
                response['status'] = HTTPStatus.OK
                response['data'] = {'message': 'Response already uploaded'}
                return response

            except Exception as message:
                response['status'] = HTTPStatus.BAD_REQUEST
                response['data'] = {'message': 'Bad Request'}
                return response
