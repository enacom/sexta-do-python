from science_api.flask import BaseResource, BaseApp

from science_api_examples.io.example_io import ExampleIO
from science_api_examples.io.example_verify import ExampleVerify


class GreeterResource(BaseResource):

    def __init__(self):
        """
        Declares each expected input of the JSON file
        """

        super().__init__()

        # Test argument
        self.parser.add_argument('people', required=True, type=dict, action="append")

        # this argument MUST NOT be removed, the queue Watcher uses it
        self.parser.add_argument('id', required=True, type=str)

    def post(self):
        """
        Executes simulation
        Returns: JSON output file

        """

        return self.aux_post(verification_class=ExampleVerify, io_class=ExampleIO)


base_app = BaseApp()
base_app.add_route(GreeterResource, "/greet")

if __name__ == '__main__':

    host_string = "0.0.0.0"

    base_app.run(ip_host=host_string)
