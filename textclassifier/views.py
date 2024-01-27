from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import HttpResponse
from .models import Category, Sentence
from .services import analyze_sentiment, classify_to_categories
import csv
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, "textclassifier/home.html", context={"categories": categories})
    
    def post(self, request, *args, **kwargs):
        text = request.POST.get("sentence")
        if not text:
            return redirect("home")
        category_names = list(Category.objects.values_list("name", flat=True))
        sentiment = analyze_sentiment(text)
        category_name = classify_to_categories(text, category_names)
        category = Category.objects.filter(name=category_name).first()
        sentence = Sentence.objects.create(sentence=text, category=category, sentiment=sentiment)
        return redirect("category_detail", pk=category.id)


class CategoryListView(View):
    def get(self, request, pk):
        categories = Category.objects.all()
        category = categories.get(pk=pk)
        sentences = Sentence.objects.filter(category=category).order_by("-created_at")
        context = {
            "current_category": category,
            "categories": categories,
            "sentences": sentences
        }
        return render(request, "textclassifier/category.html", context=context)
    
    def post(self, request, pk):
        category = Category.objects.get(pk=pk)
        sentences = Sentence.objects.filter(category_id=pk).values_list("sentence", "sentiment")
        table = [(index + 1, sentence, sentiment) for index, (sentence, sentiment) in enumerate(sentences)]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{category.name}.csv"'
        writer = csv.writer(response)
        writer.writerow(["Serial No.", "Review", "Sentiment"])
        writer.writerows(table)
        return response



