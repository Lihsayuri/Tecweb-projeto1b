from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.shortcuts import render, redirect
from .models import Note
from .models import Tag

def index(request):
    # Note.objects.filter(id=11).delete()
    # route = extract_route(request)

    # Note.objects.filter(title= "Deus é bom").update(title="Pelo amor de Deus")

    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tagNome = request.POST.get('tag')
        tag, criada = Tag.objects.get_or_create(tag=tagNome)
        if criada:
            tag.save()

        note = Note(title = title, content = content, tag = tag)
        note.save()
        # Note.objects.create(title=title, tag=tag , content=content)
        # Note.objects.create(content=content)
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')

    else:
        all_notes = Note.objects.all()
        print(all_notes)
        return render(request, 'notes/notes.html', {'notes': all_notes})

def delete(request):
    id = request.POST.get('id')
    note = Note.objects.get(id=id)
    note.delete()

    return redirect('index')

def edit(request, id):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    tagNome = request.POST.get('tag')
    note = Note.objects.filter(id=id)

    tag, criada = Tag.objects.get_or_create(tag=tagNome)
    if criada:
        tag.save()

    note.update(title=title, tag=tag, content=content)
    
    return redirect('index')

# --------------------------------Funções das Tags ---------------------------------------------------------------

def index_tag(request):
    all_tags = Tag.objects.all()
    print(all_tags)
    return render(request, 'notes/listadeTags.html', {'tags': all_tags})

def tag_details(request, tagid):
    # tag_filtrada = Tag.objects.filter(id=tagid)
    nota_filtrada = Note.objects.filter(tag=tagid)
    print(nota_filtrada)
    return render(request, 'notes/notasdeTags.html', {'notes': nota_filtrada})