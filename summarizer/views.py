from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
# Create your views here.

LANGUAGE = "english"
SENTENCES_COUNT = 5

def index(request):
    print(request)
    return render(request,"summarizer/index.html")

def summarize(request):
    if 'url' in request.POST:
        print(request.POST['url'])
        url = request.POST['url']
    else:
        return HttpResponseRedirect('/')
    summary = []
    try:
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)
        summarizer = TextRankSummarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            summary.append(str(sentence))
        sentence = ' '.join(summary)
    except Exception as e:
        return HttpResponse("We encountered a problem summarizing this link please try an "+
        "alternate link") 
    rdata = {
        'article_url':url,
        'summary': summary
    }
    return render(request,"summarizer/result.html",rdata)
    # return HttpResponse(sentence)
    # return HttpResponse(request.POST['url'])