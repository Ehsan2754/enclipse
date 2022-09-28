
# @ author Ehsan Shaghaei
# ehsan2754@gmail.com
# Sep 28,2022


from test import BaseTest



class GeneralTest:
    TEST_INPUT = ['Cat template has properties of color, age, and name.',
            'There exists a cat with the name Bob.',
            'If there exists cat named Bob aged 12 then there exists a cat named Tom aged 12.']
    def __init__(self,input):
        
        for result in input:
            print(result)
            assert 1==1