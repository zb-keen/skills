#!/usr/bin/env python3
"""
技能评审工具主入口脚本
"""

import os
import sys
import argparse
import traceback


def review_skill(skill_path):
    """评审指定技能"""
    try:
        print(f"正在评审技能: {skill_path}")
        
        # 导入结构分析模块
        from structure_analyzer import analyze_skill_structure
        structure_result = analyze_skill_structure(skill_path)
        
        # 导入质量评估模块
        from quality_evaluator import evaluate_skill_quality
        quality_result = evaluate_skill_quality(skill_path)
        
        # 导入需求匹配模块
        from requirement_matcher import match_requirements
        # 这里可以从用户输入或配置文件获取需求描述
        requirements = "分析项目代码，回答关于特定字段的问题"
        requirement_result = match_requirements(skill_path, requirements)
        
        # 导入报告生成模块
        from report_generator import generate_review_report
        generate_review_report(skill_path, structure_result, quality_result, requirement_result)
        
    except Exception as e:
        print(f"评审技能时出错: {e}")
        print(traceback.format_exc())


def generate_report():
    """生成评审报告"""
    try:
        print("正在生成评审报告...")
        # 导入报告生成模块
        from report_generator import generate_review_report
        generate_review_report()
    except Exception as e:
        print(f"生成报告时出错: {e}")
        print(traceback.format_exc())


def main():
    """主函数"""
    try:
        parser = argparse.ArgumentParser(description='技能评审工具')
        subparsers = parser.add_subparsers(dest='command', help='子命令')
        
        # 评审技能子命令
        review_parser = subparsers.add_parser('review', help='评审指定技能')
        review_parser.add_argument('skill_path', help='技能路径')
        
        # 报告生成子命令
        subparsers.add_parser('report', help='生成评审报告')
        
        args = parser.parse_args()
        
        if args.command == 'review':
            review_skill(args.skill_path)
        elif args.command == 'report':
            generate_report()
        else:
            parser.print_help()
    except Exception as e:
        print(f"执行命令时出错: {e}")
        print(traceback.format_exc())


if __name__ == '__main__':
    main()
