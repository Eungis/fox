import logging
from typing import Optional, Union
from MeCab import Tagger
from fox.constants import MECAB_KO_DIC_PATH

logger = logging.getLogger(__name__)

class KoMecabTokenizer():
    
    def __init__(self, mecab_ko_dic:str=MECAB_KO_DIC_PATH):
        self.dic_path = mecab_ko_dic
        self.mecab = Tagger(f'-d {self.dic_path}')
    
    @staticmethod
    def parse(result, join=False):
        def split(morpheme, join=False):
            if not morpheme: return ('', 'SY')
            morpheme_splited = morpheme.split('\t', 1)
            if len(morpheme_splited) != 2:
                return ('', 'SY')
            surface, tag = morpheme_splited
            if join:
                return surface + '/' + tag.split(',', 1)[0]
            else:
                return (surface, tag.split(',', 1)[0])

        return [split(morpheme, join=join) for morpheme in result.splitlines()[:-1]]
    
    def pos(self, sent:str, flatten:bool=True, join:bool=False):
        """parse part of speech"""
        
        if flatten:
            result = self.mecab.parse(sent)
            if result is None:
                split_result = []
                splited_sentence = sent.split()
                for i in splited_sentence:
                    result = self.mecab.parse(i)
                    if result is not None:
                        split_result.append(result.replace('EOS\n',''))
                split_result.append('EOS\n')
                split_result = ''.join(split_result)
                return self.parse(split_result, join=join)           
            return self.parse(result, join=join)
        else:
            return [self.parse(self.mecab.parse(eojeol), join=join) for eojeol in sent.split()]
            
            


