import socket
import sys
import logging
from multiprocessing import Process
from handler import QueryHandler

def run_socket_server_job():

    host = '0'
    port = 8888

    logger = logging.getLogger('socket_logger')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.info('Socket Created at port: %s' % str(port))



    # Bind socket to local host and port
    try:
        s.bind((host, port))
    except socket.error as msg:
        logger.critical('Bind Failed. Error Code: %s\nMessage: %s' % (str(msg[0]), msg[1]))
        logger.info('System Exit')
        sys.exit(1)

    logger.info('System Bind Complete')

    # Start listening on socket
    s.listen(10)
    logger.info('Socket Server listening at %s' % str(port))

    try:
        while True:
            client, address = s.accept()
            logger.info('Connected with %s:%s' % (address[0], str(address[1])))

            QueryHandler(client=client).start()

    except KeyboardInterrupt:
        pass

    s.close()


if __name__=='__main__':

    from elecLogging import start_logger
    start_logger()

    run_socket_server_job()
