from django.apps import AppConfig
from multiprocessing import Process
from initalization import *


class LocationConfig(AppConfig):
    name = 'location'

    def ready(self):
        print("\n[*] Do not worry about scripts running twice.")
        print("http://stackoverflow.com/questions/37441564/redefinition-of-appconfig-ready\n")

        # Create logger
        start_logger()

        # Start Socket Server
        # Process(target=run_socket_server_job).start()

        print("\n")
