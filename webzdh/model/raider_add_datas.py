import xlrd


def duob(file=None):
    """
    从文件中获取需要用到是数据
    :param file:
    :return:
    """
    if not file:
        file = "../datas/ecshop.xlsx"  # 打开Excel文件
    date = xlrd.open_workbook(file)
    table = date.sheet_by_name("snatch")  # 定位到需要用到的Excel表
    nrow = table.nrows  # 获取行
    nclo = table.ncols  # 获取列
    return [table.row_values(line) for line in range(1, table.nrows)]  # 返回列表

print(duob())
