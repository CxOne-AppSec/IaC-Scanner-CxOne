from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

def form_page(request):
    return render(request, "form.html")

@require_http_methods(["POST"])
def submit_form(request):
    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    message = request.POST.get("message", "").strip()

    if not name or not email or not message:
        return JsonResponse({"ok": False, "error": "Todos los campos son obligatorios."}, status=400)

    return JsonResponse({
        "ok": True,
        "received": {"name": name, "email": email, "message": message}
    })
