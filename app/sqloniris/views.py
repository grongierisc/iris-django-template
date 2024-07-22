from django.http import JsonResponse

import iris

def index(request):
    query = "SELECT top 10 * FROM %Dictionary.ClassDefinition"
    rs = iris.sql.exec(query)
    # Convert the result to a list of dictionaries
    result = []
    for row in rs:
        result.append(row)
    return JsonResponse(result, safe=False)
