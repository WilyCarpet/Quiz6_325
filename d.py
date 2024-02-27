from abc import ABC, abstractmethod

class LoggingMethod(ABC):
    @abstractmethod
    def log(self, message):
        pass

class Logging(LoggingMethod):
    def __init__(self, library):
        self.library = library

    def log(self, message):
        print("Message logged into Logging library")

class Loguru(LoggingMethod):
    def __init__(self, library):
        self.library = library

    def log(self, message):
        print("Message logged into Logurur library")

class Google_auth(LoggingMethod):
    def __init__(self, library):
        self.library = library

    def log(self, message):
        print("Message logged into Google_auth library")

class Application:
    def __init__(self,logging_method: LoggingMethod):
        self.logging_method = logging_method
    
    def setLoggingPreference(self,logging_method: LoggingMethod):
        self.logging_method= logging_method
    