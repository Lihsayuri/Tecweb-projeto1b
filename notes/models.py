from django.db import models

# Implemente o método __str__(self) na classe Note. Ele deve devolver uma string no seguinte formato: 
# ID. TITULO, onde ID é o id do objeto e TITULO é o título do objeto (atributo title).

# Depois de implementar esse método, a lista de anotações na tela de admin deve estar mais ou menos assim:

class Tag(models.Model):
    tag = models.CharField(max_length=200)

class Note(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    content = models.TextField()

    # def __init__(self, title, content):
    #     self.title = title
    #     self.content = content

    def __str__(self):
        return  str(self.id)+". "+str(self.title)


