import os
from pandas import read_excel
from numpy import nan, nanmean, nanstd
os.chdir(os.path.abspath(os.path.dirname(__file__)))#解析进入程序所在目录
pf_1, pf_2, pf_3 = read_excel("data1.xls"), read_excel("data2.xls"), read_excel("data3.xls")

print("Average", "Standard deviation", "Variance", "Small probability events", "Notable", sep = "\t")
for target in list(pf_1.columns):
	try:
		array_1, array_2, array_3 = sorted(list(pf_1[target])), sorted(list(pf_2[target])), sorted(list(pf_3[target]))
	except:
		continue
	for array in (array_1, array_2, array_3):
		try:
			mean = nanmean(array)
			std = nanstd(array)
			if not ((mean == 0 or mean == nan or str(mean).lower() == "nan") or (std == 0 or std == nan or str(std).lower() == "nan")):
				print("{0:.2f}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(mean, std, std ** 2, len([i for i in array if i < mean - 3 * std]), len([i for i in array if i < mean - 2 * std])))
		except:
			pass
	print()