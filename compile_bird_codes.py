#compile bird codes from BirdMacroLibrary.csv
#this file came from http://fielddata.blogspot.com/p/field-notes-data-tips-download-page.html

import os
import sys

def main():
	infile = open('BirdMacroLibrary.csv', 'r')
	outfile = open('bird_code_lookup_dict.txt','w')
	h = []
	d = ','
	nl = '\n'

	# outfile.write('bird_code_lookup = {')

	#Array of NC Bird Codes from BNA website: https://www.carolinabirdclub.org/bandcodes.html 8/25/2015
	nc_birds = ['BBWD','FUWD','GWFG','SNGO','ROGO','BRAN','BRNG','CACG','CAGO','MUSW','TRUS','TUSW','WODU','GADW','EUWI','AMWI','ABDU','MALL','MODU','BWTE','CITE','NSHO','NOPI','GARG','GWTE','CANV','REDH','RNDU','TUDU','GRSC','LESC','KIEI','COEI','HARD','SUSC','WWSC','BLSC','LTDU','BUFF','COGO','HOME','COME','RBME','MADU','RUDU','NOBO','RNEP','RUGR','WITU','RTLO','PALO','COLO','PBGR','HOGR','RNGR','EAGR','WEGR','CLGR','YNAL','BBAL','NOFU','HEPE','FEPE','BEPE','BCPE','BUPE','COSH','CVSH','GRSH','SOSH','MASH','AUSH','LISH','WISP','WFSP','EUSP','BBSP','SSTP','LHSP','BANP','WTTR','RBTR','MABO','BRBO','RFBO','NOGA','AWPE','BRPE','DCCO','GRCO','ANHI','MAFR','AMBI','LEBI','GBHE','GREG','SNEG','LBHE','TRHE','REEG','CAEG','GRHE','BCNH','YCNH','WHIB','GLIB','WFIB','ROSP','WOST','BLVU','TUVU','OSPR','STKI','WTKI','SNKI','MIKI','BAEA','NOHA','SSHA','COHA','NOGO','RSHA','BWHA','SWHA','RTHA','RLHA','GOEA','AMKE','MERL','GYRF','PEFA','YERA','BLRA','CLRA','KIRA','VIRA','SORA','PUGA','COGA','AMCO','LIMP','SACR','WHCR','NOLA','BBPL','AMGP','SNPL','WIPL','CRPL','SEPL','PIPL','KILL','MOPL','AMOY','BNST','AMAV','SPSA','SOSA','SPRE','GRYE','WILL','LEYE','UPSA','ESCU','WHIM','LBCU','BLAG','HUGO','BARG','MAGO','RUTU','REKN','SAND','SESA','WESA','RNST','LIST','LESA','WRSA','BASA','PESA','SHAS','PUSA','DUNL','CUSA','STSA','BBSA','RUFF','SBDO','LBDO','WISN','AMWO','WIPH','RNPH','REPH','BLKI','SAGU','BOGU','BHGU','LIGU','LAGU','FRGU','BTGU','MEGU','RBGU','CAGU','HERG','YLGU','THGU','ICGU','LBBG','SBGU','GLGU','GBBG','BRNO','SOTE','BRTE','LETE','GBTE','CATE','BLTE','WWTE','ROST','COTE','ARTE','FOTE','ROYT','SATE','BLSK','GRSK','SPSK','POJA','PAJA','LTJA','DOVE','COMU','TBMU','RAZO','BLGU','LBMU','ATPU','ROPI','BTPI','ECDO','WWDO','MODO','PAPI','COGD','MOPA','CAPA','YBCU','BBCU','SBAN','GBAN','BNOW','EASO','GHOW','SNOW','BUOW','BDOW','LEOW','SEOW','NSWO','LENI','CONI','ANNI','CWWI','EWPW','CHSW','GVIO','GREM','BBLH','BUFH','BLUH','RTHU','BCHU','ANHU','CAHU','BTLH','RUHU','ALHU','BEKI','RHWO','RBWO','YBSA','DOWO','HAWO','RCWO','NOFL','PIWO','IBWO','OSFL','EAWP','YBFL','ACFL','ALFL','WIFL','LEFL','GRFL','PSFL','COFL','EAPH','SAPH','VEFL','ATFL','GCFL','TRKI','COKI','WEKI','EAKI','GRAK','STFL','FTFL','LOSH','NSHR','WEVI','BEVI','YTVI','BHVI','WAVI','PHVI','REVI','BWVI','BLJA','AMCR','FICR','CORA','HOLA','PUMA','TRES','VGSW','NRWS','BANS','CLSW','CASW','BARS','CACH','BCCH','TUTI','RBNU','WBNU','BHNU','BRCR','CARW','BEWR','HOWR','WIWR','SEWR','MAWR','BGGN','GCKI','RCKI','NOWH','EABL','MOBL','TOSO','VEER','GCTH','BITH','SWTH','HETH','WOTH','AMRO','VATH','GRCA','NOMO','SATH','BRTH','EUST','WHWA','AMPI','SPPI','CEDW','LALO','CCLO','SMLO','SNBU','BAWA','BWWA','GWWA','TEWA','OCWA','NAWA','NOPA','YEWA','CSWA','MAWA','CMWA','BTBW','YRWA','BTYW','BTNW','TOWA','BLBW','YTWA','PIWA','KIWA','PRAW','PAWA','BBWA','BLPW','CERW','BAWW','AMRE','PROW','WEWA','SWWA','OVEN','NOWA','LOWA','KEWA','CONW','MOWA','MGWA','COYE','HOWA','WIWA','CAWA','YBCH','GTTO','SPTO','EATO','CASP','BACS','ATSP','CHSP','CCSP','FISP','VESP','LASP','LARB','SAVS','GRSP','HESP','LCSP','NESP','SALS','SESP','FOSP','SOSP','LISP','SWSP','WTSP','HASP','WCSP','GCSP','DEJU','SUTA','SCTA','WETA','NOCA','RBGR','BHGR','BLGR','LAZB','INBU','PABU','DICK','BOBO','RWBL','EAME','WEME','YHBL','RUBL','BRBL','COGR','BTGR','SHCO','BHCO','OROR','BUOR','BAOR','SCOR','BRAM','PIGR','PUFI','HOFI','RECR','WWCR','CORE','PISI','LEGO','AMGO','EVGR','HOSP'] 

	countline = 1	
	comma = ''
	with infile as f:
	    for line in f:

	    	line = line.strip('\n')
	    	if 'gen,' in line:
	    		line = line.replace('gen,','gen')
	    	r = line.split(d)
	    	if countline ==1:
	    		#header row, collect headers
	    		#should be: SPEC,COMMONNAME,SCINAME,SPEC6,CONF6,CONF,SP,Sort Order,Order,Family,Subfamily
	    		for i in r: 
	    			h.append(i)
	    	else:
	    		print 'line: ' + str(countline) + ' comma:' + comma
	    		print str(r)
	    		if countline>=2: 
	    			comma = ','
				# print str(len(r)) + ' line:' + str(r)

				sd = {}
				sd = dict([(h[i].strip('\n'),v.strip('"').strip('\n')) for i,v in enumerate(r)])
				outfile.write(comma + '"'+sd['SPEC'] + '":' + str(r))
				# outfile.write(comma + nl + '"'+sd['SPEC'] + '":"' + sd['SCINAME'] + '"')

	        countline +=1
	# outfile.write('}')

if __name__ == '__main__':
	main()
