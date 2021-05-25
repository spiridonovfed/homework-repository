class KeyValueStorage:
    """This is a wrapper class to work with key-value storages formatted this way:

    key1=value1
    key2=value2
    key3-value3
    ...etc

    All the keys become instance's attributes with corresponding values.

    :param path_to_file: Path to key-value storage file
    :type path_to_file: str
    """

    def __init__(self, path_to_file):
        """Constructor method"""
        with open(path_to_file) as file:
            content = [line.rstrip() for line in file.readlines()]

        for line in content:
            attr, value = line.split("=")

            # converting values to int and float if possible
            try:
                float(value)
            except ValueError:
                ...
            else:
                value = eval(value)

            # adding an attribute to instance's dict
            if attr in self.__dir__() and attr.startswith("__") and attr.endswith("__"):
                pass

            else:
                try:
                    self.__dict__[attr] = value
                except:
                    raise ValueError(
                        "Something went wrong during the attributes assigning"
                    )
