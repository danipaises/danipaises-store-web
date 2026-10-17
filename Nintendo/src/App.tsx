import {Layout} from './components/Layout';
import Home from './components/Home';
import {GameLibrary,ConsoleLibrary,FranchiseLibrary,CharacterLibrary,UniversalSearch} from './components/Catalogs';
import {GameDetail,ConsoleDetail,FranchiseDetail,CharacterDetail,NotFound} from './components/Details';
import {HistoryPage,TimelinePage,MuseumPage} from './components/History';
import {CollectionPage,QuizPage,PokedexPage,ComparePage,EvolutionPage} from './components/Tools';
import {AboutPage,SourcesPage} from './components/About';
import {CollectionProvider} from './lib/state';
export default function App({url}:{url:string}){const path=url.split('?')[0].replace(/\/$/,'')||'/';const [,section,id]=path.split('/');let content;
 if(path==='/')content=<Home/>;
 else if(section==='jogos')content=id?<GameDetail id={id}/>:<GameLibrary/>;
 else if(section==='consoles')content=id?<ConsoleDetail id={id}/>:<ConsoleLibrary/>;
 else if(section==='franquias')content=id?<FranchiseDetail id={id}/>:<FranchiseLibrary/>;
 else if(section==='personagens')content=id?<CharacterDetail id={id}/>:<CharacterLibrary/>;
 else content=({'historia':<HistoryPage/>,'linha-do-tempo':<TimelinePage/>,'museu':<MuseumPage/>,'busca':<UniversalSearch/>,'colecao':<CollectionPage/>,'quiz':<QuizPage/>,'pokedex':<PokedexPage/>,'comparar':<ComparePage/>,'evolucoes':<EvolutionPage/>,'sobre':<AboutPage/>,'fontes':<SourcesPage/>} as Record<string,React.ReactNode>)[section]||<NotFound/>;
 return <CollectionProvider><Layout path={path}><div className={path==='/'?'page-container home-container':'page-container'}>{content}</div></Layout></CollectionProvider>
}
