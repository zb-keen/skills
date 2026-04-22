#!/usr/bin/env python3
"""
报告生成脚本
"""

import os
import json
import traceback


def generate_review_report(skill_path=None, structure_result=None, quality_result=None, requirement_result=None):
    """生成技能评审报告"""
    try:
        print("正在生成技能评审报告...")
        
        # 如果没有提供参数，尝试从文件中读取
        if not structure_result:
            structure_file = './reports/structure_analysis.json'
            if os.path.exists(structure_file):
                with open(structure_file, 'r', encoding='utf-8') as f:
                    structure_result = json.load(f)
        
        if not quality_result:
            quality_file = './reports/quality_evaluation.json'
            if os.path.exists(quality_file):
                with open(quality_file, 'r', encoding='utf-8') as f:
                    quality_result = json.load(f)
        
        if not requirement_result:
            requirement_file = './reports/requirement_matching.json'
            if os.path.exists(requirement_file):
                with open(requirement_file, 'r', encoding='utf-8') as f:
                    requirement_result = json.load(f)
        
        # 生成评审报告
        os.makedirs('./reports', exist_ok=True)
        with open('./reports/skill_review.md', 'w', encoding='utf-8') as f:
            f.write('# 技能评审报告\n\n')
            
            # 基本信息
            f.write('## 基本信息\n\n')
            if skill_path:
                f.write(f'技能路径: {skill_path}\n\n')
            elif structure_result and 'skill_path' in structure_result:
                f.write(f'技能路径: {structure_result["skill_path"]}\n\n')
            
            # 结构分析
            f.write('## 结构分析\n\n')
            if structure_result:
                if 'has_skill_md' in structure_result:
                    f.write(f'- SKILL.md: {"存在" if structure_result["has_skill_md"] else "缺失"}\n')
                if 'has_scripts_dir' in structure_result:
                    f.write(f'- scripts目录: {"存在" if structure_result["has_scripts_dir"] else "缺失"}\n')
                if 'script_files' in structure_result:
                    f.write(f'- 脚本文件: {len(structure_result["script_files"])} 个\n')
                    for script in structure_result["script_files"]:
                        f.write(f'  - {script}\n')
                if 'structure_issues' in structure_result and structure_result["structure_issues"]:
                    f.write('\n**结构问题:**\n')
                    for issue in structure_result["structure_issues"]:
                        f.write(f'- {issue}\n')
            f.write('\n')
            
            # 需求匹配
            f.write('## 需求匹配\n\n')
            if requirement_result:
                if 'requirements' in requirement_result:
                    f.write(f'**用户需求:** {requirement_result["requirements"]}\n\n')
                if 'matched_features' in requirement_result:
                    f.write('**匹配的功能:**\n')
                    for feature in requirement_result["matched_features"]:
                        f.write(f'- {feature}\n')
                if 'missing_features' in requirement_result:
                    f.write('\n**缺失的功能:**\n')
                    for feature in requirement_result["missing_features"]:
                        f.write(f'- {feature}\n')
                if 'match_score' in requirement_result:
                    f.write(f'\n**匹配分数:** {requirement_result["match_score"]:.2f}/100\n')
            f.write('\n')
            
            # 质量评估
            f.write('## 质量评估\n\n')
            if quality_result:
                if 'code_quality' in quality_result:
                    f.write('**代码质量:**\n')
                    for key, value in quality_result["code_quality"].items():
                        f.write(f'- {key}: {value:.2f}/100\n')
                if 'documentation_quality' in quality_result:
                    f.write('\n**文档质量:**\n')
                    for key, value in quality_result["documentation_quality"].items():
                        f.write(f'- {key}: {value:.2f}/100\n')
                if 'overall_score' in quality_result:
                    f.write(f'\n**总体评分:** {quality_result["overall_score"]:.2f}/100\n')
            f.write('\n')
            
            # 改进建议
            f.write('## 改进建议\n\n')
            suggestions = []
            
            # 基于结构分析的建议
            if structure_result and 'structure_issues' in structure_result:
                for issue in structure_result["structure_issues"]:
                    if 'SKILL.md' in issue:
                        suggestions.append('创建完整的SKILL.md文件，包含技能的功能描述、使用方法和实现细节')
                    elif 'scripts目录' in issue:
                        suggestions.append('创建scripts目录，并添加必要的脚本文件')
            
            # 基于需求匹配的建议
            if requirement_result and 'missing_features' in requirement_result:
                for feature in requirement_result["missing_features"]:
                    if feature == '代码分析':
                        suggestions.append('添加代码分析功能，支持静态代码分析和代码扫描')
                    elif feature == '字段分析':
                        suggestions.append('添加字段分析功能，支持变量和属性的分析')
                    elif feature == '依赖分析':
                        suggestions.append('添加依赖分析功能，生成依赖关系图')
                    elif feature == '报告生成':
                        suggestions.append('添加报告生成功能，生成详细的分析报告')
                    elif feature == '错误处理':
                        suggestions.append('增强错误处理机制，提高技能的稳定性')
            
            # 基于质量评估的建议
            if quality_result:
                if 'code_quality' in quality_result:
                    code_quality = quality_result["code_quality"]
                    if code_quality.get('has_error_handling', 0) < 70:
                        suggestions.append('增加错误处理机制，提高代码的健壮性')
                    if code_quality.get('code_readability', 0) < 70:
                        suggestions.append('优化代码结构，提高代码的可读性和可维护性')
                if 'documentation_quality' in quality_result:
                    doc_quality = quality_result["documentation_quality"]
                    if doc_quality.get('documentation_completeness', 0) < 70:
                        suggestions.append('完善文档内容，确保文档的完整性和准确性')
                    if doc_quality.get('documentation_clarity', 0) < 70:
                        suggestions.append('提高文档的清晰度和易用性，添加更多的使用示例')
            
            # 输出改进建议
            if suggestions:
                for suggestion in suggestions:
                    f.write(f'- {suggestion}\n')
            else:
                f.write('未发现明显问题，技能质量良好\n')
            f.write('\n')
            
            # 结论
            f.write('## 结论\n\n')
            if quality_result and 'overall_score' in quality_result:
                score = quality_result['overall_score']
                if score >= 80:
                    f.write('技能质量优秀，满足用户需求\n')
                elif score >= 60:
                    f.write('技能质量良好，有一些改进空间\n')
                else:
                    f.write('技能质量需要显著改进\n')
            else:
                f.write('无法评估技能质量\n')
            f.write('\n')
            
            # 注意事项
            f.write('## 注意事项\n\n')
            f.write('本报告基于自动化分析生成，仅供参考\n')
            f.write('建议结合实际使用情况进行综合评估\n')
        
        print(f"技能评审报告已生成，保存到 ./reports/skill_review.md")
        return True
    except Exception as e:
        print(f"生成评审报告时出错: {e}")
        print(traceback.format_exc())
        return False


if __name__ == '__main__':
    generate_review_report()
