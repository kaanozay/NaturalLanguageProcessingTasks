import dictlib
import nltk

def lesk(sentence,ambi_word):

    sys=dictlib.getAmbition(ambi_word=ambi_word)
    sent_item=set(sentence.split())
    print(sys)
    sense=max(
        (len(sent_item.intersection(ss[1].split())),ss)for ss in sys
    )
    return sense


sentence="Sinir sistemi,canlının dış çevre ve organizma arasında ilişkisini sağlayan sistemdir.Beyin ve omuriliğe ait nöronlar uyarıları alır,değerlendirir ve uyarıyı kaslara veya salgı bezlerine götürür."   
sentence1="Kardeşimin televizyon izlerken sürekli iki kanal arasında ileri geri yapması çok can sıkıcı bana göre."
sentence2="Bugün çarşıdan kendime kış hazırlığı olması açısında iki tane atlet aldım."
sentence3="Bugün spor salonunda çok hızlı koşan bir atletle tanıştım."
sentence4="Tarıma başlayan insan,tarım alanlarını sulamak için çeşitli kanallar yaparak suyun yönünü değiştirmiş,yer altından suları çekerek kullanmıştır."


print(lesk(sentence,ambi_word="bez"))
print(lesk(sentence1,ambi_word="kanal"))
print(lesk(sentence2,ambi_word="atlet"))
print(lesk(sentence3,ambi_word="atlet"))
print(lesk(sentence4,ambi_word="kanal"))





