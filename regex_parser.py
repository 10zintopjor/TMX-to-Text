import re
from pathlib import Path

if __name__ =="__main__":
    norm_rules = []
    regex_file = Path('./regex.txt').read_text(encoding='utf-8')
    rules = regex_file.splitlines()
    for rule in rules:
        if rule:
            rule_parts = rule.split('\t')
            norm_rules.append((rule_parts[0], rule_parts[2]))
    print(norm_rules)