import django_hr.utils as sys_utils
from apps.models import BaseDataModel


class Environment(object):

    def __init__(self):
        self._model_dict = self.init_model_dict()

    @property
    def model_dict(self):
        return self._model_dict

    def init_model_dict(self):
        modules = list()
        sys_utils.iter_services("apps/", modules=modules)

        return sys_utils.models_loader(modules, BaseDataModel)


environment = Environment()
