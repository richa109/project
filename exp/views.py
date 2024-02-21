from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, SubCategory, Transaction

# Category views
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'  # Replace with your actual template file

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'  # Replace with your actual template file

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']  # Add more fields as needed
    template_name = 'category_form.html'  # Replace with your actual template file

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']  # Add more fields as needed
    template_name = 'category_form.html'  # Replace with your actual template file

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'  # Replace with the URL where you want to redirect after deletion
    template_name = 'category_confirm_delete.html'  # Replace with your actual template file

# Subcategory views
class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'subcategory_list.html'  # Replace with your actual template file

class SubCategoryDetailView(DetailView):
    model = SubCategory
    template_name = 'subcategory_detail.html'  # Replace with your actual template file

class SubCategoryCreateView(CreateView):
    model = SubCategory
    fields = ['name', 'category']  # Add more fields as needed
    template_name = 'subcategory_form.html'  # Replace with your actual template file

class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    fields = ['name', 'category']  # Add more fields as needed
    template_name = 'subcategory_form.html'  # Replace with your actual template file

class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    success_url = '/'  # Replace with the URL where you want to redirect after deletion
    template_name = 'subcategory_confirm_delete.html'  # Replace with your actual template file

# Transaction views
class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction_list.html'  # Replace with your actual template file

class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'transaction_detail.html'  # Replace with your actual template file

class TransactionCreateView(CreateView):
    model = Transaction
    fields = ['amount', 'end_date', 'category', 'subcategory', 'payment', 'status']  # Add more fields as needed
    template_name = 'transaction_form.html'  # Replace with your actual template file

class TransactionUpdateView(UpdateView):
    model = Transaction
    fields = ['amount', 'end_date', 'category', 'subcategory', 'payment', 'status']  # Add more fields as needed
    template_name = 'transaction_form.html'  # Replace with your actual template file

class TransactionDeleteView(DeleteView):
    model = Transaction
    success_url = '/'  # Replace with the URL where you want to redirect after deletion
    template_name = 'transaction_confirm_delete.html'  # Replace with your actual template file



