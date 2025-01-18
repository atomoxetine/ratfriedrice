#!/bin/bash

python3 getwords.py > words.txt
cat words.txt | ./mesher > meshed.txt
