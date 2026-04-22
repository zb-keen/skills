#!/usr/bin/env python3
"""
代码分析器主入口脚本
"""

import os
import sys
import argparse
import traceback


def analyze_structure():
    """分析项目结构"""
    try:
        print("正在分析项目结构...")
        # 导入结构分析模块
        from structure_analyzer import analyze_project_structure
        analyze_project_structure()
    except Exception as e:
        print(f"分析项目结构时出错: {e}")
        print(traceback.format_exc())


def analyze_field(field_name):
    """分析指定字段"""
    try:
        print(f"正在分析字段: {field_name}")
        # 导入代码搜索模块
        from code_searcher import search_field
        results = search_field(field_name)
        
        # 导入逻辑分析模块
        from logic_analyzer import analyze_field_logic
        analyze_field_logic(field_name, results)
    except Exception as e:
        print(f"分析字段时出错: {e}")
        print(traceback.format_exc())


def analyze_dependencies():
    """分析代码依赖"""
    try:
        print("正在分析代码依赖...")
        # 导入结构分析模块
        from structure_analyzer import analyze_dependencies
        analyze_dependencies()
    except Exception as e:
        print(f"分析代码依赖时出错: {e}")
        print(traceback.format_exc())


def generate_report():
    """生成分析报告"""
    try:
        print("正在生成分析报告...")
        # 导入报告生成模块
        from report_generator import generate_report
        generate_report()
    except Exception as e:
        print(f"生成分析报告时出错: {e}")
        print(traceback.format_exc())


def main():
    """主函数"""
    try:
        parser = argparse.ArgumentParser(description='代码分析器')
        subparsers = parser.add_subparsers(dest='command', help='子命令')
        
        # 结构分析子命令
        subparsers.add_parser('structure', help='分析项目结构')
        
        # 字段分析子命令
        analyze_parser = subparsers.add_parser('analyze', help='分析指定字段')
        analyze_parser.add_argument('field', help='要分析的字段名')
        
        # 依赖分析子命令
        subparsers.add_parser('dependencies', help='分析代码依赖')
        
        # 报告生成子命令
        subparsers.add_parser('report', help='生成分析报告')
        
        args = parser.parse_args()
        
        if args.command == 'structure':
            analyze_structure()
        elif args.command == 'analyze':
            analyze_field(args.field)
        elif args.command == 'dependencies':
            analyze_dependencies()
        elif args.command == 'report':
            generate_report()
        else:
            parser.print_help()
    except Exception as e:
        print(f"执行命令时出错: {e}")
        print(traceback.format_exc())


if __name__ == '__main__':
    main()
