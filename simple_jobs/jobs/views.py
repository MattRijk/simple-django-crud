from django.shortcuts import render, redirect, get_object_or_404
from jobs.models import Job
from jobs.forms import JobForm
# Create your views here.


def index(request):
    template = 'index.html'
    query = Job.objects.all()
    context = {'jobs': query}
    return render(request, template, context)

def add_job(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'job_form.html', {'form':form})

def update_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'job_form.html', {'form': form})

def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('index')
    return render(request, 'delete.html', {'object': job})
    
    