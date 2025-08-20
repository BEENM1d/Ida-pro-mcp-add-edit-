#!/usr/bin/env python3
"""
IDA Pro MCP 服务器编辑功能使用示例

这个脚本展示了如何使用新增的编辑功能来自动化 IDA Pro 的各种操作。
"""

import json
import requests

class IDAMCPClient:
    def __init__(self, host="127.0.0.1", port=13337):
        self.base_url = f"http://{host}:{port}"
        self.request_id = 1
    
    def call_method(self, method, *params):
        """调用 IDA MCP 方法"""
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": list(params),
            "id": self.request_id
        }
        self.request_id += 1
        
        response = requests.post(f"{self.base_url}/mcp", json=payload)
        result = response.json()
        
        if "error" in result:
            raise Exception(f"RPC Error: {result['error']}")
        
        return result.get("result")

def example_patch_nops():
    """示例：将指定地址的指令修改为 NOP"""
    client = IDAMCPClient()
    
    # 获取当前选中的地址
    current_addr = client.call_method("get_current_address")
    print(f"当前地址: {current_addr}")
    
    # 修补 3 个字节为 NOP 指令 (0x90)
    result = client.call_method("patch_bytes", current_addr, "90 90 90")
    print(f"修补结果: {result}")

def example_create_struct():
    """示例：创建自定义结构体"""
    client = IDAMCPClient()
    
    # 创建一个文件头结构体
    struct_def = """
        uint32_t magic;
        uint16_t version;
        uint16_t flags;
        uint32_t entry_point;
        uint32_t code_size;
        uint32_t data_size;
    """
    
    result = client.call_method("create_struct", "FileHeader", struct_def)
    print(f"结构体创建结果: {result}")

def example_function_management():
    """示例：函数管理操作"""
    client = IDAMCPClient()
    
    # 在指定地址创建函数
    func_addr = "0x401000"
    result = client.call_method("create_function", func_addr)
    print(f"函数创建结果: {result}")
    
    # 设置函数原型
    prototype = "int __cdecl my_function(int param1, char* param2)"
    result = client.call_method("set_function_prototype", func_addr, prototype)
    print(f"函数原型设置结果: {result}")
    
    # 重命名函数
    result = client.call_method("rename_function", func_addr, "custom_function")
    print(f"函数重命名结果: {result}")

def example_data_type_operations():
    """示例：数据类型操作"""
    client = IDAMCPClient()
    
    # 设置数据类型为 DWORD 数组
    addr = "0x402000"
    result = client.call_method("create_array", addr, "DWORD", 10)
    print(f"数组创建结果: {result}")
    
    # 创建枚举类型
    enum_members = "STATUS_SUCCESS=0, STATUS_ERROR=1, STATUS_PENDING=2"
    result = client.call_method("create_enum", "StatusCode", enum_members)
    print(f"枚举创建结果: {result}")

def example_cross_references():
    """示例：交叉引用管理"""
    client = IDAMCPClient()
    
    # 添加代码交叉引用
    from_addr = "0x401010"
    to_addr = "0x401100"
    result = client.call_method("add_cross_reference", from_addr, to_addr, "code")
    print(f"交叉引用添加结果: {result}")
    
    # 获取交叉引用
    xrefs = client.call_method("get_xrefs_to", to_addr)
    print(f"交叉引用列表: {json.dumps(xrefs, indent=2)}")

def example_advanced_editing():
    """示例：高级编辑操作"""
    client = IDAMCPClient()
    
    # 获取当前函数
    current_func = client.call_method("get_current_function")
    if current_func:
        func_addr = current_func["address"]
        print(f"当前函数: {current_func['name']} at {func_addr}")
        
        # 获取函数的栈帧变量
        stack_vars = client.call_method("get_stack_frame_variables", func_addr)
        print(f"栈变量: {json.dumps(stack_vars, indent=2)}")
        
        # 重命名第一个栈变量
        if stack_vars:
            old_name = stack_vars[0]["name"]
            result = client.call_method("rename_stack_frame_variable", 
                                      func_addr, old_name, "custom_var")
            print(f"栈变量重命名结果: {result}")

def example_batch_operations():
    """示例：批量操作"""
    client = IDAMCPClient()
    
    # 批量创建函数
    function_addresses = ["0x401000", "0x401100", "0x401200"]
    
    for addr in function_addresses:
        try:
            result = client.call_method("create_function", addr)
            print(f"在 {addr} 创建函数: {result}")
        except Exception as e:
            print(f"在 {addr} 创建函数失败: {e}")
    
    # 批量设置注释
    comments = {
        "0x401000": "主函数入口点",
        "0x401100": "初始化函数",
        "0x401200": "清理函数"
    }
    
    for addr, comment in comments.items():
        try:
            result = client.call_method("set_comment", addr, comment)
            print(f"在 {addr} 设置注释: {result}")
        except Exception as e:
            print(f"在 {addr} 设置注释失败: {e}")

if __name__ == "__main__":
    print("IDA Pro MCP 编辑功能示例")
    print("=" * 40)
    
    try:
        # 检查连接
        client = IDAMCPClient()
        connection_status = client.call_method("check_connection")
        print(f"连接状态: {connection_status}")
        
        # 运行示例
        print("\n1. 修补字节示例:")
        example_patch_nops()
        
        print("\n2. 结构体创建示例:")
        example_create_struct()
        
        print("\n3. 函数管理示例:")
        example_function_management()
        
        print("\n4. 数据类型操作示例:")
        example_data_type_operations()
        
        print("\n5. 交叉引用示例:")
        example_cross_references()
        
        print("\n6. 高级编辑示例:")
        example_advanced_editing()
        
        print("\n7. 批量操作示例:")
        example_batch_operations()
        
    except Exception as e:
        print(f"错误: {e}")
        print("请确保 IDA Pro 正在运行并且 MCP 插件已启动")