#parse eBird Records
# this file will parse through eBird Basic Dataset records and retrieve specified records
# inputs:
#		spp = species list
#		yr = year list

import os
import sys
import datetime
import bird_codes

params = {'yrs':['2002','2003'],'spp':[]}
ebird_delim = '\t' 
delim = ','
fn_delim = '_' #delim for filename
nl = '\n'

nc_birds = ['BBWD','FUWD','GWFG','SNGO','ROGO','BRAN','BRNG','CACG','CAGO','MUSW','TRUS','TUSW','WODU','GADW','EUWI','AMWI','ABDU','MALL','MODU','BWTE','CITE','NSHO','NOPI','GARG','GWTE','CANV','REDH','RNDU','TUDU','GRSC','LESC','KIEI','COEI','HARD','SUSC','WWSC','BLSC','LTDU','BUFF','COGO','HOME','COME','RBME','MADU','RUDU','NOBO','RNEP','RUGR','WITU','RTLO','PALO','COLO','PBGR','HOGR','RNGR','EAGR','WEGR','CLGR','YNAL','BBAL','NOFU','HEPE','FEPE','BEPE','BCPE','BUPE','COSH','CVSH','GRSH','SOSH','MASH','AUSH','LISH','WISP','WFSP','EUSP','BBSP','SSTP','LHSP','BANP','WTTR','RBTR','MABO','BRBO','RFBO','NOGA','AWPE','BRPE','DCCO','GRCO','ANHI','MAFR','AMBI','LEBI','GBHE','GREG','SNEG','LBHE','TRHE','REEG','CAEG','GRHE','BCNH','YCNH','WHIB','GLIB','WFIB','ROSP','WOST','BLVU','TUVU','OSPR','STKI','WTKI','SNKI','MIKI','BAEA','NOHA','SSHA','COHA','NOGO','RSHA','BWHA','SWHA','RTHA','RLHA','GOEA','AMKE','MERL','GYRF','PEFA','YERA','BLRA','CLRA','KIRA','VIRA','SORA','PUGA','COGA','AMCO','LIMP','SACR','WHCR','NOLA','BBPL','AMGP','SNPL','WIPL','CRPL','SEPL','PIPL','KILL','MOPL','AMOY','BNST','AMAV','SPSA','SOSA','SPRE','GRYE','WILL','LEYE','UPSA','ESCU','WHIM','LBCU','BLAG','HUGO','BARG','MAGO','RUTU','REKN','SAND','SESA','WESA','RNST','LIST','LESA','WRSA','BASA','PESA','SHAS','PUSA','DUNL','CUSA','STSA','BBSA','RUFF','SBDO','LBDO','WISN','AMWO','WIPH','RNPH','REPH','BLKI','SAGU','BOGU','BHGU','LIGU','LAGU','FRGU','BTGU','MEGU','RBGU','CAGU','HERG','YLGU','THGU','ICGU','LBBG','SBGU','GLGU','GBBG','BRNO','SOTE','BRTE','LETE','GBTE','CATE','BLTE','WWTE','ROST','COTE','ARTE','FOTE','ROYT','SATE','BLSK','GRSK','SPSK','POJA','PAJA','LTJA','DOVE','COMU','TBMU','RAZO','BLGU','LBMU','ATPU','ROPI','BTPI','ECDO','WWDO','MODO','PAPI','COGD','MOPA','CAPA','YBCU','BBCU','SBAN','GBAN','BNOW','EASO','GHOW','SNOW','BUOW','BDOW','LEOW','SEOW','NSWO','LENI','CONI','ANNI','CWWI','EWPW','CHSW','GVIO','GREM','BBLH','BUFH','BLUH','RTHU','BCHU','ANHU','CAHU','BTLH','RUHU','ALHU','BEKI','RHWO','RBWO','YBSA','DOWO','HAWO','RCWO','NOFL','PIWO','IBWO','OSFL','EAWP','YBFL','ACFL','ALFL','WIFL','LEFL','GRFL','PSFL','COFL','EAPH','SAPH','VEFL','ATFL','GCFL','TRKI','COKI','WEKI','EAKI','GRAK','STFL','FTFL','LOSH','NSHR','WEVI','BEVI','YTVI','BHVI','WAVI','PHVI','REVI','BWVI','BLJA','AMCR','FICR','CORA','HOLA','PUMA','TRES','VGSW','NRWS','BANS','CLSW','CASW','BARS','CACH','BCCH','TUTI','RBNU','WBNU','BHNU','BRCR','CARW','BEWR','HOWR','WIWR','SEWR','MAWR','BGGN','GCKI','RCKI','NOWH','EABL','MOBL','TOSO','VEER','GCTH','BITH','SWTH','HETH','WOTH','AMRO','VATH','GRCA','NOMO','SATH','BRTH','EUST','WHWA','AMPI','SPPI','CEDW','LALO','CCLO','SMLO','SNBU','BAWA','BWWA','GWWA','TEWA','OCWA','NAWA','NOPA','YEWA','CSWA','MAWA','CMWA','BTBW','YRWA','BTYW','BTNW','TOWA','BLBW','YTWA','PIWA','KIWA','PRAW','PAWA','BBWA','BLPW','CERW','BAWW','AMRE','PROW','WEWA','SWWA','OVEN','NOWA','LOWA','KEWA','CONW','MOWA','MGWA','COYE','HOWA','WIWA','CAWA','YBCH','GTTO','SPTO','EATO','CASP','BACS','ATSP','CHSP','CCSP','FISP','VESP','LASP','LARB','SAVS','GRSP','HESP','LCSP','NESP','SALS','SESP','FOSP','SOSP','LISP','SWSP','WTSP','HASP','WCSP','GCSP','DEJU','SUTA','SCTA','WETA','NOCA','RBGR','BHGR','BLGR','LAZB','INBU','PABU','DICK','BOBO','RWBL','EAME','WEME','YHBL','RUBL','BRBL','COGR','BTGR','SHCO','BHCO','OROR','BUOR','BAOR','SCOR','BRAM','PIGR','PUFI','HOFI','RECR','WWCR','CORE','PISI','LEGO','AMGO','EVGR','HOSP']

print bird_4code_lookup['BACS']

#retrieve command line arguments
#arg 1 = program file
#arg 2 = file to be processed
#other arg syntax:
#	yrs=2002,2003
#	spp=BACS,RUGR

# def parse_key_value_pairs(in):
	#input text - k,v pairs separated by =
	#vaues may represent a range, output range (e.g., 2002-2005 -> [2002,2003,2004,2005])


rundt = str(datetime.datetime.now().strftime('%Y%m%d%H%M'))
for argn, arg in enumerate(sys.argv): 
	print arg
	if argn>1: #parse values
		#format should be: argname=[val1,val2,val3]
		flag = arg.split('=')
		params[flag[0]]= flag[1].split(',')
	elif argn==1:
		fn = arg
	elif argn==0:
		dirfilesep = arg.rfind('\\')+1
		rootdir = arg[:dirfilesep]
		sourcefile = arg[dirfilesep:] 

def main():
	# outname = str(fn_delim.join(params.values()))
	print str(params['yrs'])
	print str(fn_delim.join(params['yrs']))
	out = open(rootdir + rundt + 'ebird_temp.txt','w')
	count = 0
	with open('ebird_sample.txt') as f:
	    for line in f:
	        out.write(line + nl)
	        count +=1
	        if count>100: break



if __name__ == '__main__':
	main()
