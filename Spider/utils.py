class Url:
    def __init__(self, target):
        self.__type = target[:target.find("://")]

        self.__domain = target[target.find("://") + 3:target.find("/", target.find("://") + 3)]
        self.__resource = target[target.find("/", target.find("://") + 3) + 1:target.find("?")]
        self.__sub_domain = self.__domain.split(".")
        self.__sub_domain.remove(self.__sub_domain[len(self.__sub_domain) - 1])

    def type(self):
        return self.__type

    def get_domain(self):
        return self.__domain

    def get_resource(self):
        return self.__resource

    def get_sub_domain(self):
        return self.__sub_domain
