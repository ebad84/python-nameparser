# -*- coding: utf-8 -*-
from __future__ import unicode_literals

FIRST_NAME_TITLES = set([
    'aunt',
    'auntie',
    'brother',
    'dame',
    'father',
    'king',
    'maid',
    'master',
    'mother',
    'pope',
    'queen',
    'sir',
    'sister',
    'uncle',
    'sheikh',
    'sheik',
    'shaik',
    'shayk',
    'shaykh',
    'shaikh',
    'cheikh',
    'shekh',
])
"""
When these titles appear with a single other name, that name is a first name, e.g.
"Sir John", "Sister Mary", "Queen Elizabeth".
"""

#: **Cannot include things that could also be first names**, e.g. "dean".
#: Many of these from wikipedia: https://en.wikipedia.org/wiki/Title.
#: The parser recognizes chains of these including conjunctions allowing 
#: recognition titles like "Deputy Secretary of State".
TITLES = FIRST_NAME_TITLES | set([
    "attaché",
    "chargé d'affaires",
    "king's",
    "marchioness",
    "marquess",
    "marquis",
    "marquise",
    "queen's",
    '10th',
    '1lt',
    '1sgt',
    '1st',
    '1stlt',
    '1stsgt',
    '2lt',
    '2nd',
    '2ndlt',
    '3rd',
    '4th',
    '5th',
    '6th',
    '7th',
    '8th',
    '9th',
    'a1c',
    'ab',
    'abbess',
    'abbot',
    'abolitionist',
    'academic',
    'acolyte',
    'activist',
    'actor ',
    'actress',
    'adept',
    'adjutant',
    'adm',
    'admiral',
    'advertising',
    'adviser',
    'advocate',
    'air',
    'akhoond',
    'alderman',
    'almoner',
    'ambassador',
    'amn',
    'analytics',
    'anarchist',
    'animator',
    'anthropologist',
    'appellate',
    'apprentice',
    'arbitrator',
    'archbishop',
    'archdeacon',
    'archdruid',
    'archduchess',
    'archduke',
    'archeologist',
    'architect',
    'arhat',
    'army',
    'arranger',
    'assistant',
    'assoc',
    'associate',
    'asst',
    'astronomer',
    'attache',
    'attorney',
    'author',
    'award-winning',
    'ayatollah',
    'baba',
    'bailiff',
    'ballet',
    'bandleader',
    'banker',
    'banner',
    'bard',
    'baron',
    'barrister',
    'baseball',
    'bearer',
    'behavioral',
    'bench',
    'bg',
    'bgen',
    'biblical',
    'bibliographer',
    'biochemist',
    'biographer',
    'biologist',
    'bishop',
    'blessed',
    'blogger',
    'blues',
    'bodhisattva',
    'bookseller',
    'botanist',
    'bp',
    'brigadier',
    'briggen',
    'british',
    'broadcaster',
    'buddha',
    'burgess',
    'burlesque',
    'business',
    'businessman',
    'businesswoman',
    'bwana',
    'canon',
    'capt',
    'captain',
    'cardinal',
    'cartographer',
    'cartoonist',
    'catholicos',
    'ccmsgt',
    'cdr',
    'celebrity',
    'ceo',
    'cfo',
    'chair',
    'chairs',
    'chancellor',
    'chaplain',
    'chef',
    'chemist',
    'chief',
    'chieftain',
    'choreographer',
    'civil',
    'classical',
    'clergyman',
    'clerk',
    'cmsaf',
    'cmsgt',
    'co-chair',
    'co-chairs',
    'co-founder',
    'coach',
    'col',
    'collector',
    'colonel',
    'comedian',
    'comedienne',
    'comic',
    'commander',
    'commander-in-chief',
    'commodore',
    'composer',
    'compositeur',
    'comptroller',
    'computer',
    'comtesse',
    'conductor',
    'consultant',
    'controller',
    'corporal',
    'corporate',
    'correspondent',
    'councillor',
    'counselor',
    'count',
    'countess',
    'courtier',
    'cpl',
    'cpo',
    'cpt',
    'credit',
    'criminal',
    'criminologist',
    'critic',
    'csm',
    'curator',
    'customs',
    'cwo-2',
    'cwo-3',
    'cwo-4',
    'cwo-5',
    'cwo2',
    'cwo3',
    'cwo4',
    'cwo5',
    'cyclist',
    'dancer',
    'dcn',
    'deacon',
    'delegate',
    'deputy',
    'designated',
    'designer',
    'detective',
    'developer',
    'diplomat',
    'dir',
    'director',
    'discovery',
    'dissident',
    'district',
    'division',
    'do',
    'docent',
    'docket',
    'doctor',
    'doyen',
    'dpty',
    'dr',
    'dra',
    'dramatist',
    'druid',
    'drummer',
    'duchesse',
    'duke',
    'dutchess',
    'ecologist',
    'economist',
    'editor',
    'edmi',
    'edohen',
    'educator',
    'effendi',
    'ekegbian',
    'elerunwon',
    'eminence',
    'emperor',
    'empress',
    'engineer',
    'english',
    'ens',
    'entertainer',
    'entrepreneur',
    'envoy',
    'essayist',
    'evangelist',
    'excellency',
    'excellent',
    'exec',
    'executive',
    'expert',
    'fadm',
    'family',
    'father',
    'federal',
    'field',
    'film',
    'financial',
    'first',
    'flag',
    'flying',
    'foreign',
    'forester',
    'founder',
    'fr',
    'friar',
    'gaf',
    'gen',
    'general',
    'generalissimo',
    'gentiluomo',
    'giani',
    'goodman',
    'goodwife',
    'governor',
    'graf',
    'grand',
    'group',
    'guitarist',
    'guru',
    'gyani',
    'gysgt',
    'hajji',
    'headman',
    'heir',
    'heiress',
    'her',
    'hereditary',
    'high',
    'highness',
    'his',
    'his eminence',
    'his eminence metropolitan',
    'historian',
    'historicus',
    'historien',
    'holiness',
    'hon', # sorry Hon Solo, but judges seem more common.
    'honorable',
    'honourable',
    'host',
    'illustrator',
    'imam',
    'industrialist',
    'information',
    'instructor',
    'intelligence',
    'intendant',
    'inventor',
    'investigator',
    'investor',
    'journalist',
    'journeyman',
    'jr',
    'judge',
    'judicial',
    'junior',
    'jurist',
    'keyboardist',
    'kingdom',
    'knowledge',
    'lady',
    'lama',
    'lamido',
    'law',
    'lawyer',
    'lcdr',
    'lcpl',
    'leader',
    'lecturer',
    'legal',
    'librarian',
    'lieutenant',
    'linguist',
    'literary',
    'lord',
    'lt',
    'ltc',
    'ltcol',
    'ltg',
    'ltgen',
    'ltjg',
    'lyricist',
    'madam',
    'madame',
    'mademoiselle',
    'mag',
    'mag-judge',
    'mag/judge',
    'magistrate',
    'magistrate-judge',
    'magnate',
    'maharajah',
    'maharani',
    'mahdi',
    'maj',
    'majesty',
    'majgen',
    'manager',
    'marcher',
    'marchess',
    'marketing',
    'marquis',
    'mathematician',
    'mathematics',
    'matriarch',
    'mayor',
    'mcpo',
    'mcpoc',
    'mcpon',
    'md',
    'member',
    'memoirist',
    'merchant',
    'met',
    'metropolitan',
    'mg',
    'mgr',
    'mgysgt',
    'military',
    'minister',
    'miss',
    'misses',
    'missionary',
    'mister',
    'mlle',
    'mme',
    'mobster',
    'model',
    'monk',
    'monsignor',
    'most',
    'mountaineer',
    'mpco-cg',
    'mr',
    'mrs',
    'ms',
    'msg',
    'msgt',
    'mufti',
    'mullah',
    'municipal',
    'murshid',
    'musician',
    'musicologist',
    'mystery',
    'nanny',
    'narrator',
    'national',
    'naturalist',
    'navy',
    'neuroscientist',
    'novelist',
    'nurse',
    'obstetritian',
    'officer',
    'opera',
    'operating',
    'ornithologist',
    'painter',
    'paleontologist',
    'pastor',
    'patriarch',
    'pediatrician',
    'personality',
    'petty',
    'pfc',
    'pharaoh',
    'phd',
    'philantropist',
    'philosopher',
    'photographer',
    'physician',
    'physicist',
    'pianist',
    'pilot',
    'pioneer',
    'pir',
    'player',
    'playwright',
    'po1',
    'po2',
    'po3',
    'poet',
    'police',
    'political',
    'politician',
    'prefect',
    'prelate',
    'premier',
    'pres',
    'presbyter',
    'president',
    'presiding',
    'priest',
    'priestess',
    'primate',
    'prime',
    'prin',
    'prince',
    'princess',
    'principal',
    'printer',
    'printmaker',
    'prior',
    'private',
    'pro',
    'producer',
    'prof',
    'professor',
    'provost',
    'pslc',
    'psychiatrist',
    'psychologist',
    'publisher',
    'pursuivant',
    'pv2',
    'pvt',
    'rabbi',
    'radio',
    'radm',
    'rangatira',
    'ranger',
    'rdml',
    'rear',
    'rebbe',
    'registrar',
    'rep',
    'representative',
    'researcher',
    'resident',
    'rev',
    'revenue',
    'reverend',
    'right',
    'risk',
    'rock',
    'royal',
    'rt',
    'sa',
    'sailor',
    'saint',
    'sainte',
    'saoshyant',
    'satirist',
    'scholar',
    'schoolmaster',
    'scientist',
    'scpo',
    'screenwriter',
    'se',
    'secretary',
    'security',
    'seigneur',
    'senator',
    'senior',
    'senior-judge',
    'sergeant',
    'servant',
    'sfc',
    'sgm',
    'sgt',
    'sgtmaj',
    'sgtmajmc',
    'shehu',
    'sheikh',
    'sheriff',
    'siddha',
    'singer',
    'singer-songwriter',
    'sma',
    'smsgt',
    'sn',
    'soccer',
    'social',
    'sociologist',
    'software',
    'soldier',
    'solicitor',
    'soprano',
    'spc',
    'speaker',
    'special',
    'sr',
    'sra',
    'srta',
    'ssg',
    'ssgt',
    'st',
    'staff',
    'state',
    'states',
    'strategy',
    'subaltern',
    'subedar',
    'suffragist',
    'sultan',
    'sultana',
    'superior',
    'supreme',
    'surgeon',
    'swami',
    'swordbearer',
    'sysselmann',
    'tax',
    'teacher',
    'technical',
    'technologist',
    'television ',
    'tenor',
    'theater',
    'theatre',
    'theologian',
    'theorist',
    'timi',
    'tirthankar',
    'translator',
    'travel',
    'treasurer',
    'tsar',
    'tsarina',
    'tsgt',
    'uk',
    'united',
    'us',
    'vadm',
    'vardapet',
    'vc',
    'venerable',
    'verderer',
    'vicar',
    'vice',
    'viscount',
    'vizier',
    'vocalist',
    'voice',
    'warden',
    'warrant',
    'wing',
    'wm',
    'wo-1',
    'wo1',
    'wo2',
    'wo3',
    'wo4',
    'wo5',
    'woodman',
    'writer',
    'zoologist',
])
