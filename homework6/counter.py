"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Decorator, that counts instances of a class.
    Adds methods 'get_created_instances' and 'reset_instances_counter' to a class"""

    def get_created_instances():
        """Function returns quantity of instances of a class.
        ClassName or instance_name could be passed in"""
        return cls.counter

    def reset_instances_counter():
        """Function returns quantity of instances of a class and sets it to 0.
        ClassName or instance_name could be passed in"""
        returning_value = cls.counter
        cls.counter = 0
        return returning_value

    # Making copy of original __init__ and creating a counter
    orig_init = cls.__init__
    cls.counter = 0

    # assigning new methods to the class
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    def __init__(self, *args, **kwargs):
        cls.counter += 1

        # assigning new methods to any instance of the class
        self.get_created_instances = get_created_instances
        self.reset_instances_counter = reset_instances_counter

        # use saved original __init__
        orig_init(self, *args, **kwargs)

    cls.__init__ = __init__
    return cls


@instances_counter
class User:
    pass


# if __name__ == "__main__":
#     User.get_created_instances()  # 0
#     user, _, _ = User(), User(), User()
#     user.get_created_instances()  # 3
#     user.reset_instances_counter()  # 3
