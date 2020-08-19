from abc import ABCMeta, abstractmethod

class Service(object):

    def __init__(self, config):
        self._config = config

    @property
    def configuration(self):
        return self._config

    def load_additional_config(self, service_config):
        pass

    @abstractmethod
    def ask_question(self, client_context, question: str):
        """
        Never knowingly Implemented
        """