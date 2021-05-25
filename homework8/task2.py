import sqlite3


class TableData:
    """This is a wrapper class TableData for database table, that when
    initialized with database name and table acts as collection object

    :param database_name: full path to a database_file
    :type database_name: str
    :param table_name: a name of a chosen table inside database_file
    :type table_name: str
    """

    def __init__(self, database_name, table_name):
        """Constructor method"""
        self.database_name = database_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.database_name)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def __len__(self):
        """Returns a quantity of rows in a chosen datatable

        :return: quantity of rows in a chosen datatable
        :rtype: int
        """
        self.cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        return self.cursor.fetchone()[0]

    def __getitem__(self, item):
        """Gets a whole row of data with tabledata[name] notation

        :param item: name of an element in datatable chosen
        :type item: str
        :return: whole row of data in datatable
        :rtype: tuple
        """
        self.cursor.execute(
            f"SELECT * from {self.table_name} WHERE name=:item", {"item": item}
        )
        return tuple(self.cursor.fetchone())

    def __contains__(self, item):
        """Checks if there is an element in a tabledata with the name given

        :param item: name of an element in datatable chosen
        :type item: str
        :return: True if element with this name is in datatable, False otherwise
        :rtype: bool
        """
        self.cursor.execute(
            f"SELECT * from {self.table_name} WHERE name=:item", {"item": item}
        )
        return self.cursor.fetchone()

    def __iter__(self):
        """Iterates through rows of data in datatable"""
        yield from self.cursor.execute(f"SELECT * from {self.table_name}")

    def close_connection(self):
        """Closes connection to a database"""
        self.connection.close()
