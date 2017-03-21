from django.http import JsonResponse


# Errors
def invalid_param_error():
    return error_message('InvalidParamError', 'Parameter is invalid or missing')


def error_message(error_name=None, message=None):
    return JsonResponse({'success': 0, 'error': error_name, 'result': message})


def error_no_object():
    return error_message('ObjectDoesNotExist')


def success_message(message=None):
    return JsonResponse({'success': 1, 'result': message})