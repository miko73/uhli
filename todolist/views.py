from django.shortcuts import render

# Create your views here.
# inside views.py

# inside views.py
def home(response):
    return render(response, "todolist/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)  # adds the to do list to the current logged in user

            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "todolist/create.html", {"form":form})

# inside views.py
def view(response):
    return render(response, "todolist/view.html", {})

# inside views.py
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")


        return render(response, "todolist/list.html", {"ls":ls})

    return render(response, "todolist/home.html", {})