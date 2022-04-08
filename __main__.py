import argparse

a = """ 
	
██████╗░░█████╗░██╗░░░██╗██████╗░██╗░░░░░███████╗  ██╗░░░██╗██████╗░██╗░░░░░
██╔══██╗██╔══██╗██║░░░██║██╔══██╗██║░░░░░██╔════╝  ██║░░░██║██╔══██╗██║░░░░░
██║░░██║██║░░██║██║░░░██║██████╦╝██║░░░░░█████╗░░  ██║░░░██║██████╔╝██║░░░░░
██║░░██║██║░░██║██║░░░██║██╔══██╗██║░░░░░██╔══╝░░  ██║░░░██║██╔══██╗██║░░░░░
██████╔╝╚█████╔╝╚██████╔╝██████╦╝███████╗███████╗  ╚██████╔╝██║░░██║███████╗
╚═════╝░░╚════╝░░╚═════╝░╚═════╝░╚══════╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚══════╝

███████╗███╗░░██╗░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░
██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
█████╗░░██╔██╗██║██║░░╚═╝██║░░██║██║░░██║██║██╔██╗██║██║░░██╗░
██╔══╝░░██║╚████║██║░░██╗██║░░██║██║░░██║██║██║╚████║██║░░╚██╗
███████╗██║░╚███║╚█████╔╝╚█████╔╝██████╔╝██║██║░╚███║╚██████╔╝
╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░
"""

print(a)

dic_o = {'<': '%3C', '>': '%3E', '/': '%2F'}
dic_d = {'<':'%253C', '>':'%253E', '/':'%252F'}

parser = argparse.ArgumentParser(description='Double url encoding for xss payload.')
parser.add_argument('-p', '--payload', action='store', dest='payload',
					required=True, help="The payload you want to encode.")
parser.add_argument('-t', '--type', action='store', dest='type',
					required=False, default=1, help="Type of encode")
arguments = parser.parse_args()
payload = arguments.payload
type_d = arguments.type

if type_d == 'o':
	payload = payload.replace('<', dic_o['<'])
	payload = payload.replace('>', dic_o['>'])
	payload = payload.replace('/', dic_o['/'])
else:
	payload = payload.replace('<', dic_d['<'])
	payload = payload.replace('>', dic_d['>'])
	payload = payload.replace('/', dic_d['/'])

print('Payload encoded!!:\n')
print(payload)
