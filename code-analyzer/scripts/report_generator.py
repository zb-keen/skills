#!/usr/bin/env python3
"""
报告生成脚本
"""

import os
import json


def generate_report():
    """生成综合分析报告"""
    reports_dir = '../reports'
    
    # 检查报告目录
    if not os.path.exists(reports_dir):
        print("没有分析结果，请先运行分析命令")
        return
    
    # 收集所有分析结果
    reports = {
        'structure': None,
        'dependencies': None,
        'field_analyses': []
    }
    
    # 读取项目结构报告
    structure_file = os.path.join(reports_dir, 'structure_report.json')
    if os.path.exists(structure_file):
        with open(structure_file, 'r', encoding='utf-8') as f:
            reports['structure'] = json.load(f)
    
    # 读取依赖分析报告
    dependencies_file = os.path.join(reports_dir, 'dependencies.json')
    if os.path.exists(dependencies_file):
        with open(dependencies_file, 'r', encoding='utf-8') as f:
            reports['dependencies'] = json.load(f)
    
    # 读取字段分析报告
    for file in os.listdir(reports_dir):
        if file.endswith('_logic_analysis.json'):
            field_name = file.replace('_logic_analysis.json', '')
            field_file = os.path.join(reports_dir, file)
            with open(field_file, 'r', encoding='utf-8') as f:
                reports['field_analyses'].append({
                    'field': field_name,
                    'analysis': json.load(f)
                })
    
    # 生成综合报告
    with open(os.path.join(reports_dir, 'comprehensive_report.md'), 'w', encoding='utf-8') as f:
        f.write('# 综合代码分析报告\n\n')
        
        # 项目结构部分
        if reports['structure']:
            f.write('## 项目结构\n\n')
            f.write(f'项目根目录: {reports["structure"]["root"]}\n\n')
            f.write(f'文件数量: {len(reports["structure"]["files"])}\n')
            f.write(f'目录数量: {len(reports["structure"]["directories"])}\n\n')
        
        # 依赖分析部分
        if reports['dependencies']:
            f.write('## 代码依赖\n\n')
            f.write(f'分析文件数量: {len(reports["dependencies"])}\n\n')
        
        # 字段分析部分
        if reports['field_analyses']:
            f.write('## 字段分析\n\n')
            for field_analysis in reports['field_analyses']:
                field_name = field_analysis['field']
                analysis = field_analysis['analysis']
                
                f.write(f'### {field_name} 字段\n\n')
                total_usage = sum(len(items) for items in analysis.values())
                f.write(f'总使用次数: {total_usage}\n\n')
                
                for pattern_type, items in analysis.items():
                    if items:
                        f.write(f'- {pattern_type}: {len(items)} 处\n')
                f.write('\n')
        
        # 总结和建议
        f.write('## 总结和建议\n\n')
        f.write('### 代码结构建议\n')
        f.write('- 保持代码结构清晰，避免过多的嵌套依赖\n')
        f.write('- 合理组织文件和目录，提高代码可读性\n')
        f.write('- 定期进行代码分析，及时发现潜在问题\n\n')
        
        f.write('### 字段使用建议\n')
        f.write('- 为字段添加清晰的注释，说明其用途\n')
        f.write('- 避免在多个文件中频繁修改同一字段\n')
        f.write('- 考虑使用常量或枚举替代硬编码值\n\n')
        
        f.write('### 性能优化建议\n')
        f.write('- 避免不必要的字段赋值和访问\n')
        f.write('- 优化条件判断逻辑，减少复杂度\n')
        f.write('- 考虑使用缓存减少重复计算\n')
    
    print(f"综合分析报告已生成，保存到 ../reports/comprehensive_report.md")
