class RequestInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        print("REQUEST STARTED")
        print("Requested Path:", request.path)  
        print("Requested Method:", request.method) 
        response = self.get_response(request)
        print("REPONSE RETURNED")   
        return response