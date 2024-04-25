import os
import subprocess
import win32api
import win32con
from rich.console import Console
from rich.markdown import Markdown

console = Console()
is_test_mode = False  # 控制是否打印详细调试信息

def get_installed_cuda_versions():
    paths = win32api.GetEnvironmentVariable("Path").split(";")
    cuda_versions = {}
    for path in paths:
        # 此处尝试更精确地定位版本号
        parts = path.split("\\")
        for i, part in enumerate(parts):
            if part == "CUDA" and i+1 < len(parts):
                version = parts[i+1].lstrip('v')  # 从路径部分提取版本号
                if version not in cuda_versions:
                    cuda_versions[version] = set()
                cuda_versions[version].add(path)
    if is_test_mode:
        console.log("Detected CUDA paths:", cuda_versions)
    return cuda_versions



def get_current_cuda_version():
    try:
        output = subprocess.check_output("nvcc -V", shell=True, stderr=subprocess.STDOUT, text=True)
        if is_test_mode:
            console.print("[bold blue]Current CUDA version output:[/bold blue]", style="bold blue")
            console.print(output, style="bold yellow")  # 使用黄色粗体显示输出
    except subprocess.CalledProcessError as e:
        if is_test_mode:
            console.log("Failed to execute nvcc -V:", e.output)
    return output


def switch_cuda_version(current_version, new_version):
    if current_version == new_version:
        console.log(f"No change required, already on CUDA version {new_version}")
        return

    env = win32api.GetEnvironmentVariable("Path")
    new_env = []
    paths_to_move_up = []

    for path in env.split(';'):
        if f"CUDA\\v{current_version}" in path:
            paths_to_move_up.append(path.replace(current_version, new_version))
        else:
            new_env.append(path)

    new_env = paths_to_move_up + new_env
    new_env = ';'.join(new_env)
    win32api.SetEnvironmentVariable("Path", new_env)
    win32api.SendMessageTimeout(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment', win32con.SMTO_ABORTIFHUNG, 5000)
    if is_test_mode:
        console.log(f"Switched CUDA version from {current_version} to {new_version} and updated Path.")

def main():
    global is_test_mode
    is_test_mode = True  # Enable test mode

    console.log("Fetching installed CUDA versions...")
    cuda_versions = get_installed_cuda_versions()
    current_version_output = get_current_cuda_version()

    # 解析当前激活的CUDA版本
    current_active_version = None
    if "release" in current_version_output:
        current_active_version = current_version_output.split("release")[-1].split(",")[0].strip()
    
    if not cuda_versions:
        console.log("No CUDA versions installed.")
        return
    console.log("Please select the CUDA version index you want to switch to:")
    version_list = sorted(cuda_versions.keys())
    for index, version in enumerate(version_list):
        if version == current_active_version:
            # 显示当前激活的版本，带有特殊标记
            console.print(f"{index}: [bold green]CUDA v{version}[/bold green] [italic]activated[/italic] :smile:", emoji=True)
        else:
            console.print(f"{index}: CUDA v{version}")
    selected_index = int(input("Enter the version index: "))
    selected_version = version_list[selected_index]
    switch_cuda_version(current_active_version, selected_version)  # Assuming the first one is current


if __name__ == "__main__":
    main()
