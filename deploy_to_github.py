#!/usr/bin/env python3
"""
一键部署到 GitHub 脚本
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, check=True):
    """运行命令并返回结果"""
    print(f"🔧 执行命令: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ 命令执行失败: {e}")
        if e.stderr:
            print(f"错误信息: {e.stderr}")
        return None

def main():
    """主函数"""
    print("🚀 IDA Pro MCP 增强版 - GitHub 部署脚本")
    print("=" * 50)
    
    # 检查是否在正确的目录
    if not Path("server.py").exists() or not Path("mcp-plugin.py").exists():
        print("❌ 请在项目根目录运行此脚本")
        sys.exit(1)
    
    # 获取 GitHub 仓库信息
    repo_name = input("📝 请输入 GitHub 仓库名 (默认: ida-pro-mcp-enhanced): ").strip()
    if not repo_name:
        repo_name = "ida-pro-mcp-enhanced"
    
    username = input("📝 请输入你的 GitHub 用户名: ").strip()
    if not username:
        print("❌ 必须提供 GitHub 用户名")
        sys.exit(1)
    
    # 初始化 Git 仓库
    print("\n📦 初始化 Git 仓库...")
    if not Path(".git").exists():
        run_command("git init")
    
    # 添加所有文件
    print("📁 添加文件到 Git...")
    run_command("git add .")
    
    # 提交更改
    print("💾 提交更改...")
    commit_msg = "Initial commit: Enhanced IDA Pro MCP Server with comprehensive editing capabilities"
    run_command(f'git commit -m "{commit_msg}"')
    
    # 设置远程仓库
    print("🔗 设置远程仓库...")
    remote_url = f"https://github.com/{username}/{repo_name}.git"
    
    # 检查是否已有远程仓库
    result = run_command("git remote -v", check=False)
    if result and "origin" in result.stdout:
        run_command(f"git remote set-url origin {remote_url}")
    else:
        run_command(f"git remote add origin {remote_url}")
    
    # 推送到 GitHub
    print("🚀 推送到 GitHub...")
    run_command("git branch -M main")
    
    print(f"\n📋 接下来的步骤:")
    print(f"1. 在 GitHub 上创建仓库: https://github.com/new")
    print(f"   - 仓库名: {repo_name}")
    print(f"   - 设置为 Public")
    print(f"   - 不要初始化 README、.gitignore 或 LICENSE")
    print(f"\n2. 创建完成后，运行以下命令推送代码:")
    print(f"   git push -u origin main")
    print(f"\n3. 可选：设置 PyPI 发布")
    print(f"   - 在仓库设置中添加 PYPI_API_TOKEN secret")
    print(f"   - 创建 release 标签来触发自动发布")
    
    # 询问是否立即推送
    push_now = input(f"\n❓ 是否立即推送到 GitHub？(需要先创建仓库) [y/N]: ").strip().lower()
    if push_now in ['y', 'yes']:
        result = run_command("git push -u origin main", check=False)
        if result and result.returncode == 0:
            print(f"\n🎉 成功推送到 GitHub!")
            print(f"🔗 仓库地址: https://github.com/{username}/{repo_name}")
        else:
            print(f"\n⚠️  推送失败，请先在 GitHub 创建仓库，然后手动运行:")
            print(f"   git push -u origin main")
    
    print(f"\n✅ 部署脚本完成!")

if __name__ == "__main__":
    main()