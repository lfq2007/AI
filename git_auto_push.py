#!/usr/bin/env python3
"""
自动 Git 提交和推送脚本
用法：python git_auto_push.py [commit_message]
"""

import os
import sys
import subprocess
import datetime
from pathlib import Path

def run_command(command, cwd=None):
    """执行 shell 命令并返回结果"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def git_status():
    """检查 git 状态"""
    print("📊 检查 Git 状态...")
    code, stdout, stderr = run_command("git status")
    if code != 0:
        print(f"❌ Git 状态检查失败: {stderr}")
        return False
    print(stdout)
    return True

def git_add_all():
    """执行 git add ."""
    print("📁 添加所有文件到暂存区...")
    code, stdout, stderr = run_command("git add .")
    if code != 0:
        print(f"❌ Git add 失败: {stderr}")
        return False
    print("✅ 文件已添加到暂存区")
    return True

def git_commit(message):
    """执行 git commit"""
    print(f"💾 提交更改: {message}")
    code, stdout, stderr = run_command(f'git commit -m "{message}"')
    if code != 0:
        print(f"❌ Git commit 失败: {stderr}")
        return False
    print("✅ 提交成功")
    print(stdout)
    return True


def git_push(branch="main"):
    """执行 git push"""
    print(f"🚀 推送到远程仓库 (分支: {branch})...")
    code, stdout, stderr = run_command(f"git push origin {branch}")
    if code != 0:
        print(f"❌ Git push 失败: {stderr}")
        return False
    print("✅ 推送成功")
    print(stdout)
    return True

def git_pull(branch="main"):
    """先拉取最新更改"""
    print(f"⬇️  拉取远程最新更改 (分支: {branch})...")
    code, stdout, stderr = run_command(f"git pull origin {branch}")
    if code != 0:
        print(f"⚠️  Git pull 失败: {stderr}")
        return False
    print("✅ 拉取成功")
    return True

def main():
    # 获取当前目录
    current_dir = os.getcwd()
    print(f"📂 当前目录: {current_dir}")
    
    # 检查是否是 git 仓库
    if not os.path.exists(os.path.join(current_dir, ".git")):
        print("❌ 当前目录不是 Git 仓库")
        return
    
    # 获取提交信息
    if len(sys.argv) > 1:
        commit_message = " ".join(sys.argv[1:])
    else:
        # 使用默认提交信息
        now = datetime.datetime.now()
        commit_message = f"Auto commit at {now.strftime('%Y-%m-%d %H:%M:%S')}"
    
    print(f"📝 提交信息: {commit_message}")
    print("=" * 50)
    
    # 执行流程
    if not git_status():
        return
    
    print("\n" + "=" * 50)
    if not git_add_all():
        return
    
    print("\n" + "=" * 50)
    if not git_commit(commit_message):
        return
    
    print("\n" + "=" * 50)
    
    # 询问是否先拉取
    choice = input("是否先拉取远程更改？(y/n, 默认 y): ").strip().lower()
    if choice not in ['n', 'no']:
        git_pull()
    
    print("\n" + "=" * 50)
    
    # 询问推送分支
    branch = input("输入推送的分支名 (默认 main): ").strip()
    if not branch:
        branch = "main"
    
    if git_push(branch):
        print("\n🎉 所有操作完成！")
    else:
        print("\n⚠️  部分操作失败，请手动检查")

if __name__ == "__main__":
    main()