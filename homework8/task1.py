def possibly_convert_str_to_int_float(string):
    """Converts strings passed to int and float if possible

    :param string: string passed
    :type string: str

    :return: returns int/float if changing type was possible, returns string passed otherwise
    :rtype: int, float, str
    """
    try:
        float(string)
    except ValueError:
        return string
    else:
        int_or_float = eval(string)
        return int_or_float


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

        kw_storage_dict = {}

        for line in content:
            attr, value = line.split("=")
            value = possibly_convert_str_to_int_float(value)

            # adding an attribute to instance's dict
            try:
                kw_storage_dict[attr] = value
            except:
                raise ValueError("Something went wrong during the attributes assigning")
            self.kw_storage_dict = kw_storage_dict

    def __getitem__(self, item):
        """Custom __getitem__, returns corresponding value from inner keyword storage"""
        return self.kw_storage_dict[item]

    def __getattr__(self, item):
        """Custom __getattr__, returns corresponding value from inner keyword storage"""
        return self.kw_storage_dict[item]
