import math

# Could create a way for them to add drums and weights to the table; not necessary now
drum_weight_table = {
	'51663':{'no_drum': 384, 'with_drum': 409},
	'10834':{'no_drum': 390, 'with_drum': 415},
	'51359':{'no_drum': 384, 'with_drum': 409},
	'50798':{'no_drum': 384, 'with_drum': 409},
	'51581':{'no_drum': 340, 'with_drum': 365},
	'50688':{'no_drum': 340, 'with_drum': 365},
	'50629':{'no_drum': 340, 'with_drum': 365},
	'50628':{'no_drum': 340, 'with_drum': 365},
	'10449':{'no_drum': 384, 'with_drum': 409},
	'50670':{'no_drum': 384, 'with_drum': 409},
	'10854':{'no_drum': 452, 'with_drum': 477},
	'10523':{'no_drum': 340, 'with_drum': 365},
	'51559':{'no_drum': 340, 'with_drum': 365},
	'50552':{'no_drum': 384, 'with_drum': 409},
	'50290':{'no_drum': 384, 'with_drum': 409},
	'51325':{'no_drum': 340, 'with_drum': 365},
	'50551':{'no_drum': 384, 'with_drum': 409},
	'51874':{'no_drum': 384, 'with_drum': 409},
	'11170':{'no_drum': 384, 'with_drum': 409},
	'50668':{'no_drum': 340, 'with_drum': 365},
	'12015':{'no_drum': 384, 'with_drum': 409},
	'12012':{'no_drum': 384, 'with_drum': 409},
	'10504':{'no_drum': 384, 'with_drum': 409},
	'11185':{'no_drum': 452, 'with_drum': 477},
	'11367':{'no_drum': 452, 'with_drum': 477},
	'11150':{'no_drum': 452, 'with_drum': 477},
	'10254':{'no_drum': 340, 'with_drum': 365},
	'10840':{'no_drum': 452, 'with_drum': 477},
	'10122':{'no_drum': 452, 'with_drum': 477},
	'12020':{'no_drum': 370, 'with_drum': 395},
	'51358':{'no_drum': 384, 'with_drum': 409},
	'51676':{'no_drum': 384, 'with_drum': 409},
	'50687':{'no_drum': 340, 'with_drum': 365},
	'50686':{'no_drum': 340, 'with_drum': 365},
	'10757':{'no_drum': 340, 'with_drum': 365},
	'13129':{'no_drum': 384, 'with_drum': 409},
	'50674':{'no_drum': 384, 'with_drum': 409},
	'11352':{'no_drum': 384, 'with_drum': 409},
	'10530':{'no_drum': 452, 'with_drum': 477},
	'12075':{'no_drum': 452, 'with_drum': 477},
	'10258':{'no_drum': 452, 'with_drum': 477},
	'51692':{'no_drum': 452, 'with_drum': 477},
	'13249':{'no_drum': 452, 'with_drum': 477},
	'13157':{'no_drum': 452, 'with_drum': 477},
	'13114':{'no_drum': 384, 'with_drum': 409},
	'13265':{'no_drum': 452, 'with_drum': 477},
	'13139':{'no_drum': 452, 'with_drum': 477},
	'13481':{'no_drum': 452, 'with_drum': 477},
	'13153':{'no_drum': 360, 'with_drum': 385},
	'13277':{'no_drum': 452, 'with_drum': 477}
}

# Should it take a csv and generate the list, or should it take a list?

def remove_invalid_scans(scan_list):
	# Replace letter, 9th char, with a "D" first
	scan_list = [scan[:8] + 'D' + scan[9:] for scan in scan_list]
	# Remove scans that are too short
	scan_list = [scan for scan in scan_list if len(scan) > 12]
	# Remove duplicate scans
	scan_list = list(set(scan_list))
	return scan_list

def get_unique_drums(scan_list):
	# Drum = item code + date
	itemCode_date_list = [scan[3:15] for scan in scan_list]
	itemCode_date_unique_list = list(set(itemCode_date_list))
	return itemCode_date_unique_list

def calculate_count_of_unique_drums(scan_list):
	itemCode_date_list = [scan[3:15] for scan in scan_list]
	# Calculate the counts for each drum
	itemCode_date_dict = {}
	for drum in itemCode_date_list:
		if drum in itemCode_date_dict:
			itemCode_date_dict[drum]['count'] += 1
		else:
			itemCode_date_dict[drum] = {'count': 1}
	return itemCode_date_dict

def calculate_weight_of_unique_drums(itemCode_date_dict, drum_weight_table):
	for drum in itemCode_date_dict:
		itemCode = drum[:5]
		itemCode_date_dict[drum]['weight'] = itemCode_date_dict[drum]['count'] * drum_weight_table[itemCode]['with_drum']
	return itemCode_date_dict

def calculate_pallet_count(itemCode_date_dict):
	total_drums = 0
	for drum in itemCode_date_dict:
		total_drums += itemCode_date_dict[drum]['count']
	pallet_count = math.ceil(total_drums/4)
	return pallet_count

def calculate_pallet_weight(pallet_count):
	pallet_weight = pallet_count * 7.5
	return pallet_weight

scan_list = [
'06910258A0328174520000120',
'06910258A0328174520000121',
'06910258A0328174520000122',
'06910258A0328174520000123',
'06910258A0328174520000124',
'06910258A0328174520000125',
'06910258A0328174520000126',
'06910258A0328174520000127',
'06910258A0328174520000128',
'06910258A0328174520000129',
'06910258A0328174520000130',
'06910258A0328174520000131',
'06910258A0328174520000132',
'06910258A0328174520000133',
'06910258A0328174520000134',
'06910258A0328174520000135',
'06910258A0328174520000136',
'06910258A0328174520000137',
'06910258A0328174520000138',
'06910258A0328174520000139',
'06910258A0328174520000140',
'06910258A0328174520000141',
'06910258A0328174520000142',
'06910258A0328174520000143',
'06910258A0328174520000144',
'06910258A0328174520000145',
'06910258A0328174520000146',
'06910258A0328174520000147',
'06910258A0328174520000148',
'06910258A0328174520000149',
'06910258A0328174520000150',
'06910258A0328174520000151',
'06910258A0328174520000152',
'06910258A0328174520000153',
'06910258A0328174520000154',
'06910258A0328174520000155',
'06910258A0328174520000156',
'06910258A0328174520000157',
'06910258A0328174520000158',
'06910258A0328174520000159',
'06910258A0328174520000160',
'06910258A0328174520000161',
'06910258A0328174520000162',
'06910258A0328174520000163',
'06910258A0328174520000164',
'06910258A0328174520000165',
'06910258A0328174520000166',
'06910258A0328174520000167',
'06910258B0328174520020515',
'06910258B0328174520020516',
'06910258B0328174520020517',
'06910258B0328174520020518',
'06910258B0328174520020519',
'06910258B0328174520020520',
'06910258B0328174520020521',
'06910258B0328174520020522',
'06910258B0328174520020523',
'06910258B0328174520020524',
'06910258B0328174520020525',
'06910258B0328174520020526',
'06910258B0328174520020527',
'06910258B0328174520020528',
'06910258B0328174520020529',
'06910258B0328174520020530',
'06910258B0328174520020531',
'06910258B0328174520020532',
'06910258B0328174520020533',
'06910258B0328174520020534',
'06910258B0328174520020535',
'06910258B0328174520020536',
'06910258B0328174520020537',
'06910258B0328174520020538',
'06910258B0328174520020539',
'06910258B0328174520020540',
'06910258B0328174520020541',
'06910258B0328174520020542',
'06910258B0328174520020543',
'06910258B0328174520020544',
'06910258B0328174520020545',
'06910258B0328174520020546',
'06910258B0328174520020547',
'06910258B0328174520020548',
'06910258B0328174520020549',
'06910258B0328174520020550',
'06910258B0328174520020551',
'06910258B0328174520020552',
'06910258B0328174520020553',
'06910258B0328174520020554']