def is_xhr(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
