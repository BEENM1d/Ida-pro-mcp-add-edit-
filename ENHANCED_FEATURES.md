# IDA Pro MCP 服务器增强功能

本项目已经增强了 IDA Pro MCP 服务器，添加了强大的编辑功能，使其不仅能够分析二进制文件，还能直接修改和编辑 IDA Pro 数据库。

## 新增的编辑功能

### 1. 字节修补 (Byte Patching)
- **patch_bytes(address, hex_bytes)**: 在指定地址修补字节
  - 支持十六进制格式输入 (如: "90 90 90" 表示三个 NOP 指令)
  - 自动验证地址和字节格式
  - 实时更新 IDA 数据库

### 2. 函数管理
- **create_function(address)**: 在指定地址创建新函数
- **delete_function(address)**: 删除指定地址的函数
- 自动处理函数边界和调用图更新

### 3. 指令操作数类型设置
- **set_instruction_operand_type(address, operand_index, operand_type)**: 设置指令操作数类型
  - 支持的类型: offset, number, char, segment, enum, struct
  - 提升反汇编代码的可读性

### 4. 结构体管理
- **create_struct(struct_name, members)**: 创建新的结构体定义
  - 支持 C 语法格式的成员定义
- **add_struct_member(struct_name, member_name, member_type, offset)**: 向现有结构体添加成员
  - 动态扩展结构体定义

### 5. 枚举管理
- **create_enum(enum_name, members)**: 创建新的枚举类型
  - 支持 "NAME1=value1,NAME2=value2" 格式

### 6. 数据类型设置
- **set_data_type(address, data_type, size)**: 在指定地址设置数据类型
  - 支持所有 IDA 内置数据类型
  - 自动应用类型信息

### 7. 数组创建
- **create_array(address, element_type, count)**: 在指定地址创建数组
  - 支持任意元素类型和数量

### 8. 交叉引用管理
- **add_cross_reference(from_address, to_address, ref_type)**: 添加交叉引用
- **delete_cross_reference(from_address, to_address)**: 删除交叉引用
  - 支持代码和数据引用类型

## 使用示例

### 修补字节
```python
# 将地址 0x401000 处的 3 个字节修改为 NOP 指令
patch_bytes("0x401000", "90 90 90")
```

### 创建函数
```python
# 在地址 0x402000 创建新函数
create_function("0x402000")
```

### 创建结构体
```python
# 创建一个包含两个成员的结构体
create_struct("MyStruct", "int field1; char field2;")
```

### 设置数据类型
```python
# 将地址 0x403000 设置为 DWORD 类型
set_data_type("0x403000", "DWORD", 4)
```

## 安全特性

- 所有编辑操作都使用 `@idawrite` 装饰器确保线程安全
- 自动验证输入参数的有效性
- 提供详细的错误信息和异常处理
- 支持操作回滚和撤销

## 兼容性

- 完全兼容现有的 IDA Pro MCP 功能
- 支持 IDA Pro 7.x 和 8.x 版本
- 适配 Windows、macOS 和 Linux 平台
- 与各种 MCP 客户端兼容 (Cline, Claude, Cursor 等)

## 注意事项

1. 编辑操作会直接修改 IDA 数据库，建议在操作前备份
2. 某些操作可能需要重新分析代码以获得最佳效果
3. 复杂的结构体和类型定义建议使用 C 语法格式
4. 交叉引用的添加和删除会影响代码分析结果

这些增强功能使 IDA Pro MCP 服务器成为一个完整的逆向工程自动化平台，不仅能够分析二进制文件，还能进行精确的编辑和修改操作。