#!/usr/bin/env python3
"""
分离30讲例题汇总的题目和解析
- 题目文件：只保留题目
- 解析文件：保留完整解析
"""
import re
from pathlib import Path


def split_examples(input_file: Path):
    content = input_file.read_text(encoding='utf-8')
    lines = content.split('\n')

    questions = []
    solutions = []

    # 状态机：0=frontmatter, 1=普通内容, 2=例题题目, 3=例题解析
    state = 0
    current_example_title = ''
    current_question_lines = []
    current_solution_lines = []
    in_frontmatter = True
    first_line = True

    def save_current_example():
        nonlocal current_example_title, current_question_lines, current_solution_lines
        if current_example_title:
            # 清理题目末尾空行
            while current_question_lines and current_question_lines[-1].strip() == '':
                current_question_lines.pop()

            questions.append(current_example_title)
            questions.extend(current_question_lines)
            questions.append('')
            questions.append('---')
            questions.append('')

            solutions.append(current_example_title)
            solutions.extend(current_solution_lines)
            solutions.append('')
            solutions.append('---')
            solutions.append('')

            current_example_title = ''
            current_question_lines = []
            current_solution_lines = []

    for i, line in enumerate(lines):
        # 跳过 frontmatter
        if in_frontmatter:
            if first_line and line.strip() == '---':
                first_line = False
                continue
            if not first_line and line.strip() == '---':
                in_frontmatter = False
                questions.append(line)
                solutions.append(line)
                continue
            questions.append(line)
            solutions.append(line)
            continue

        # 检测讲标题
        if re.match(r'^## 第\d+讲', line):
            save_current_example()
            questions.append(line)
            solutions.append(line)
            continue

        # 检测例题标题
        example_match = re.match(r'^### 例(\d+\.\d+)$', line)
        if example_match:
            save_current_example()
            current_example_title = line
            state = 2  # 开始收集题目
            continue

        # 检测解析开始
        is_solution_start = (
            re.match(r'^分析\s*$', line) or
            re.match(r'^分析\s+', line) or
            re.match(r'^解\s*$', line) or
            re.match(r'^解\s+', line) or
            re.match(r'^方法总结\s*$', line) or
            re.match(r'^方法总结\s+', line) or
            re.match(r'^注\s*$', line) or
            re.match(r'^注\s+', line) or
            re.match(r'^公式\s', line) or
            line.startswith('方法总结 ') or
            line.startswith('注 ')
        )

        if state == 2 and is_solution_start:
            state = 3  # 切换到解析
            current_solution_lines.append(line)
            continue

        # 收集内容
        if state == 2:
            current_question_lines.append(line)
        elif state == 3:
            current_solution_lines.append(line)
        else:
            # 不在例题中，直接添加到两个文件
            questions.append(line)
            solutions.append(line)

    # 保存最后一个例题
    save_current_example()

    return '\n'.join(questions), '\n'.join(solutions)


def main():
    input_file = Path('D:/tool/Obsidian/math/02_Learning/30讲例题汇总.md')
    output_dir = Path('D:/tool/Obsidian/math/02_Learning')

    questions, solutions = split_examples(input_file)

    # 写入题目文件
    question_file = output_dir / '30讲例题汇总_题目.md'
    question_file.write_text(questions, encoding='utf-8')
    print(f"题目文件已生成: {question_file}")

    # 写入解析文件
    solution_file = output_dir / '30讲例题汇总_解析.md'
    solution_file.write_text(solutions, encoding='utf-8')
    print(f"解析文件已生成: {solution_file}")

    # 统计
    q_count = len(re.findall(r'^### 例\d+\.\d+', questions, re.MULTILINE))
    s_count = len(re.findall(r'^### 例\d+\.\d+', solutions, re.MULTILINE))
    print(f"\n统计：")
    print(f"  题目文件: {q_count} 道例题")
    print(f"  解析文件: {s_count} 道例题")


if __name__ == '__main__':
    main()
