from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250,
                          null=True,
                          blank=True,
                          help_text='Nombre del producto'
                          )
    
    description = models.TextField(null=True,
                                   blank=True,
                                   help_text='Descripcion del producto')
    
    price = models.DecimalField(max_digits=10,
                                 decimal_places=2,
                                 null=True,
                                 blank=True,
                                 help_text='Precio del producto')
    
    is_active = models.BooleanField(default=False,
                                    help_text='Booleano para indicar estado del producto')
    
    class Meta:
        db_table = 'products'
        ordering = ['pk']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        permissions = [
            ['autorizar_productos', f'Puede Autorizar {verbose_name_plural}'],
            ['viewcrud_products', f'Puede Visualizar {verbose_name_plural} en el menú'],
        ]
        

    def __str__(self):
        return "Pk: {0}| Nombre: {1} | Precio {2}".format(self.pk, self.name, self.price)
    