import sys
import os

class Options(object):
    def __init__(self):
        self.DEBUG = True
        self.PORT = 8888
        self.HOST = '127.0.0.1'
        self.LIVE_EMAILING = False
        self.ENV = os.environ.get('PG_ENV', 'dev')

    def parse_command_line(self):
        # TODO this function sucks

        if '--prod' in sys.argv:
            self.HOST = '0.0.0.0'
            self.LIVE_EMAILING = True
            self.DEBUG = False

        if '--nodebug' in sys.argv:
            self.DEBUG = False

        if '--port' in sys.argv:
            self.PORT = int(sys.argv[sys.argv.index('--port') + 1])

        if '--host' in sys.argv:
            self.HOST = sys.argv[sys.argv.index('--host') + 1]

        if '--live-emailing' in sys.argv:
            self.LIVE_EMAILING = True


options = Options()
