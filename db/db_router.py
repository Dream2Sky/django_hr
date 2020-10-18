class Router:

    def db_for_read(self, model, **hints):
        """
        在一主多从的情况下，随机返回一个从库
        :param model:
        :param hints:
        :return:
        """
        import random
        return random.choice(['salve'])

    def db_for_write(self, model, **hints):
        return "default"
