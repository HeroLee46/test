import subprocess
print("="*40, "Install package", "="*40)
# 执行命令 'pip install GPUtil'
result = subprocess.run('pip install GPUtil', capture_output=True, text=True, shell=True)

# 检查命令是否成功执行
if result.returncode == 0:
    # 输出命令结果
    print(result.stdout)
else:
    # 输出错误信息
    print(result.stderr)

# 执行命令 'pip install psutil'
result = subprocess.run('pip install psutil', capture_output=True, text=True, shell=True)

# 检查命令是否成功执行
if result.returncode == 0:
    # 输出命令结果
    print(result.stdout)
else:
    # 输出错误信息
    print(result.stderr)

# 执行命令 'pip install tabulate'
result = subprocess.run('pip install tabulate', capture_output=True, text=True, shell=True)

# 检查命令是否成功执行
if result.returncode == 0:
    # 输出命令结果
    print(result.stdout)
else:
    # 输出错误信息
    print(result.stderr)

# 执行命令 'pip list'
result = subprocess.run('pip list', capture_output=True, text=True, shell=True)

# 检查命令是否成功执行
if result.returncode == 0:
    # 输出命令结果
    print(result.stdout)
else:
    # 输出错误信息
    print(result.stderr)
