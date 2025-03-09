import json
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 记录请求参数
        request_body = await request.body()
        request_data = json.loads(request_body.decode('utf-8'))
        request_id = request_data.get('id', None)
        logger.info(f"url: {request.url}, method: {request.method}, body: {request_body.decode('utf-8')}")

        response = await call_next(request)

        # 记录返回结果
        response_body = [chunk async for chunk in response.body_iterator]
        response_body = b''.join(response_body)
        response_data = json.loads(response_body.decode('utf-8'))
        if request_id is not None:
            response_data['id'] = request_id
        response_body = json.dumps(response_data).encode('utf-8')

        # 更新响应体和 Content-Length 头
        response = Response(content=response_body, status_code=response.status_code, headers=dict(response.headers))
        response.headers['Content-Length'] = str(len(response_body))
        logger.info(f"status_code: {response.status_code}, body: {json.dumps(response_data)}")

        return response