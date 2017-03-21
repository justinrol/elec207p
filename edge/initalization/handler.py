import os
import json
import requests
import logging
import datetime
from multiprocessing import Process
from django.views.decorators.csrf import csrf_exempt

class QueryHandler(Process):

    def __init__(self, client):

        super(QueryHandler, self).__init__()

        self.logger = logging.getLogger('socket_logger')

        self.socket_client = client

    def run(self):
        while True:
            socket_t1 = datetime.datetime.now()
            data = self.socket_client.recv(1028)
            print(data)
            if 'terminate' in data:
                print(data)
                break

            data = data.replace(' ', '')

            mac_address = data.split(',')
            device_id = mac_address[0]
            mac_address = mac_address[1:]

            payload = dict()
            payload['mac_address'] = json.dumps(mac_address)
            # print(payload)
            url = 'http://127.0.0.1:8888/a/weather'

            r = requests.post(url, payload)

            try:
                r = r.json()
            except ValueError:
                self.logger.critical('Failed to parse response')
                continue

            try:
                # Server said its not successful
                if r['success'] is not 1:
                    self.logger.critical('Server error')
                    self.socket_client.sendall('sorry')
                    continue

                res = json.loads(r['result'])

                weather = res.get('weather')
                device_id = res.get('device_id')

                cli_res = '%s, %s' % (weather, device_id)
                self.socket_client.sendall(cli_res)

                self.logger.info('Socket Converse time: %s' % str(datetime.datetime.now() - socket_t1))

            except KeyError:
                logging.critical('Key Missing')

        self.logger.info('Closing Socket Connection')
        self.socket_client.close()

    @staticmethod
    def get_env_variable(name=None):
        if name is None:
            raise EnvVariableException

        var = os.environ.get(name, None)

        if var is None:
            raise EnvVariableException

        return var


class EnvVariableException(Exception):
    pass
