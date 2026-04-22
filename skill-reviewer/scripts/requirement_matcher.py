#!/usr/bin/env python3
"""
需求匹配脚本
"""

import os
import sys
import json
import traceback


def match_requirements(skill_path, requirements):
    """匹配用户需求与技能功能"""
    try:
        print(f"正在匹配需求: {requirements}")
        
        # 读取SKILL.md文件内容
        skill_md_path = os.path.join(skill_path, 'SKILL.md')
        skill_content = ''
        if os.path.exists(skill_md_path):
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                skill_content = f.read()
        
        # 分析需求匹配度
        match_result = {
            'requirements': requirements,
            'skill_content_analyzed': len(skill_content) > 0,
            'matched_features': [],
            'missing_features': [],
            'match_score': 0
        }
        
        # 简单的关键词匹配
        requirements_lower = requirements.lower()
        skill_content_lower = skill_content.lower()
        
        # 定义一些常见的功能关键词
        feature_keywords = {
            '代码分析': ['代码分析', '静态分析', '代码扫描'],
            '字段分析': ['字段分析', '变量分析', '属性分析'],
            '依赖分析': ['依赖分析', '依赖图', '依赖关系'],
            '报告生成': ['报告生成', '分析报告', '生成报告'],
            '错误处理': ['错误处理', '异常处理', '错误检测']
        }
        
        # 检查每个功能关键词
        for feature, keywords in feature_keywords.items():
            matched = False
            for keyword in keywords:
                if keyword in skill_content_lower:
                    matched = True
                    break
            
            if matched:
                match_result['matched_features'].append(feature)
            else:
                match_result['missing_features'].append(feature)
        
        # 计算匹配分数
        if feature_keywords:
            match_result['match_score'] = len(match_result['matched_features']) / len(feature_keywords) * 100
        
        # 保存需求匹配结果
        os.makedirs('./reports', exist_ok=True)
        with open('./reports/requirement_matching.json', 'w', encoding='utf-8') as f:
            json.dump(match_result, f, ensure_ascii=False, indent=2)
        
        print(f"需求匹配完成，结果已保存到 ./reports/requirement_matching.json")
        return match_result
    except Exception as e:
        print(f"匹配需求时出错: {e}")
        print(traceback.format_exc())
        return {'error': str(e)}


if __name__ == '__main__':
    if len(sys.argv) > 2:
        match_requirements(sys.argv[1], ' '.join(sys.argv[2:]))
    else:
        print("请提供技能路径和需求描述")
