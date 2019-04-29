import sys,os
os.environ['SPARK_HOME']="D:\software_install_address\spark-2.3.0-bin-hadoop2.7"
sys.path.append("D:\software_install_address\spark-2.3.0-bin-hadoop2.7\python")
from operator import add
from pyspark import SparkContext
import pyspark
if __name__ == "__main__":
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile('words.txt')
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))
    sc.stop()
