import pandas as pd

from domain.name_columns import NameColumns


'''
读取excel文件，获取文件中的数据
返回值：pandas.DataFrame
'''
def read_excel():
    #file_path = input("请将文件拖拽到这里或粘贴文件路径: ").strip('\"')  # 去除可能存在的引号
    file_path = "c:/Users/RuanXee/Desktop/cece.xlsx"
    try:
        return pd.read_excel(file_path, sheet_name=0, header=0)
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到，请检查路径是否正确。")
    except IOError as e:
        print(f"读取文件 {file_path} 时发生错误: {e}")

"""
获取姓名列数组
参数：pandas.DataFrame
返回值：list[NameColumns] 和 无效行号数组
"""
def get_name_columns(data):
    # 有效的姓名列名
    name_columns = []
    # 无效行号
    invalid_row_numbers = []
    for i in range(len(data)):
        # columnsList[0] 是因为默认了第一列为姓名列
        # 如果姓名列是空的，则将行号加入无效行号数组
        if pd.isna(data.loc[i, columnsList[0]])  or data.loc[i, columnsList[0]] == "":
            invalid_row_numbers.append(i+2)
        else:
            nc = NameColumns(data.loc[i, columnsList[0]], i)
            sroceArr = data.iloc[i].to_numpy()
            if len(sroceArr) > 0:
                sroceArr = sroceArr[1:]
                nc.add_score(sroceArr)
            else:
                nc.add_score([])
            # nc.add_score
            name_columns.append(nc)
    return name_columns, invalid_row_numbers

"""
统计某一列的总分,空行跳过
参数：list[NameColumns] 和 列索引
返回值：int
"""
def count_score(name_columns, index):
    count = 0
    for nc in name_columns:
        if not pd.isna(nc.score[index]):
            count += nc.score[index]
    return count


if __name__ == '__main__':
    data = read_excel()
    columnsList = data.columns.tolist() # 获取表头列表
    # 打印所有人姓名并统计人数
    name_columns, invalid_row_numbers = get_name_columns(data)
    # names = ", ".join([person.name for person in name_columns])
    print(f"有效人数共有 {len(name_columns)} 人")
    for nc in name_columns:
        print(nc)
    print(f"无效行的行号为：{invalid_row_numbers}")
    