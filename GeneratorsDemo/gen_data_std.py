# gen_data_std.py 

class DataStd:
    """
    Data Standardization Class
    """
    def lowercase_cols():
        pass
    def filter_data():
        pass
    def rename_format():
        pass
    def remove_nostd_cols():
        pass
    def convert_date_cols():
        pass
    def write_and_clear():
        pass


def all_std_steps():
    """
    Do all standardization steps in order 
    Runs until all steps are done (or the function breaks)
    """
    DataStd.lowercase_cols()
    DataStd.filter_data()
    DataStd.rename_format()
    DataStd.remove_nostd_cols()
    DataStd.convert_date_cols()
    DataStd.write_and_clear()


def gen_std_steps():
    """
    Iterate through standardization steps 
    """
    yield DataStd.lowercase_cols()
    yield DataStd.filter_data()
    yield DataStd.rename_format()
    yield DataStd.remove_nostd_cols()
    yield DataStd.convert_date_cols()
    yield DataStd.write_and_clear()


def std_steps():
    """
    Iterate through standardization steps 
    ---------------
    Prints the standardization step that will be ran 
    """
    print('lower case')
    yield DataStd.lowercase_cols()
    print('filter')
    yield DataStd.filter_data()
    print('rename')
    yield DataStd.rename_format()
    print('remove nonstandard')
    yield DataStd.remove_nostd_cols()
    print('convert dates')
    yield DataStd.convert_date_cols()
    print('write and clear')
    yield DataStd.write_and_clear()