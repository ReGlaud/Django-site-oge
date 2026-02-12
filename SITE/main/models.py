from django.db import models

class Math(models.Model):
    name = models.TextField('Номер варианта')

    text = models.TextField('Текст', blank=True)
    imaget = models.ImageField('Картинка', blank=True)

    vopr1 = models.TextField('Вопрос 1')
    otv1 = models.TextField('Ответ 1')
    ob1 = models.TextField('Объяснение 1')
    image1 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr2 = models.TextField('Вопрос 2')
    otv2 = models.TextField('Ответ 2')
    ob2 = models.TextField('Объяснение 2')
    image2 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr3 = models.TextField('Вопрос 3')
    otv3 = models.TextField('Ответ 3')
    ob3 = models.TextField('Объяснение 3')
    image3 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr4 = models.TextField('Вопрос 4')
    otv4 = models.TextField('Ответ 4')
    ob4 = models.TextField('Объяснение 4')
    image4 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr5 = models.TextField('Вопрос 5')
    otv5 = models.TextField('Ответ 5')
    ob5 = models.TextField('Объяснение 5')
    image5 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr6 = models.TextField('Вопрос 6')
    otv6 = models.TextField('Ответ 6')
    ob6 = models.TextField('Объяснение 6')
    image6 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr7 = models.TextField('Вопрос 7')
    otv7 = models.TextField('Ответ 7')
    ob7 = models.TextField('Объяснение 7')
    image7 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr8 = models.TextField('Вопрос 8')
    otv8 = models.TextField('Ответ 8')
    ob8 = models.TextField('Объяснение 8')
    image8 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr9 = models.TextField('Вопрос 9')
    otv9 = models.TextField('Ответ 9')
    ob9 = models.TextField('Объяснение 9')
    image9 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr10 = models.TextField('Вопрос 10')
    otv10 = models.TextField('Ответ 10')
    ob10 = models.TextField('Объяснение 10')
    image10 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr11 = models.TextField('Вопрос 11')
    otv11 = models.TextField('Ответ 11')
    ob11 = models.TextField('Объяснение 11')
    image11 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr12 = models.TextField('Вопрос 12')
    otv12 = models.TextField('Ответ 12')
    ob12 = models.TextField('Объяснение 12')
    image12 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr13 = models.TextField('Вопрос 13')
    otv13 = models.TextField('Ответ 13')
    ob13 = models.TextField('Объяснение 13')
    image13 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr14 = models.TextField('Вопрос 14')
    otv14 = models.TextField('Ответ 14')
    ob14 = models.TextField('Объяснение 14')
    image14 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr15 = models.TextField('Вопрос 15')
    otv15 = models.TextField('Ответ 15')
    ob15 = models.TextField('Объяснение 15')
    image15 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr16 = models.TextField('Вопрос 16')
    otv16 = models.TextField('Ответ 16')
    ob16 = models.TextField('Объяснение 16')
    image16 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr17 = models.TextField('Вопрос 17')
    otv17 = models.TextField('Ответ 17')
    ob17 = models.TextField('Объяснение 17')
    image17 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr18 = models.TextField('Вопрос 18')
    otv18 = models.TextField('Ответ 18')
    ob18 = models.TextField('Объяснение 18')
    image18 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr19 = models.TextField('Вопрос 19')
    otv19 = models.TextField('Ответ 19')
    ob19 = models.TextField('Объяснение 19')
    image19 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr20 = models.TextField('Вопрос 20')
    otv20 = models.TextField('Ответ 20')
    ob20 = models.TextField('Объяснение 20')
    image20 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr21 = models.TextField('Вопрос 21')
    otv21 = models.TextField('Ответ 21')
    ob21 = models.TextField('Объяснение 21')
    image21 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr22 = models.TextField('Вопрос 22')
    otv22 = models.TextField('Ответ 22')
    ob22 = models.TextField('Объяснение 22')
    image22 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr23 = models.TextField('Вопрос 23')
    otv23 = models.TextField('Ответ 23')
    ob23 = models.TextField('Объяснение 23')
    image23 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr24 = models.TextField('Вопрос 24')
    otv24 = models.TextField('Ответ 24', blank=True)
    ob24 = models.TextField('Объяснение 24')
    image24 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr25 = models.TextField('Вопрос 25')
    otv25 = models.TextField('Ответ 25')
    ob25 = models.TextField('Объяснение 25')
    image25 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/math/{self.id}'





class Physics(models.Model):
    name = models.TextField('Номер варианта')

    vopr1 = models.TextField('Вопрос 1')
    otv1 = models.TextField('Ответ 1')
    ob1 = models.TextField('Объяснение 1')
    image1 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr2 = models.TextField('Вопрос 2')
    otv2 = models.TextField('Ответ 2')
    ob2 = models.TextField('Объяснение 2')
    image2 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr3 = models.TextField('Вопрос 3')
    otv3 = models.TextField('Ответ 3')
    ob3 = models.TextField('Объяснение 3')
    image3 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr4 = models.TextField('Вопрос 4')
    otv4 = models.TextField('Ответ 4')
    ob4 = models.TextField('Объяснение 4')
    image4 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr5 = models.TextField('Вопрос 5')
    otv5 = models.TextField('Ответ 5')
    ob5 = models.TextField('Объяснение 5')
    image5 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr6 = models.TextField('Вопрос 6')
    otv6 = models.TextField('Ответ 6')
    ob6 = models.TextField('Объяснение 6')
    image6 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr7 = models.TextField('Вопрос 7')
    otv7 = models.TextField('Ответ 7')
    ob7 = models.TextField('Объяснение 7')
    image7 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr8 = models.TextField('Вопрос 8')
    otv8 = models.TextField('Ответ 8')
    ob8 = models.TextField('Объяснение 8')
    image8 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr9 = models.TextField('Вопрос 9')
    otv9 = models.TextField('Ответ 9')
    ob9 = models.TextField('Объяснение 9')
    image9 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr10 = models.TextField('Вопрос 10')
    otv10 = models.TextField('Ответ 10')
    ob10 = models.TextField('Объяснение 10')
    image10 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr11 = models.TextField('Вопрос 11')
    otv11 = models.TextField('Ответ 11')
    ob11 = models.TextField('Объяснение 11')
    image11 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr12 = models.TextField('Вопрос 12')
    otv12 = models.TextField('Ответ 12')
    ob12 = models.TextField('Объяснение 12')
    image12 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr13 = models.TextField('Вопрос 13')
    otv13 = models.TextField('Ответ 13')
    ob13 = models.TextField('Объяснение 13')
    image13 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr14 = models.TextField('Вопрос 14')
    otv14 = models.TextField('Ответ 14')
    ob14 = models.TextField('Объяснение 14')
    image14 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr15 = models.TextField('Вопрос 15')
    otv15 = models.TextField('Ответ 15')
    ob15 = models.TextField('Объяснение 15')
    image15 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr16 = models.TextField('Вопрос 16')
    otv16 = models.TextField('Ответ 16')
    ob16 = models.TextField('Объяснение 16')
    image16 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr17 = models.TextField('Вопрос 17')
    otv17 = models.TextField('Ответ 17')
    ob17 = models.TextField('Объяснение 17')
    myurl17 = models.TextField('Ссылка 17')
    image17 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr18 = models.TextField('Вопрос 18')
    otv18 = models.TextField('Ответ 18')
    ob18 = models.TextField('Объяснение 18')
    image18 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr19 = models.TextField('Вопрос 19')
    otv19 = models.TextField('Ответ 19')
    ob19 = models.TextField('Объяснение 19')
    image19 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr20 = models.TextField('Вопрос 20')
    otv20 = models.TextField('Ответ 20')
    ob20 = models.TextField('Объяснение 20')
    image20 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr21 = models.TextField('Вопрос 21')
    otv21 = models.TextField('Ответ 21')
    ob21 = models.TextField('Объяснение 21')
    image21 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr22 = models.TextField('Вопрос 22')
    otv22 = models.TextField('Ответ 22')
    ob22 = models.TextField('Объяснение 22')
    image22 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/physics/{self.id}'





class Informatics(models.Model):
    name = models.TextField('Номер варианта')

    vopr1 = models.TextField('Вопрос 1')
    otv1 = models.TextField('Ответ 1')
    ob1 = models.TextField('Объяснение 1')
    image1 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr2 = models.TextField('Вопрос 2')
    otv2 = models.TextField('Ответ 2')
    ob2 = models.TextField('Объяснение 2')
    image2 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr3 = models.TextField('Вопрос 3')
    otv3 = models.TextField('Ответ 3')
    ob3 = models.TextField('Объяснение 3')
    image3 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr4 = models.TextField('Вопрос 4')
    otv4 = models.TextField('Ответ 4')
    ob4 = models.TextField('Объяснение 4')
    image4 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr5 = models.TextField('Вопрос 5')
    otv5 = models.TextField('Ответ 5')
    ob5 = models.TextField('Объяснение 5')
    image5 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr6 = models.TextField('Вопрос 6')
    otv6 = models.TextField('Ответ 6')
    ob6 = models.TextField('Объяснение 6')
    image6 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr7 = models.TextField('Вопрос 7')
    otv7 = models.TextField('Ответ 7')
    ob7 = models.TextField('Объяснение 7')
    image7 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr8 = models.TextField('Вопрос 8')
    otv8 = models.TextField('Ответ 8')
    ob8 = models.TextField('Объяснение 8')
    image8 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr9 = models.TextField('Вопрос 9')
    otv9 = models.TextField('Ответ 9')
    ob9 = models.TextField('Объяснение 9')
    image9 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr10 = models.TextField('Вопрос 10')
    otv10 = models.TextField('Ответ 10')
    ob10 = models.TextField('Объяснение 10')
    image10 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr11 = models.TextField('Вопрос 11')
    otv11 = models.TextField('Ответ 11')
    ob11 = models.TextField('Объяснение 11')
    image11 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr12 = models.TextField('Вопрос 12')
    otv12 = models.TextField('Ответ 12')
    ob12 = models.TextField('Объяснение 12')
    image12 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr13 = models.TextField('Вопрос 13')
    otv13 = models.TextField('Ответ 13')
    ob13 = models.TextField('Объяснение 13')
    myurl13 = models.TextField('Ссылка 13')
    image13 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr14 = models.TextField('Вопрос 14')
    otv14 = models.TextField('Ответ 14')
    ob14 = models.TextField('Объяснение 14')
    myurl14 = models.TextField('Ссылка 14')
    image14 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr15 = models.TextField('Вопрос 15')
    otv15 = models.TextField('Ответ 15')
    ob15 = models.TextField('Объяснение 15')
    image15 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    vopr16 = models.TextField('Вопрос 16')
    otv16 = models.TextField('Ответ 16')
    ob16 = models.TextField('Объяснение 16')
    image16 = models.ImageField('Картинка к вопросу', upload_to='questions/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/informatics/{self.id}'
