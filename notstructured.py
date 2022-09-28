
# @ author Ehsan Shaghaei
# ehsan2754@gmail.com
# Sep 28,2022


from enclipse import Enclipse

TEXT = ['Cat template has properties of color, age, and name.',
        'There exists a cat with the name Bob.',
        'If there exists cat named Bob aged 12 then there exists a cat named Tom aged 12.']


if __name__ == '__main__':
    e2c = Enclipse(' '.join(TEXT))
