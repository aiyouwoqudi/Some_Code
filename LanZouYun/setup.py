from lanzou.api import LanZouCloud
from lanzou.api import core

lzy = LanZouCloud()

cookie = {'ylogin': '1729256','UM_distinctid': '75cc291e0d54-096f78fe735993-230346c-144000-175cc291e0e6b','folder_id_c': '-1','PHPSESSID': '6uokp3g66rvobna8m98qcueec111461','CNZZDATA1253610886': '1691681055-1605446183-https%253A%252F%252Fup.woozooo.com%252F%7C1605451585','phpdisk_info': 'VWACNwNjV2IDMw9qXDABUgBkAQoIYAFjUmRVMQcxAzBYbF9tDGwGOg49UwpZZ1I9UzUBMAE8VmUOOVc%2FDj4HNVUwAjADaFc4AzgPO1wwAWoAMwFlCDUBNFI1VWcHOANiWGVfbgxoBjwOOFM1WQpSOVM2ATYBbFYxDjxXNw44BzdVYQIx'}

if lzy.login_by_cookie(cookie) == LanZouCloud.SUCCESS:
    print('登录成功')
else:
    print('登陆失败')

# 列出 id 为 1037070 的文件夹的子文件夹
sub_dirs = lzy.get_dir_list(2577257)
print(sub_dirs)


# 显示上传进度条的回调函数
def show_progress(file_name, total_size, now_size):
        """显示进度条的回调函数"""
        percent = now_size / total_size
        bar_len = 40  # 进度条长总度
        bar_str = '>' * round(bar_len * percent) + '=' * round(bar_len * (1 - percent))
        print('\r{:.2f}%\t[{}] {:.1f}/{:.1f}MB | {} '.format(
            percent * 100, bar_str, now_size / 1048576, total_size / 1048576, file_name), end='')
        if total_size == now_size:
            print('')  # 下载完成换行

code = lzy.upload_file(r"C:\Users\MaZongYang\Desktop\1767119213-马宗阳.docx", show_progress)
print(core)
if code != LanZouCloud.SUCCESS:
    print('上传失败!')



# 获取文件详细信息列表
file_list = lzy.get_file_list(2577282)
print(file_list)