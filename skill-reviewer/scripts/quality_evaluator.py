#!/usr/bin/env python3
"""
质量评估脚本
"""

import os
import sys
import json
import traceback


def evaluate_skill_quality(skill_path):
    """评估技能质量"""
    try:
        print(f"正在评估技能质量: {skill_path}")
        
        quality_result = {
            'skill_path': skill_path,
            'code_quality': {
                'has_error_handling': 0,
                'code_readability': 0,
                'performance_considerations': 0
            },
            'documentation_quality': {
                'documentation_completeness': 0,
                'documentation_clarity': 0,
                'documentation_structure': 0
            },
            'overall_score': 0
        }
        
        # 评估代码质量
        scripts_dir = os.path.join(skill_path, 'scripts')
        if os.path.exists(scripts_dir) and os.path.isdir(scripts_dir):
            error_handling_count = 0
            total_files = 0
            
            for file in os.listdir(scripts_dir):
                if file.endswith('.py'):
                    total_files += 1
                    file_path = os.path.join(scripts_dir, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            # 检查错误处理
                            if 'try:' in content and 'except:' in content:
                                error_handling_count += 1
                    except Exception as e:
                        print(f"分析文件 {file} 时出错: {e}")
            
            if total_files > 0:
                quality_result['code_quality']['has_error_handling'] = error_handling_count / total_files * 100
                # 简单评估代码可读性（基于文件长度）
                quality_result['code_quality']['code_readability'] = min(100, 100 - (total_files * 5))
                # 简单评估性能考虑（基于文件数量）
                quality_result['code_quality']['performance_considerations'] = min(100, 100 - (total_files * 3))
        
        # 评估文档质量
        skill_md_path = os.path.join(skill_path, 'SKILL.md')
        if os.path.exists(skill_md_path):
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # 简单评估文档完整性（基于文档长度）
                quality_result['documentation_quality']['documentation_completeness'] = min(100, len(content) / 5)
                # 简单评估文档清晰度（基于关键词）
                clarity_keywords = ['使用指南', '功能特点', '工作流程', '使用案例', '操作命令']
                clarity_count = sum(1 for keyword in clarity_keywords if keyword in content)
                quality_result['documentation_quality']['documentation_clarity'] = clarity_count / len(clarity_keywords) * 100
                # 简单评估文档结构（基于标题数量）
                structure_count = content.count('#')
                quality_result['documentation_quality']['documentation_structure'] = min(100, structure_count * 10)
        
        # 计算总体评分
        code_score = sum(quality_result['code_quality'].values()) / len(quality_result['code_quality'])
        doc_score = sum(quality_result['documentation_quality'].values()) / len(quality_result['documentation_quality'])
        quality_result['overall_score'] = (code_score * 0.6 + doc_score * 0.4)
        
        # 保存质量评估结果
        os.makedirs('./reports', exist_ok=True)
        with open('./reports/quality_evaluation.json', 'w', encoding='utf-8') as f:
            json.dump(quality_result, f, ensure_ascii=False, indent=2)
        
        print(f"技能质量评估完成，结果已保存到 ./reports/quality_evaluation.json")
        return quality_result
    except Exception as e:
        print(f"评估技能质量时出错: {e}")
        print(traceback.format_exc())
        return {'error': str(e)}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        evaluate_skill_quality(sys.argv[1])
    else:
        print("请提供技能路径")
