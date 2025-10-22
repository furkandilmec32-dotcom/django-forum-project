from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.contrib import messages
from .models import Category, Forum, Thread, Reply


class HomeView(ListView):
    """Ana sayfa - kategoriler ve forumlar"""
    model = Category
    template_name = 'forum/home.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Son 5 thread'i getir
        context['recent_threads'] = Thread.objects.select_related(
            'forum', 'author'
        ).order_by('-created_at')[:5]
        return context


class ForumListView(ListView):
    """Tüm forumların listesi"""
    model = Forum
    template_name = 'forum/forum_list.html'
    context_object_name = 'forums'
    
    def get_queryset(self):
        return Forum.objects.select_related('category').order_by('category__ordering', 'ordering')


class ForumDetailView(ListView):
    """Bir forumun içindeki thread'ler"""
    model = Thread
    template_name = 'forum/forum_detail.html'
    context_object_name = 'threads'
    paginate_by = 10
    
    def get_queryset(self):
        self.forum = Forum.objects.get(pk=self.kwargs['pk'])
        queryset = Thread.objects.filter(forum=self.forum).select_related('author')
        
        # Arama
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
        
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forum'] = self.forum
        context['search_query'] = self.request.GET.get('q', '')
        return context
class ThreadDetailView(ListView):
    """Thread detayı ve yanıtları"""
    model = Reply
    template_name = 'forum/thread_detail.html'
    context_object_name = 'replies'
    paginate_by = 10
    
    def get_queryset(self):
        self.thread = Thread.objects.select_related('forum', 'author').get(pk=self.kwargs['pk'])
        return Reply.objects.filter(thread=self.thread).select_related('author').order_by('created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = self.thread
        return context
class ThreadCreateView(LoginRequiredMixin, CreateView):
    """Yeni thread oluşturma"""
    model = Thread
    template_name = 'forum/thread_form.html'
    fields = ['title', 'body']
    
    def dispatch(self, request, *args, **kwargs):
        self.forum = get_object_or_404(Forum, pk=self.kwargs['forum_pk'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.forum = self.forum
        form.instance.author = self.request.user
        messages.success(self.request, 'Thread created successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forum'] = self.forum
        return context
    
    def get_success_url(self):
        return reverse('thread_detail', kwargs={'pk': self.object.pk})
class ReplyCreateView(LoginRequiredMixin, CreateView):
    """Thread'e yanıt ekleme"""
    model = Reply
    template_name = 'forum/reply_form.html'
    fields = ['content']
    
    def dispatch(self, request, *args, **kwargs):
        self.thread = get_object_or_404(Thread, pk=self.kwargs['thread_pk'])
        if self.thread.is_closed and not request.user.is_staff:
            messages.error(request, 'This thread is closed.')
            return redirect('thread_detail', pk=self.thread.pk)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.instance.thread = self.thread
        form.instance.author = self.request.user
        messages.success(self.request, 'Reply posted successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = self.thread
        return context
    
    def get_success_url(self):
        return reverse('thread_detail', kwargs={'pk': self.thread.pk})
