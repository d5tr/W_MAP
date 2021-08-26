import os

XX = os.getcwd()
CLAN = str(XX)
cc =CLAN.replace('W_MAP', '')

os.system(f'cd {cc} && cp -r W_MAP /root')
os.system('mv W-MAP.sh /bin/W-MAP')

print('Done ... ')

