from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.contrib import messages

from django.urls import reverse
# Create your views here.

from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.embed import components
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource

from .models import Question, Choice


def home(request):
    
    latest_question_list = Question.objects.order_by('-publish_date')
    
    context = {'title':'main page', 'latest_questions':latest_question_list}

    return render(request, 'polls/index.html', context)

def details(request, pk):
    
    details = None
    context = {'title':'details page'}

    messages.success(request, 'Please vote')

    try:
        question = Question.objects.get(pk=pk)
        context['question'] = question
    except Question.DoesNotExist:
        raise Http404("Question des not exists")

    return render(request, 'polls/details.html', context)


def create_bokeh_circle_plot(x_val, y_val):
    
    title = "Votes results in bokeh figure"
    x_label = "Answers related to question"
    y_label = "Number of votes"
    plot = figure(title=title,
                tools="pan,wheel_zoom,box_zoom,reset, hover", #toolbar_location=None,
                plot_width=700,plot_height=350,
                x_axis_label=x_label, y_axis_label=y_label
                )
    plot.circle(x_val,y_val, size=20, color="blue")

    plot.title.text_font_size = "16pt"
    plot.title.align = "center"
    plot.background_fill_color = "lightgrey"
    plot.border_fill_color = "whitesmoke"
    plot.min_border_left = 40
    plot.min_border_right = 40

    return components(plot)

def create_bokeh_bar_plot(x_val, y_val):

    source = ColumnDataSource(data=dict(x_val=x_val, y_val=y_val))

    x_label = "Answers related to question"
    y_label = "Number of votes"

    p = figure(x_range=x_val, plot_height=350, 
            tools = "pan,wheel_zoom,box_zoom,reset,poly_select,tap,save,crosshair",
            x_axis_label=x_label, y_axis_label=y_label,
            title="Votes count")
    
    p.vbar(x='x_val', top='y_val', width=0.3, source=source, legend_field="x_val",
        line_color='white', fill_color=factor_cmap('x_val', palette=Spectral6, factors=x_val))

    p.xgrid.grid_line_color = None
    
    p.y_range.start = 0
    p.toolbar.logo = None
    p.title.align = "center"
    p.y_range.end =  max(y_val) + 2
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"


    return components(p)

def results(request, pk):
    
    results = get_object_or_404(Question, pk=pk)
    # x_val =[c.choice_text for c in results.choice_set.all()]
    
    val =[ [i+1, c.votes, c.choice_text] for i, c in enumerate(results.choice_set.all())]
    # val =[ [c.choice_text, c.votes] for c in results.choice_set.all()]
    x_val, y_val, _ = zip(*val)
    script, div = create_bokeh_circle_plot(x_val, y_val)

    _, y_val, x_val = zip(*val)
    script2, div2 = create_bokeh_bar_plot(x_val, y_val)

    context = {'title':'results page', 'question':results, 'script':script, 'div':div, 'script2':script2, 'div2':div2}

    return render(request, 'polls/results.html', context)

def vote(request, pk):

    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except: #(KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def vote_results(request, pk):
    results = {}
    votes = Question.objects.get(pk=pk).choice_set.all()
    for v in votes:
        results[v.choice_text]= v.votes
    
    return JsonResponse([results], safe=False)