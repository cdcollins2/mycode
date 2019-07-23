#!/usr/bin/env python3
import yaml

def main():
    yammyfile = open("/home/student/mycode/yamlintro/myYaml.yml", "r")

    pyyammy = yaml.load(yammyfile)

    print(pyyammy)

main()
