from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255,
                            null=True,
                            blank=True)
    
    class Meta:
        db_table = 'category'
        ordering = ['pk']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        permissions = [
            ['autorizar_category', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_category', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]
        

    def __str__(self):
        return "Pk: {0}| Nombre: {1}".format(self.pk, self.name,)
    