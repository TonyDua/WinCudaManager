import win32api
import win32con
from rich.console import Console

console = Console()

def add_fake_cuda_path():
    # 获取当前的用户环境变量Path
    user_path = win32api.GetEnvironmentVariable("Path", win32con.HKEY_CURRENT_USER)
    # 添加一个假的CUDA路径
    fake_path = "C:\\Fake\\CUDA\\v11.8\\bin;" + user_path
    win32api.SetEnvironmentVariable("Path", fake_path)
    console.log("Added fake CUDA path to user Path.")

def add_fake_cuda_system_variable():
    # 在系统变量中创建一个假的CUDA路径
    fake_system_path = "C:\\System\\Fake\\CUDA\\v12.1\\bin"
    win32api.SetEnvironmentVariable("FAKE_CUDA_PATH", fake_system_path)
    console.log("Created fake system CUDA path.")

def modify_fake_cuda_version(new_version):
    # 修改系统变量FAKE_CUDA_PATH中的版本号
    current_path = win32api.GetEnvironmentVariable("FAKE_CUDA_PATH")
    new_path = current_path.replace(current_path.split("\\")[4], f"v{new_version}")
    win32api.SetEnvironmentVariable("FAKE_CUDA_PATH", new_path)
    console.log(f"Modified FAKE_CUDA_PATH to new version: {new_version}")

def test_environment_variable_operations():
    add_fake_cuda_path()
    add_fake_cuda_system_variable()
    modify_fake_cuda_version("12.2")  # 修改假CUDA路径的版本号为12.2

    # 检查变量是否正确更新
    updated_user_path = win32api.GetEnvironmentVariable("Path", win32con.HKEY_CURRENT_USER)
    updated_fake_cuda_path = win32api.GetEnvironmentVariable("FAKE_CUDA_PATH")
    console.log(f"Updated user Path: {updated_user_path}")
    console.log(f"Updated FAKE_CUDA_PATH: {updated_fake_cuda_path}")

if __name__ == "__main__":
    test_environment_variable_operations()
