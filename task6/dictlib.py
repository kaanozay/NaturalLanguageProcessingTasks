
synset1=[["bez", "Pamuk veya keten ipliğinden yapılan dokuma."],["bez", "İçinde geçen kandan veya öz sudan bazı maddeler ayırarak salgı oluşturan organ."]]
synset2=[["kanal","Kimi toprakları ve alanlarını sulamak, bataklıkları kurutmak ya da gemilerin ulaşımını sağlamak amacıyla, insan eliyle açılmış suyolu."],["kanal","Telefon,telgraf,televizyon vb. araçlarla iletişimi sağlayan yol,hat."]]
synset3=[["atlet","atletizmle uğraşan kimse , spor yapan kimse"],["atlet","kolsuz erkek fanilası"]]

synsets=[["bez",synset1],["kanal",synset2],["atlet",synset3]]
def getAmbition(ambi_word):

    for definitions in synsets:
        if definitions[0]==ambi_word:
            return definitions[1]