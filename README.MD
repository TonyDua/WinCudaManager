# CUDA 环境管理器

![Python 3.9.19](https://img.shields.io/badge/python-3.9.19-blue.svg)
![rich](https://img.shields.io/badge/dependency-rich-green.svg)

这个脚本提供了在Windows系统上管理CUDA版本的工具。它允许用户通过修改系统环境变量来切换不同的CUDA版本。

## 开发状态
**此脚本目前处于开发中。请勿在生产环境中使用。**

## 最新更新
- 添加了动态切换CUDA路径的功能。
- 引入了CUDA版本检测的错误处理。

## 功能
- 获取并显示已安装的CUDA版本。
- 通过更新Path环境变量来切换可用的CUDA版本。

## 待办事项
- [ ] 在应用更改之前添加用户确认。
- [ ] 实现环境变量的备份与恢复功能。

## 依赖关系
此脚本依赖于以下Python包：
- `rich`
- `pywin32`

您可以通过pip安装这些依赖：

```bash
pip install rich pywin32
```

## 使用方法
要运行此脚本，请克隆仓库，导航到脚本所在的目录，并执行Python脚本。

```bash
git clone https://github.com/TonyDua/WinCudaManager.git
cd WinCudaManager
python cuda_switcher.py
```



## 许可证
该项目采用MIT许可证 - 详见 [LICENSE.md](LICENSE) 文件。
