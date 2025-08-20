# IDA Pro MCP 服务器增强版

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![IDA Pro](https://img.shields.io/badge/IDA%20Pro-7.0+-red.svg)](https://www.hex-rays.com/products/ida/)

一个功能完整的 IDA Pro MCP (Model Context Protocol) 服务器，提供强大的编辑功能和完美的 32/64 位适配。

## ✨ 主要特性

### 🔧 核心编辑功能
- **字节修补** - 直接修改二进制数据
- **函数管理** - 创建、删除、重命名函数
- **注释系统** - 添加详细的分析注释
- **数据类型设置** - 设置各种数据类型和数组

### 🏗️ 高级类型系统
- **C 语法类型声明** - 完全支持 C 语法
- **结构体创建** - 创建自定义结构体
- **枚举定义** - 创建枚举类型
- **本地类型管理** - 查看和管理所有定义的类型

### 🔗 变量和引用管理
- **全局变量操作** - 重命名和类型设置
- **栈帧变量管理** - 完整的栈变量操作
- **交叉引用管理** - 添加和删除代码引用
- **指令操作数类型** - 提升反汇编可读性

### 🎯 32/64 位完美适配
- **自动检测** - 动态检测 IDA Pro 架构
- **智能选择** - 自动选择正确的 DLL 文件
- **无警告运行** - 消除所有架构兼容性警告

## 🚀 快速开始

### 前置要求
- IDA Pro 7.0 或更高版本
- Python 3.11 或更高版本
- 支持 MCP 协议的客户端（如 Claude Desktop、Cline 等）

### 一键安装

#### 方法 1: 直接下载安装
```bash
# 克隆仓库
git clone https://github.com/BEENM1d/Ida-pro-mcp-add-edit-.git
cd Ida-pro-mcp-add-edit-

# 运行安装脚本
python install.py
```

#### 方法 2: pip 安装（即将支持）
```bash
# 注意：PyPI 包正在准备中，目前请使用方法 1
# pip install ida-pro-mcp-enhanced
```

### 手动安装
1. 下载 `mcp-plugin.py` 文件
2. 将文件复制到你的 IDA Pro 安装目录下的 plugins 文件夹中
   - 例如：`C:\Program Files\IDA Pro 7.7\plugins\`
   - 或者：`D:\IDA_Pro_v7.7\plugins\`
   - 具体路径取决于你的 IDA Pro 安装位置

## 📖 使用方法

### 1. 启动 MCP 服务器
在 IDA Pro 中：
- 按 `Ctrl+Alt+M` 或
- 菜单栏选择 `Edit -> Plugins -> MCP`

### 2. 配置 MCP 客户端
运行 `python install.py` 后，脚本会自动生成正确的配置。
将生成的配置添加到你的 MCP 客户端配置文件中。

配置示例：
```json
{
  "mcpServers": {
    "github.com/mrexodia/ida-pro-mcp": {
      "timeout": 60,
      "type": "stdio",
      "command": "python",
      "args": ["C:\\path\\to\\Ida-pro-mcp-add-edit-\\server.py"]
    }
  }
}
```

### 3. 开始使用
现在你可以通过 MCP 协议调用各种 IDA Pro 编辑功能！

## 🛠️ 功能示例

### 字节修补
```python
# 将地址 0x401000 处的 3 个字节修改为 NOP 指令
patch_bytes("0x401000", "90 90 90")
```

### 创建结构体
```python
# 创建一个自定义结构体
declare_c_type("struct MyStruct { int id; char name[32]; void* ptr; };")
```

### 函数重命名
```python
# 重命名函数
rename_function("0x401000", "my_custom_function")
```

### 添加注释
```python
# 在指定地址添加注释
set_comment("0x401000", "这是一个重要的函数入口点")
```

## 📚 完整 API 文档

### 核心编辑功能
- `patch_bytes(address, hex_bytes)` - 修补字节
- `create_function(address)` - 创建函数
- `delete_function(address)` - 删除函数
- `rename_function(address, new_name)` - 重命名函数
- `set_comment(address, comment)` - 设置注释

### 类型系统
- `declare_c_type(c_declaration)` - C 语法类型声明
- `create_struct(struct_name, members)` - 创建结构体
- `create_enum(enum_name, members)` - 创建枚举
- `list_local_types()` - 列出本地类型

### 数据管理
- `set_data_type(address, data_type, size)` - 设置数据类型
- `create_array(address, element_type, count)` - 创建数组
- `set_instruction_operand_type(address, operand_index, operand_type)` - 设置操作数类型

### 变量管理
- `rename_global_variable(old_name, new_name)` - 重命名全局变量
- `set_global_variable_type(variable_name, new_type)` - 设置全局变量类型
- `create_stack_frame_variable(function_address, offset, variable_name, type_name)` - 创建栈变量

### 引用管理
- `add_cross_reference(from_address, to_address, ref_type)` - 添加交叉引用
- `delete_cross_reference(from_address, to_address)` - 删除交叉引用

## 🔧 故障排除

### 常见问题

**Q: 出现 "32-bit module detected" 警告**
A: 这个版本已经完全解决了 32/64 位适配问题，不会再出现此警告。

**Q: 连接失败**
A: 确保在 IDA Pro 中启动了 MCP 插件 (`Ctrl+Alt+M`)

**Q: 某些 API 不工作**
A: 确保你的 IDA Pro 版本支持相应的功能，某些高级功能需要 IDA Pro 7.5+

### 调试模式
启用调试输出：
```python
# 在 IDA Pro 控制台中
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 贡献

欢迎贡献代码！请遵循以下步骤：

1. Fork 这个仓库
2. 创建你的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 基于 [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) 项目
- 感谢 IDA Pro 和 Hex-Rays 团队
- 感谢 MCP 协议开发团队

---

⭐ 如果这个项目对你有帮助，请给它一个星标！
