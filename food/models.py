from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название блюд")
    # SET_NULL - если удалим категорию, то объект останется без категории
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория", null=True)
    image = models.ImageField(upload_to='food/', verbose_name="Изображение")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.TextField(max_length=500, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    def __str__(self) -> str:
        return f"{self.title} - {self.category}"
    
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class Events(models.Model):
    image = models.ImageField(upload_to='events/', verbose_name="Изображение")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.TextField(max_length=500, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.title} - {self.price} - {self.created_at}"
    
    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"


class Reservation(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    email = models.EmailField(max_length=100, verbose_name="Email")
    phone = models.CharField(max_length=13, verbose_name="Номер телефона")
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")
    persons = models.PositiveIntegerField(verbose_name="Количество людей")
    message = models.TextField(max_length=500, verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone} - {self.date} - {self.time} - {self.persons}"
    
    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"


class Testimonials(models.Model):
    image = models.ImageField(upload_to='testimonials/', verbose_name="Изображение", blank=True, null=True)
    first_name = models.CharField(max_length=120, verbose_name="Имя")
    last_name = models.CharField(max_length=120, verbose_name="Фамилия")
    description = models.TextField(max_length=500, verbose_name="Описание")
    profession = models.CharField(verbose_name="Профессия", max_length=120)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | Профессия: {self.profession} | {self.created_at}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"Фотография была загружена {self.created_at}"
    
    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Галерея"


class Role(models.Model):
    title = models.CharField(max_length=120, verbose_name="Роль")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.title} | {self.created_at}"
    
    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class Chefs(models.Model):
    image = models.ImageField(upload_to='chefs/', verbose_name="Изображение", blank=True, null=True)
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name="Должность")
    twitter  = models.URLField(blank=True, null=True, unique=True, verbose_name="twitter Url", max_length=300)
    facebook = models.URLField(blank=True, null=True, unique=True, verbose_name="facebook Url", max_length=300)
    instagram = models.URLField(blank=True, null=True, unique=True, verbose_name="instagram Url", max_length=300)
    linkedin = models.URLField(blank=True, null=True, unique=True, verbose_name="linkedin Url", max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} | {self.role} | {self.created_at}"
    
    class Meta:
        verbose_name = "Повар"
        verbose_name_plural = "Повара"


class Contact(models.Model):
    full_name = models.CharField(max_length=120, verbose_name="ФИО")
    email = models.EmailField(max_length=120, verbose_name="Email")
    subject = models.CharField(max_length=120, verbose_name="Тема")
    message = models.TextField(max_length=500, verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} | {self.subject} | {self.message} | {self.created_at}"
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"