from django.shortcuts import render, redirect, get_object_or_404

from django.views import generic

from django.utils import timezone
from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DeleteView):
    template_name = 'polls/detail.html'
    model = Question

class ResultsView(generic.DeleteView):
    template_name = 'polls/results.html'
    model = Question

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You don't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', pk=pk)
