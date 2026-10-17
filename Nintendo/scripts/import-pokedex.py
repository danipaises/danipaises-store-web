"""Importação pública e reproduzível: uma leitura por CSV, sem sprites nem textos de jogos."""
import csv, io, json, pathlib, subprocess, datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE='https://raw.githubusercontent.com/PokeAPI/pokeapi/master/data/v2/csv/'
CACHE=ROOT/'.cache'/'pokeapi'
CACHE.mkdir(parents=True,exist_ok=True)
def read(name):
    path=CACHE/(name+'.csv')
    if not path.exists():
        subprocess.run(['curl','--fail','-L','--retry','2','--max-time','45','-sS',BASE+name+'.csv','-o',str(path)],check=True)
    return list(csv.DictReader(io.StringIO(path.read_text())))
species=read('pokemon_species'); pokemon={int(p['species_id']):p for p in read('pokemon') if p['is_default']=='1'}
names={int(p['pokemon_species_id']):p['name'] for p in read('pokemon_species_names') if p['local_language_id']=='9'}
type_names={1:'Normal',2:'Lutador',3:'Voador',4:'Venenoso',5:'Terrestre',6:'Pedra',7:'Inseto',8:'Fantasma',9:'Aço',10:'Fogo',11:'Água',12:'Planta',13:'Elétrico',14:'Psíquico',15:'Gelo',16:'Dragão',17:'Sombrio',18:'Fada'}
types={}
for row in read('pokemon_types'):
    if int(row['type_id']) in type_names: types.setdefault(int(row['pokemon_id']),[]).append(type_names[int(row['type_id'])])
out=[]
for s in species:
    i=int(s['id']); p=pokemon.get(i)
    if not p: continue
    out.append(dict(id=i,name=names.get(i,s['identifier']),generation=int(s['generation_id']),types=types.get(int(p['id']),[]),height=int(p['height'])/10,weight=int(p['weight'])/10,legendary=s['is_legendary']=='1',mythical=s['is_mythical']=='1',prevo=int(s['evolves_from_species_id']) if s['evolves_from_species_id'] else None,chain=int(s['evolution_chain_id'])))
assert len(out)>1000 and len({p['id'] for p in out})==len(out)
target=ROOT/'src/data/pokedex.json'; target.write_text(json.dumps(out,ensure_ascii=False,separators=(',',':'))+'\n')
meta={'source':'https://github.com/PokeAPI/pokeapi/tree/master/data/v2/csv','retrievedAt':datetime.date.today().isoformat(),'records':len(out),'scope':'Espécies; forma padrão atual. Sem formas regionais, megas, sprites ou texto de jogos. Tipos atuais, não tipos históricos de cada geração.'}
(ROOT/'src/data/pokedex-meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(meta,ensure_ascii=False))
