class LoggerClass(object):

    def logger(self, func):
        def inner(*args, **kwargs):
            print("Arguments were : %s, %s だなっと" % (args, kwargs))
            return func(*args, **kwargs)
        return inner
