from django.shortcuts import render, redirect
from .models import Math, Informatics, Physics
from django.views.generic import DetailView


def math(request):
    model = Math.objects.order_by('name')
    return render(request, "main/math.html", {'model': model})

def physics(request):
    model = Physics.objects.order_by('name')
    return render(request, "main/physics.html", {'model': model})

def informatics(request):
    model = Informatics.objects.order_by('name')
    return render(request, "main/informatics.html", {'model': model})

class TaskMath(DetailView):
    model = Math
    template_name = 'main/task_m.html'
    context_object_name = 'el'


class TaskPhysics(DetailView):
    model = Physics
    template_name = 'main/task_p.html'
    context_object_name = 'el'


class TaskInformatics(DetailView):
    model = Informatics
    template_name = 'main/task_i.html'
    context_object_name = 'el'


class End_m(DetailView):
    model = Math
    template_name = 'main/end_m.html'
    context_object_name = 'el'


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        my_data = {}
        for i in range(1, 26):
            my_data[str(i)] = request.POST.get(str(i))

        request.session['value'] = my_data

        pk = self.kwargs.get('pk')
        return redirect('end_m', pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        obj = Math.objects.get(id=pk)

        otv = self.request.session.get('value', {})

        value = {}
        for i in range(1, 26):
            model_value = getattr(obj, f'otv{i}', None)
            session_value = otv.get(str(i), None)
            value[i] = (model_value == session_value)

        otv_u = self.request.session.get('value', {})

        for i in range(1, 26):
            context[f'user_answer{i}'] = otv_u.get(str(i), '')
            context[f'otv{i}'] = getattr(obj, f'otv{i}', '')
            context[f'ob{i}'] = getattr(obj, f'ob{i}', '')

        context['my_value'] = value
        return context


class End_p(DetailView):
    model = Physics
    template_name = 'main/end_p.html'
    context_object_name = 'el'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        my_data = {}
        for i in range(1, 26):
            my_data[str(i)] = request.POST.get(str(i))

        request.session['value'] = my_data

        pk = self.kwargs.get('pk')
        return redirect('end_p', pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        obj = Physics.objects.get(id=pk)

        otv = self.request.session.get('value', {})

        value = {}
        for i in range(1, 26):
            model_value = getattr(obj, f'otv{i}', None)
            session_value = otv.get(str(i), None)
            value[i] = (model_value == session_value)

        otv_u = self.request.session.get('value', {})

        for i in range(1, 26):
            context[f'user_answer{i}'] = otv_u.get(str(i), '')
            context[f'otv{i}'] = getattr(obj, f'otv{i}', '')
            context[f'ob{i}'] = getattr(obj, f'ob{i}', '')

        context['my_value'] = value
        return context

class End_i(DetailView):
    model = Informatics
    template_name = 'main/end_i.html'
    context_object_name = 'el'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        my_data = {}
        for i in range(1, 26):
            my_data[str(i)] = request.POST.get(str(i))

        request.session['value'] = my_data

        pk = self.kwargs.get('pk')
        return redirect('end_i', pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        obj = Informatics.objects.get(id=pk)

        otv = self.request.session.get('value', {})

        value = {}
        for i in range(1, 26):
            model_value = getattr(obj, f'otv{i}', None)
            session_value = otv.get(str(i), None)
            value[i] = (model_value == session_value)

        otv_u = self.request.session.get('value', {})

        for i in range(1, 26):
            context[f'user_answer{i}'] = otv_u.get(str(i), '')
            context[f'otv{i}'] = getattr(obj, f'otv{i}', '')
            context[f'ob{i}'] = getattr(obj, f'ob{i}', '')

        context['my_value'] = value
        return context