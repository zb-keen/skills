#!/usr/bin/env python3
"""
代码逻辑分析脚本
"""

import os
import json
import traceback


def analyze_field_logic(field_name, search_results):
    """分析字段的逻辑使用情况"""
    try:
        # 分析字段的使用模式
        patterns = {
            'definition': [],  # 字段定义
            'assignment': [],  # 字段赋值
            'usage': [],       # 字段使用
            'condition': []    # 条件判断
        }
        
        for result in search_results:
            line = result['content']
            
            # 分析使用模式
            if '=' in line and field_name in line:
                # 检查是否是条件判断中的等于比较
                if '==' in line or '===' in line:
                    patterns['condition'].append(result)
                else:
                    # 可能是赋值
                    if field_name + '=' in line or field_name + ' =' in line:
                        patterns['assignment'].append(result)
                    else:
                        patterns['usage'].append(result)
            elif 'if' in line or 'else' in line or 'switch' in line:
                # 可能是条件判断
                patterns['condition'].append(result)
            elif 'var ' in line or 'let ' in line or 'const ' in line or 'def ' in line or 'class ' in line:
                # 可能是定义
                patterns['definition'].append(result)
            else:
                # 其他使用
                patterns['usage'].append(result)
        
        # 保存逻辑分析结果
        os.makedirs('./reports', exist_ok=True)
        with open(f'./reports/{field_name}_logic_analysis.json', 'w', encoding='utf-8') as f:
            json.dump(patterns, f, ensure_ascii=False, indent=2)
        
        # 生成逻辑分析报告
        with open(f'./reports/{field_name}_logic_analysis.md', 'w', encoding='utf-8') as f:
            f.write(f'# {field_name} 字段使用模式分析报告\n\n')
            f.write('## 注意事项\n\n')
            f.write('本分析基于规则对使用场景进行分类，可能不完全准确。\n')
            f.write('建议结合实际代码进行验证。\n\n')
            
            for pattern_type, items in patterns.items():
                if items:
                    f.write(f'## 可能的{pattern_type}场景 ({len(items)} 处)\n\n')
                    for item in items:
                        f.write(f'### {item["file"]}:{item["line"]}\n')
                        f.write(f'```\n{item["content"]}\n```\n\n')
            
            # 使用文件统计
            f.write('## 使用文件统计\n\n')
            files_used = set()
            for result in search_results:
                files_used.add(result['file'])
            f.write(f'字段在 {len(files_used)} 个文件中被找到\n\n')
            for file in files_used:
                f.write(f'- {file}\n')
        
        print(f"字段逻辑分析完成，报告已保存到 ./reports/{field_name}_logic_analysis.md")
    except Exception as e:
        print(f"分析字段逻辑时出错: {e}")
        print(traceback.format_exc())
