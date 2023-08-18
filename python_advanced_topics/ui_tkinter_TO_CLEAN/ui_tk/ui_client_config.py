# TODO: add header
import logging
import configparser
import os


class UIClientConfig:
    protocol = None
    host = None
    port = None
    user = None
    password = None
    sleep_time = None
    f_config_name = 'ui_settings.conf'

    def __init__(self, protocol=None, host=None, port=None, user=None, password=None, sleep_time=5):
        logging.info('Constructor ClientConfig()')
        if os.path.isfile(self.f_config_name):
            logging.info('Load config from file')
            self.read_config()
        else:
            logging.debug('Load default config')
            self.protocol = 'http'
            self.host = '127.0.0.1'
            self.port = '9000'
            self.user = ''
            self.password = ''
        # ---------------------------------
        self.url = self.protocol + '://' + self.host + ':' + self.port
        logging.info('user=' + self.user)
        logging.info('user=' + self.password)
        logging.info('user=' + self.url)

    def read_config(self):
        '''
        Read config from file ui_settings.conf
        :return:
        '''
        f_config = configparser.ConfigParser()
        f_config.read(self.f_config_name)
        self.protocol = f_config['DEFAULT']['protocol']
        self.host = f_config['DEFAULT']['host']
        self.port = f_config['DEFAULT']['port']
        self.user = f_config['DEFAULT']['user']
        self.password = f_config['DEFAULT']['password']

    def __del__(self):
        logging.info('Finalize ClientConfig()')
