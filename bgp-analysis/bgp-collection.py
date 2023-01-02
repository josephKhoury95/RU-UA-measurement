import pybgpstream
from pandas import *
from csv import reader
import csv

##############################
## russia ASN
##############################
## needs to compile a list of Russian ASNs
df = read_csv(r'./russian_asn.csv')
#print (df.tail())

df["ASN3"] = df["ASN3"].fillna(0)

df["ASN1"] = df["ASN1"].astype('int')
df["ASN2"] = df["ASN2"].astype('int')
df["ASN3"] = df["ASN3"].astype('int')

ASN1 = df["ASN1"].tolist()
ASN2 = df["ASN2"].tolist()
ASN3 = df["ASN3"].tolist()

ru_asn = ASN1 + ASN2 + ASN3
ru_asn = list(set(ru_asn))
ru_asn = [str(x) for x in ru_asn]

##############################
## ukraine ASN
##############################
## needs to compile a list of Ukrainian ASNs
df = read_csv(r'./ukraine_asn.csv')

df["ASN1"] = df["ASN1"].astype('int')

ASN1 = df["ASN1"].tolist()
ua_asn = list(set(ASN1))
ua_asn = [str(x) for x in ua_asn]



stream = pybgpstream.BGPStream(
    collectors=["rrc00", "rrc24", "rrc25", "rrc13"],#, "rrc01", "rrc03"],
    #collectors=["route-views2", "rrc00", "rrc12"],
    #collectors=["route-views2"],
    #record_type="ribs",
    record_type="updates",
    filter = "community *:666"
    #filter="peer 12389"
)


## December 2021 to June 2022
stream.add_interval_filter(1638316800, 1656719999)

Type_b = 0

for rec in stream.records():
    for elem in rec:
        ases = elem.fields['as-path'].split()
        if len(ases) > 0:
            ASN_n = ases[-1]

        if ASN_n in ru_asn or ASN_n in ua_asn:
            comm = [i.split(":")[1] for i in elem.fields['communities']]
            if '666' in comm:
                Type_b = 1
                data = [elem.record.time, ASN_n, elem.fields['communities'], elem.fields['prefix'], Type_b]
                
                with open ("./bgp_data_rrc00_rrc24_rrc25_rrc13_dec_jun.csv", 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
