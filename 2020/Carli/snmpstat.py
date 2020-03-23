#!/usr/bin/python3

#PYTHON SCRIPT TO MONITOR CPU LOAD AND MEMORY USAGE WITH SNMP AGENT

#IMPORT
from easysnmp import Session, snmp_get

#PARAMETERS
community = input('Enter the community --> ')
hostname = input('Enter hostname --> ')
version = int(input('Enter SNMP version --> '))

#########################################

#CPU LOAD
def CPU_load(session):
	print('[CPU LOAD]')

	CPU_1minuteload = session.get('laLoad.1')
	CPU_5minuteload = session.get('laLoad.2')
	CPU_10minuteload = session.get('laLoad.3')

	print('1 minute load: ' + CPU_1minuteload.value)
	print('5 minute load: ' + CPU_5minuteload.value)
	print('10 minute load: ' + CPU_10minuteload.value + '\n')

#####################################################

#MEMORY STATS
def MEM_stats(session):
	print('[MEMORY STATISTICS]')

	MEM_tot = session.get('memTotalReal.0')
	MEM_avail = session.get('memAvailReal.0')
	MEM_buff = session.get('memBuffer.0')
	MEM_cache = session.get('memCached.0')

	print('Total:    ' + MEM_tot.value + ' kB')
	print('Available: ' + MEM_avail.value + ' kB')
	print('Buffered:   ' + MEM_buff.value + ' kB')
	print('Cached:   ' + MEM_cache.value + ' kB')

#####################################################

session = Session(hostname=hostname,community=community,version=version) #SNMP SESSION
print('\n************ REPORT ************')
CPU_load(session)
MEM_stats(session)
print('********** END OF REPORT **********')

