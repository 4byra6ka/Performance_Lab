import json
import os


def task3(values_file: str, tests_file: str, report_file: str) -> None:
    if os.path.exists(values_file):
        with open(values_file, 'r', encoding='utf-8') as r_file:
            values = json.load(r_file)
    if os.path.exists(tests_file):
        with open(tests_file, 'r', encoding='utf-8') as r_file:
            tests = json.load(r_file)
    report = get_report(tests['tests'], values['values'])
    with open(report_file, 'w', encoding='utf-8') as w_file:
        json.dump({'tests': report}, w_file, indent=2)


def get_report(report: list, values: list) -> list:
    if isinstance(report, list):
        for one_report in report:
            if 'value' in one_report:
                one_report['value'] = get_value(values, one_report['id'])
            if 'values' in one_report:
                get_report(one_report['values'], values)
    return report


def get_value(values: list, value_id: int) -> str:
    for value in values:
        if value['id'] == value_id:
            values.pop(values.index(value))
            return value['value']


if __name__ == '__main__':
    print(task3('values.json', 'tests.json', 'report.json'))
