from nltk import word_tokenize, pos_tag
import copy

# Ehsan Shaghaei
# B19-AAI01
#

TEXT = ['Cat template has properties of color, age, and name.',
        'There exists a cat with the name Bob.',
        'If there exists cat named Bob then there exists a cat named Tom.']


class EnglishToClips:
    class CMD:
        DEFRULE = 0
        DEFTEMPLATE = 1
        ASSERT = 2

    ALLOWED_POS = ['IN', 'RB', 'VBZ', 'NN', '.']
    ASSERT_CORPUS = ['exists', 'exist', ]
    DEFTEMPLEATE_CORPUS = ['has', 'contains']

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
            tmp = tmp[:],
            return ' '.join(map(str,tmp))
        elif cmd_type == self.CMD.DEFTEMPLATE:
            tmp = copy.deepcopy(list(map(list,self.filterPosTags(postag, ['NN','VBZ']))))
            
            return ' '.join(map(str,tmp))
        elif cmd_type == self.CMD.ASSERT:
            tmp = copy.deepcopy(list(map(list,self.filterPosTags(postag, ['NN','RB']))))
            return ' '.join(map(str,tmp))


if __name__ == '__main__':
    e2c = EnglishToClips(' '.join(TEXT))
