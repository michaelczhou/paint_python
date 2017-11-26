import argparse
import re
import numpy as np
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path',type=str, default='/home/zc/project/17-11-23/1/exe.txt')
    args = parser.parse_args()

    #tar = re.compile('curr_target: (\d+.\d+)  (\d+.\d+)')
    #tar.match
    res = [re.findall(r'curr_target: (\d+.\d+)  (\d+.\d+)',line)
            for line in open(args.path)]
    res = [(float(e[0][0]), float(e[0][1])) for e in res if e]
    print len(res)
    #print res
    res1 = [re.findall(r'position: (\d+.\d+)   (-?\d+.\d+)   (\d+.\d+)',line)
            for line in open(args.path)]
    res1 = [(float(e[0][1]), float(e[0][2])) for e in res1 if e]
    print len(res)
    #print res1
    x, y = zip(*res)
    x1,y1 = zip(*res1)
    # #print x
    plt.figure()
    plt.plot(x, y,'g-', label="target")
    plt.plot(x1,y1,'r-', label="position")
    plt.legend()
    plt.show()
    
    
if __name__ == '__main__':
	main()