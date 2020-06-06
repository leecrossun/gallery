from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', blank=True) # null 값 허용
    # blank=True 와 null=True는 다르다.
    # blank=True 는 validate 검사를 통과하도록 자동으로 '' 를 붙여서 전송시킨다.
    # null=True 는 데이터베이스상의 null값을 허용한다는 의미이다.
    # 원래 null=True 로 했다가 계속 validate 검사에서 막혔는데
    # valid검사와 관련된 것은 blank 속성이라는 것을 기억해두자.
    body = models.TextField()

    def __str__(self):
        return self.title    


