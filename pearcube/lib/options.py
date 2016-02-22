import sys

class Options(object):
    def __init__(self):
        self.DEBUG = True
        self.PORT = 8000
        self.HOST = '127.0.0.1'
        self.LIVE_EMAILING = False

    def parse_command_line(self):
        # TODO this function sucks

        if '--debug' not in sys.argv:
            self.PORT = 80
            self.HOST = '0.0.0.0'
            self.LIVE_EMAILING = True

        if '--port' in sys.argv:
            self.PORT = int(sys.argv[sys.argv.index('--port') + 1])

        if '--host' in sys.argv:
            self.HOST = sys.argv[sys.argv.index('--host') + 1]

        if '--live_emailing' in sys.argv:
            self.LIVE_EMAILING = True


options = Options()
