from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import generic

from .models import Question, Choice, QuestionForm, ChoiceInlineForm

class QuestionList(generic.ListView):
    template_name = 'polls2/question_list.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class QuestionDetail(generic.DeleteView):
    template_name = 'polls2/question_detail.html'
    model = Question

class QuestionResults(generic.DeleteView):
    template_name = 'polls2/question_results.html'
    model = Question

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls2/question_list.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls2:question_results', pk=pk)
        
def question_create(request):
    form = QuestionForm(request.POST)
    context = {'form': form}
    if request.method == "POST" and form.is_valid():
        question = form.save(commit=False)
        formset = ChoiceInlineForm(request.POST, instance=question)
        context['formset'] = formset
        if formset.is_valid():
            question.save()
            formset.save()
            pk = question.pk
            return redirect('polls2:question_detail', pk=pk)
    else:
        context['formset'] = ChoiceInlineForm()
    return render(request, 'polls2/question_create.html', context)