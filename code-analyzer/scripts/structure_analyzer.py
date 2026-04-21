#!/usr/bin/env python3
"""
项目结构分析脚本
"""

import os
import json


def analyze_project_structure():
    """分析项目结构"""
    project_root = os.getcwd()
    structure = {
        'root': project_root,
        'files': [],
        'directories': []
    }
    
    # 扫描项目目录
    for root, dirs, files in os.walk(project_root):
        # 排除一些不需要分析的目录
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'venv', '__pycache__']]
        
        # 分析目录
        rel_path = os.path.relpath(root, project_root)
        if rel_path != '.':
            structure['directories'].append(rel_path)
        
        # 分析文件
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.tsx', '.jsx', '.java', '.c', '.cpp', '.h')):
                file_path = os.path.join(rel_path, file)
                structure['files'].append(file_path)
    
    # 保存结构分析结果
    os.makedirs('../reports', exist_ok=True)
    with open('../reports/structure_report.json', 'w', encoding='utf-8') as f:
        json.dump(structure, f, ensure_ascii=False, indent=2)
    
    # 生成结构报告
    with open('../reports/structure_report.md', 'w', encoding='utf-8') as f:
        f.write('# 项目结构分析报告\n\n')
        f.write(f'## 项目根目录\n{project_root}\n\n')
        f.write('## 文件列表\n')
        for file in structure['files']:
            f.write(f'- {file}\n')
        f.write('\n## 目录列表\n')
        for directory in structure['directories']:
            f.write(f'- {directory}\n')
    
    print(f"项目结构分析完成，报告已保存到 ../reports/structure_report.md")


def analyze_dependencies():
    """分析代码依赖"""
    project_root = os.getcwd()
    dependencies = {}
    
    # 扫描项目文件
    for root, dirs, files in os.walk(project_root):
        # 排除一些不需要分析的目录
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'venv', '__pycache__']]
        
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.tsx', '.jsx')):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, project_root)
                
                # 分析导入语句
                imports = []
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        lines = content.split('\n')
                        
                        for line in lines:
                            line = line.strip()
                            # Python 导入
                            if line.startswith('import ') or line.startswith('from '):
                                imports.append(line)
                            # JavaScript/TypeScript 导入
                            elif line.startswith('import ') or line.startswith('require('):
                                imports.append(line)
                except Exception as e:
                    print(f"分析文件 {rel_path} 时出错: {e}")
                
                if imports:
                    dependencies[rel_path] = imports
    
    # 保存依赖分析结果
    os.makedirs('../reports', exist_ok=True)
    with open('../reports/dependencies.json', 'w', encoding='utf-8') as f:
        json.dump(dependencies, f, ensure_ascii=False, indent=2)
    
    # 生成依赖报告
    with open('../reports/dependencies_report.md', 'w', encoding='utf-8') as f:
        f.write('# 代码依赖分析报告\n\n')
        for file_path, imports in dependencies.items():
            f.write(f'## {file_path}\n')
            for imp in imports:
                f.write(f'- {imp}\n')
            f.write('\n')
    
    print(f"代码依赖分析完成，报告已保存到 ../reports/dependencies_report.md")
