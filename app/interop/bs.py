from iop import BusinessService
from msg import HttpMessageRequest, HttpMessageResponse
from django.core.handlers.wsgi import WSGIRequest

class BS(BusinessService):
    def on_process_input(self, message_input:WSGIRequest)->HttpMessageResponse:
        # Create a new HttpMessageRequest
        msg = HttpMessageRequest(
            method=message_input.method,
            url=message_input.path,
            headers={k: v for k, v in message_input.headers.items() if k != 'content-length'},
            body=message_input.body.decode('utf-8')
        )
        self.log_info(f"Request: {msg}")
        response = self.send_request_sync('BO', msg)
        return response