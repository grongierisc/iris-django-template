import json
import dataclasses

from iop import BusinessOperation

from msg import HttpMessageRequest, HttpMessageResponse

class BO(BusinessOperation):
    def on_http_request(self, message_request: HttpMessageRequest)->HttpMessageResponse:
        # Create a new response
        # Where the body contains the a json with the message_request attributes
        response = HttpMessageResponse(
            status=200,
            headers={'Content-Type': 'application/json'},
            body=json.dumps(dataclasses.asdict(message_request))
        )
        return response