#!/usr/bin/env python3
"""
代码搜索脚本
"""

import os
import re
import json


def search_field(field_name):
    """搜索指定字段的使用情况"""
    project_root = os.getcwd()
    results = []
    
    # 扫描项目文件
    for root, dirs, files in os.walk(project_root):
        # 排除一些不需要分析的目录
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'venv', '__pycache__']]
        
        for file in files:
            if file.endswith(('.py', '.js', '.ts', '.tsx', '.jsx', '.java', '.c', '.cpp', '.h')):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, project_root)
                
                # 搜索字段
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        lines = content.split('\n')
                        
                        for line_num, line in enumerate(lines, 1):
                            # 搜索字段
                            if field_name in line:
                                # 提取上下文
                                start = max(0, line_num - 2)
                                end = min(len(lines), line_num + 2)
                                context = lines[start:end]
                                
                                results.append({
                                    'file': rel_path,
                                    'line': line_num,
                                    'content': line.strip(),
                                    'context': context
                                })
                except Exception as e:
                    print(f"搜索文件 {rel_path} 时出错: {e}")
    
    # 保存搜索结果
    os.makedirs('./reports', exist_ok=True)
    with open(f'./reports/{field_name}_search_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # 生成搜索报告
    with open(f'./reports/{field_name}_search_report.md', 'w', encoding='utf-8') as f:
        f.write(f'# {field_name} 字段搜索报告\n\n')
        f.write(f'## 搜索结果统计\n')
        f.write(f'共找到 {len(results)} 处使用\n\n')
        
        for result in results:
            f.write(f'### {result["file"]}:{result["line"]}\n')
            f.write(f'```\n{result["content"]}\n```\n\n')
            if result["context"]:
                f.write(f'**上下文:**\n')
                for i, ctx_line in enumerate(result["context"]):
                    f.write(f'- {ctx_line}\n')
                f.write('\n')
    
    print(f"字段搜索完成，报告已保存到 ./reports/{field_name}_search_report.md")
    return results
