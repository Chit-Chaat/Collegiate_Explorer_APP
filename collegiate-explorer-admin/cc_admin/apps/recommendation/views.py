from JsonResponseResult import JsonResponseResult


def index(request):
    data = [{
        'id': '1',
        'name': 'University of AAAAAA',
        'logo': 'school_logo.jpg',
        'desc': 'this is desc this is this is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc  is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
        'rating': {
            'A': 5,
            'B': 3,
            'A_val': '5',
            'B_val': '3'
        },
        'review': '3453',
        'level': 'A',
        'detail': 'detail/school_id',
        'address': '1420 22nd W St, Los Angeles, CA, 90007',
        'tuition': '$17,234'
    },
        {
            'id': '2',
            'name': 'University of bbbbbbbb',
            'logo': 'school_logo2.jpg',
            'desc': 'this is desc this is this is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
            'rating': {
                'A': 2,
                'B': 3,
                'A_val': '2',
                'B_val': '3'
            },
            'review': '3453',
            'level': 'A',
            'detail': 'detail/school_id',
            'address': '1420 22nd W St, Los Angeles, CA, 90007',
            'tuition': '$17,234'
        },
        {
            'id': '3',
            'name': 'University of cCCCCC',
            'logo': 'school_logo.jpg',
            'desc': 'this is desc this is this is desc this isthis is des desc this isthis is des desc this isthis is des desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this isthis is desc this is',
            'rating': {
                'A': 4,
                'B': 3,
                'A_val': '4',
                'B_val': '3'
            },
            'review': '3453',
            'level': 'A',
            'detail': 'detail/school_id',
            'address': '1420 22nd W St, Los Angeles, CA, 90007',
            'tuition': '$17,234'
        }]
    return JsonResponseResult(code=200, data=data, msg="OK")
