from django.db import models
from Pessoa.models import Pessoa
from Vagas.models import Vagas

def path_curriculum(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'curriculo_{0}_{1}_{2}'.format(instance.pessoa.nome.split()[0],instance.pessoa.nome.split()[1], filename)

class Curriculum(models.Model):

    def __unicode__(self):
            return "%s" %(self.anexo)

    pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE, null=True, blank=True, related_name="curriculos")
    vaga = models.ForeignKey(Vagas,on_delete=models.CASCADE, null=True, blank=True, related_name="curriculos_vaga")
    anexo = models.FileField(upload_to=path_curriculum, blank=True, null=True)
