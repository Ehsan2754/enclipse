from nltk import word_tokenize, pos_tag
import copy


class Enclipse:
    class CMD:
        DEFRULE = 0
        DEFTEMPLATE = 1
        ASSERT = 2

    ALLOWED_POS = ['IN', 'RB', 'VBZ', 'NN', '.']
    ASSERT_CORPUS = ['exists', 'exist', ]
    DEFTEMPLEATE_CORPUS = ['has', 'contains','template']

    def __init__(self, sentences: str):
        self.sentences = filter(lambda x: x, sentences.split('.'))
        self.tokens = map(lambda x: word_tokenize(x.lower()), self.sentences)
        self.postags = map(pos_tag, self.tokens)
        self.filtered_postags = map(self.filterPosTags, self.postags)
        self.cmd_types = map(self.extractCMD, map(list, self.filtered_postags))
        fp = copy.deepcopy(self.filtered_postags)
        ct = copy.deepcopy(self.cmd_types)
        fp = list(map(list, fp))
        ct = list(ct)
        self.ruleSeed=0
        print(*list(map(lambda x: self._parseCMD(*x), zip(fp, ct))),sep='\n')

    def filterPosTags(self, postag, allwoedtags=ALLOWED_POS):
        return filter(lambda pair: pair[1] in allwoedtags, postag)

    def extractCMD(self, postag):

        tags = []
        for pair in postag:
            tags.append(pair[1])
        try:
            token, _ = list(postag)[tags.index('VBZ')]
            if ('IN' in tags) and ('RB' in tags):
                return self.CMD.DEFRULE
            elif token in self.ASSERT_CORPUS:
                return self.CMD.ASSERT
            else:
                return self.CMD.DEFTEMPLATE

        except ValueError:
            print(f'Your each sentence must at least have a verb. ->{postag}')

    def _parseCMD(self, postag, cmd_type: int) -> str:
        if cmd_type == self.CMD.DEFRULE:
            tmp = copy.deepcopy(list(map(list,self.filterPosTags(postag, ['NN','VBZ','RB']))))
            tags = [pair[1] for pair in tmp if pair[1] != 'VBZ']  
            tokens = [pair[0] for pair in tmp if pair[1] != 'VBZ']  
            cond,resp = list(set(tokens[:tags.index('RB')])),list(set(tokens[tags.index('RB')+1:]))
            self.ruleSeed+=1
            return f'(defrule rule{self.ruleSeed} ({cond[0]}({", ".join(cond[1:])}))) => (assert ({resp[0]}({", ".join(resp[1:])})))'
        elif cmd_type == self.CMD.DEFTEMPLATE:
            tmp = copy.deepcopy(list(map(list,self.filterPosTags(postag, ['NN','VBZ','RB']))))
            tags = [pair[1] for pair in tmp if (pair[1] == 'NN') and (pair[0] not in self.DEFTEMPLEATE_CORPUS)]  
            tokens = [pair[0] for pair in tmp if (pair[1] == 'NN') and (pair[0] not in self.DEFTEMPLEATE_CORPUS)] 
            return f'(deftemplate {tokens[0]} {" ".join([f"(slot {slot})" for slot in tokens[1:]])})'
        elif cmd_type == self.CMD.ASSERT:
            tmp = copy.deepcopy(list(map(list,self.filterPosTags(postag, ['NN']))))
            tags = [pair[1] for pair in tmp if (pair[1] == 'NN') and (pair[0] not in self.DEFTEMPLEATE_CORPUS)]  
            tokens = [pair[0] for pair in tmp if (pair[1] == 'NN') and (pair[0] not in self.DEFTEMPLEATE_CORPUS)] 
            return f'(assert ({tokens[0]} {" ".join([f"({key} ``{value}``)" for key,value in zip(tokens[1::2],tokens[2::2])])}))'

