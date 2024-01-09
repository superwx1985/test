from xml.sax.handler import ContentHandler
from xml.sax import parse

import csv

csv_header = ['timeStamp', 'elapsed', 'label', 'responseCode', 'responseMessage', 'threadName', 'dataType', 'success', 'failureMessage', 'bytes', 'sentBytes', 'grpThreads', 'allThreads', 'Latency', 'IdleTime', 'Connect']
xml_attr = ['ts', 't', 'lb', 'rc', 'rm', 'tn', 'dt', 's', '(failureMessage)', 'by', 'sby', 'ng', 'na', 'lt', 'it', 'ct']
mapping = dict(zip(xml_attr, csv_header))


class Converter(ContentHandler):

    def __init__(self, csv_filename):
        self.output_file = open(csv_filename, 'w', newline='')
        self.csv_writer = csv.DictWriter(self.output_file, mapping.values())

    def __del__(self):
        self.output_file.close()

    def startDocument(self):
        self.csv_writer.writeheader()

    def startElement(self, name, attrs):
        if name == 'httpSample':
            d = {}
            for name in attrs.getNames():
                d[mapping[name]] = attrs.getValue(name)
            self.csv_writer.writerow(d)


def change_jmeter_result_format(filename):
    parse(filename, Converter("%s.csv" % filename))
    print("%s.csv" % filename)


if __name__ == '__main__':
    import sys

    #try:
    # main(sys.argv[1])
    change_jmeter_result_format(r'C:\SWDTOOLS\apache-jmeter-4.0\bin\case\test1.xml')
    #except:
    #    print("\nUsage: %s input_file" % (sys.argv[0]))
    #    print("\n  Input file should contain http samples created by JMeter in JTL format.\n")