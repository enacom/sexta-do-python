from configparser import ConfigParser

from science_api.online_queue.sqs_base_watcher import SqsBaseWatcher
from science_api.sqs.sqs_base import SqsBase

from science_api_examples.io.example_io import ExampleIO

if __name__ == '__main__':
    '''
    Runs a watcher to keep checking the sqs queue to run the API and post the result
    '''

    settings_path = './settings.cfg'
    parser = ConfigParser()
    parser.read(settings_path)

    sqs_setup = {
        'aws_region': parser.get('sqs_info', 'AWS_REGION'),
        'send_url': parser.get('sqs_info', 'SEND_URL'),
        'receive_url': parser.get('sqs_info', 'RECEIVE_URL'),
        'aws_access_key': parser.get('credentials', 'AWS_ACCESS_KEY_ID'),
        'aws_secret_key': parser.get('credentials', 'AWS_SECRET_ACCESS_KEY'),
    }

    watcher_setup = {
        'url': parser.get('post_info', 'URL')
    }

    sqs_api = SqsBase(region=sqs_setup['aws_region'],
                      aws_access_key=sqs_setup['aws_access_key'],
                      aws_secret_key=sqs_setup['aws_secret_key'],
                      send_queue_url=sqs_setup['send_url'],
                      receive_queue_url=sqs_setup['receive_url'])

    server_watcher = SqsBaseWatcher(sqs_api=sqs_api,
                                    io_class=ExampleIO,
                                    post_url=watcher_setup['url'])

    server_watcher.run()
