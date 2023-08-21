from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')





class Port(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    last_update = models.DateTimeField(null=True, blank=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.name


class Quai(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    capacite = models.PositiveIntegerField()
    last_update = models.DateTimeField(null=True, blank=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    port = models.ForeignKey(Port, on_delete=models.PROTECT)
    def __str__(self):
        return self.nom 

    
class PosteNavire(models.Model):
    nom = models.CharField(max_length=100)
    taille_max = models.DecimalField(max_digits=5, decimal_places=2)
    quai_assigne = models.ForeignKey(Quai, on_delete=models.PROTECT)
    date_arrivee = models.DateField()
    heure_arrivee = models.TimeField()
    date_depart = models.DateField(null=True, blank=True)
    heure_depart = models.TimeField(null=True, blank=True)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    # Autres champs de votre modèle
    last_update = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.nom


class Navire(models.Model):
    numeroDeScanne = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    CHOICES_MARCHANDISE = (
        ('conteneurs', 'Conteneurs'),
        ('vrac_sec', 'Vrac sec'),
        ('vrac_liquide', 'Vrac liquide'),
        ('marchandises_generales', 'Marchandises générales'),
        ('marchandises_dangereuses', 'Marchandises dangereuses'),
        ('produits_chimiques', 'Produits chimiques'),
        ('hydrocarbures', 'Hydrocarbures'),
        ('minerais', 'Minerais'),
        ('denrees_alimentaires', 'Denrées alimentaires'),
        ('bois', 'Bois'),
        ('machines_et_equipements', 'Machines et équipements'),
        ('textiles', 'Textiles'),
        ('equipements_medicaux', 'Équipements médicaux'),
        ('vehicules', 'Véhicules'),
        ('produits_electroniques', 'Produits électroniques'),
       
    )

    type_marchandise= models.CharField(max_length=50, choices=CHOICES_MARCHANDISE)

    
    capacite = models.PositiveIntegerField()
    date_arrivee = models.DateField()
    heure_arrivee = models.TimeField()
    date_depart = models.DateField(null=True, blank=True)
    heure_depart = models.TimeField(null=True, blank=True)
    quai_de_preference = models.ForeignKey(Quai, on_delete=models.PROTECT)
    posteNavire= models.ForeignKey(PosteNavire, on_delete=models.PROTECT)

    port = models.ForeignKey(Port, on_delete=models.PROTECT)
    shifts_requis = models.PositiveIntegerField(default=0)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    last_update = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.nom
  

    

class Affectation(models.Model):
    navire = models.OneToOneField(Navire, on_delete=models.CASCADE)
    quai = models.ForeignKey(Quai, on_delete=models.CASCADE)
    poste = models.ForeignKey(PosteNavire, on_delete=models.CASCADE)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
    
    last_update = models.DateTimeField(null=True, blank=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.navire} - {self.quai} - {self.port} - {self.poste}"





