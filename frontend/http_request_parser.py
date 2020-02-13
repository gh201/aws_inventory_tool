def get_client_ip(request):
    request_metadata = request.META.get('HTTP_X_FORWARDED_FOR')

    if request_metadata:
        ip = request_metadata.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
