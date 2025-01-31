#!/usr/bin/env python3

import subprocess

def free_space():
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    output, error = p.communicate()
    if p.returncode != 0:
        return ""
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
