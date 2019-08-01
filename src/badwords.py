#!/usr/bin/env python3
import json
import os
import sys

def make_results(grep_lines, base_path):
    output = []
    for line in grep_lines:
        if not (len(line.strip())):
            continue
        print(line)

        filename = line.split(":")[0]
        filename = os.path.relpath(filename, base_path)
        line_num = int(line.split(":")[1])
        if filename.startswith("./"):
            filename = filename[2:]

        obj = {"check_id": "badword", "path": filename, "start": {"line": line_num}}
        output.append(obj)
    return output


def format_json(grep_lines, stream, base):
    results = make_results(grep_lines, base)
    obj = {"results": results}
    json.dump(obj, stream, indent=4, separators=(",", ": "))


if __name__ == "__main__":
    print("starting now")
    base = sys.argv[1]
    fout_name = sys.argv[2]
    grep_output = sys.stdin.readlines()
    with open(fout_name, "w") as fout:
        format_json(grep_output, fout, base)