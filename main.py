import italautomata
import sorozat
import park

# 1. Feladat
italautomata.italok()
# 2. Feladat
dollarLista = sorozat.dollar()
dollar = sorozat.otteloszthatoak_szama(dollarLista)
print(sorozat.konzolra_ir(dollar))
sorozat.fajlba_ir(dollar)
# 3. Feladat
parkLista = park.beolvas()
print(park.vizsgalt_evek(parkLista))
park.park_atlag(parkLista)
park.legtobb_latogato(parkLista)
