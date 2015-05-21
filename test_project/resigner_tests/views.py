from django.http import JsonResponse

from resigner.server import signed_req_required

@signed_req_required("MY_API_KEY")
def my_test_api_view(request):
    req = request.POST if request.method == 'POST' else request.GET
    test_data = req.get("MY_TEST_DATA", "")

    result = "test ok" if test_data else "no data received"

    return JsonResponse({"result":result})
