from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """Ana kategori - ornek: Genel, Teknoloji, Oyunlar"""
    name = models.CharField(max_length=100, unique=True, help_text="Kategori adi")
    description = models.TextField(blank=True, help_text="Kategori aciklamasi")
    ordering = models.IntegerField(default=0, help_text="Siralama (kucuk sayi ustte)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['ordering', 'name']


class Forum(models.Model):
    """Alt forum - ornek: Python Tartismalari, Django Sorulari"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='forums')
    title = models.CharField(max_length=200, help_text="Forum basligi")
    description = models.TextField(help_text="Forum aciklamasi")
    ordering = models.IntegerField(default=0, help_text="Siralama")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum_detail', kwargs={'pk': self.pk})
    
    def thread_count(self):
        """Bu forumda kac konu var"""
        return self.threads.count()
    
    def last_thread(self):
        """En son olusturulan konu"""
        return self.threads.order_by('-created_at').first()
    
    class Meta:
        verbose_name = "Forum"
        verbose_name_plural = "Forums"
        ordering = ['ordering', 'title']


class Thread(models.Model):
    """Konu/Baslik - kullanicilarin actigi tartismalar"""
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='threads')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=200, help_text="Konu basligi")
    body = models.TextField(help_text="Konu icerigi")
    is_closed = models.BooleanField(default=False, help_text="Konu kapali mi?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('thread_detail', kwargs={'pk': self.pk})
    
    def reply_count(self):
        """Bu konuda kac yanit var"""
        return self.replies.count()
    
    def last_reply(self):
        """En son yanit"""
        return self.replies.order_by('-created_at').first()
    
    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"
        ordering = ['-created_at']


class Reply(models.Model):
    """Yanit - konulara verilen cevaplar"""
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField(help_text="Yanit icerigi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author.username} - {self.thread.title[:30]}"
    
    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"
        ordering = ['created_at']