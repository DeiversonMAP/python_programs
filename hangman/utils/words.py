from random import choice
from re import A, U
from typing import List

words : List[str] = ['amor', 'aurélio', 'anuência', 'análogo', 'alienado', 'abstrato', 'apogeu', 'ardiloso', 'apático', 'ascensão', 'altruísmo', 'altruísta', 'arbitrário', 'acepção', 'audácia', 'aleatório', 'astúcia', 'auspicioso', 'algoz', 'afeto', 'analogia', 'apologia', 'ativista', 'alusão', 'anseio', 'alicerce', 'alheio', 'aspecto', 'analítico', 'abnegado', 'anátema', 'afável', 'amálgama', 'anacrônico', 'autóctone', 'aquém', 'alegria', 'adorno', 'animosidade', 'assim', 'audaz', 'ademais', 'almejar', 'antagonismo', 'autêntico', 'adesão', 'autonomia', 'aferir', 'astuto', 'através', 'arrogante', 'austero', 'ambíguo', 'alcunha', 'adjacente', 'apreço', 'ação', 'ambição', 'abstrair', 'alteridade', 'alento', 'amizade', 'anexo', 'após', 'aquisição', 'ambiguidade', 'ambicioso', 'auferir', 'ansioso', 'arcabouço', 'abster', 'aprovisionado', 'arquétipo', 'analisar', 'alçada', 'alienação', 'altivez', 'auge', 'assento', 'amigo', 'acento', 'alegoria', 'austeridade', 'assintomático', 'atemporal', 'assunção', 'arraigado', 'acesso', 'atenuar', 'atípico', 'axioma', 'abominável', 'admoestar', 'afeição', 'admoestação', 'avidez', 'ardil', 'apreciação', 'ausência', 'anomalia',
    'beneplácito', 'benevolência', 'beligerante', 'benignidade', 'brio', 'bizarro', 'benevolente', 'bem', 'basculho', 'buscar', 'boçal', 'brado', 'bíblia', 'balbúrdia', 'bom', 'bastardo', 'bélico', 'bordão', 'benefício', 'brando', 'banal', 'blasfêmia', 'beleza', 'balbuciar', 'baluarte', 'bruma', 'brasileiro', 'base', 'batráquio', 'benigno', 'bravo', 'burro', 'bálsamo', 'beneficência', 'bênção', 'barganha', 'beldade', 'brega', 'bojo', 'bucólico', 'bonito', 'bondade', 'butique', 'bajulador', 'benesse', 'bárbaro', 'benemérito', 'brasil', 'belicoso', 'belo', 'binômio', 'botar', 'bravata', 'bochecha', 'brevidade', 'bonança', 'brisa', 'blasé', 'bullying', 'banalizar', 'buço', 'beata', 'banzo', 'bom', 'senso', 'boemia', 'bola', 'balizar', 'breve', 'bêbado', 'burocracia', 'branda', 'bastante', 'bilateral', 'bolo', 'bíblico', 'basilar', 'burocrático', 'boutique', 'brava', 'bando', 'banzeiro', 'bajular', 'burrice', 'brincar', 'brecha', 'bilíngue', 'bençãos', 'brincadeira', 'bruços', 'branco', 'brandura', 'biltre', 'baixar', 'bondoso', 'biodiversidade', 'beligerância',
    'condescendente', 'cônjuge', 'cínico', 'caráter', 'concessão', 'corroborar', 'condolências', 'contemporâneo', 'concepção', 'complacência', 'corolário', 'contundente', 'característica', 'conceito', 'convém', 'condescendência', 'comorbidade', 'compreensão', 'circunstância', 'conserto', 'cultura', 'confiança', 'cinismo', 'consequência', 'caos', 'casual', 'concerne', 'conveniência', 'cordial', 'cético', 'compaixão', 'consonância', 'consiste', 'como', 'clichê', 'critério', 'contingente', 'complexo', 'compartilhar', 'contingência', 'contencioso', 'concernente', 'companhia', 'candura', 'constante', 'contexto', 'compassivo', 'contemplar', 'cerne', 'céu', 'comunhão', 'consideração', 'contudo', 'cumprimento', 'coercitivo', 'conjuntura', 'compreender', 'coragem', 'cognitivo', 'convergência', 'concomitante', 'cordialidade', 'consoante', 'carência', 'conciso', 'colosso', 'conhecimento', 'cumplicidade', 'convencional', 'contenda', 'concerto', 'custódia', 'convicção', 'ciência', 'credibilidade', 'conceder', 'condição', 'cessão', 'colapso', 'coerente', 'constância', 'canalha', 'caridade', 'complexidade', 'concisão', 'contíguo', 'concomitantemente', 'conhecer', 'controvérsia', 'contrapartida', 'conveniente', 'coerência', 'consolidar', 'coadunar', 'contenção', 'conforme', 'casa', 'cortês', 'cobiça', 'cuidado',
    'dicionário', 'denegrir', 'dissimulado', 'diligência', 'dstubeferido', 'detrimento', 'dicotomia', 'desgraça', 'discrepância', 'disruptivo', 'devaneio', 'determinação', 'deliberar', 'discernimento', 'demasiado', 'dê', 'descrição', 'diligente', 'despeito', 'destarte', 'disposição', 'demagogo', 'depreender', 'distinto', 'discrição', 'desfecho', 'demasiadamente', 'desdenhar', 'deboche', 'dissensão', 'dádiva', 'desígnio', 'democracia', 'desde', 'discorrer', 'desenvolvimento', 'dissolução', 'desumilde', 'designação', 'difuso', 'dimensão', 'disseminação', 'demanda', 'dispor', 'deliberação', 'diversidade', 'difusão', 'desprovido', 'déspota', 'divergência', 'dinâmico', 'divergente', 'discriminação', 'disseminar', 'deleitar', 'displicente', 'disciplina', 'diferença', 'definir', 'devasso', 'distinguir', 'destreza', 'dengo', 'displicência', 'desprezo', 'deveras', 'dinamismo', 'desgraçado', 'desafio', 'dignidade', 'difícil', 'defina', 'dispêndio', 'deferir', 'distinção', 'doutrina', 'dizer', 'diferente', 'dever', 'detém', 'dirimir', 'deferência', 'digno', 'diante', 'discussão', 'disperso', 'dúvida', 'descrever', 'declínio', 'debochado', 'deturpado', 'debalde', 'desenvolver', 'dar', 'decisão', 'diferir', 'danado', 'desídia', 'doravante' ,'despojar',
    'empatia', 'embuste', 'exceção', 'exceto', 'efêmero', 'escrúpulo', 'equidade', 'essência', 'extrovertido', 'estória', 'essencial', 'eminente', 'extensão', 'empírico', 'esdrúxulo', 'encarecidamente', 'extraordinário', 'expectativa', 'esperança', 'escopo', 'estigma', 'estável', 'exortar', 'eminência', 'entretanto', 'escória', 'excêntrico', 'emergir', 'eclesiástico', 'experiência', 'explícito', 'equivocado', 'exequível', 'exímio', 'esmo', 'escárnio', 'elegível', 'espectro', 'escrutínio', 'excelência', 'excerto', 'expressão', 'endêmico', 'execrável', 'epifania', 'emulação', 'expedido', 'excesso', 'esplêndido', 'ensejo', 'espontâneo', 'eficaz', 'eloquente', 'estúpido', 'erudito', 'embora', 'escroto', 'exótico', 'estereótipo', 'etnia', 'empecilho', 'escusa', 'especulação', 'excelente', 'exilado', 'exílio', 'estagnado', 'enxergar', 'emotivo', 'elucubração', 'excitado', 'exacerbado', 'estirpe', 'entediado', 'excedente', 'ego', 'exortação', 'enfadonho', 'epistemologia', 'esporádico', 'expor', 'escrever', 'estabelecer', 'etéreo', 'empáfia', 'estupefato', 'ermo', 'etimologia', 'excludente', 'eximir', 'então', 'elucidar', 'escasso', 'excepcional', 'emergente', 'especial', 'espairecer', 'espúrio', 'extasiado', 'ensejar',
    'fato', 'família', 'fomentar', 'fel', 'fazer', 'felicitações', 'fidedigno', 'fleumático', 'fosse', 'frívolo', 'fulguras', 'formal', 'finalidade', 'fomento', 'fútil', 'facção', 'felicidade', 'fé', 'fático', 'facultativo', 'fundamento', 'formidável', 'fraternidade', 'factível', 'fortuito', 'filantropo', 'faceta', 'formoso', 'flâmula', 'formos', 'fenômeno', 'fugaz', 'forte', 'facínora', 'fidelidade', 'fase', 'franco', 'fanfarrão', 'frivolidade', 'fatídico', 'facultado', 'feliz', 'fidalgo', 'fúlgido', 'falar', 'forma', 'florão', 'flexível', 'fluir', 'feição', 'face', 'flagelo', 'frisar', 'florescer', 'forjar', 'fascismo', 'frugal', 'fálico', 'fluxo', 'façanha', 'fariseu', 'fragmentação', 'foco', 'falso', 'famigerado', 'filosofia', 'fácil', 'favorável', 'favor', 'função', 'fulcral', 'fundamental', 'foi', 'furtivo', 'fizesse', 'fator', 'faccioso', 'falta', 'façam', 'farsa', 'frívola', 'filho', 'pródigo', 'falácia', 'fardo', 'força', 'fulgor', 'fictício', 'fragmentado', 'forasteiro', 'fértil', 'feixe', 'fascinante', 'fortaleza', 'fraude', 'fragrância', 'fusão', 'flanco', 'fonte', 'felicitação', 'fito',
    'genocida', 'genuíno', 'gratidão', 'gentil', 'genérico', 'glória', 'generoso', 'genro', 'graça', 'generalizar', 'gleba', 'grande', 'garrida', 'grotesco', 'ganância', 'gênese', 'gênero', 'guisa', 'garboso', 'genioso', 'gerar', 'generosidade', 'garbo', 'gregário', 'genocídio', 'galgar', 'grato', 'gênio', 'gentileza', 'geração', 'gente', 'gesto', 'gratificante', 'galanteador', 'gratuito', 'gambito', 'gestão', 'gama', 'gentalha', 'gostoso', 'guia', 'guarida', 'guardar', 'grátis', 'genealogia', 'gaiato', 'gramática', 'grau', 'garantir', 'gradual', 'galardoador', 'galhardia', 'grupo', 'gerir', 'genitor', 'glossário', 'gostar', 'grafar', 'grosso', 'grilhões', 'genitora', 'guerra', 'gradativo', 'gana', 'girassol', 'generalizado', 'grave', 'galardão', 'granjear', 'geografia', 'glosa', 'guarda', 'grata', 'gato', 'glutonaria', 'galante', 'guardião', 'globalização', 'grandeza', 'grandiloquente', 'glutão', 'gracejo', 'genuinamente', 'gênesis', 'gradação', 'garatuja', 'germinar', 'gata', 'borralheira', 'guilda', 'ganhar', 'grotão', 'grafia', 'geral', 'gracioso', 'grandemente', 'grosseiro', 'gentio', 'gabriel', 'generalização'  ,'genética',
    'hipócrita', 'hegemonia', 'hermético', 'heterogeneidade', 'hipocrisia', 'hostil', 'história', 'hábito', 'honra', 'híbrido', 'harmonia', 'humildade', 'hesitar', 'heterogêneo', 'haver', 'hábil', 'holístico', 'homogêneo', 'hipótese', 'hipotético', 'honestidade', 'herege', 'hierarquia', 'hodiernamente', 'hermenêutica', 'habilidade', 'hodierno', 'hedonismo', 'humilde', 'herói', 'heresia', 'hipoteticamente', 'hostilizar', 'havia', 'humanidade', 'histérica', 'histriônico', 'homônimo', 'hum', 'hombridade', 'hostilidade', 'hereditário', 'honesto', 'honorário', 'humor', 'herético', 'honorários', 'hiato', 'homogeneidade', 'hidrópico', 'haja', 'hera', 'horda', 'higidez', 'hoje', 'hediondo', 'honorífico', 'humano', 'há', 'heurístico', 'houve', 'honrar', 'hesitação', 'habitar', 'helena', 'histórico', 'homologar', 'homenagem', 'honrado', 'humilhar', 'hierárquico', 'hein', 'horizonte', 'holocausto', 'homologação', 'hipérbole', 'hercúleo', 'heroico', 'hiperbólico', 'hortifrúti', 'homólogo', 'homicida', 'harmonioso', 'habitual', 'hegemônico', 'hosana', 'hipossuficiente', 'histeria', 'hora', 'higienizar', 'hesitante', 'humilhação', 'higiene', 'highlander', 'hecatombe', 'hígido', 'herança', 'hobby', 'humanitário', 'horrendo',
    'imprescindível', 'inerente', 'intrínseco', 'impressão', 'intempérie', 'idôneo', 'idílico', 'iminente', 'implícito', 'invasivo', 'inconveniente', 'inspiração', 'idiossincrasia', 'inexorável', 'incidente', 'inócuo', 'incipiente', 'inferir', 'intrinsecamente', 'indulgente', 'independente', 'iniquidade', 'inserção', 'indelével', 'inóspito', 'icônico', 'intermitente', 'incidência', 'impetuoso', 'idiota', 'indiferente', 'inusitado', 'infame', 'imputar', 'imensurável', 'intensidade', 'inefável', 'inenarrável', 'indolência', 'ingerência', 'infortúnio', 'inato', 'incumbência', 'imparcial', 'impávido', 'ideia', 'intervenção', 'instigar', 'importante', 'insípido', 'ignorante', 'imanente', 'incrível', 'indiferença', 'instância', 'interesse', 'itinerário', 'iminência', 'imersão', 'irascível', 'intrínseca', 'isenção', 'intransigente', 'inércia', 'intenso', 'insólito', 'insensato', 'intenção', 'incólume', 'integridade', 'indubitável', 'indulgência', 'incógnita', 'idoneidade', 'ilação', 'interação', 'incisivo', 'imponente', 'inferência', 'indagar', 'importância', 'ignóbil', 'inspirar', 'indivíduo', 'isento', 'intuito', 'indolente', 'incauto', 'identificar', 'influência', 'imprevisível', 'insolente', 'impertinente', 'impacto', 'inverossímil', 'idem', 'interlocutor', 'intercorrência', 'ingratidão', 'irrepreensível',
    'jurídico', 'jactância', 'julgar', 'justo', 'júbilo', 'justiça', 'jeito', 'juízo', 'jugo', 'jamais', 'já', 'justificar', 'joia', 'jovem', 'justaposição', 'jovial', 'jurista', 'junto', 'jocoso', 'jornada', 'jazia', 'jiboia', 'jardim', 'jubileu', 'jargão', 'jaguara', 'jus', 'julgamento', 'jirau', 'jurisprudência', 'juiz', 'joio', 'junco', 'judeu', 'jurisdição', 'júlia', 'junção', 'jactancioso', 'janota', 'jaz', 'justificativa', 'juntar', 'já', 'já', 'jagunço', 'jejum', 'juntamente', 'jubilar', 'jiló', 'jactar', 'jazigo', 'jogar', 'jaez', 'jovialidade', 'janela', 'jazer', 'justaposto', 'jubiloso', 'justa', 'juvenil', 'jubilado', 'jaja', 'jornal', 'jurisdicionado', 'justificação', 'juventude', 'jerimum', 'jeová', 'jabá', 'jurisdicional', 'juízo', 'de', 'valor', 'judicioso', 'jenipapo', 'junta', 'jacaré', 'jeitoso', 'justapor', 'justamente', 'jusante', 'jazida', 'mineral', 'judicial', 'jipe', 'jurisconsulto', 'jegue', 'joelho', 'jabuti', 'jorrar', 'jeca', 'joaninha', 'jurar', 'joaquim', 'jóquei', 'juridicamente', 'júnior', 'jia', 'justificado', 'jornaleiro', 'juro', 'judiação', 'jantar', 'jerivá',
    'kafkaesco', 'kit', 'kafkiano', 'k', 'kamikaze', 'ketchup', 'karaokê', 'kiwi', 'kaiser', 'kilo', 'kg', 'kardecista', 'kardecismo', 'km2', 'kart', 'km', 'kitchenette', 'kung', 'fu', 'kitsch', 'kelvin', 'krill', 'keep', 'calm', 'kantiano', 'kyrie', 'kartódromo', 'keynesianismo', 'klaxon', 'kebab', 'kantismo', 'kibutz', 'kichute', 'kilt', 'kantista', 'kalio', 'kepleriano', 'knob', 'keynesiano', 'kartista', 'kcal', 'káon', 'kimberlito', 'kirsch', 'kartismo', 'kummel', 'kb', 'kaiserismo', 'kaiserista', 'kneippismo', 'kilobit', 'kansa', 'krausismo', 'kneippista' ,'kieserita',
    'lisonjeado', 'legado', 'litígio', 'limiar', 'lábaro', 'limítrofe', 'ludibriar', 'leniência', 'límpido', 'liberdade', 'lapso', 'leviano', 'lealdade', 'libertinagem', 'linear', 'lírico', 'latente', 'logradouro', 'lunático', 'lactante', 'lograr', 'locatário', 'lúgubre', 'letárgico', 'longânimo', 'lúcido', 'lícito', 'louco', 'letargia', 'locupletar', 'lacuna', 'longevidade', 'longanimidade', 'lavrar', 'limite', 'logo', 'luz', 'limbo', 'latifundiário', 'lugar', 'luzindo', 'lavrador', 'léxico', 'literalmente', 'legal', 'lástima', 'legitimidade', 'lembrança', 'laico', 'levar', 'lucidez', 'lastro', 'linda', 'lambisgoia', 'lua', 'longitudinal', 'leigo', 'lavra', 'leviandade', 'labor', 'lazarento', 'lume', 'labuta', 'ladino', 'loquaz', 'leito', 'latifúndio', 'lisonja', 'líder', 'leviana', 'luta', 'litigante', 'literal', 'ler', 'legenda', 'língua', 'lesado', 'lazer', 'lamento', 'lamúria', 'lembrar', 'lancinante', 'longínquo', 'liame', 'livro', 'ludibriado', 'lapidar', 'lotado', 'liturgia', 'lei', 'lisura', 'litigar', 'leal', 'lide', 'ladainha', 'lastimável', 'legítimo', 'lida', 'lenda', 'lamentável',
    'mister', 'mito', 'mexer', 'modéstia', 'mérito', 'mesquinho', 'monótono', 'medíocre', 'mórbido', 'mútua', 'metódico', 'mitigar', 'maestria', 'moral', 'mal', 'mediante', 'muito', 'modesto', 'molestar', 'mãe', 'magnânimo', 'mancebo', 'magnífico', 'meticuloso', 'militância', 'mútuo', 'morosidade', 'mazela', 'moleque', 'miserável', 'medo', 'mote', 'moribundo', 'metáfora', 'mas', 'moléstia', 'maledicência', 'melancólico', 'mesquinhez', 'mentecapto', 'mundo', 'minucioso', 'mormente', 'misericórdia', 'mediocridade', 'menção', 'melhor', 'mudança', 'maroto', 'martírio', 'método', 'melindre', 'modalidade', 'magnitude', 'mais', 'mutuamente', 'maravilhoso', 'mercê', 'maquiavélico', 'mercenário', 'mensurável', 'manso', 'mesmo', 'meiga', 'momento', 'ministrar', 'meio', 'meta', 'mitigação', 'manancial', 'metamorfose', 'melindroso', 'mágoa', 'marasmo', 'multifacetado', 'melindrosa', 'mártir', 'mobilidade', 'melancolia', 'matiz', 'menosprezar', 'metódica', 'missão', 'monotonia', 'matilha', 'maleável', 'maçante', 'monopólio', 'mítico', 'morte', 'marrenta', 'martirizar', 'modelo', 'mediador', 'moderado', 'mistério', 'militante', 'macambúzio', 'mero', 'mobilizador',
    'néscio', 'negro', 'nobre', 'nocivo', 'notívago', 'necessidade', 'nostalgia', 'não', 'obstante', 'no', 'entanto', 'notório', 'necessário', 'nuance', 'negligência', 'natureza', 'nômade', 'neófito', 'nevrálgico', 'neném', 'nativo', 'nefasto', 'nós', 'nojo', 'numa', 'noia', 'nexo', 'noção', 'novo', 'noite', 'nicho', 'negligenciar', 'natural', 'nosocômio', 'nada', 'nobreza', 'nomenclatura', 'notável', 'ninguém', 'nome', 'nato', 'nítido', 'nominal', 'nude', 'nórdico', 'nó', 'naturalidade', 'nossa', 'negligente', 'nostálgico', 'nem', 'nortear', 'nenhuma', 'nunca', 'nojento', 'nação', 'num', 'norma', 'nascer', 'normal', 'namorar', 'nacionalidade', 'nódoa', 'nuança', 'nível', 'neutro', 'narrativa', 'nefelibata', 'normativo', 'neologismo', 'negócio', 'niilismo', 'navio', 'núcleo', 'nefasta', 'nau', 'notícia', 'nuances', 'nosso', 'naquele', 'nostálgica', 'noutro', 'nazismo', 'narcisista', 'novidade', 'namastê', 'nipônico', 'nego', 'naquela', 'negrito', 'nepotismo', 'neo', 'nitidez', 'nos', 'necessitar', 'núpcias', 'número', 'norteador', 'nosocomial', 'nosologia' ,'néctar',
    'ordinário', 'obstante', 'objetivo', 'orgulho', 'oriundo', 'otário', 'obstinado', 'outrossim', 'ocioso', 'outrem', 'opróbrio', 'ousadia', 'objeto', 'oportunista', 'oblíquo', 'olvidar', 'orgânico', 'opinião', 'obséquio', 'outorgar', 'obsoleto', 'onírico', 'origem', 'obsceno', 'objeção', 'ora', 'ortodoxo', 'outrora', 'ordem', 'obsessão', 'orgulhoso', 'ontológico', 'oposição', 'onde', 'oportuno', 'observar', 'ociosidade', 'ontem', 'oportunidade', 'ojeriza', 'opressor', 'obstinação', 'ontologia', 'obter', 'ostracismo', 'organização', 'omissão', 'omitir', 'olhar', 'opulência', 'oneroso', 'obcecado', 'otimizar', 'opressão', 'orla', 'ouvir', 'oblação', 'ousado', 'oligarquia', 'onerar', 'orientação', 'outorgado', 'outro', 'ostensivo', 'ocorrência', 'obtuso', 'obedecer', 'ofício', 'original', 'ofuscar', 'obrigado', 'obtenção', 'otimista', 'ordinária', 'obstar', 'ostentação', 'ofensa', 'orientar', 'oposto', 'ostentas', 'ode', 'obrigação', 'opor', 'omisso', 'obstáculo', 'obscuro', 'oráculo', 'oração', 'obliterar', 'ocaso', 'ocasião', 'opulento', 'oferecer', 'oponível', 'obstruir', 'obstrução', 'onipotente', 'opção', 'ocorrer' ,'orar',
    'perseverança', 'perspicaz', 'peculiar', 'perspectiva', 'prescindir', 'presunçoso', 'prolixo', 'prudente', 'paradigma', 'pandemia', 'presunção', 'prerrogativa', 'propósito', 'parcimônia', 'plenitude', 'pêsames', 'peremptório', 'premissa', 'procrastinar', 'prepotente', 'pragmático', 'perspicácia', 'passível', 'prodígio', 'persuadir', 'pródigo', 'promíscuo', 'pertinente', 'pressuposto', 'plena', 'preconizar', 'precedente', 'preconceito', 'pressa', 'proceder', 'paz', 'pretensioso', 'primazia', 'prudência', 'pretensão', 'portanto', 'proeminente', 'perfídia', 'paradoxo', 'paixão', 'percepção', 'porém', 'processo', 'poder', 'paralelo', 'pejorativo', 'problema', 'proposição', 'primordial', 'paciência', 'prosaico', 'preceito', 'presteza', 'pecuniária', 'parcial', 'presságio', 'prendado', 'preceder', 'ponderar', 'perverso', 'padecer', 'perene', 'plausível', 'perplexo', 'proveniente', 'piedade', 'pois', 'pretérito', 'profano', 'pernóstico', 'privilégio', 'primícias', 'preâmbulo', 'provérbio', 'prognóstico', 'promover', 'pusilânime', 'proselitismo', 'pernicioso', 'pleitear', 'prescindível', 'plácidas', 'precisão', 'preciso', 'provisão', 'profícuo', 'parâmetro', 'pedante', 'posterior', 'providência', 'perpendicular', 'postergar', 'princípio', 'pesar', 'pragmatismo',
    'quimera', 'quiçá', 'qualidade', 'quando', 'quesito', 'que', 'quinhão', 'quanto', 'qualquer', 'questão', 'qualitativo', 'quintessência', 'querer', 'querela', 'quarentena', 'quer', 'quão', 'quaisquer', 'quiser', 'quilombo', 'qual', 'querido', 'quota', 'quase', 'quis', 'queijo', 'quem', 'questionar', 'questionamento', 'quantidade', 'quadrilha', 'quimérico', 'quitute', 'queixa', 'quisesse', 'qualificar', 'quiescente', 'quantitativo', 'queira', 'queixo', 'quociente', 'quieto', 'querida', 'quadro', 'querência', 'quinquilharia', 'quente', 'quiz', 'quarteirão', 'quisera', 'qualificação', 'quixotesco', 'quilombola', 'qualificado', 'queda', 'quietude', 'quartel', 'quebrantado', 'quite', 'quebranto', 'quebrar', 'queixar', 'quantas', 'quais', 'quantum', 'quitanda', 'quê', 'quedar', 'quotidiano', 'quadra', 'quantificar', 'quinquênio', 'quitação', 'querigma', 'quatorze', 'quebrantar', 'quadrúpede', 'quilograma', 'quitinete', 'quinhentos', 'quebrado', 'querelante', 'quitar', 'quiropata', 'quiabo', 'quieta', 'queixume', 'quorum', 'quatro', 'química', 'questiúncula', 'queto', 'quilo', 'quarto', 'quebra', 'quisto', 'quadrante' ,'quintal',
    'respeito', 'resiliência', 'recíproco', 'reciprocidade', 'remanescente', 'retificar', 'ratificar', 'referência', 'reiterar', 'relativo', 'redimir', 'recesso', 'resignação', 'refutar', 'resignado', 'remissão', 'respaldo', 'regozijar', 'retórica', 'rechaçar', 'retrógrado', 'resolução', 'restringir', 'refletir', 'restrição', 'resoluto', 'repudiar', 'reivindicar', 'redenção', 'responsabilidade', 'resistência', 'reflexão', 'relação', 'relevante', 'razão', 'recíproca', 'racismo', 'relevância', 'ressignificar', 'redundância', 'reverberar', 'ridículo', 'renunciar', 'retumbante', 'revogado', 'receio', 'remoto', 'revogar', 'ressentimento', 'reminiscência', 'resiliente', 'realizar', 'retaliação', 'resplandecer', 'retidão', 'ressaltar', 'rancor', 'relutante', 'redarguir', 'resquício', 'ressalva', 'rotina', 'requerente', 'retificação', 'relativizar', 'regular', 'retroativo', 'racional', 'reputação', 'respectivo', 'respectivamente', 'revés', 'reportar', 'rude', 'redundante', 'retenção', 'réplica', 'religião', 'relacionar', 'regra', 'refúgio', 'referente', 'remeter', 'round', 'recôndito', 'radical', 'receoso', 'revoada', 'refratário', 'rima', 'reaça', 'réu', 'reparar', 'recorrente', 'resplandece', 'repúdio', 'restrito', 'regeneração', 'recrudescer' ,'réprobo',
    'significado', 'sagaz', 'supérfluo', 'sublime', 'sucinto', 'sororidade', 'serenidade', 'senso', 'sagacidade', 'sapiência', 'subterfúgio', 'solidariedade', 'soberba', 'sinônimo', 'subestimar', 'suscetível', 'síntese', 'simultaneamente', 'sutil', 'superficial', 'sucumbir', 'singular', 'suscitar', 'sucesso', 'subjetivo', 'seção', 'sanar', 'supressão', 'sóbrio', 'sob', 'ser', 'solícito', 'sintetizar', 'sanidade', 'signatário', 'solene', 'sessão', 'sensato', 'salutar', 'supracitado', 'sintético', 'saudade', 'subjacente', 'sobre', 'subsistência', 'subsídio', 'subsequente', 'subjugar', 'sede', 'sarcástico', 'submissão', 'suplantar', 'sonho', 'salientar', 'sentido', 'sistematizar', 'sórdido', 'submisso', 'sufrágio', 'substantivo', 'satisfação', 'sanção', 'soberano', 'situação', 'saga', 'subversivo', 'segmento', 'sisudo', 'suprimir', 'submeter', 'seara', 'suma', 'sutileza', 'supremacia', 'sistemático', 'saudosista', 'singelo', 'sentimento', 'sarcasmo', 'solidário', 'saber', 'sempre', 'subordinado', 'sina', 'sensatez', 'solitude', 'sancionar', 'soberbo', 'sendo', 'substancial', 'seriedade', 'serelepe', 'sensível', 'subsistir', 'símbolo', 'sedentário', 'sabedoria', 'simplório', 'são' ,'sofisma',
    'talarico', 'termo', 'trivial', 'transcender', 'tênue', 'tribulação', 'transgressão', 'taciturno', 'também', 'torpe', 'transeunte', 'transcendente', 'ter', 'tange', 'tergiversar', 'trabalho', 'tendência', 'tempo', 'tangível', 'tolo', 'todavia', 'tenaz', 'tráfego', 'temor', 'talento', 'tácita', 'tudo', 'transição', 'temerário', 'tenacidade', 'ternura', 'tenro', 'tirano', 'trás', 'transmutar', 'transformação', 'temperança', 'teoria', 'trazer', 'tranquilo', 'tecnologia', 'tópico', 'temer', 'teor', 'traz', 'tendencioso', 'tal', 'transgredir', 'transversal', 'todos', 'translúcido', 'teve', 'tornar', 'tinhoso', 'torpeza', 'triste', 'tríade', 'tédio', 'talvez', 'tratativa', 'tomar', 'tipificar', 'todo', 'típico', 'tragédia', 'tecer', 'tese', 'tristeza', 'tempestivo', 'tensão', 'traduzir', 'transcrever', 'tendo', 'tratar', 'transcendental', 'terminologia', 'trouxe', 'tímido', 'tráfico', 'tende', 'transpor', 'translado', 'toada', 'transformar', 'tradição', 'terno', 'titubear', 'transcendência', 'trocadilho', 'terra', 'torpor', 'tema', 'tóxico', 'trivialidade', 'terrível', 'transitório', 'tenra', 'tanto', 'transposição' ,'tipo',
    'utopia', 'urge', 'usura', 'ufanismo', 'um', 'universo', 'ulterior', 'união', 'unânime', 'urbanidade', 'utilizar', 'uma', 'vez', 'que', 'usurpador', 'unguento', 'unidade', 'unilateral', 'urbano', 'uníssono', 'ultraje', 'usurpar', 'umbral', 'ubíquo', 'usar', 'utensílio', 'unívoco', 'ufanar', 'unicidade', 'universal', 'utópico', 'ubiquidade', 'uniformidade', 'ultrajado', 'urdidura', 'unanimidade', 'unificado', 'unidade', 'federativa', 'uniforme', 'urgente', 'urgia', 'uns', 'ufanista', 'uso', 'usuário', 'ultrajante', 'utilizado', 'unificar', 'unissex', 'urgência', 'usurpadora', 'usurpação', 'uau', 'ultrapassar', 'urdir', 'ufano', 'ululante', 'ufa', 'utilidade', 'unir', 'ultimato', 'unigênito', 'urgir', 'ultra', 'usual', 'urbe', 'usufrutuário', 'ungido', 'untar', 'uno', 'universalidade', 'ultrajar', 'ultimamente', 'urdido', 'utilitarismo', 'unção', 'usurário', 'ungir', 'utilitário', 'urubu', 'umidade', 'utilização', 'ubi', 'societas', 'ibi', 'jus', 'univocidade', 'unitário', 'uniformemente', 'uva', 'usucapião', 'utente', 'unicórnio', 'ultrapassado', 'unificação', 'usufruto', 'uni', 'urucubaca', 'urgentemente', 'untuoso', 'urze', 'universitário', 'unanimemente', 'urbanização',
    'verbete', 'vicissitude', 'viés', 'vereda', 'vagabundo', 'você', 'virtude', 'vislumbrar', 'vigor', 'vocábulo', 'vil', 'vocabulário', 'verídico', 'vide', 'ver', 'versátil', 'vertente', 'volátil', 'vigente', 'vigoroso', 'verossímil', 'vida', 'verossimilhança', 'veemente', 'veemência', 'vitupério', 'vulgar', 'varonil', 'volúvel', 'verborragia', 'vovó', 'vedado', 'vão', 'vir', 'veio', 'verdade', 'valha', 'vício', 'vulnerável', 'vaidade', 'vulgo', 'vigência', 'veementemente', 'ventura', 'venham', 'vertiginoso', 'voga', 'viril', 'viagem', 'vó', 'veredito', 'vosmecê', 'vendo', 'veracidade', 'visar', 'vermos', 'valor', 'vestígio', 'virtuoso', 'vênia', 'vale', 'vitalidade', 'visceral', 'visão', 'valia', 'vital', 'vínculo', 'vivaz', 'vontade', 'verificar', 'virtuosa', 'virtual', 'vetado', 'vis', 'vocação', 'viver', 'vitimismo', 'várias', 'vassalo', 'vemos', 'vilipendiado', 'velho', 'videira', 'viável', 'vácuo', 'vergonha', 'volatilidade', 'vangloriar', 'vernáculo', 'viabilizar', 'voltar', 'volitivo', 'virgem', 'velar', 'vazio', 'vitalício', 'vimos', 'vultoso', 'venerar',
    'xenofobia', 'xingar', 'xeque', 'xícara', 'xará', 'xale', 'xerife', 'xodó', 'xenofóbico', 'xaveco', 'xucro', 'xadrez', 'xampu', 'xepa', 'xá', 'xixi', 'xenófobo', 'xereta', 'xácara', 'xexelento', 'xingamento', 'xilogravura', 'xarope', 'xifópago', 'xaxado', 'xingo', 'xenofobismo', 'xiita', 'xaxim', 'xiquexique', 'xote', 'xinxim', 'xilindró', 'xisto', 'xavante', 'xerox', 'xupé', 'xenofilia', 'xero', 'xuá', 'xilofone', 'xeretar', 'x', 'xerém', 'xamã', 'xilografia', 'xoxo', 'ximbica', 'xexéu', 'xi', 'xilo', 'xeique', 'xaréu', 'xamânico', 'xibio', 'xerocar', 'xereré', 'xis', 'xangô', 'xilopódio', 'xelim', 'xô', 'xotar', 'xororó', 'xérox', 'xifoide', 'xamanismo', 'xerófilo', 'xavier', 'xavecar', 'xarada', 'xilófilo', 'xistoso', 'xexé', 'xerocópia', 'xintoísmo', 'xerostomia', 'xixixi', 'xadrezista', 'xacra', 'xepeiro', 'xuxo', 'xaropear', 'xenófilo', 'xilema', 'xibolete', 'xilógrafo', 'xofrango', 'xantocrômico', 'xerodermia', 'xopotó', 'xerocopiar', 'xiririca', 'xaroposo', 'xenógeno', 'xila', 'xiba', 'ximango' ,'xenobiótico',
    'yakisoba', 'yogurt', 'yakuza',
    'zelo', 'zombar', 'zelar', 'zeloso', 'zangado', 'zoológico', 'zumbi', 'zombeteiro', 'zoar', 'zoeira', 'zen', 'zombaria', 'zoada', 'zênite', 'zona', 'zoomórfico', 'zero', 'zebra', 'z', 'ziquizira', 'zíper', 'zombador', 'zoom', 'zumbido', 'zunir', 'zarpar', 'zarolho', 'zodíaco', 'zigoto', 'zéfiro', 'zangão', 'zelador', 'zoólogo', 'zica', 'zonzo', 'zangar', 'zoologia', 'zabelê', 'zumbir', 'zanga', 'zunido', 'zircão', 'zoo', 'zoonótico', 'zurrar', 'zoonose', 'zilhão', 'zigurate', 'zebu', 'zimbo', 'zeugma', 'zagaia', 'zimbro', 'zoomorfismo', 'zaino', 'zanzar', 'zurro', 'zapear', 'zona', 'tropical', 'zurzir', 'zabumba', 'zepelim', 'zaragatoa', 'zimbório', 'zerar', 'zaragata', 'zureta', 'zurrapa', 'zônula', 'zelote', 'zerado', 'zum', 'zarabatana', 'zambujeiro', 'zoófito', 'zinco', 'zagueiro', 'zorô', 'zoneamento', 'zoófilo', 'zulu', 'zinabre', 'zaga', 'zetética', 'zesto', 'zootecnia', 'zeladoria', 'zorro', 'zeta', 'zoomorfia', 'zape', 'zinho', 'zagal', 'zambelê', 'zetético', 'zoofagia', 'zarro', 'zona', 'temperada', 'ziguizira' ]

def word(num:int)-> str:
    return choice(list(filter(lambda x : len(x)== num and str.isalnum(x), words)))
