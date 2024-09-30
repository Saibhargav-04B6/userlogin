import time

class ExecutionTimeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self, request):
        starttime=time.time()
        res=self.get_response(request)
        exetime=time.time()-starttime
        print(f"Execution time is {exetime}")
        return res