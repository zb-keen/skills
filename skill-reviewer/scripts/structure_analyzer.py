#!/usr/bin/env python3
"""
技能结构分析脚本
"""

import os
import sys
import json
import traceback


def analyze_skill_structure(skill_path):
    """分析技能结构"""
    try:
        print(f"正在分析技能结构: {skill_path}")
        
        structure = {
            'skill_path': skill_path,
            'has_skill_md': False,
            'has_scripts_dir': False,
            'script_files': [],
            'has_reports_dir': False,
            'structure_issues': []
        }
        
        # 检查SKILL.md文件
        skill_md_path = os.path.join(skill_path, 'SKILL.md')
        if os.path.exists(skill_md_path):
            structure['has_skill_md'] = True
        else:
            structure['structure_issues'].append('缺少SKILL.md文件')
        
        # 检查scripts目录
        scripts_dir = os.path.join(skill_path, 'scripts')
        if os.path.exists(scripts_dir) and os.path.isdir(scripts_dir):
            structure['has_scripts_dir'] = True
            # 列出脚本文件
            for file in os.listdir(scripts_dir):
                if file.endswith('.py'):
                    structure['script_files'].append(file)
        else:
            structure['structure_issues'].append('缺少scripts目录')
        
        # 检查reports目录
        reports_dir = os.path.join(skill_path, 'reports')
        if os.path.exists(reports_dir) and os.path.isdir(reports_dir):
            structure['has_reports_dir'] = True
        else:
            # reports目录不是必须的，可以在运行时创建
            pass
        
        # 保存结构分析结果
        os.makedirs('./reports', exist_ok=True)
        with open('./reports/structure_analysis.json', 'w', encoding='utf-8') as f:
            json.dump(structure, f, ensure_ascii=False, indent=2)
        
        print(f"技能结构分析完成，结果已保存到 ./reports/structure_analysis.json")
        return structure
    except Exception as e:
        print(f"分析技能结构时出错: {e}")
        print(traceback.format_exc())
        return {'error': str(e)}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyze_skill_structure(sys.argv[1])
    else:
        print("请提供技能路径")
