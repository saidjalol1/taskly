from django.db import models



class CategoryTask(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi ...")


    class Meta:
        verbose_name = "Kategoriyalar"
        verbose_name_plural = "Kategoriyalar"


    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=300)
    due = models.DateTimeField(blank=False)

    category = models.ForeignKey(CategoryTask, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Vazifalar"
        verbose_name_plural = "Vazifalar" 


    def __str__(self):
        return f"{self.name}-{self.category.name}-{self.due}"