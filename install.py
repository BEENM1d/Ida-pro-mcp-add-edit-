#!/usr/bin/env python3
"""
IDA Pro MCP 服务器增强版 - 自动安装脚本
"""

import os
import sys
import shutil
import platform
from pathlib import Path

def get_ida_plugins_dir():
    """获取 IDA Pro 插件目录"""
    system = platform.system().lower()
    
    if system == "windows":
        # Windows 路径
        appdata = os.environ.get('APPDATA')
        if appdata:
            return Path(appdata) / "Hex-Rays" / "IDA Pro" / "plugins"
    elif system == "darwin":
        # macOS 路径
        home = Path.home()
        return home / ".idapro" / "plugins"
    elif system == "linux":
        # Linux 路径
        home = Path.home()
        return home / ".idapro" / "plugins"
    
    return None

def install_plugin():
    """安装 MCP 插件"""
    print("🚀 IDA Pro MCP 服务器增强版安装程序")
    print("=" * 50)
    
    # 获取插件目录
    plugins_dir = get_ida_plugins_dir()
    if not plugins_dir:
        print("❌ 无法确定 IDA Pro 插件目录")
        print("请手动将 mcp-plugin.py 复制到 IDA Pro 插件目录")
        return False
    
    print(f"📁 IDA Pro 插件目录: {plugins_dir}")
    
    # 创建插件目录（如果不存在）
    plugins_dir.mkdir(parents=True, exist_ok=True)
    
    # 复制插件文件
    source_file = Path(__file__).parent / "mcp-plugin.py"
    target_file = plugins_dir / "mcp-plugin.py"
    
    if not source_file.exists():
        print(f"❌ 找不到源文件: {source_file}")
        return False
    
    try:
        shutil.copy2(source_file, target_file)
        print(f"✅ 插件已安装到: {target_file}")
    except Exception as e:
        print(f"❌ 安装失败: {e}")
        return False
    
    # 复制服务器文件
    server_file = Path(__file__).parent / "server.py"
    if server_file.exists():
        target_server = plugins_dir / "ida_pro_mcp_server.py"
        try:
            shutil.copy2(server_file, target_server)
            print(f"✅ 服务器文件已安装到: {target_server}")
        except Exception as e:
            print(f"⚠️  服务器文件安装失败: {e}")
    
    print("\n🎉 安装完成！")
    print("\n📖 使用方法:")
    print("1. 启动 IDA Pro")
    print("2. 按 Ctrl+Alt+M 或选择 Edit -> Plugins -> MCP")
    print("3. 在你的 MCP 客户端中配置连接")
    print("\n📚 更多信息请查看 README.md")
    
    return True

def uninstall_plugin():
    """卸载 MCP 插件"""
    print("🗑️  IDA Pro MCP 服务器增强版卸载程序")
    print("=" * 50)
    
    plugins_dir = get_ida_plugins_dir()
    if not plugins_dir:
        print("❌ 无法确定 IDA Pro 插件目录")
        return False
    
    files_to_remove = [
        plugins_dir / "mcp-plugin.py",
        plugins_dir / "ida_pro_mcp_server.py"
    ]
    
    removed_count = 0
    for file_path in files_to_remove:
        if file_path.exists():
            try:
                file_path.unlink()
                print(f"✅ 已删除: {file_path}")
                removed_count += 1
            except Exception as e:
                print(f"❌ 删除失败 {file_path}: {e}")
    
    if removed_count > 0:
        print(f"\n🎉 卸载完成！已删除 {removed_count} 个文件")
    else:
        print("\n📝 没有找到需要删除的文件")
    
    return True

def main():
    """主函数"""
    if len(sys.argv) > 1 and sys.argv[1] == "uninstall":
        uninstall_plugin()
    else:
        install_plugin()

if __name__ == "__main__":
    main()