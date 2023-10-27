from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from easy_pdf.views import PDFTemplateResponseMixin

from registar.models.krstenje import Krstenje
from registar.forms import SearchForm


class KrstenjaListView(ListView):
    template_name = 'registar/krstenja_list.html'
    context_object_name = 'krstenja_entries'
    model = Krstenje  # or queryset = Krstenje.objects.all()

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            return Krstenje.objects.filter(dete__name__icontains=query)
        return Krstenje.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context


# def krstenja(request):
#     # krstenja_entries = Krstenje.objects.all()
#     # return render(request, 'registar/krstenja_list.html', {'krstenja_entries': krstenja_entries})
#     form = SearchForm(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['query']
#         krstenja_entries = Krstenje.objects.filter(dete__name__icontains=query)
#     else:
#         krstenja_entries = Krstenje.objects.all()
#     return render(request, 'registar/krstenja_list.html', {'krstenja_entries': krstenja_entries, 'form': form})


class KrstenjePDF(PDFTemplateResponseMixin, DetailView):
    model = Krstenje
    template_name = "registar/print_krstenje.html"


class KrstenjeView(DetailView):
    model = Krstenje
    template_name = "registar/view_krstenje.html"
    context_object_name = "krstenje"
    pk_url = "uid"

    font_name = "DejaVuSans"

    def get_object(self):
        k_rbr = self.kwargs.get(self.pk_url)
        return get_object_or_404(Krstenje, uid=k_rbr)
