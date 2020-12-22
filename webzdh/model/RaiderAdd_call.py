import xlrd


def raider_datas(file=None):
    """
    从文件中获取需要用到的数据
    :param file:
    :return:
    """
    if not file:
        file = "../datas/ecshop.xlsx"
    date = xlrd.open_workbook(file)
    table = date.sheet_by_name("snatch")
    now = table.nrows  # 获取行数
    low = table.ncols  # 获取列数
    return [table.row_values(lin) for lin in range(1, table.nrows)]
print(raider_datas()[0][0])
