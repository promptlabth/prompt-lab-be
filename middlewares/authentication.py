from fastapi import Response, Request


def auth():
    async def auth_dependency(request: Request, response: Response) -> None:
        
        token_with_bearer = request.headers.get('Authorization')

        token = token_with_bearer.split(" ")[1]

        response.headers['user-agent'] = 'Testing'
    return auth_dependency





def options(request: Request, response: Response) -> None:
    request_origin = request.headers.get('origin')
    
    
